import hashlib
class hashh:
    def dohash(self, text, hashing_fun):
        self.clear_text = text.encode("utf-8") # turn the charcters to bytes because hash work on bytes not chracters
        self.hash_obj = hashlib.new(hashing_fun) # to creat an object from class hash and define the hash algorithm
        self.hash_obj.update(self.clear_text) # update the hash object with the bytes 
        return self.hash_obj.hexdigest() # this return digest of the data passed to the update() method so far in string object



#h=hashh()
#h.dohash("ramy", "md5")





