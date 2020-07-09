class fileop:
    def rwfun(self, text_file):
        f=open(text_file, "r")
        return f.readlines() # this will return a list of the lines 


#obj= file_class()
#l=obj.rwfun("clear2.txt")
#print(l)
#for i in l:
    #i=i.rstrip("\n") # to strip the enter
    #if i == "":    # to ignor the blank lines
        #continue
    #print(i)