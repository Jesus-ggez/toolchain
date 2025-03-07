from lab.app import data


a = data.get('lab0')
b = a.get('lab1')
c = b.get('lab2')
d = c.get('main')

d()

print(type(a), type(b))
