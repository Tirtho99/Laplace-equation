import numpy as np
import matplotlib.pyplot as p
from scipy.interpolate import interp1d
L=30
h=.5
w=1.5
M=int(L/h+0.5)
r=int(15/h+0.5)
d=int(8/h+0.5)
V=np.zeros((M,M))
for i in range(0,M):
	H=1000.0/d
	Z=0
	for j in range(0,M):
		if( j<d+1):
			V[i,j]=Z
		else:
			V[i,j]=1000
		Z=(j+1)*H
for i in range(r+1,M):
	for j in range(d+1,M):
		V[i,j]=0
U=0
err=2
while(err>.0001):
	V1=V.copy()
	for i in range(0,M-1):
		for j in range(1,M-1):
			if (i>=r and j>=d):
				continue
			else:
				if i==0:
					U=(1/6.0)*(4*V[i+1,j] + V[i,j+1]+V[i,j-1])
				else:
					U=(1/4.0)*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])+(1/(8.0*i*h))*(V[i+1,j]-V[i-1,j])
				V[i,j]=V[i,j]+w*(-V[i,j]+U)
				
	err=np.sum(np.abs(V-V1))
print(err)
Z=np.arange(0,L,h)
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(800))
	else:
		R1.append(-i*h)
		X1.append(inter(800))
		R1.insert(0,i*h)
		X1.insert(0,inter(800))
p.plot(X1,R1,label="800V")
X1=np.array(X1)	
X2=-1*X1
p.plot(X2,R1)	
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(600))
	else:
		R1.append(-i*h)
		X1.append(inter(600))
		R1.insert(0,i*h)
		X1.insert(0,inter(600))
p.plot(X1,R1)
X1=np.array(X1)	
X2=-1*X1
p.plot(X2,R1)
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(400))
	else:
		R1.append(-i*h)
		X1.append(inter(400))
		R1.insert(0,i*h)
		X1.insert(0,inter(400))
p.plot(X1,R1)
X1=np.array(X1)	
X2=-1*X1
p.plot(X2,R1)	
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(200))
	else:
		R1.append(-i*h)
		X1.append(inter(200))
		R1.insert(0,i*h)
		X1.insert(0,inter(200))
p.plot(X1,R1,label="200V")
X1=np.array(X1)	
X2=-1*X1
p.plot(X2,R1,label="-200V")
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(1000))
	else:
		R1.append(-i*h)
		X1.append(inter(1000))
		R1.insert(0,i*h)
		X1.insert(0,inter(1000))
p.plot(X1,R1,lw=4,c="black")
X1=np.array(X1)	
X2=-1*X1
p.plot(X2,R1,lw=4,c="black")
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(900))
	else:
		R1.append(-i*h)
		X1.append(inter(900))
		R1.insert(0,i*h)
		X1.insert(0,inter(900))
p.plot(X1,R1)
X1=np.array(X1)	
X2=-1*X1
p.plot(X2,R1,label="-900V")
R1=np.arange(-L,L,h)
X1=np.zeros(2*M)
p.plot(X1,R1)					
p.xlabel("Z axis")
p.ylabel("R axis")
p.title("Equipotetial surfaces")
p.plot(X1,R1)	
p.legend()
p.savefig("Lp1")				
p.show()

