squad_713 = [
    'Alice',
    'Alpha',
    'Anthony',
    'Barent',
    'Branden',
    'Channee',
    'Cristina',
    'Cabassa',
    'Elaine',
    'Han',
    'Irene',
    'Joshua',
    'Levin',
    'Lizz',
    'Margaret',
    'Nicholas',
    'Philip',
    'Rohun',
    'Sameh',
    'Shane',
    'Steven',
    'Subrata',
    'Tanner',
    'Yoel',
    'Adam',
    'Pete',
    'Rome',
    'Taylor'
]


with open("713.txt", "w") as groupFile:
    groupFile.write("\n".join(squad_713))
    groupFile.close() 
    open_file = open('713.txt', 'r') 
    Lines = open_file.readlines() 
    count = 0
for line in Lines:
    count += 1 
    print("{}".format(line))