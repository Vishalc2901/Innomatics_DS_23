import streamlit as st
from tensorflow import keras
import numpy as np
from PIL import ImageOps, Image
from streamlit_drawable_canvas import st_canvas

def predict(image_data):
    # code to handle prediction request
    model = keras.models.load_model('mnist.h5')
    # Load the image data into a PIL Image object
    image = Image.fromarray(image_data)

    # Preprocess the image data
    image = image.resize((28, 28)).convert('L')
    image = ImageOps.invert(image)
    image_data = np.array(image).reshape(1, 28, 28, 1) / 255.0

    # Make a prediction using the machine learning model
    prediction = model.predict(image_data)[0]

    # Return the predicted digit
    return np.argmax(prediction)

def main():
    st.title('Handwritten Digit Recognition')

    # Define a canvas to allow users to draw an image
    canvas_result = st_canvas(
        fill_color="#ffffff",
        stroke_width=20,
        stroke_color="#000000",
        background_color="#ffffff",
        height=150,
        width=150,
        drawing_mode="freedraw",
        key="canvas"
    )

    if canvas_result.image_data is not None:
        # Display the drawn image
        image = Image.fromarray(canvas_result.image_data.astype('uint8'))
        st.image(image, caption='Drawn Image', use_column_width=True)

        # Make a prediction and display the result
        prediction = predict(canvas_result.image_data)
        st.write(f"Prediction: {prediction}")

if __name__ == '__main__':
    main()
