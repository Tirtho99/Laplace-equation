from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as p
L=20
h=.4
w=1.5
M=int(L/h+0.5)
r=int(5/h+0.5)
d=int(2/h+0.5)
V=np.zeros((M,2*M+1))
for i in range(0,M):
	H=1000.0/(2*d)
	k=0
	Z=-1000
	for j in range(0,2*M+1):
		if(j>(M-d) and j<(M+d)):
			V[i,j]=Z
			k=k+1
		elif j<=(M-d):
			V[i,j]=-1000
		else:
			V[i,j]=0
		Z=-1000+(k+1)*H
for i in range(r+1,M):
	for j in range(M+d,2*M-1):
		V[i,j]=0
	for j in range(0,M-d):
		V[i,j]=0
print(V)
U=0
err=2
while(err>.0001):
	#print(1)
	V1=V.copy()
	for i in range(0,M-1):
		#print(2)
		for j in range(1,M+d):
			#print(3)
			if (i>=r and j<=M+-d):
				#print(4)
				continue
			else:
				if i==0:
					U=(1/6.0)*(4*V[i+1,j] + V[i,j+1]+V[i,j-1])
					#print(U)
				else:
					U=(1/4.0)*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])+(1/(8.0*i*h))*(V[i+1,j]-V[i-1,j])
				V[i,j]=V[i,j]+w*(-V[i,j]+U)
				
	err=np.sum(np.abs(V-V1))
print(err)
print(V)
Z=np.arange(-L,L+h,h)
print(np.shape(Z))
print(np.shape(V))
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(-800))
	else:
		R1.append(-i*h)
		X1.append(inter(-800))
		R1.insert(0,i*h)
		X1.insert(0,inter(-800))
p.plot(X1,R1)	
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(-900))
	else:
		R1.append(-i*h)
		X1.append(inter(-900))
		R1.insert(0,i*h)
		X1.insert(0,inter(-900))
p.plot(X1,R1)	
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(-200))
	else:
		R1.append(-i*h)
		X1.append(inter(-200))
		R1.insert(0,i*h)
		X1.insert(0,inter(-200))
p.plot(X1,R1)
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(-1000))
	else:
		R1.append(-i*h)
		X1.append(inter(-1000))
		R1.insert(0,i*h)
		X1.insert(0,inter(-1000))
p.plot(X1,R1,lw=4,c='black')
X1=2*np.ones(M)
R1=np.linspace(-20,20,M)
p.plot(X1,R1,lw=4,c='black')
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(-100))
	else:
		R1.append(-i*h)
		X1.append(inter(-100))
		R1.insert(0,i*h)
		X1.insert(0,inter(-100))
p.plot(X1,R1)
R1=[]
X1=[]
for i in range(0,M):
	inter=interp1d(V[i],Z)
	if(i==0):
		R1.append(-i*h)
		X1.append(inter(-500))
	else:
		R1.append(-i*h)
		X1.append(inter(-500))
		R1.insert(0,i*h)
		X1.insert(0,inter(-500))
p.xlabel("Z axis")
p.ylabel("R axis")
p.title("Equipotetial surfaces")
p.plot(X1,R1)
p.savefig("Lpe 2")
p.show()


