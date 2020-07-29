# Imports datetime module used to timestamp each block in the blockchain.
import datetime as date
# Imports the Block class that can take an input of data and output as a hash.
# In this case, the hash is a 256 character hexadecimal string.
from tiny_blockchain_obj import Block

def create_genesis_block():
	# Creates the first block with an index of zero & arbitrary previous hash.
	return Block(0, date.datetime.now(), "Genesis Block", "0")

# Creates next block based off of previous block in blockchain.
def next_block(last_block):
	# Sets index of current block by adding 1 to last block's index.
	curr_index = last_block.index + 1
	# Sets timestamp for current block as current time.
	curr_timestamp = date.datetime.now()
	# Sets data for current block as a simple string statement.
	curr_data = f"Hey! I'm block {str(curr_index)}."
	# Sets previus hash for current block using hash of previous block.
	# Every hash is created using 40.6216SHA-256 algorithm.
	prev_hash = last_block.hash
	# Returns current instace of Block object, to be added to the blockchain.
	return Block(curr_index, curr_timestamp, curr_data, prev_hash)

# Creates the blockchain and adds the genesis block.
blockchain = [create_genesis_block()]
# Assigns the last (and only) block as previous_block.
previous_block = blockchain[0]

# Defines the number of blocks to be added to the chain after genesis.
additional_blocks = 20

# Adds the additional blocks to the chain.
for i in range(0, additional_blocks):
	# Assigns new Block instance to block_to_add using next_block() function.
	block_to_add = next_block(previous_block)
	# Appends the new Block instance to the blockchain.
	blockchain.append(block_to_add)
	# Updates previous_block as the most current block (ie, block_to_add).
	previous_block = block_to_add
	# Prints index of current block added to blockchain.
	print(f"Block #{str(block_to_add.index)} has been added to the blockchain!")
	# Prints hash of current block added to blockchain.
	print(f"Hash: {str(block_to_add.hash)}\n")