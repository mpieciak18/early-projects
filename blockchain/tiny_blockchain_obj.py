import hashlib as hasher

# Simple class "Block" for an individual block of a blockchain.
class Block:
	# Initializes the attributes of the Block class.
	def __init__(self, index, timestamp, data, previous_hash):
		# Is the index of the block in the blockchain.
		self.index = index
		# Is the time that the block is added to the blockchain.
		self.timestamp = timestamp
		# Is the data of the block being added to the blockchain.
		self.data = data
		# Is the hash of the previous block in the blockchain.
		self.previous_hash = previous_hash
		# Creates the hash for the current block in the blockchain.
		self.hash = self.hash_block()

	def hash_block(self):
		# Creates a SHA-256 hash object and assigns it to variable "sha".
		sha = hasher.sha256()
		# Updates the hash object with the bytes-like attributes from the block.
		sha.update((str(self.index) +
					str(self.timestamp) +
					str(self.data) +
					str(self.previous_hash)).encode())
		# Returns the digest of data passed to the hash object through the
		# update() method. Data is returned as a string of hexadecimal digits
		# (as opposed to a bytes-object.)
		return sha.hexdigest()