import os
from src.pred.model import make_prediction
import io
from fastapi import FastAPI, File, UploadFile
from PIL import Image



app = FastAPI()

home_dir = os.getcwd()
model_dir = os.path.join(home_dir, "assets/model/plant_disease_model.tflite")
categories_dir = os.path.join(home_dir, "assets/categories.json")

# image_dir = os.path.join(home_dir, "assets/samples/sample.jpg")


#make_prediction(model_dir, image_dir, categories_dir)

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    res = make_prediction(model_dir, image, categories_dir)


    return {'category': res}