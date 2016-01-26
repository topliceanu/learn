#/bin/bash
set -e

./ex17bis /tmp/db c
./ex17bis /tmp/db s 0 alex alex@gmail.com
./ex17bis /tmp/db s 1 topli topli@gmail.com
./ex17bis /tmp/db s 2 alext alex@vibtrace.com
./ex17bis /tmp/db l
./ex17bis /tmp/db g 0
./ex17bis /tmp/db g 1
./ex17bis /tmp/db g 2
./ex17bis /tmp/db f gmail
./ex17bis /tmp/db f alex
./ex17bis /tmp/db d 0
./ex17bis /tmp/db l

rm /tmp/db
