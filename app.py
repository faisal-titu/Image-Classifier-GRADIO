# import gradio as gr
# import tensorflow as tf
# import numpy as np
# import requests

# inception_net = tf.keras.applications.InceptionV3() # load the model

# # Download human-readable labels for ImageNet.
# response = requests.get("https://git.io/JJkYN")
# labels = response.text.split("\n")

# def classify_image(inp):
#   inp = np.expand_dims(inp, axis=0)  # add a batch dimension
#   inp = tf.keras.applications.inception_v3.preprocess_input(inp)
#   prediction = inception_net.predict(inp).flatten()
#   return {labels[i]: float(prediction[i]) for i in range(1000)}

# image = gr.inputs.Image(shape=(299, 299, 3))
# label = gr.outputs.Label(num_top_classes=3)

# gr.Interface(fn=classify_image, inputs=image, outputs=label, capture_session=True).launch()


# import gradio as gr
# import tensorflow as tf
# import numpy as np
# import requests

# # Load the pre-trained model
# inception_net = tf.keras.applications.InceptionV3()

# # Download human-readable labels for ImageNet.
# response = requests.get("https://git.io/JJkYN")
# labels = response.text.split("\n")

# def classify_image(inp):
#   # Option 1: Extract width and height from shape (assuming no additional processing)
#   # Uncomment this block if you're not performing any preprocessing before resizing

#   # image_width, image_height, _ = inp.shape  # Assuming inp is the image data
#   # inp = tf.keras.applications.inception_v3.preprocess_input(
#   #     tf.image.resize(inp, (image_width, image_height))
#   # )

#   # Option 2: Use processing argument in Gradio Image component (recommended)
#   # This requires using a newer version of Gradio. Refer to their documentation
#   # for details on using the processing argument.
#   # inp = tf.keras.applications.inception_v3.preprocess_input(inp)

#   # Add a batch dimension
#   inp = np.expand_dims(inp, axis=0)
#   prediction = inception_net.predict(inp).flatten()
#   return {labels[i]: float(prediction[i]) for i in range(1000)}

# # Define Gradio components
# image = gr.components.Image(shape=(299, 299, 3), processing="auto")  # Use processing if available
# label = gr.components.Label(num_top_classes=3)

# # Launch the Gradio interface with public link sharing
# interface = gr.Interface(fn=classify_image, inputs=image, outputs=label)
# interface.launch(share=True)


import gradio as gr
import tensorflow as tf
import numpy as np
import requests

inception_net = tf.keras.applications.InceptionV3() # load the model

# Download human-readable labels for ImageNet.
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def classify_image(inp):
  inp = inp.reshape((-1, 299, 299, 3))
  inp = tf.keras.applications.inception_v3.preprocess_input(inp)
  prediction = inception_net.predict(inp).flatten()
  return {labels[i]: float(prediction[i]) for i in range(1000)}

image = gr.inputs.Image(shape=(299, 299))
label = gr.outputs.Label(num_top_classes=5)

gr.Interface(fn=classify_image, inputs=image, outputs=label, capture_session=True).launch()
# interface.launch(share=True)