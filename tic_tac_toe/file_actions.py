file = open('example.txt', 'w')
file.write('Зевну, укроюсь с головою,\nбудильник заведу на март.\n')
file.close()




file = open('example.txt', 'r')
content = file.read(12)
print(content)
file.close()
