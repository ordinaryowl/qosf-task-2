import numpy as np 
import random as rd
from numpy import sin,cos 
import matplotlib.pyplot as plt

def prob_from_measurement(a,b,c,n_meas=1):
	
	p0=cos(c/2)**2*(cos(a/2)**2*cos(b/2)**2+sin(a/2)**2*sin(b/2)**2)
	p1=sin(c/2)**2*(cos(a/2)**2*cos(b/2)**2+sin(a/2)**2*sin(b/2)**2)
	p2=sin(c/2)**2*(cos(a/2)**2*sin(b/2)**2+sin(a/2)**2*cos(b/2)**2)
	p3=cos(c/2)**2*(cos(a/2)**2*sin(b/2)**2+sin(a/2)**2*cos(b/2)**2)

	meas_outcomes=rd.choices([0,1,2,3],[p0,p1,p2,p3],k=n_meas)
	P0=meas_outcomes.count(0)/n_meas
	P1=meas_outcomes.count(1)/n_meas
	P2=meas_outcomes.count(2)/n_meas
	P3=meas_outcomes.count(3)/n_meas

	return P0,P1,P2,P3

def loss_function(p0,p1,p2,p3):
	return p0**2+(p1-0.5)**2+(p2-0.5)**2+p3**2

def gradient(a,b,c,p0,p1,p2,p3):

	grad_a=sin(a)*cos(b)*(cos(c/2)**2*(p3-p0)+sin(c/2)**2*(p2-p1))
	grad_b=sin(b)*cos(a)*(cos(c/2)**2*(p3-p0)+sin(c/2)**2*(p2-p1))
	grad_c_term1=sin(c)*((cos(a/2)**2*cos(b/2)**2+sin(a/2)**2*sin(b/2)**2)*(p1-p0-0.5))
	grad_c_term2=sin(c)*((cos(a/2)**2*sin(b/2)**2+sin(a/2)**2*cos(b/2)**2)*(p3-p2+0.5))
	grad_c=grad_c_term1+grad_c_term2
	return grad_a,grad_b,grad_c



def gradient_descent(err=10**-8,rate=1,max_steps=10000,n_meas=10):
	#err=0.01,rate=1,max_steps=100,n_meas=100
	a=0.1;b=0.1;c=0.1	
	# a,b,c=np.random.uniform(0.1,3.14,3)
	step=1
	P0,P1,P2,P3=prob_from_measurement(a,b,c,n_meas)
	grad=np.array(gradient(a,b,c,P0,P1,P2,P3))
	a-=grad[0]*rate
	b-=grad[1]*rate
	c-=grad[2]*rate
	e=loss_function(P0,P1,P2,P3)
	print('step:%d| a:%0.5f b:%0.5f c:%0.5f| error:%0.2e| prob: %.2f,%.2f,%.2f,%.2f'%(step,a,b,c,e,P0,P1,P2,P3))	
	while(e>err and step<max_steps):
		step+=1
		P0,P1,P2,P3=prob_from_measurement(a,b,c,n_meas)
		grad=np.array(gradient(a,b,c,P0,P1,P2,P3))
		a-=grad[0]*rate
		b-=grad[1]*rate
		c-=grad[2]*rate
		e=loss_function(P0,P1,P2,P3)
		print('step:%d| a:%0.5f b:%0.5f c:%0.5f| error:%0.2e| prob: %.2f,%.2f,%.2f,%.2f'%(step,a,b,c,e,P0,P1,P2,P3))
	return a

def plot_bc(a):
	# fig = plt.figure()
	# ax = fig.gca(projection='3d')
	# from matplotlib import cm
	# a=np.pi
	fig,ax=plt.subplots(figsize=(6,6))
	b = np.arange(0, np.pi+0.2, 0.1)
	c = np.arange(0, 2*np.pi+0.2, 0.1)
	b, c = np.meshgrid(b, c)
	p0=cos(c/2)**2*(cos(a/2)**2*cos(b/2)**2+sin(a/2)**2*sin(b/2)**2)
	p1=sin(c/2)**2*(cos(a/2)**2*cos(b/2)**2+sin(a/2)**2*sin(b/2)**2)
	p2=sin(c/2)**2*(cos(a/2)**2*sin(b/2)**2+sin(a/2)**2*cos(b/2)**2)
	p3=cos(c/2)**2*(cos(a/2)**2*sin(b/2)**2+sin(a/2)**2*cos(b/2)**2)
	Z=p0**2+(p1-0.5)**2+(p2-0.5)**2+p3**2
	# surf = ax.contour(b, c, Z,cmap=cm.coolwarm)
	cf=ax.contourf(b,c,Z)
	fig.colorbar(cf, ax=ax)
	ax.set_xlabel('$b$', fontsize=20)
	ax.set_title('$a=%0.2f$'%(a),fontsize=20)
	ax.set_ylabel('$c$',fontsize=20)
	plt.show()

a=gradient_descent()
# plot_bc(a)








