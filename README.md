# A-Simple-Blockchain-in-Python

Blockchain is the methodology to maintain and propagate the movement of the cryptocurrencies accross the world along with maintaining the integrity. The transaction details of the digital currencies from one party to another is recorded and protected using a Hash key. Blockchain contains a group of blocks linked together containing the trivial information. The transaction details are open to everyone but are immutable because the information is linked to the hash key. If the information is altered the Keys change and hence it can be determined by the miners that the information has been altered.

There are various methods to find the Hash Key of the Block using the previous key and the transaction details. But it requires huge computations.


# Implementation


This is an implementaion of a Simple Blockchain in which each block has 3 parameters. 1st is the Hash of the previous Block, 2nd is the transaction details and 3rd is the Hash of the current Block. 

The Hash has been calculated using the sha256 algorithm. It is 64 bit length of numbers and characters.
