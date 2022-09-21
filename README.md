# Python Ceasar's Cipher 🐍📘

*Day 8 of 100 days of Code*

This is Ceasar's Cypher created with Python. 
The prorgam allows a user to either encode or decode a message based on a certain 
shift number. For encoding the program will shift the letters forward for by the determined amount. 
To decode, the program will shift the letters back by the gievn shift amount. 

To account for new index positions after the shift that are greater than the lists last index position, 
the modulo operator was used. The list contains a final index number of 25. For new index of 26 or greater the 
index position becomes new_index % 26.

The program also makes use of a while loop so that the user can eneter multiple messages to encode or decode 
before the program exits. 

What I learnt 🧑‍💻: 
- While Loops 
- Using functions and returning outputs 
- Accounting for capitalisation with user input using .lower() and .upper()
