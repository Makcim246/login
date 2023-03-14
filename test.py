resalt = ''
res = ''
with open('vise/base.html', 'r') as file:
    resalt = file.read()

with open('vise/abaut.html', 'r') as file:
    res = file.read()

r = resalt.replace("{body}", res)
print(r)