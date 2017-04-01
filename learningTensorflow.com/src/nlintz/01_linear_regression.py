import tensorflow as tf
import numpy as np

trX = np.linspace(-1, 1, 101)
trY = 2 * trX + np.random.randn(*trX.shape) * 0.33
# create a y value which is approximately linear but with some random noise

Y = tf.placeholder("float")
X = tf.placeholder("float")

def model(X, w):
	return tf.mul(X, w)
	# lr is just a X*w so this model is pretty simple.

# create a shared variable.
w = tf.Variable(0.0, name="weights")
y_model = model(X, w)

# use a square error for cost function
cost = tf.square(Y - y_model)

# create a optimizer to minize cost and fit line to my data.
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# global init variables.

# launch the graph in a session
with tf.Session() as sess:
	# you need to init variables.
	tf.global_variables_initializer().run()
	
	for i in range(100):
		for (x,y) in zip(trX, trY):
			sess.run(train_op, feed_dict={X: x, Y: y})

			# it should be around 2.
			print(sess.run(w))