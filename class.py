from rodent import Rodent
file=open("data.csv")
rodents = dict()
while True:
    line = file.readline()
    args=line.split(' ')
    if rodents.has_key(args[0])
        rodnets[args[0]].add_weight(args[1])
    else:
        rodents[args[0]]=Rodent(args[0])
        rodents[args[0]].add_weight(args[1])
    if not line:
        break
        
file.close()
