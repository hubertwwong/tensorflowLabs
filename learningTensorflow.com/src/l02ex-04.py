import numpy as np
import tensorflow as tf

data = np.random.randint(1000, size=20)
#data = lambda shape, dtype, partition_info=None: np.random.randint(1000, size=10)
#x=tf.get_variable('x', initializer=data, shape=10, dtype=tf.int32)
x = tf.Variable(data, name="x")
y = tf.Variable(0.0, name='y')

#init = lambda shape, dtype: np.random.rand(*shape)
#tf.tf.get_variable('var_name', initializer=init, shape=[1, 2])

model = tf.global_variables_initializer()

with tf.Session() as session:
  for i in range(5):
    session.run(model)
    #y = np.average(data)
    #print(np.average(data))
    #y = tf.Variable(np.average(data))
    print(type(x))
    #x = data
    y = y + np.average(data)
    #print(session.run(x))
    print(session.run(y))

# This is weird...
# http://stackoverflow.com/questions/38190365/how-does-one-initialize-a-variable-with-tf-get-variable-and-a-numpy-value-in-ten
# seems like its a lambda.
# http://stackoverflow.com/questions/41560212/tensorflow-lambda-got-an-unexpected-keyword-argument-partition-info
# big issue is that i'm not sure...