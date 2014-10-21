__author__ = 'a'


file = open("intext.txt", 'r')
clone = file.readlines()
file.close()
file = open("outtext.txt", 'w')
for i in clone:
    if i.find('Л'):
        file.write(i)
file.close()