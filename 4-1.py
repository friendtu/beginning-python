people={ 
    "Alice":{
        'phone':'12321',
        'addr':"shanghai"
    },
    "Donnie":{
        'phone':"123232",
        'addr':"beijin"
    }
}
#add a line from desktop




labels={
    'phone':"phone number",
    'addr':'address'
}

name=input("Name: ")
request=input("Phone(p) or Address(a):")
if request=='p':
    key='phone'
if request=='a':
    key='addr'

if name in people: 
    print("{}'s {} is {}".format(name,labels[key],people[name][key]))
