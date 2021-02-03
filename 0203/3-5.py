#305
j=[]
l=[]
b=0
f=0
g=100
fg=[]
dg=[]
def high (i,d,j,f):
    df=[]
    for i in range(d):
        if j[i]>f:
            f=j[i]
            fd=l[i]
    df.append(f)
    df.append(fd)
    return df
def low (i,d,j,g):
    fgh=[]
    for i in range(d):
        if j[i]<g:
            g=j[i]
            gd=l[i]
    fgh.append(g)
    fgh.append(gd)
    return (fgh)
def lkj (b,d):
    average=b/d
    return average
d=int(input('people'))
for i in range(d):
    bn=input('name:')
    score=int(input('score:'))
    b=b+score
    j.append(score)
    l.append(bn)
for i in range(d):
    fg=high(i,d,j,f)
    dg=low(i,d,j,g)
kk=lkj(b,d)
print(j,l)
print('average:',kk)
print('high:',fg[0],'people:',fg[1],'low',dg[0],'people:',dg[1])