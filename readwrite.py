fw= open('sample.txt', 'w')
fw.write('this is some basic text\n')
fw.write('shit \n')
fw.close()


fr= open('sample.txt', 'r')
text = fr.read() # applies read to fr then stores as text
print(text)
fr.close()