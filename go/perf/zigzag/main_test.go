package main

import (
  "bytes"
  "encoding/binary"
  "fmt"
  "runtime"
  "sync"
)

type testrange struct {
    start int64
    end   int64
}

func zigzagExhaustiveTest() {
    runtime.GOMAXPROCS(8)

    var wg sync.WaitGroup

    fnRangeTester := func(fnum int, tr testrange, chfailures chan string) {
        fmt.Printf("FN %d STARTED\n", fnum)
        defer wg.Done()
        buf := new(bytes.Buffer)
        for i := tr.start; i != tr.end; i++ {
            buf.Reset()

            in := i
            zzin := varint.ZigzagEncodeUInt64(in)
            err := varint.VarintEncode(buf, zzin)
            if err != nil {
                chfailures <- fmt.Sprintf("Failed on %d: varintEncode err: %v", i, err)
            }

            zzout, err := ReadVarIntToUint(buf)
            if err != nil {
                chfailures <- fmt.Sprintf("Failed on %d: ReadVarIntToUint err: %v", i, err)
            }
            if zzin != zzout {
                chfailures <- fmt.Sprintf("Failed on %d: ReadVarIntToUint zzin != zzout: %d != %d", i, zzin, zzout)
            }

            out := varint.ZigzagDecodeInt64(zzout)
            if in != out {
                chfailures <- fmt.Sprintf("Failed on %d: ReadVarIntToUint in != out: %d != %d", i, in, out)
            }
        }
        fmt.Printf("FN %d is DONE\n", fnum)
    }

    ranges := []testrange{
        {-9223372036854775808, -6917529027641081856},
        {-6917529027641081855, -4611686018427387904},
        {-4611686018427387903, -2305843009213693952},
        {-2305843009213693951, -1},
        {0, 2305843009213693952},
        {2305843009213693953, 4611686018427387904},
        {4611686018427387905, 6917529027641081855},
        {6917529027641081856, 9223372036854775807},
    }

    wg.Add(len(ranges))
    failchan := make(chan string, 10)

    for i, trange := range ranges {
        go fnRangeTester(i, trange, failchan)
    }

    go func() {
        wg.Wait()
        close(failchan)
    }()

    // main thread monitors for failures, waiting for the failchan to be closed
    for failmsg := range failchan {
        fmt.Println(failmsg)
    }
    fmt.Println("DONE")
}

func ReadVarIntToUint(r io.Reader) (uint64, error) {
   var (
       varbs []byte
       ba    [1]byte
       u     uint64
       n     int
       err   error
   )

   varbs = make([]byte, 0, 10)

   /* ---[ read in all varint bytes ]--- */
   for {
       n, err = r.Read(ba[:])
       if err != nil {
           return 0, oerror.NewTrace(err)
       }
       if n != 1 {
           return 0, oerror.IncorrectNetworkRead{Expected: 1, Actual: n}
       }
       varbs = append(varbs, ba[0])
       if IsFinalVarIntByte(ba[0]) {
           varbs = append(varbs, byte(0x0))
           break
       }
   }

   /* ---[ decode ]--- */
   var buf bytes.Buffer
   if len(varbs) == 1 {
       buf.WriteByte(varbs[0])

   } else {
       var right, left uint
       for i := 0; i < len(varbs)-1; i++ {
           right = uint(i) % 8
           left = 7 - right
           if i == 7 {
               continue
           }
           vbcurr := varbs[i]
           vbnext := varbs[i+1]

           x := vbcurr & byte(0x7f)
           y := x >> right
           z := vbnext << left
           buf.WriteByte(y | z)
       }
   }

   padTo8Bytes(&buf)
   err = binary.Read(&buf, binary.LittleEndian, &u)
   if err != nil {
       return 0, err
   }
   return u, nil
 }

func VarintEncode(w io.Writer, v uint64) error {
   ba := [1]byte{}
   nexp := 0
   ntot := 0
   for (v & 0xFFFFFFFFFFFFFF80) != 0 {
       ba[0] = byte((v & 0x7F) | 0x80)
       n, _ := w.Write(ba[:])
       ntot += n
       nexp++
       v >>= 7
   }
   ba[0] = byte(v & 0x7F)
   n, err := w.Write(ba[:])
   ntot += n
   nexp++
   if err != nil {
       return oerror.NewTrace(err)
   }
   if ntot != nexp {
       return fmt.Errorf("Incorrect number of bytes written." +
                         " Expected %d. Actual %d", nexp, ntot)
   }
   return nil
}
