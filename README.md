# Plant Disease Prediction

Welcome to the Plant Disease Prediction repository. This project aims to provide an efficient and accurate way to predict plant diseases using machine learning models. The prediction model can be integrated with various applications through a RESTful API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This project utilizes machine learning algorithms to identify and predict diseases in plants from images. By using advanced techniques in computer vision, the model can classify the type of disease affecting a plant, which can help in timely intervention and treatment.

## Features

- Image-based disease prediction
- RESTful API for easy integration
- High accuracy and performance
- Scalable and modular codebase

## API Endpoints

Below is the API endpoint available in this project. Please replace the placeholders with the actual endpoints and details once you set up the project.

### Endpoint 1: Upload Image

- **URL**: `/predict/`
- **Method**: `POST`
- **Description**: Uploads an image for disease prediction.
- **Parameters**:
  - `image`: (file) The image of the plant leaf to be analyzed.

## Setup Instructions

To set up this project on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/plant-disease-prediction.git](https://github.com/CodeWithOlaf/PlantDocAI_API.git)
    cd PlantDocAI_API
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```


4. **Run the development server**:
    ```bash
    uvicorn main:app --reload
    ```


## Usage

Once the project is set up, you can start making API requests to predict plant diseases. Use the provided endpoints to upload images and retrieve predictions.

Installing curl on windows: https://developer.zendesk.com/documentation/api-basics/getting-started/installing-and-using-curl/

Example usage with `curl`:

```bash
# Get Prediction
curl -X POST -F 'image=@path/to/your/image.jpg' http://localhost:8000/predict/

## Contributing

We welcome contributions from the community. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Acknowledgements
We would like to thank the contributors and the community for their support and contributions to this project.

---

Feel free to customize this README file according to your project's requirements. If you have any questions or need further assistance, please open an issue or contact the repository owner.
