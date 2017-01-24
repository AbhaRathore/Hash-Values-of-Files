# import hashlib module
import hashlib

def hash_file(filename):
   "SHA-1 hash of the Input file."

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 2048 bytes at a time
           chunk = file.read(2048)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("test.py")
print(message)