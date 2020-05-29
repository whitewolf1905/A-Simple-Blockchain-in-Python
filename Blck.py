from Block import Block


Blockchain = []

genesis_Block = Block("Some Random String", ["A sent 100 BTC to B"])      						# Creation of Genesis Block using some Random Transatcion Data 

print("Hash of the Genesis_Block ", genesis_Block.current_hash) 								# Hash of Genesis Block


Blockchain.append(genesis_Block)


x = Blockchain[0]

# Building the Blockchain

for i in range(0, 100):
	y = Block(x.current_hash, [str(i) +" sent " + str(10*i) + " BTC to " + str(i+3)])
	Blockchain.append(y)
	x = y

print("\nPrevious Hash, Transatcion details and current hash of 1st 5 blocks\n")
for i in range(1, 11):
	print("Previous Hash of " + str(i) + " Block is ", Blockchain[i].previous_hash)
	print("Transatcion details of " + str(i) + " Block is ", Blockchain[i].transaction)
	print("Hash of " + str(i) + " Block is ",  Blockchain[i].current_hash)						# Hash of other blocks of Blockchain
	print("\n")



