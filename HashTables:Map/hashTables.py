'''
Generating a value from a string using a mathematical formula is called hashing

A hash function takes a string of characters and maps it to a value of a certain length ( called a hash value )

A good hash function is easy to compute, uniform distribution, and low collisions

------------------------
  COLLISION HANDLING
------------------------

Chaining is one technique to handle collisions where each cell fo the table will point to a linked-list

Open addressing is another technique where the values are stored in the hash table. If a hash index is available, the value is inserted into the table directly.
If not available, probe the table until you find an empty index.

Linear Probing is a way to probe the hash table.
Quadratic probing and double hashing are other probing techniques. 

Chaining                                   |         Open Addressing
----------------------------------------------------------------------------------------------------
Simple to implement                        |    - Requires more computation  
Hash Tables never get full                 |    - Hash tables can get full
Cache performance of chaining is not good  |    - Open addressing provides better cache performance
Uses extra space                           |    - No extra space is required
Mostly used when the number of keys is     |    - Mostly used when the frequency and number of keys is unknown
unknown
'''
