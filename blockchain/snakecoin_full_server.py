from tiny_blockchain_obj import Block
from flask import Flask
from flask import request
import json
import requests
import hashlib as hasher
import datetime as date
node = Flask(__name__)

# Generates the first ever block of the SnakeCoin blockchain.
def create_genesis_block():
	# Creates the first block with an index of zero, timestamp of now, data that
	# consists of POW + transactions, & an arbitrary previous hash.
	return Block(0, date.datetime.now(), {"proof-of-work": 9, "transactions":
  		None}, "0")

# Sets a randomized miner address for "this" node.
miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"
# Creates the variable for the blockchain on "this" node.
blockchain = []
# Generates the first block & adds it to "this" node's blockchain.
blockchain.append(create_genesis_block())
# Creates the variable to store the transactions that this node has.
this_nodes_transactions = []
# Creates a variable to store the url data of every other node in the network.
peer_nodes = []
# Creates a variable to declare if this node is mining & sets it to "True".
mining = True

# Uses node to accept POST requests for SnakeCoin transcations.
# Transactions are JSON objects whose request body contains data the sender,
# the recipient, and the amount being transferred.
# Transactions are in JSON format to be able to transmit to our server.
@node.route('/txion', methods = ['POST'])
def transaction():
	if request.method == 'POST':
		# Extracts transaction data on each new POST request.
		new_txion = request.get_json()
		# Adds the transaction to our list.
		this_nodes_transactions.append(new_txion)
		# Logs the successful transcation to the console.
		print("New transcation")
		print(f"FROM: {new_txion['from']}")
		print(f"TO: {new_txion['to']}")
		print(f"AMOUNT: {new_txion['amount']}")
		# Lets the client know the transaction was successful.
		return "Transaction submission successful\n"

## Consesus algorithm for blockchain. ##

@node.route('/blocks', methods=['GET'])
def get_blocks():
	# Sets chain_to_send variable to hold the list of blockchain blocks that
	# are currently on "this" node.
	chain_to_send = blockchain
	# Converts our blocks into dictionaries to send as JSON objects later.
	for block in chain_to_send:
		block_index = str(block.index)
		block_timestamp = str(block.timestamp)
		block_data = str(block.data)
		block_hash = block.hash
		block = {
			"index": block_index,
			"timestamp": block_timestamp,
			"data": block_data,
			"hash": block_hash
		}
	# Converts Python dictionary to JSON object.
	chain_to_send = json.dumps(chain_to_send)
	return chain_to_send

def find_new_chains():
	# Creates variable used to collect blockchains from other nodes.
	other_chains = []
	# Gets the blockchains of every other node.
	for node_url in peer_nodes:
		# Gets other blockchains using GET request.
		block = requests.get(node_url + "/blocks").content
		# Converts blockchain from JSON object to Python dictionary.
		block = json.loads(block)
		# Adds converted blockchain to other_chains list.
		other_chains.append(block)
	return other_chains

def consensus():
	# Retreives blockchains from all other nodes.
	other_chains = find_new_chains()
	# Sets "this" node's blockchain as the longest chain, by default.
	longest_chain = blockchain
	# Loops through each chain to find the longest.
	for chain in other_chains:
		if len(longest_chain) < len(chain):
			longest_chain = chain
	# Sets our blockchain to the longest blockchain. (Nothing happens if "this"
	# node's blockchain was already the longest.)
	blockchain = longest_chain

## End of consesus algorithm for blockchain. ##

# Defines Proof-of-Work algorithm for SnakeCoin miners.
def proof_of_work(last_proof):
	# Creates variables to be used to find next proof of work.
	incrementor = last_proof + 1
	# Increments until it's equal to a number divisble by 9 AND the previous
	# proof of work.
	while incrementor % 9 != 0 and incrementor % last_proof != 0:
		incrementor += 1
	# When the number is found, it's returned as the new proof of work.
	return incrementor

# Uses node to accept GET requests for SnakeCoin mining.
@node.route('/mine', methods = ['GET'])
def mine():
	# Obtains last block from blockchain, then obtains its proof of work.
	last_block = blockchain[len(blockchain) - 1]
	last_proof = last_block.data['proof-of-work']
	# Finds proof of work for current block being mined. (Takes time to finish).
	proof = proof_of_work(last_proof)
	# Rewards miner with transaction for the work (of mining a block).
	this_nodes_transactions.append(
		{ "from": "network", "to": miner_address, "amount": 1 }
	)
	# Gathers data to create new block.
	# Assigns POW & transactions data to new block's data.
	new_block_data = {
		"proof-of-work": proof,
		"transactions": list(this_nodes_transactions)
		}
		# Increments last block's index by 1 & assigns it to new block's index.
	new_block_index = last_block.index + 1
	# Assigns current time to new block's timestamp.
	new_block_timestamp = this_timestamp = date.datetime.now()
	# Assigns last block's hash to new block's previous hash.
	last_block_hash = last_block.hash
	# Empty transaction list
	this_nodes_transactions[:] = []
	# Creates new block & assigns it to variable mined_block.
	mined_block = Block(new_block_index, new_block_timestamp, new_block_data, 
						last_block_hash)
	# Adds newly mined block to blockchain.
	blockchain.append(mined_block)
	# Converts Python dictionary (of newly mined block) to JSON object.
	# Notifies client that block has successfully been mined.
	return json.dumps({
		"index": new_block_index,
		"timestamp": str(new_block_timestamp),
		"data": new_block_data,
		"hash": last_block_hash
	}) + "\n"

node.run()