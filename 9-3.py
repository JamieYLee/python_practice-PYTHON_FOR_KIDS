# 방법 2
# import shutil
# shutil.copy('test.txt', 'output.txt')


# 방법 1
f = open('test.txt')
s = f.read()
f.close()
f = open('output.txt', 'w')
f.write(s)
f.close()