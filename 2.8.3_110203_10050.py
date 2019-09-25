def Days(info):
	days=0
	for i in range(info[0]):
		for j in info[2:]:
			if (i+1)%7-1==5 or (i+1)%7-1==6:break
			if (i+1)%j==0:
				#print(i+1,j)
				days+=1
				break
				#print('days',days)
	return days
result=[]
group=int(input())
for i in range(group):
	g=[int(input())]
	g.append(int(input()))
	for j in range(g[1]):
		g.append(int(input()))
	result.append(Days(g))
for i in result:
	print(i)
