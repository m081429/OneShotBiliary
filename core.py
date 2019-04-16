import tensorflow as tf

from model import build_network
from preprocess import generate_inputs, get_epoch_size

class_paths = ['/people/m087494/OneShotBiliary/data/positive',
               '/people/m087494/OneShotBiliary/data/negative']
log_dir = "/people/m087494/OneShotBiliary/logs"

num_epochs = 5


steps_per_epoch = get_epoch_size(class_paths)

# Build the model
model = build_network()

# tf.keras.utils.plot_model(
#    model,
#    to_file='/Users/m087494/Desktop/model.png',
#    show_shapes=True)
# model.summary()

# Write tensorboard callback function
tbCallback = tf.keras.callbacks.TensorBoard(log_dir=log_dir,
                                            histogram_freq=50,
                                            write_graph=True,
                                            write_grads=True,
                                            write_images=True)



# Training the model
items = generate_inputs(class_paths, img_size=256)
for i in items:
    model.fit_generator(i,
                        steps_per_epoch=steps_per_epoch,
                        epochs=num_epochs,
                        callbacks=[tbCallback],
                        validation_data=None,
                        validation_steps=None,
                        class_weight=None,
                        max_queue_size=10,
                        workers=1,
                        use_multiprocessing=False,
                        shuffle=True,
                        initial_epoch=0
                        )
