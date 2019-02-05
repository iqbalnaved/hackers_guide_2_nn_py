# Strategy#3: Analytic Gradient
def forwardMultiplyGate(x,y):
	return x * y

x, y = -2, 3
out = forwardMultiplyGate(x,y)
x_gradient = y #by mathematical derivation
y_gradient = x

step_size = 0.01
x += step_size * x_gradient
y += step_size * y_gradient

out_new = forwardMultiplyGate(x,y)

print ('out=%f, out_new=%f' % (out, out_new))

