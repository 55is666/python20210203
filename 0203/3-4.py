#304
j=[]

b=0
f=0
g=100
d=int(input('people'))
for i in range(d):
    bn=input('name:')
    score=int(input('score:'))
    b=b+score
    j.append(score)
    j.append(bn)
for i in range(0,d,2):
    
    if j[i]>f:
        f=j[i]
        fd=j[i*2+1]
    if j[i*2]<g:
        g=j[i*2]
        gd=j[i*2+1]
average=b/d
print(j)
print('average:',average)
print('high:',f,'是',fd,'low:',g,'是',gd)