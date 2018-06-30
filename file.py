# how to open a file
fo = open('file.txt', 'w')

print('name', fo.name)
print('Is Closed: ', fo.closed)
print('Opening Mode: ', fo.mode)
# write
fo.write('I Love python')
fo.write(' and Javascript')
# close
fo.close()

# Append
fo = open('file.txt', 'a')
fo.write('I also like PHP')
fo.close()

# Read => + : create
fo = open('file.txt', 'r+')
text = fo.read()
print(text)

fo = open('file2.txt', 'w+')
fo.write('hi')
fo.close()




