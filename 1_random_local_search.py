# strategy#1: Random Local Search
import random 

def forwardMultiplyGate(x,y):
	return x * y

x, y = -2, 3 # some input values

# try changing xy, y randomly small amounts and keep track of what works best
tweak_amount = 0.01
best_out = -float("inf")
for k in range(100):
	x_try = x + tweak_amount * (random.random() * 2 - 1)
	y_try = y + tweak_amount * (random.random() * 2 - 1)
	out = forwardMultiplyGate(x_try, y_try)
	if out > best_out:
		best_out = out
		best_x = x_try
		best_y = y_try


print ('best_x=%f , best_y=%f, best_out=%f' % (best_x, best_y, best_out))
