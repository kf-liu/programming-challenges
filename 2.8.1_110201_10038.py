str=input()
num=str.split(' ')
diff=[]
for i in range(1,len(num)-1):
	#print(i)
	diff.append(abs(int(num[i+1])-int(num[i])))
	#print('diff',diff)
#print(diff)
diff.sort()
#print(diff)
if diff==[i for i in range(1,len(diff)+1)]:
	print('Jolly')
else:
	print('Not Jolly')
