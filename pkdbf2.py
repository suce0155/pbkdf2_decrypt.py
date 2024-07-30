import hashlib
import binascii

def pbkdf2_hash(password, salt, iterations=50000, dklen=50):
	hash_value = hashlib.pbkdf2_hmac(
'sha256', # hashing algorithm
password.encode('utf-8'), # password
salt, # salt
iterations, # number of iterations
dklen=dklen # key length
)
	return hash_value

def find_matching_password(dictionary_file, target_hash, salt, iterations=50000, dklen=50):

	target_hash_bytes = binascii.unhexlify(target_hash)

	
	with open(dictionary_file, 'r', encoding='utf-8') as file:
		
    	
		for line in file:

			password = line.strip()

# generating hash
			hash_value = pbkdf2_hash(password, salt, iterations, dklen)

# Check if hash is correct
			if hash_value == target_hash_bytes:
				print(f"Found password: {password}")
				return password

		print("Password not found.")
	return None

# Parameters
salt = binascii.unhexlify('f0ae32ee41452d8401e3953e54d43505') # Salt from gitea.db
target_hash = '75c200d3ece7eda2e1fdeddecb2287142a6f2259ac7cf6b02a9c3b8a78f83ffac55ac80b168e4f28bd69c948e09ea8e240eb' # hash from gitea.db

# Patch to dictionary
dictionary_file = '/usr/share/wordlist/rockyou.txt'

find_matching_password(dictionary_file, target_hash, salt)
