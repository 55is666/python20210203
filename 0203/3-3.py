#303
j=[]
l=[]
b=0
f=0
g=100
d=int(input('people'))
for i in range(d):
    bn=input('name:')
    score=int(input('score:'))
    b=b+score
    j.append(score)
    l.append(bn)
for i in range(d):
    
    if j[i]>f:
        f=j[i]
        fd=l[i]
    if j[i]<g:
        g=j[i]
        gd=l[i]
average=b/d
print(j,l)
print('average:',average)
print('high:',f,'是',fd,'low',g,'是',gd)