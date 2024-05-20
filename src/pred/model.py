from src.utils.image import load_image, load_categories
# from src.utils.model import predict_func
import tensorflow as tf    
import numpy as np
def make_prediction(model_dir, image, categories_dir):
    
    img = load_image(image)
    categories = load_categories(categories_dir)
    # prediction = predict_func(model_dir, image=img)

    # print("PREDICTED: class: %s, confidence: %f" % (list(prediction.keys())[0], list(prediction.values())[0]))
    
    # return prediction

    # Load the TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path=model_dir)
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Print input and output details for debugging
    print("Input details:", input_details)
    print("Output details:", output_details)

    # Assuming the input shape is (1, 224, 224, 3) for an image classifier
    input_shape = input_details[0]['shape']

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], img)

    # Run the interpreter
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])


    predicted_index = np.argmax(output_data)

    # Map the index to the corresponding category
    predicted_category = categories[predicted_index]

    print("Predicted category:", predicted_category)

    return predicted_category