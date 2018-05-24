import tensorflow as tf

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


X = tf.placeholder(tf.float64, name="X")
Y = tf.placeholder(tf.float64, name="Y")

addoperation = tf.add(X, Y, name="Add")

with tf.Session() as session:
    result = session.run(addoperation, feed_dict={X: 1, Y: 2})
    print(result)


