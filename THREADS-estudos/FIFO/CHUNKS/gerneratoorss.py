names = ['mario','gabriel']
generator = (n for n in names)
generator2 = iter(names)
for c in generator:
    print(c)

for c in generator2:
    print(c)