# Category theory for programmers

## Chapter 1.
- there are 4 components of a category:
  - a set of objects; objects can be anything
  - a collection of arrows (morphisms) between these object; ie. a way for the objects to relate to each other. `a -> b`
  - composition (a rule for glueying arrows together): `f: a -> b and g: b -> c then f . g = h, h : a -> c`. If f and g exist then h must exist too.
  - the existance of an identity morphism: for every object in the category, there exists a morphism that relates the object to itself. `id : a -> a`
- a category is a set of objects, the arrows between these objects (or morphism), a rule for arrow composition and an identity arrow
- properties of composition:
  - closure/totality: the composition of any two morphism is a valid morphism.
  - associativity: `f . (g . h) = (f . g) . h` 
  - the existance of an identity morphism: `f . id = f = id . f = f`
- there is a relationship between functional purity and memoization.
  
## Chapter 2. Types and Functions
- Q: somehow bottom value `_|_` is linked to recursion and non-terminating functions; how?
  - A: a recursive function may not terminate; a non-terminating function returns bottom. Bottom is used for runtime crashes and infinite loops.
  - every data type is "lifted" to include the bottom value.
  - the Bottom type is a type with a single value "bottom" and it's a subtype of every other type in the system.

- "denotational semantics" vs "operational semantics"
  - operational: how a program executes it's steps and changes to its state.
  - denotational: how a program calculates, the meaning of a program is strictly built from the mathematical meaning of its smaller parts.

- the Void type, ie. the type that has no members.
  - you can never call `absurd :: Void -> a` because you can't product a value of type Void.
  - "ex falso sequitur quodlibet" - from falsity follows nothing.

- the `unit` type, denoted as `()` has one member, the unit `()` 
- functions that can be implemented for any type are called `parametrically polymorphic`.

**Challenges**
5. How many different functions are there from Bool to Bool?
A: There are 4 functions: `always_false :: _ = false`; `always_true :: _ = true`; `inv true = false; inv false = true`; `id true = true; id false = false`.

## Chapter 3: Categories Great and Small
- a "free category" (aka a "path category"): if the set is a graph, the morphisms are all the possible directed paths through the graph.
  - Formally, for any two values in the set, take all the dirrect and indirect paths between the two values.

- orders 
  - `preorder` (or quasiorder): reflexivity, transitivity. Eg. a directed graph, cycles are allowed, there are nodes where there is not path between them.
  - `partial order` (poset): reflexivity, transitivity and antisymmetry. Eg. a tree (directed graph), no cycles but also there exist two elements without a path between them.
  - `total order` (linear order): reflexivity, transitivity, antisymmetry, connexity. Eg. a strict line where everything can be ranked.
where:
  - `reflexifity`: every element in the set has a relation to itself (ie. existance of identity or a neutral element). Eg. a <= a, for all a.
  - `transitivity`: if a relates to b and b relates to c then a related directly to c. Eg. a <= b and b <= c then a <= c.
  - `antisymmetry`: two distinct elements can't point at each other, otherwise they are the same element. Eg a <= b and b <= a then a == b.
  - `connexity`: any two distinct elements in the set must have a relation to each other. Eg either a <= b or b <= a for any a and b.

- **monoid**: a set + a binary operation (has associativity and reflexivity)
  Eg. natural number form a monoid under addition (the neutral element being 0)
  - it's called a monoid because it has a single operation (as opposed to rings/fields which have two!). Also, because a monoid can be seen as a category with a single object.
  - monoids are useful in parallel processing of data, because individual datum processed by different processes can be combined in any order they arrive at the aggregator.
  - two methods: `mempty :: m` and `mappend :: m -> m -> m`

- arguments of function are sometimes called `points`, as in the evaluation of a function f at point x. Function equality without specifying the arguments is called `point free`.
- monoid can be seen as category with a single object `*` and an infinite number of loop arrows from * to *; eg. the arrow `5` is a loop from * to * five times. Similar to Church numerals, a number is a behaviour.

TODO: challenges in chapter 3

## Chapter 4: Composition of logs

- Kleisli categories: a category based on a monad: the objects are nothing special, but the composition of morphisms is more complex than just passing the output of one to the input of the next.
- a partial function is one that is not defined for all possible input values that it can have.
