#encoding:utf8

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import os
import sys

if __name__ == "__main__":
    mnist = input_data.read_data_sets("../MNIST_data", one_hot = True)
    sess = tf.InteractiveSession()     
    x = tf.placeholder(tf.float32, shape=[None, 784])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])

    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    sess.run(tf.global_variables_initializer())
    y = tf.matmul(x, W) + b
    
    cross_entropy = tf.reduct_mean(tf.nn.softmax_cross_entropy_with_logits(label = y_, logits = y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    for _ in range(1000):
        batch = mnist.train.next_batch(100)
        train_step.run(feed_dict={x : batch[0], y_ : batch[1]})
    tf. 
    
