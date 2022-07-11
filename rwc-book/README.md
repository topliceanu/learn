# Book: Real world cryptography

## Ch1. Introduction

* Secret-key cryptography OR Symmetric cryptography
- both users know the key and they keep it secret
- AES - Advanced Encryption Standard - symmetric encryption standard (based on a block cipher)
- block cipher is a deterministic algorithm operating on fixed-length groups of bits, called blocks.
- Kerckhoff's Principle; a system should be secure even if everything about the system (except the key) is public knowledge.
- _Ars ipsi secreta magistro_ - an art secret even for the master.
- problem: key distribution

* Public-key cryptography OR Asymmetric cryptography
- Diffie-Helman key exchange - key exchange protocol
  - transports a secret key between two parties through an insecure channel.
  - sussceptible to man-in-the-middle attacks.
- RSA - Ron Rivest, Adi Shamir, Leonard Adleman
  - contains the spec for a public key encryption algorithm and a digital signature scheme.
  - Alice disseminates her public key, anyone wishing to talk to Alice uses her public
  key to encrypt messages that only Alice can decrypt with her private key.
  - Alice uses her private key to sign messages that can be verified with the public key

* Hybrid encryption
- asymetric encryption only works for small messages as it's expensive and slow.
- encrypt a symetric key using asymetric encryption in order to distribute it to the peer you want to talk to.
- then communicate using symetric key cryptography.

* Goals of cryptography:
- confidentiality: protect information from attackers.
- authentication: identify the party you are talking to.

- Schnorr signature algorithm is far better than anything else.

## Ch2. Hash functions

- hexadecimal (base 16) encoding: 2characters (0-9,a-f) to 8bits
- the output of a hash function is deterministic and fixed length: SHA256 produces 256bits
```
$ openssl dgst -sha256 downloaded_file
$ echo -n "hello" | openssl dgst -sha256
```

* Properties:
- first _pre-image resistance_:
  - Given a hash function and the output digest, it is impossible to recover the input
  - Note: you can't hash something that is too small or predictable. This is vulnerable to brute-force attacks.
- hash functions have the _second pre-image resistance_ property:
  - Given an input and the corresponding hash (pre-image pair), the attacker is unable to find a
  different input with the same digest.
- _collision resistance_ property:
  - Given a hash function, the attacker is unable to produce two different inputs with the same digest.

* Considerations
- theoretically, there are an infinite number of inputs that hash to one digest.
- birthday bounds: given a space of 2^N possibilities, you can expect a collision with a 50% probability after generating 2^(N/2) posibilities.
  - use 256bit hashes for collision resistance.
  - use 128bit hashes for pre-image and second pre-image resistance.

* Uses:
- commitments: you can hash a commitment about the future, distribute the hash,
then, at a future time, reveal the commitment and prove it by hashing it to
match what you distributed in the past. (first and second pre-image resistance).
- resource integrity: associate a digest to resources you serve to insure they were not tampered with.
- distributed ledgers (blockchains)
- content-addressable networks (like bittorrent) files are split into chunks, each chunk is hashed, the client uses the hashes to find peers that store the chunks.

* Standards
- SHA stands for Secure Hash Algorithm
- MD5 and SHA-1 are considered broken: faults were discovered in the hash functions + advances in computing.

* SHA-2 - designed by Ralph Merkle and Ivan Damgard independently
  - four versions based on the output size in bits: SHA-224, SHA-256, SHA-384, SHA-512
```
$ echo -n "hello world" | openssl dgst -sha224
$ echo -n "hello world" | openssl dgst -sha256
$ echo -n "hello world" | openssl dgst -sha384
$ echo -n "hello world" | openssl dgst -sha512
```
  - algorithm:
    1. pad input with bits to get to a multiple of the configured block size, eg 512bits
    2. iteratively apply the compression function (eg. XOR) to message blocks.
       The result of each step is fed to the next step. The last result is the output of the hash function.
       The first compression receives a "nothing-up-my-sleves" input value (iv), eg. the sqrt of a prime.
```
    xxxxx  xxxxx  xxxxx
      |      |      |
      v      v      v
iv-->(CP)-->(CP)-->(CP)-->output

```
  - vulnerable to length-extension attacks, so **don't use for secrets hashing!**

* SHA-3 - Keccak
- not vulnerable to lenght-extensions and can be used to hash secrets
- variants: SHA-3-224, SHA-3-256, SHA-3-384, SHA-3-512 each specifying the output

* XOFs: extendable output functions
- like hashes but produce a configurable variable length digest - XOF (zof)
- Eg: SHAKE, cSHAKE
- If you use multiple cryptographic primitives, do not use the same key and apply _domain separation_!

* Ambigous hashing of tuples
- if you are hashing a data structure - say and array or a tuple - you need to make sure
it is serialised in a way that is unambiguous
  - Eg: ("Alice", "Bob", 1000, 15) -> "Alice||Bob||1000||15" -> hash
    If you do "AliceBob100015" this becomes ambiguous.

"Defence in depth" - layering imperfect defenses in the hope that an attacker will not defeat them all.
- Q: How do you monitor these layers? It would be nice to see what layer an attacker is at.

