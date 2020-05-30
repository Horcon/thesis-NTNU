#Tensorflow config to prevent lag
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction=0.10
session = tf.compat.v1.Session(config=config)