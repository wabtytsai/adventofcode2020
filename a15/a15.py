fin = open('a15.in')
line = fin.readline()
fin.close()

dic = {}
for i,j in enumerate(line.split(',')):
    last = int(j)
    dic[last] = i

start = len(dic.values())
 for turn in range(start, 30000000):
     if not last in dic:
         cur = 0
     else:
         cur = abs(turn - 1 - dic[last])
     dic[last] = turn - 1

     last = cur
print(last)
