names=['Donnie',"GuaGua"]
i=0
while i<len(names):
    if 'Gua' in names[i]:
        print ("Hello,{}".format(names[i]))
    i=i+1
#add a line from macbook
for index,string in enumerate(names):
    if 'Gua' in string:
        print ("Hello,%s" % string)
    
