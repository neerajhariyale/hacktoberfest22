myfile=open(r'C:\Users\pc\Desktop\Python programs\Poem.txt','r')
s=myfile.readlines()
linecount=len(s)
print("No.of lines in Poem ",linecount)
myfile.close()
