# Recursive Case: Circuits with Multiple Gates
def forwardMultiplyGate(x,y):
	return x * y
def forwardAddGate(x,y):
	return x + y
def forwardCircuit(x,y,z):
	q = forwardAddGate(x,y)
	f = forwardMultiplyGate(q,z)
	return f

x, y , z = -2, 5, -4

f = forwardCircuit(x, y, z)
print ('f=%f' % f)

# initial conditions
q = forwardAddGate(x,y)
f = forwardMultiplyGate(q,z)

print('q=%f, f=%f' % (q, f))

# gradient of the MULTIPLY gate w.r.t its inputs
derivative_f_wrt_z = q  # df/dz = d(q*z)/dz = q
derivative_f_wrt_q = z  # df/dq = d(q*z)/dz = z

# derivative of the ADD gate wrt its inputs
derivative_q_wrt_x = 1.0 # dq/dx = d(x+y)/dx = 1 + 0 = 1
derivative_q_wrt_y = 1.0 # dq/dy = d(x+y)/dy = 0 + 1 = 1

# chain rule
derivative_f_wrt_x = derivative_q_wrt_x * derivative_f_wrt_q # df/dx=dq/dx * df/dq
derivative_f_wrt_y = derivative_q_wrt_y * derivative_f_wrt_q # df/dy=dq/dy * df/dq

# let the inputs respond to the force/tug
step_size = 0.01
x = x + step_size * derivative_f_wrt_x
y = y + step_size * derivative_f_wrt_y
z = z + step_size * derivative_f_wrt_z

q = forwardAddGate(x,y)
f = forwardMultiplyGate(q,z)

print('q_new=%f, f_new=%f' % (q, f))

# numerical gradient check
h = 0.0001
x_derivative = (forwardCircuit(x+h,y,z)-forwardCircuit(x,y,z))/h
y_derivative = (forwardCircuit(x,y+h,z)-forwardCircuit(x,y,z))/h
z_derivative = (forwardCircuit(x,y,z+h)-forwardCircuit(x,y,z))/h

print('analytic gradients: dx=%f,dy=%f,dz=%f' % (derivative_f_wrt_x,derivative_f_wrt_y,derivative_f_wrt_z))
print('numeric gradients: dx=%f,dy=%f,dz=%f' % (x_derivative,y_derivative,z_derivative))
