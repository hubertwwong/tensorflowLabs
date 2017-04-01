import numpy as np
import tensorflow as tf

data = np.random.randint(1000, size=100000)
x = tf.Variable(data, name="x")
y = tf.Variable(5*x.initialized_value() * x.initialized_value() -3*x.initialized_value()+15, name='y')

model = tf.global_variables_initializer()

with tf.Session() as session:
  session.run(model)
  print(session.run(y))