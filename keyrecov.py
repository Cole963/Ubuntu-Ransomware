from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("key.bin", "rb")

private_key = RSA.import_key(open("ransomprvkey.pem").read())

enc_data = file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
data = cipher_rsa.decrypt(enc_data)

file_in.close()

file_out = open("key.txt", "w")
file_out.write(data.decode("UTF-8"))
file_out.close()

print("Key Decrypted to key.txt")


