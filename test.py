with open('./local/cat.py', 'r') as file:
        data = file.read()

# print(data)

data = data.split()


i=0
list_cat = []
 
while i <= 19:
        for cat in data :
                print(cat)
                i += 1

print(list_cat)