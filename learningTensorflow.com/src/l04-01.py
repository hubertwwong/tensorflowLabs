import tensorflow as tf

x = tf.placeholder("float", 3)
y = x * 2

# no models

with tf.Session as session:
  result = session.run(y, feed_dict={x: [1,2,3]})
  print(result)

# http://learningtensorflow.com/lesson8/
# https://github.com/nlintz/TensorFlow-Tutorials