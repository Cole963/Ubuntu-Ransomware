import glob
import os

# Read the key.txt file and get the cipher
file_in = open("key.txt", "r")
subCipherUpper = file_in.read()
file_in.close()
subCipherLower = subCipherUpper.lower()
alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetLower = alphabetUpper.lower()

# Loop thru the .enc files, read them and decrypt
txtFiles = glob.glob('*.enc')
for f in txtFiles:
	
	fileText = ""
	file_in = open(f, "r")
	fileText = file_in.read()
	file_in.close()
	

	#Opens a new .txt file and writes to it the decrypted txt
	file_out = open(f[:-4], "w")
	decryptedContent = ""
	
	for s in fileText:
		if s in subCipherUpper:
			index = subCipherUpper.index(s)
			decryptedContent += alphabetUpper[index]
		elif s in subCipherLower:
			index = subCipherLower.index(s)
			decryptedContent += alphabetLower[index]	
		else:
			decryptedContent += s

	file_out.write(decryptedContent)
	file_out.close()
	
	os.remove(f)

print("Your txt files have been recovered")



