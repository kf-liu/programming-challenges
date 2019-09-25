def getL(num,pn):
	if num==1:return pn+1
	elif num%2==0:return getL(num/2,pn+1)
	else:return getL(3*num+1,pn+1)

max=0
#begin=int(input())
#end=int(input())
begin,end=map(int,input().split())#一次性输入两个数字
if begin<end:
	a=begin
	b=end
else:
	a=end
	b=begin
for i in range(a+1,b):
	if getL(i,0)>max:
		max=getL(i,0)
print('%d %d %d'%(begin,end,max))
