class Something():
    def __init__(self, name):
        self.name = name

n = Something('Amit')
print('Name : ', n.name)

n.name = 'Arun'

print('Name : ', n.name)

print('Hello object')