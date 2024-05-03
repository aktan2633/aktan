file = open('/home/aktan/Рабочий стол/basic python code/aktan2/text.txt')
print(file.read(4))
print(file.read(4))
print(file.readline())
print(file.readline())
print(file.readline ())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

for symb in file:
    print(symb)

    s = file.readlines()
    print(s)
    