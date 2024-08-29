Section 3


3.1
1. Input data (e.g. a string)
2. Convert each character to its ASCII value, and sum these values. Then use a measurable operation to fit these values into a fixed range.
Handling Collisions:
1. Chaining - colliding values are put into a list with the same table index. Chaining uses extra memory for the list of collisions = not space efficient
2. Open addressing - uses probes to find another empty slot in the table.
All elements are stored directly in the hash table = more space efficient 

3.2
Table size = 10 
Hash function = hash(key) = key % tabl size
Linear probing 

Hash Table = [n, n, n, n, n, n, n, n, n, n]

Insert Key: 23:
- Compute the hash value: hash(23) = 3 % 10 = 3
- Insert 23 at index 3

= Hash Table = [n,n,n, 23,n, n, n, n, n, n]

Insert other keys e.g; 35

Compute the Hash Value: hash(35) = 35 % 10 = 5
Insert 35 at index 5

Hash Table = [n,n, n, 23, n, 35, n, n, n, n]

3.3
Insert 13
Compute the Hash Value: hash(13) = 13 % 10 = 3
Index 3 is already occupied
Use Linear Probing
Insert 13 at next index
Hash Table: [n,n,n, 23, 13, 35,n,n,n,n]
