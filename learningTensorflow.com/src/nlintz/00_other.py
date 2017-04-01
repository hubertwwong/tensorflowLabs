import tensorflow as tf

a = tf.placeholder("int32")
b = tf.placeholder("int32")

y = tf.add(a,b)

init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init, feed_dict={a: 5, b: 4})
	#sess.run(y, feed_dict={a: 5, b: 4})
	print(y)
	#print(sess.run(y, feed_dict={a: 3, b: 4}))