* Hashing passwords
- salts are random numbers used in conjunction with passwords to produce hashes
- state of the art, recommendation for hashing passwords: [Argon2](https://password-hashing.net/)
- others used: BPKDF2, bcrypt, scrypt. These can be used with insecure parameters!

## Ch 3. Message authentication codes (MACs)
- the goal is to protect the integrity of data.
Q: Is it the same as a signature? A: yes, but a signature uses asymetric encryption and provides authenticat#ion, while MACs don't.
- a MAC takes in an input messages and a secret key and produces an authentication tag.
- since hash functions are public, a MAC is like a private hash function that only the owner of the secret key can compute.
- a popular implementatin is HMAC - hash-based message authentication code
Properties:
- MACs are resistant against forgery as long as the key remains secret!
- the authentication tag needs to be of a minimum length to be secure, usually 128bit
- MACs are vulnerable to replay. The solution is to add a counter. Counters should never be variable length to prevent ambiguous attacks.
- verifying an authentication tag needs to be done in constant time otherwise it's vulnerale to timing attacks.
  Always use the library provided verification function!
Uses:
- can be used to generate random numbers deterministically.
"Many major applications use a MAC with a random key in place of the non-cryptographic hash function."
- HMACs are used to derive private keys. See Ch. 7

* HMAC:
- uses SHA2 which is vulnerable to length-extension attacks, thus it needs to split the key.
  ! Never hash secrets with sha2 dirrectly, use HMAC.
- creates two keys from the main key using two constants: k1 = k XOR ipad, k2 = k XOR opad
```
  auth_tag = hash(hash(message + k1) + k2), k1 = key XOR ipad, k2 = key XOR opad
```
- HS256 (HMAC with SHA-256) is used in JWT.

* KMAC:
- uses sha3 which is not vulnerable to length-extension attacks
```
  auth_tag = SHA-3-256(key || message)
  auth_tag = cSHAKE(key, message, output_length)
```

## Ch 4. Authenticated encryption (Symmetric Encryption)
- _encryption algorithm_ aka _cipher_. The input is a _plaintext_ and a _secret key_ and the output is a _ciphertext_.

* AES (Advanced encryption standard) block cipher - don't use!
  - Variants: AES-128 (16bytes), AES-196 (24byte), AES-256 (32bytes). Use 128, it's enough
  - AES is a _pseudorandom permutation_
  - it arranges the 16byte input in a 4x4 byte array, then iterates over a _round_ function several times.
```
+---------+   +--------+       +--------+   +----------+
|plaintext|-->|round fn|->...->|round fn|-->|ciphertext|
+---------+   +--------+       +--------+   +----------+
```
  - each _round_ takes the output of the previous round and a round key derived from the main key,
  then performes a sequence of operations: SubBytes, ShiftRows, MixColumns, AddRoundKey (XOR).
```
+-+              +-+               +-+                +-+                 +-+
|X|->(SubBytes)->|X|->(ShiftRows)->|X|->(MixColumns)->|X|->(AddRoundKey)->|X|
+-+              +-+               +-+                +-+       ^         +-+
                                                                |
                                                            (RoundKey)
```
  - AES is implemented in hardware by CPUs
  - if the plaintext is smaller than 16byte, it needs to be padded. PKCS#7 add bytes to the end to reach 16. Each bytes is the number of padding bytes needed to be added.
```
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|1f|0e|ef|52|f3|60|b4|cd|08|08|08|08|08|08|08|08|   // 8 bytes padding cointaining the number 8.
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
```
  - AES-CBC: if the plaintext is larger, split in chunks of 16bytes, generate a random IV(_initial value_ or _initialization vector_) and use CBC (cipher block chaining) mode:
```
   (IV)         (key)               (key)               (key)
     |            |                   |                   |
     |          +-v-+               +-v-+               +-v-+
    XOR-------->|AES|----->XOR----->|AES|----->XOR----->|AES|--->....
     |          +---+       |       +---+       |       +---+
(Plaintext)            (Plaintext)         (Plaintext)
( Chunk#1 )            ( Chunk#2 )         ( Chunk#3 )
```
  - IV is public, so it needs to be unique (cannot repeat) and unpredictable (trully random). Don't generate the IV yourself!
  - The IV and the ciphertext can be modified by an attacker, so we add an integrity mechanism: AES-CBC-HMAC
  - Don't use AES-CBC-HMAC in practice!

* AEAD (authenticated encryption with associated data) - use this!
  - similar to AES-CBC-HMAC + confidentiality + authentication for associated data (think IV, authentication tag)
  - the most used AEAD is `AES-GCM` (Galois/Counter Mode) and `ChaCha20-Poly1305`
  - Nonces should never be re-used for these two! AES-GCM-SIV is nonce misuse resistant.
  - AES-GCM:
```
       (Nonce||Counter)     // Counter has 4bytes and counts the number of chunks
              |             // Nonce is randomly generated.
              v
            +---+
  (Key)---->|AES|
            +-+-+
              |
              v
          (KeyStream)
              |
              v
(Plaintext)->XOR
              |
              v
        (Ciphertext)

```
  - both use a _stream cipher_ (instead of block ciphers). They generate a keystream that is XORed with the plaintext to give the ciphertext.
  - There are limits on how many messages can be encrypted under a single key, before the key become vulnerable.
  - chacha20-poly1305:
```
(key) (Nonce) (counter=0)      (key) (Nonce) (counter=1)
  |      |        |              |      |        |
  |  +---v----+   |              |  +---v----+   |
  +->|Chacha20|<--+              +->|Chacha20|<--+
     +---+----+                     +---+----+
         |                              |
         v               (plaintext)-->XOR
       (r|s)                            |
         |                         (ciphertext)
         |                              |
         |     (associated data||ciphertext||len(ciphertext)||len(associated data)
         |                              |
         |                          +---v----+
         +------------------------->|Poly1305|
                                    +---+----+
                                        |
                                (authentication tag)
* Phones and laptops do disk encryption using unauthenticated encryption in wide blocks - _wide-block cipher_ - to protect agains _bitflip attacks_.
* Database encryption means encrypting data at rest on disk, to query the data, it must be decrypted by the DB.
```

## Ch 5. Key Exchanges
* Group theory
  - a group is a set of elements and an operation
  - properties: closure (if a,b are in the group, then ab in the group), associativity (a(bc)==(ab)c), identity (ax1=1xa=a), inverse (a^(-1)xa=1)
  - groups with commutativity (ab==ba) are Galois groups
  - subgroup is a group defined on a subset of elements in a group
  - cyclic subgroup is a subgroup generated from a single generate (or base) that is multiplied to itself to yield elements of the same subgroup.
```
4 mod 5 = 4
4x4 mod 5 = 1
4x4x4 mod 5 = 4
```
  - We use finite fields (ie. mod p) to limit the size of the group and to make it cyclic. This is sometimes called FFDH (finite field Diffie-Hellman)
  - Note: when the modulus is prime, every possible generator forms a subgroup.
  - The number of elements in a group is the Order of the group.

* Diffie-Hellman key exchange - deprecated, use Eliptic Curve DH
  - DH uses groups that are Galoais groups, multiplicative module a large prime number, where every possible generator forms a cyclic subgroup.
  - based on the _discret logarithm problem_: given the equation b^x = a mod m, where b, a and m are know, find x.
  - Alice and Bob agree on a large prime P and a generator g
  - Alice chooses a private key `a` and computes the public key `A = g^a mod p`
  - Bob chooses a private key `b` and computes the public key `B = g^b mod p`
  - the shared key can be computed by both Alice and Bob using each-other's public keys:
      `A^b mod p == (g^a mod p)^b mod p = g^(ab) mod p = (g^b mod p)^a mod p = B^a mod p`
  - RFC 7919 is recommended, while RFC 5114 for DH is broken so don't use it!
    - the prime modulus p is large (2048bits) generator g is 2 because is makes multiplication fast on computers. The group order is q=(p-1)/2
    - disadvantage: private and public keys are large 2kb

* Eliptic curve Diffie-Hellman (ECDH) key exchange - use this! (or ECDHE)
  - advantage: keys are small for the same level of security.
  - based on the _eliptic curve dicrete logarithm problem_
  - the two curves to use are P-256 (aka. secp256r1) and Curve25519.
  - P-256 provides 128 bits of security. There is also P-384 P-512 which offers 256 bits of security
  - Curve25519 offers 128 bits of security. Curve448 offers 224 bits
  - The combination of ECDH and Curve25519 is dubbed X25519, while ECDH and Curve448 is known as X448
  - Make sure that the implementation verifies the validity of public keys.

TODO: review attacks on DH and ECDH

## Ch 6. Asymmetric encryption and hybrid encryption
- Basic asymmetric cryptography does not provide authentication. Bob doesn't know if he's using Alice's
  public key and Alice doesn't know who sent the encrypted message because everyone has access to her public key.
- Limitations: length of messages that it can encrypt (currently, 500 characters) and speed of encryption/decryption.

* Key exchanges
  - RSA uses asymmetric encryption to exchange a symmetric key. The rest of the encryption is done using symmetric encryption. Don't use RSA, use ECDH.

* Hybrid encryption (a mix of asymmetric and symmetric primitives)
  - the idea is to use asymmetric encryption to encrypt a symmetric key, then use the key to encrypt the message itself.
```
                                               +-------------+
              +---------+   (plaintext)------->|Authenticated|
              |Generate |                      |Encryption   |---->(ciphertext)--+
(sec param)-->|symmetric|-->(symmetric key)--->+-------------+                   |
(num bits)    |key      |         |                                              |
              +----+----+         +--------------->+----------+                 (||)-->.... send over to Alice
                                                   |Asymmetric|   (encypted )    |
                            (alice's public key)-->|Encryption|-->(symmetric)----+
                                                   +----------+   (key      )
```
  - the first part is called the Key Encapsulation Mechanism (KEM)
  - the second part is the Data Encapsulation Mechanism (DEM)
  - ECIES - Eliptic Curve Integrated Encryption Scheme.

* RSA
  - based on the _factorization problem_
  - RSA can only encrypt messages that are smaller than its modulus (eg. <256bits)
  - RSA wih padding (like PKCS#1) is vulnerable to adaptive chosen ciphertext attack (CCA2)

TODO read how RSA works!

* Standards
  - use [keylength.com](https://www.keylength.com/en/1/) to compute the size of the security parameter to use for your case.
  - RSA with OAEP (optimal assymetric encryption padding) is the current recommended standard for asymmetric encryption with RSA.
  - ECIES - eliptic curve integrated encryption scheme - popular hybrid encryption standard.

## Ch 7. Signatures and zero-knowledge proofs
- signatures are good for authenticating the origin and the integrity of messages
- popular signature scheme: ED25519.
- (use case) Authenticated key exchange: Alice sends her public key to Bob along with a signature of the public key using her private key.

* Public key infrastructure
  - based on the idea of transitivity of trust: authorities maintain a mapping of ids and public keys that they trust.
    - Eg. PKI - Web Public Key Infrastructure - a system of certificate authorities that maintain a mapping beetween website
  domains and thir signing key. Clients (browsers) trusts an authority to certify that some domain is linked to the public key presented by the website.

* Zero Knowledge Proof
  - _witness_ is the hidden information (secret) based on which statements are made.
  - proof of knowledge: the _prover_ convinces the _verifier_ it knows the _witness_ without revealing it.
  - a zkp scheme is sound if the prover can't cheat, ie. the prover can't convince the verifier it knows the witness even if it doesn't.

*  Schnorr Identification process aka. sigma protocol is an interactive zkp:

1. Peggy wants to prove to Victor that she knows x in `Y=g^x mod p`, without revealing x. Y, g and p are known to Victor
She generates a random k (nonce), computes a commitment R = g^k and sends R to Victor
2. Victor generates a random challenge c and sends it to Peggy.
3. Peggy computes a hidden witness: s = k + c * x and sends it to Victor
4. Victor verifies that g^s == Y^c * R because g^(k+c * x) == g^x^c * g^k

* Non-interractive zero-knowledge proofs (the Schnorr signature scheme)

1. Peggy wants to prove to Victor that she knows x in Y=g^x mod p, without revealing x. Y, g and p are known to Victor
She generates a random k, computes a commitment R = g^k. Does not send it to Victor, yet
2. Computes a random challenge herself as a hash: c = HASH(R, msg)
3. Computes the hidden withness s = k + c * x.
The signature that Peggy sends to Victor is a pair of (R, s) where R is a commitment to some secret random value
and s is a value computed with the help of the commitment R, the witness x acting as a private key and the message.

  - digital signature can be seen as just non-interractive ZKPs.
- "A digital signature does not uniquely identify a key or a message"

* RSA for signatures
  - hash the message, (optionally pad the hash) then ecrypt it with RSA.
  - standards: RSA-PKCS#1 v1.5 (broken!) RSA-PSS (PSS encoding based on PKCS#1 v2.1 similar to OAEP), FDH(Full-domain-hash, not used but simpler and secure).

* ECDSA as the eliptic curve version of DSA
  - private key is a large number x generated randomly; public key is [x]G, where G is the group's generator
  - generate a random number k (_nonce_ or _ephemeral key_) that is unique per signature. It has to never be repeated and it must be secret! Usually k is generated behind the scenes.
    - NOTE: this means signatures are not deterministic! because of this random nonce.
  - the signatures is pair of two integers (r, s):
    - `r` is the x-coordinate of the [k]G point on the curve.
    - `s=k^-1 * (Hash(message) + xr) mod p`
  - to check the signature, the verifier:
    - computes a point: `(Hash(message)*s^-1)*G + [r*s^-1]*public_key`
    - validate theat the x-coordinate of the point obtained above is the same as the value r of the signature.
  - main type of attack is targeted at k, RFC 6979 defines a way for k to be generated deterministically from the message and the private key.
  - curves used: P-256 (most populate, sometimes referred to secp256r1) and secp256k1 (used in bitcoin, ethereum, etc.).

TODO read about Schnorr signatures.

* EdDSA (Eddwards-curve DSA) - State of the art!
  - produces signatures that are deterministic.
  - curves used: Edwards25519 for 128 bits of security (most used in practice, called Ed25519, uses SHA-512 as a hash function), Edwards448 for 224 bits of security (Ed448)
  - first generate a secret key from which we derive a signing key and a nonce key.
  - compute the nonce: `HASH(nonce key || message)`
  - compute the commitment `R=[nonce]G` where G is the base point of the group.
  - compute the challenge `HASH( commitment || public key || message)`
  - compute the proof: `S=nonce+challenge*signing key`
  - the signature is the pair (R, S)

```
                                   (secret key)
                                         |
                                     +---v---+
                                     |SHA-512|     // note that this is not a KDF!
                +--------+           +---+---+
                |Multiply|               |
(public key)<---|with G  |<---(signing key|nonce key)
     |          +--------+                     |
     |                                     +---v---+
     | +----------------(message)--------->|SHA-512|
     | |                                   +---+---+
     | |                                       |
     | |                                    (nonce)
     | |                                       |
  +--v-v--+                               +----v---+
  |SHA-512|<-------------(commitment)<----|[nonce]G|
  +---+---+                               +--------+
      |
      v
 (challenge)
```

* Attacks:
  - most signature schemes are malleable: given a valid signature, it can be modified to create another valid signature (with a different, unknown private key).
  - do not rely on uniqueness of signatures!
  - key substitution attack: craft a different a different public key that validates an existing (message, signature).
  - message key substitution attack: craft a different (message, public key) that validates an existing signature.

## Ch 8. Randomness and secrets
- sources for hardware randomness: thermal noise, the photoelectric effect, quantum effect, etc.
- ASLR - address space layout randomization - randomize the memory layout of a process every time it runs.
- Acronyms:
  PRNG - pseudorandom number generator;
  CSPRNG - cryptographically secure PRNG,
  DRBG - deterministic random bit generator.
  TRNG - true random number generator (usually hardware randomness).

* PRNGs:
- use a hardware source to seed a pseudo-random generator that will produce a deterministic sequence of random numbers.
- properties:
  - deterministic: using the same seed twice generates the same sequence.
  - indistinguishable from random: PRNG simulates picking a number uniformly at random.
    It should be impossible to extract the internal state of the PRNG to determine future or past values in the sequence.
  - forward secrecy: if an attacker does get a hold of the internal state of the PRNG, it can't retrieve the previously generated random numbers.
  - backward secrecy: compromising the state of the PRNG does not allow predicting fugure random number. It's implemented by the ability to reseed the PRNG at any point.
- hash functions, XOFs, block ciphers, stream ciphers and MACs can be used to produce random numbers.
- key exchanges and signatures can't be used to produce random numbers.
- OSes clean and mix multiple sources of entropy, then use a hashing algorithm to provide a stream or random values (chacha20 in unix, sha-1 for macos).
- Stick to randomness provided by the OS: use `getrandom` instead of reading from `/dev/urandom` which can be predictable at boot time.
- NOTE: seeds shouldn't be predictable!
  Don't use the current timestamp as a seed! Reason: very little entropy, the top bits are always the say during the course of the day and the bottom bits are mostly 0 (usually increments are in ms instead of ns)

* Public randomness

- two types: on-to-many (VRFs) and many-to-many (Beacons - a set of participants want to produce randomness together)

- A _VRF_ - verifiable random functions use asymetric cryptography to publish randomness
  - generate a key pair and publish the verifying key (public key). Also publish a seed.
  - sign the public seed and hash the signature. The digest is the random number. Publish the signature as a proof.
  - to verify, anyone can hash the signature to check if it matches the random number.
```
    (private key)  (seed as message)        (proof)           (public key)   (seed as message)   (proof as signature)
             \      /                          |                    |               |                    |
              +----+                           v                    |               v                    |
              |Sign|                         +----+                 |            +------+                |
              +--+-+                         |Hash|                 +----------->|Verify|<---------------+
                 |                           +-+--+                              +------+
(signature)<-----+                             |                                    |
(as proof )      |                             v                                    v
                 v                       (should match )                          (true?)
              +----+                     (random number)
              |Hash|
              +--+-+
                 |
                 v
          (random number)
```
  - the source of randomness is the private key!
  - because the signature is unique (you need to use deterministic signature schemes like BLS - Boneh-Lynn-Shacham)
  and the public seed is fixed, there is no way for the signer to generate a different random number.
  - you end up with chains of randomness, where the previously generated random number is used as the seed to the next generation.

* Descentralised randomness beacons
  - The aim is to produce the same verifiable randomness even if a subset of participants won't take part in a protocol round.
  - Uses a threshold distributed key: a key that is split between multiple participants:
  Any large enough subset of participats (above a threshold) and combine their key shares to produce a valid signature.

* Key derivation with HKDF (HMAC-based Extract-and-Expand Key Derivation Function, RFC5869)
  - it's similar to PRNG except that it does not expect a uniformly random secret/seed.
  - it's usually used when participants need to rederive the same keys several times (like a crypto wallet).
  - derives a limited number of keys.
  - it has two steps: extract and expand
  - Extract
    - remove biases from input, producing a uniformly random secret, usually via hashing
    - accepts an optional (but use it!) parameter `salt` meant to differentiate different uses of Extract in the same protocol (domain separation)
    - doesn't have to be secret!
  - Expand
    - produces an arbitrary length and uniformly random output
    - accepts an optional `info` parameter meant to differentiate the current version of HKDF from others.
  - Q: What if as a client I only have access to a derived public key and I want to check a signature made with the original private key?
```
(input)            (salt)
(key  )               |
   |  +------------+  |
   +->|HKDF-Extract|<-+
      +-----+------+
            |
      (pseudo-random)   (info)     (output)
          (key)         (string)   (length)
            |              |           |
            |              v           |
            |        +-----------+     |
            +------->|HKDF-Expand|<----+
                     +-----+-----+
                           |
                           v
                  (output key material)
```
  - HKDF outputs are deterministic! Given the same input key, salt, info string and output length, the same key should be obtained.
  - Password-based KDFs (like Argon2) use passwords instead of the input key. This is a mechanism to create an asymmetric key from a symmetric key

* Key management: key rotation, key revocation, key specialization for separate roles, key delegation.

* Threshold cryptography
  - secret sharing (or secret splitting): split the secret in n chunks. Eg: SSS - Shamir's Secret Sharing
  - naive multi-signature (or multisig) systems: accept n signatures from n different public keys.
  - signature aggregation: compress multiple signature down to a single one.
  - distributed key generation (DKG): allow n public key sto be aggregated into a single public key. Field: secure multi-party computation.
  - all of these can be made to work when only a threshold m (m <= n) of participants are online or not malicious.

## Ch 9. Secure transport - TLS

- Application-level, session-based protocol
- TLS uses TCP for transport, there exists DTLS that uses UDP for transport.
- two layers: handshake phase (where a secure communication channels is negotiated) and post-handshake phase (encrypted communication).

* TLS handshake
  - protocols negociation
    - the version of SSL/TLS to be used. SSL, TLS1, TLS1.1 are supported for backwards compatibility but are insecure and are deprecated (March 2021)
    - one or more key exchange algo. TLS1.3 supports ECDH with curves P-256, P-384, P-512, X25519, X448, FFDH.
    - two or more digital signature algorithms and the hash functions to use. TLS1.3 supports RSA PKCS#1 v1.5, RSA-PSS, ECDSA, EdDSA
    - one or more hash functions to be used with HMAX and HKDF (different from signatures). TLS1.3 supports SHA-2-256 and SHA-2-384.
    - one or more authentication encryption algorithms. AES-GCM (128 and 256bits), ChaCha20-Poly1305 and AES-GCM.
  - key exchange
    - client sends a `CLIENT_HELLO` message with a range of protocols it supports.
    - server responds with `SERVER_HELLO` by picking the protocols to use. If it can't pick, the connection is aborted.
    - ALL KEYS ARE EPHEMERAL. Using HKDF to derive temporary keys for each session from the server's main private key!
      This gives _forward secrecy_ meaning that if the server's main private key is compromised, it can't be used to decrypt old sessions.
    - `CLIENT_HELLO` and `SERVER_HELLO` are not encrypted, but the rest of the handshake is!
  - authentication. The client (browser) must have a way to ensure that it is talking to a specific domain.
    - in web PKI, only the server authenticates. mTLS (mutually-authenticated TLS) is a way for both client and server to authenticate.
    - browsers trust a set of root public keys - usually hardcoded. These are called _certificate authorities_ or CAs.
    - websites must obtain a certification - a signature of their public key - from an authority.
    - the server sends a certificate chain to the client: from the hardcoded CA to intermediate CAs down to the domain.
      Each certificate in the chain contains useful metadata, a public key and a signature from the previous step in the chain.
    - once the authentication happens, the server sends a new derived session symmetric key, signed with the server's permanent private key that the client can validate.
    - at the end, the server sends a Finished message with an HMAC of all the authentication communication.
      The client then verifies this MAC! An error means the communication was tempered with, so the connection is aborted.
    - X.503 certificates are widely used, but are difficult to implement correctly. If given a choice, don't use them!
  - session resumption. The handshake is expensive so for clients reconnecting to the same server, there are mechanisms to fast-track a secure session.
    - TLS v1.3 supports pre-shared keys (PSK), useful for service-to-service communication and/or session resumption.

* Post handshake
  - TLS ensures messages can't be replayed or reordered using a nonce that starts at a fixed value an is then incremented for each new message. On error, the connection is killed.

* State of encrypted web.
  - The first request to an HTTP server is usually unencrypted. The server usually redirects to HTTPS, using HSTS (HTTP strict transport security) header.
  - NTP (time) and DNS (names) are not encrypted.
  - _Certificate revocation_ allows CAs to invalidate a certificate and ward browsers about it.
    OCSP (online certificate status protocol) is a protocol for clients to query CAs and check if a certificate is still valid.
    OCSP stapling - the website is responsible for providing the client with a signed statement from a CA that the certificate is still valid.
  - _Certificate monitoring_ forces CAs to publicly log every signed certificate. They then need to provide a SCT (signed certificate timestamp and log id) for browsers to (optionally) check.
    This is called Certificate Transparency (or CT)
  - _Certificate pinning_ only allow secure comminication with specifig certificate or public keys.

* Other secure protocols are similar to TLS:
  - Secure Shell (SSH)
  - Wi-Fi Protected Access (WPA)
  - IPSec - popular VPN protocol. OpenVPN is also popular and used TLS dirrectly!

* Noise protocol framework - modern alternative to TLS
  - no negociation for cryptographic algorithms, they are all decided at instantiation by the server.

TODO: learn more about Noise

## Ch. 10 End-to-end encryption

- _root of trust_ is the concept that at some point you need to trust something and build security on top of that. There is no global root of trust.
- _attestation_: a trusted authority attests that a public key belongs to a given identifier (like an email address or a phone number).

* Encrypted email: S/MIME, PGP
  - PGP (Pretty Good Privacy) - application to encrypt email. OpenPGP - standard for email encryption (1998, RFC2440), GPG - GNU privacy guard - an OSS implementation of OpenGPG.
    - the mechanism is hybrid encryption, but uses old cryptographic primitives.
    - to send to multiple recipients, it encrypts the same message for each public key, concatentes them and sends the blob to everyone!
    - the subject and the email's metadata is not encrypted! Plaintext metadata can deannonymise you!
    - encryption is not authenticated. Signatures can be added to the plaintext, but the intended recipient can be changed by an attacker.
    - OpenPGP does not provide forward secrecy by default, so if a key becomes compromised, the attacker can read all previous messages.
  - WOT - web of trust - you meet people IRL and you exchange keys, then you delegate trust to their network of trusted peers.
  - key registry: a mapping betweekn identities and public keys, along with signatures from as many people as possible to attest the validity of the association.
  - alternative: keybase

* Signal protocol
  - _federated protocols_ - no central entity is required for the network to work! Eg. Matrix protocol. Signal is centralized, with a single server and a single client application.
  - TOFU - trust on first use - two users blindly trust each other the first time they communicate in order to establish a long-lasting secure communication channel.
    Later on, users can check if the first exchage was MITM-ed, by checking their session secret (or fingerprint) out-of-bound (ie. IRL).
    - fingerprint - hex encoded public key or hash of a public key.
  - Goal: non-interactive (ie. asynchronous) forward-secrecy (past sessions cannot be decrypted by a compromised key) and backward-secrecy (or PCS - post-compromise security - future sessions cannot be decrypted by a compromised key).
  - X3DH - Extended Triple Diffie-Hellman
    - identity keys: long-term keys that represent users. The corresponding public keys are uploaded to Signal.
    - one-time (or ephemeral) prekeys: single-use, ephemeral keys uploaded to Signal and deleted after being used. This is used when the recipient of a new conversation is not online.
    - signed prekeys: a medium-term public key uploaded to Signal and signed with the user's identity key. It's used to generate new one-time prekeys if none already exist. This key is periodically rotated.
    - when you sign up for Signal, you upload an identity key, a signed prekey and a set number of one-time prekeys:
    - the x3dh key exchange is composed of multiple ECDH key exchanges: (TODO: why this very complex protocol)
```
                                    +--------------------+
                                    |                    |
(alice's)   (bob's        )   (alice's      )   (bob's ) |   (bob's           )
(id key )   (signed prekey)   (ephemeral key)   (id key) |   (ephemeral prekey)
    |             |                  |             |     |           |
    |   +----+    |       +----+     |   +----+    |     |   +----+  |
    +-->|ECDH|<---+------>|ECDH|<----+-->|ECDH|<---+     +-->|ECDH|<-+
        +--+-+            +-+--+         +-+--+              +--+-+
           |                |                |                  |
           |                |                |                  |
           +----------------+--->(concat)<---+------------------+
                                   |
                                   V
                                 +---+
                                 |KDF|
                                 +-+-+
                                   |
                              (session key)
```

  - Symmetric ratchet
    - Signal has forward secrecy at the message level.
    - after obtaining the session key, both Alice and Bob, use KDF to each create root keys for sending and receiving chains.
    - every time Alice sends a message, she also sends her ratchet so Bob can perform a DH with his current racket key and generate a new key in his receiving chain.

TODO: Read the Signal protocol spec.

## Ch. 11 User authentication
- message/payload authentication: proving that a message is genuine and hasn't been modified since its creation.
- origin/entity/identity authentication: proving that an entity is who they say they are. Eg. a domain name
- user authentication or how machines authenticate users
- user-aided authentication or how humans help machines authenticate to one-another.

* SSO - single sign-on
  - federated protocol that allows a user to use one account (eg. Google) to register or log into other services.
  - SAML - Security assertion markup language 2.0. Legacy but still used a lot in enterprise!
  - OpenID Connect (OIDC) - an extension to OAuth 2.0. [openid spec](https://openid.net/). Used widely!

* PAKE - password-authentication key exchange
  - users don't have to communicate their password to the server at all.
  - with asymmetric PAKE, the server doesn't know the password at all. With symmetric PAKE, the server knows the password, but user doesn't have to communicate it to log in.
  - recommended: CPace - symmetric/ballanced PAKE, OPAQUE - asymmetric/ballanced PAKE

* OPRF - Oblivious pseudo-random function (PRF - pseudo-random function)
  - _oblivious_ refers to protocols where one party computes an operation without knowing the input provided by another party.
  - implementation in a group with the discrete logarithm problem:
    - Alice converts her input to a group element x
    - Alice generates a random blinding factor r, computes `blinded_input = x^r`, then sends it to Bob
    - Bob computes `blinded_output = blinded_input^k`, where k is Bob's secret key. He sends the output back to Alice
    - Alice unblinds the result by doing `output = blinded_output^(1/r) = x^k`.

* OPAQUE [rfc](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-opaque-02)
  - at registration:
    - Alice generates a long-term key pair and uploads the public key on the server. The server stores it associated with her username.
    - Alices uses OPRF to obtain a strong symmetric key from her password, derives a key pair from that using a password based KDF (like Argon2), encrypts it and sends it to the server.
  - at login:
    - Alice downloads the encrypted key pair corresponding to her username.
    - Alice performs OPRF with her password to obtain a symmetric key capable of decrypting her key pair. She decrypts her key pair.
    - Alice signs a challenge from the server with here decrypted private key. The server checks the challenge with Alice's public key.
    - Alternatively, Alice can engage in a key exchange with the server using her encrypted key pair.

  - server sends Alice a unique salt (to prevent precomputation attacks)
  - Alice uses the salt to derive an asymmetric private key from her password using a password-based KDF (like Argon2)
  - Alice sends her public key to the server for storage.
  - Alice and the server perform an OPRF protocol at the end of which an encrypted key pair uniquely identifying Alice is uploaded to the server.

TODO: research OPAQUE

* OTP - one-time passwords
  - the server generates a symmetric key and sends it to the client (say via a QR code)
  - Alice derives an one-time password from her symmetric key and some additional data and sends it to the server.
```
(additional data)-->+-------------+
                    |OTP algorithm|----->(OTP)
(symmetric key)---->+-------------+
```
  - two variants: HOTP - the additional data is a counter; TOTP - where the additional data is time.
  - TOTP is the most used (eg. by the Google authenticator app)
    - on registration, the server sends Alice a symmetric key (16 or 32 byte long) via a QR code.
    - Alice uses the TOTP app to compute an OTP: HMAC(symmetric key, timestamp). The timestamp is rounded to the minute, so the OTP is valid for a minute. Also, to account for clock skew.
    - the TOTP app displays to the user a ping: a truncated and human-readable version of that hash digest, usually 6 digits.
    - Alice pastes the pin in the app
    - the server generates the TOTP the same say and compare it's result with Alice's input.
  - the server can fake an OTP because it has the symmetric key.

* Post-handshake user authentication with FIDO2 - fast identity online v2
  - connection is secured and one party is authenticated - think TLS1.3 with the server authenticated via web PKI.
  - uses hardware authenticators: roaming authenticator (eg. yubikey) or a built-in authenticator (mac keyboard fingerprint touch).
  - two protocol standards:
    - CTAP (Client to Authenticator Protocol): a way for roaming authenticators and clients (OSes, browsers, etc.) to communicate.
    - WebAuthn (Web Authentication): a way for web apps to authenticate using hardware authenticators.

* User-aided authentication:
  - how humans can help machines upgrade an insecure connetion into a mutually authenticated connection.

* CPace - composable password authenticated connection establishement
  - a version of password-authenticated key exchange (PAKE) that uses symmetric keys (ie. passwords)
  - two devices derive a generator based on a common password in some predefined, hardcoded, cyclic group. Known as _hash to curve_ algorithm.
  - then the two devices perform an ephemeral DH key exchange.
  - Eg. used when connecting to the wifi router.

* SAS - short authenticated strings
  - based on TOFU: devices assume a secure channel and perform the initial key exchange, then, in post-handshake, you compare the fingerprints (hashed of the shared secret on both devices).
  - because fingerprints are long and hard to compare, a short string is derived from them.
  - a SAS string is tipically a 6-digit number so it's easy to hack.
  - the standard (MA-DH - manually authenticated diffie-hellman) has Alice send a commitment of a public key to Bob.
    Once Bob sends his public key to Alice, Alice can then reveal her public key and the DH key exchange can proceed.
    Finally, Alice and Bob compare SAS pins.

## Ch 12. Cryptocurrencies

* BFT
  - consensus algorithm, log replication, state machine replication, atomic broadcast are all synonyms.

* Merkle trees
  - the idea is to reduce the size of data needed to check that a transaction is in a block.
  - to check the inclusion of a tx in a block you need the subtree from the root to the leaf, together with all the other heighbour hashes, O(logn).

* Diem BFT - based on the Hotstuff BFT protocol.
  - safety: no contradictory states can appear, ie. no forks.
  - liveness: the system never stops processing transactions.

  - a round in DiemBFT:
    - a validator is chosen deterministically to lead a round.
    - it collects a number of txes from clients and builds a block.
    - signs the block and sends it to all the other validators.
    - a non-leader validator votes on the receiving proposed block by signing it with its key and sending the sig to the leader of the next round.
    - if the leader in the next round receives sufficient sigs, it bundles them in a QC (quorum certificate) which certifies the blockj
    - the new leader uses the QC from the previous block to start building a new block. Ie. the new block contains the QC of the previous block, hence building a chain.
    - if the round times out and not enough votes are received.

  - rules of voting:
    - voters can't vote in the past
    - voters can only vote for a block extending a block at their preferred round or higher.
    A _preferred round_ is the round of the block that is the grandfather of the block you are voting on now.
```
round 1    round 3    round 4    round 6
+-----+    +-----+    +-----+    +-----+        // if you voted on round 6, your preferred round becomes 3
|Block|<-+-|Block|<-+-|Block|<---|Block|        // hence you can vote for round 8, but not round 7 (because that expands block 2)
+-----+  | +-----+  | +-----+    +-----+
         |          |
         | round 7  | round 8
         | +-----+  | +-----+
         +-|Block|  +-|Block|
           +-----+    +-----+
```

  - finalization
    - blocks that are certified (or pending) are not yet finalized (or committed).
    - a block and all the pending blocks it extends become commited if:
      - a block starts a chain of 3 blocks that are proposed in contiguous rounds
      - the last block of a 3-block chain becomes certified.
```        round 2
         +-+-----+
         | |Block|
         | +-----+
         |
round 1  | round 3    round 4    round 5    round 9     // rounds 3, 4 and 5 have a chain of certified blocks.
+-----+  | +-----+    +-----+    +-----+    +-----+     // a validator observing the QC of round 5 in round 9
|Block|<-+-|Block|<---|Block|<---|Block|<---|Block|     // can commit the round 3 block and it's ancestors (here round 1).
+-----+    +-----+    +-----+    +-----+    +-----+     // the round 2 block gets discarded
```

  - two different blocks can't be certified during the same round.

TODO: read the DiemBFT protocol

## Ch. 13. Hardware cryptography
- the _evil maid_ attack: an attacker has temporary access to your hardware
- _white box_ cryptography: scramble a crypto implementation with the keys it uses,
  so that even if the attacker obtains the source code, it can't determine the key. No white box algo has be proven to be secure!
- security through obscurity and obfuscation: scrambling the code to make it look unintelligible.
- _digital rights management_ - DRM - how much access a customer can get to a product they bought?!
- HSM - hardware security model - hardware designed to make it hard for an attacker to steal keys. Eg. verify card pins, root CAs key storage, TLS termination
- TPM - trusted platform module - a standard spec for secure hardware with a well defined interface. Cheap separate chips, found in most laptops and phones.
  The module can generate and store keys securely, can perform cryptographic primitives. Eg. Microsoft Pluton, Apple Secure Enclave.

* TEE - trusted execution environments - circuitry in the CPU designed for secure cryptography, exposed to the programmer as an extra instruction set.
  - Eg. Intel's Software Guard Extensions (SGX), ARM's TrustZone.
  - goal: users running code on cloud servers that's can't see or tamper with that code.
  - How do you trust that the response came from an enclave in the CPU or from an impersonator? _Attestation_:
    - local attestation: two enclaves running in the same CPU prove to each other that they are secure.
    - remote attestation: the client needs to know that the remove enclave produced the output.
    Since each enclave is proviced with unique keys at manufacturing (_Root sealing keys_) and the public,
    key part is signed by Intel's own CA, clients can check the signature of the enclave.

* Leakage-resistant crypto
  - _side channel_ - indirectly leak information about a key so that an attacker can reconstruct the key.
    - DPA - differential power consumption - power consumption
    - returned errors can leak critical information.
    - timings attacks: the time it takes for a request to be processed can leak information. Avoid returning early! Use constant time algorithms.
    - cache attacks: a cache miss can tell the attacking observer that the victim is performing an operation it hasn't before.
    - fault attacks: injecting faults into the CPU (via chaning temperature, voltage, shooting laser beams at specific points, etc.)
  - software mitigations:
    - constant time programming: make sure that the part of the code that deals with secrets doesn't branch, instead always performs both operations.
    - blinding: don't use the secret dirrectly instead combine it with a random blinding factor. Eg. base binding and scalar binding
    - masking: modifying the input of a crypto operation in a way that the modification can be removed from the result. Eg. XORing the input with a random value.

## Ch. 14. Quantum cryptography
- quantum physics phenomena: superposition and entaglement
- _quantum supremacy_: a quantum computer achieved something that a classical computer couldn’t.
- symmetric cryptography is mostly fine, asymmetric cryptography is not.

* One-time signature or Lamport Signature (OTS - Lamport, 1979)
  - signing a single bit b:
    - generate two random numbers (256bit each), one for b=0, r0 and one for b=1, r1. The private key is (r0, r1)
    - hash them: h0 = Hash(r0), h1 = Hash(r1). The public key becomes (h0, h1).
    - to sigh b, reveal the part of the private key corresponding to the value of b. If b==0, then sig=r0, otherwise sig=r1.
    - to check the signature, the input is the bit b, the public key (h0, h1) and the signature sig. Depending on the value of b, the verifier checks that sig=Hash(r0) or sig=Hash(r1).
  - this can only be used once as it reveals half of the private key (since it's the signature).
  - the size of the key pairs is very large.

* Winternitz one-time signatures (WOTS)

## Ch 15. Next generation cryptograpy

* MPC - Secure multi-party computation

## Resources:
- [crypto book by Boneh](http://toc.cryptobook.us/)
- [Boneh course on Coursera](https://www.coursera.org/learn/crypto)
- [Intro to crypto](https://livebook.manning.com/book/real-world-cryptography/welcome/v-9/8)
- [Verifiable Random Functions Internet draft](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-vrf-10)
- [drand](https://drand.love/) is a unpredictable, publicly verifiable, bias-resistant, decentralized and always available source of public randomness.
- [signal docs](https://signal.org/docs/) the most popular end-to-end encrypted application.
