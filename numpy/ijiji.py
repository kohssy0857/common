weights=[0.1,0.2,0]
def neural_network(input,weights):
    prediction=w_sum(input,weights)
    return round(prediction,3)
toes=[8.5,9.5,9.9,9.0]
wlrec=[0.65,0.8,0.8,0.9]
nfans=[1.2,1.3,0.5,1.0]
input=[toes[0],wlrec[0],nfans[0]]

def w_sum(a,b):
    assert(len(a)==len(b))
    output=0
    for i in range(len(a)):
        output+=(a[i]*b[i])
    return output

pred= neural_network(input,weights)
print(pred)

h=[]
for i in zip(toes,wlrec,nfans):
    n=neural_network(i,weights)
    h+=[n]

print(sum(h)/len(toes))

import numpy as np



w=[[0.1,0.1,-0.3],[0.1,0.2,0.0],[0.0,1.3,0.1]]
inp=[8.5,0.65,1.2]
nlis=[neural_network(inp,w[i]) for i in range(3)]
print(nlis)

ww=np.array(w)
ip=np.array(inp)
print(np.dot(w,ip))