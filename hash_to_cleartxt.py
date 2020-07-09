from hashing_sctipt import hashh
from file_rw import fileop
# in this code we take the clear text from the user and hashing it then searching inside the wordlist for this hashed text if it founded we return it with its clear text alse
do_hash= hashh() # this is a object form class hashh which return hashed text
do_wr= fileop()  # this is a object form class fileop which read the file 

word_list=input("please enter the word list file name --> ")
hash_algorithm=input("please enter the algorthm-->  ")
hashed_phrase=input("please enter the hashed text that you want turn to clear text-->  ")
list_of_lines=do_wr.rwfun(word_list) # to read the file
for i in list_of_lines:
    i=i.rstrip("\n") # to discard the new line (enter) 
    if i == "":      # to discard the blank line
        continue 
    x=do_hash.dohash(i, hash_algorithm) # here we call dohash method which inside the class hashh with the object do_hash
    if x == hashed_phrase:
        print("the clear text for--> {} fount and its--> {}".format(x,i))
        break
    



