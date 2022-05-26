# hash-collision-proof

> In computer science, a hash collision or clash[citation needed] is when two pieces of data in a hash table share the same hash value. The hash value in this case is derived from a hash function which takes a data input and returns a fixed length of bits.[1]. Although hash algorithms have been created with the intent of being collision resistant, they can still sometimes map different data to the same hash (by virtue of the pigeonhole principle). Malicious users can take advantage of this to mimic, access, or alter data.[2]

[Hash_collision](https://en.wikipedia.org/wiki/Hash_collision)

Example: 
Hash Collision Proof - 2 strings having same value:

Enter 2 strings seperated by space, ex: hello world --- hello elloh
h 1 104 104
e 2 101 306
l 3 108 630
l 1 108 738
o 2 111 960
960 hello
e 1 101 101
l 2 108 317
l 3 108 641
o 1 111 752
h 2 104 960
960 elloh
Strings have same hash value.

