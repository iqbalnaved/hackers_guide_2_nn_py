# Example: Single Neuron
import math

class Unit:
    def __init__(self, value, grad):
        self.value = value
        self.grad = grad

class multiplyGate:
	def forward(self, u0, u1):
		# store pointers to input Units u0 and u1 and output unit u top
		self.u0 = u0
		self.u1 = u1
		self.utop = Unit(u0.value * u1.value, 0.0)
		return self.utop
	def backward(self):
		# take the gradient in output unit and chain it with the
		# local gradients, which we derived for multiply gate before
		# then write those gradients to those Units.
		self.u0.grad += self.u1.value * self.utop.grad
		self.u1.grad += self.u0.value * self.utop.grad

class addGate:
	def	forward(self, u0, u1):
		self.u0 = u0
		self.u1 = u1 # stoer pointers to input units
		self.utop = Unit(u0.value+u1.value, 0.0)
		return self.utop
	def backward(self):
		# add gate. derivative wrt both inputs is 1
		self.u0.grad += 1 * self.utop.grad
		self.u1.grad += 1 * self.utop.grad

class sigmoidGate:
	def forward(self,u0):
		self.u0 = u0
		self.utop = Unit(sigmoid(self.u0.value), 0.0)
		return self.utop
	def backward(self):
		s = sigmoid(self.u0.value)
		self.u0.grad += (s * (1-s)) * self.utop.grad

def sigmoid(x):
	sig = 1 / (1 + math.exp(-x))
	return sig

# create input units
a = Unit(1.0, 0.0)
b = Unit(2.0, 0.0)
c = Unit(-3.0, 0.0)
x = Unit(-1.0, 0.0)
y = Unit(3.0, 0.0)

# create the gates
mulg0 = multiplyGate()
mulg1 = multiplyGate()
addg0 = addGate()
addg1 = addGate()
sg0 = sigmoidGate()

# do the forward pass
def forwardNeuron():
	ax = mulg0.forward(a,x)
	by = mulg1.forward(b,y)
	axpby = addg0.forward(ax,by)
	axpbypc = addg1.forward(axpby,c)
	s = sg0.forward(axpbypc) # f(x,y,a,b,c)=sig(ax+by+c)
	return s

s = forwardNeuron()

print('circuit output: %.4f' % s.value)


s.grad = 1.0
sg0.backward()   # writes gradient to axpbypc
addg1.backward() # writes gradients into axpby and c
addg0.backward() # writes gradients into ax and by
mulg1.backward() # writes gradients into b and y
mulg0.backward() # writes gradients into a and x

step_size = 0.01
a.value += step_size * a.grad
b.value += step_size * b.grad
c.value += step_size * c.grad
x.value += step_size * x.grad
y.value += step_size * y.grad

s = forwardNeuron()

print('a.grad=%.3f,b.grad=%.3f,c.grad=%.3f,x.grad=%.3f,y.grad=%.3f' % (a.grad,b.grad,c.grad,x.grad,y.grad))

print('circuit output after one backprop: %.4f ' % s.value)


def forwardCircuitFast(a,b,c,x,y):
	return 1/(1+math.exp(-(a*x+b*y+c)))

a, b, c, x, y = 1,2,-3,-1,3

h = 0.0001

a_grad = (forwardCircuitFast(a+h,b,c,x,y)-forwardCircuitFast(a,b,c,x,y))/h
b_grad = (forwardCircuitFast(a,b+h,c,x,y)-forwardCircuitFast(a,b,c,x,y))/h
c_grad = (forwardCircuitFast(a,b,c+h,x,y)-forwardCircuitFast(a,b,c,x,y))/h
x_grad = (forwardCircuitFast(a,b,c,x+h,y)-forwardCircuitFast(a,b,c,x,y))/h
y_grad = (forwardCircuitFast(a,b,c,x,y+h)-forwardCircuitFast(a,b,c,x,y))/h


print('a_grad=%.3f,b_grad=%.3f,c_grad=%.3f,x_grad=%.3f,y_grad=%.3f' % (a_grad,b_grad,c_grad,x_grad,y_grad))


























		

