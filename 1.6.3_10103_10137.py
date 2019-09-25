def cul():
	s=0
	an=0
	for i in group[1:]:
		s+=i
	a=s/group[0]
	for i in group:
		if i>a:
			an+=(i-a)
	answer.append(an)
	
group=[]
answer=[]

while True:
	a=float(input())
	if len(group)==0:
		if a==0:break
		else:group=[a]
	elif group[0]<=len(group)-1:
		cul()
		if a==0:break
		group=[a]
	else:
		group.append(a)
#	print(group)
#	print(answer)
	
#print(group)
#print(answer)
for i in answer:
	print('$%.2f'%i)
