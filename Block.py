import hashlib

class Block:

	def __init__(self, previous_hash, transaction):
		self.previous_hash = previous_hash
		self.transaction = transaction
		current_hash_string = "".join(transaction) + previous_hash
		current_hash = hashlib.sha256(current_hash_string.encode()).hexdigest()
		self.current_hash = current_hash 
