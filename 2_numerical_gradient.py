# strategy#2: Numerical gradient
def forwardMultiplyGate(x,y):
	return x * y

x, y = -2, 3
out = forwardMultiplyGate(x,y)
h = 0.0001

# compute derivative with respect to x
xph = x + h
out2 = forwardMultiplyGate(xph,y)
x_derivative = (out2 - out ) / h

# compute derivative w.r.t y
yph = y + h
out3 = forwardMultiplyGate(x,yph)
y_derivative = (out3-out) / h


step_size = 0.01
x = x + step_size * x_derivative
y = y + step_size * y_derivative
out_new = forwardMultiplyGate(x,y)

print ('out=%f, out_new=%f' % (out, out_new))
