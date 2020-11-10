fr = open('test.txt','r')
fw = open('test_copy.txt','w')

fw.write(fr.read())

fr.close()
fw.close()