#!/usr/bin/python
from Crypto.Cipher import AES
import base64
import string
import random

#Generating a random string
def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

#getting the key
key = id_generator()
print(key)

#the message text/data
msg_text = 'test some plain text here'.rjust(256)
secret_key = key # create new & store somewhere safe

#encrypting the data
cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = base64.b64encode(cipher.encrypt(msg_text))
print(encoded)

#decrypting the data
decoded = cipher.decrypt(base64.b64decode(encoded))
print(decoded.strip())
