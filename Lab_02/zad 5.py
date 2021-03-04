import sys as system

system.stdout.write("Wpisz dowolny ciąg znaków: ")
ciag = system.stdin.readline()
system.stdout.write(ciag)

print(ciag.count('a'))