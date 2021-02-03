#302
j=[]
b=0
f=0
g=100
d=int(input('people'))
for i in range(d):
    score=int(input('score:'))
    b=b+score
    if f<score:
        f=score
    if g>score:
        g=score
    j.append(score)
average=b/d
print(j)
print('average:',average)
print('high:',f,'low',g)