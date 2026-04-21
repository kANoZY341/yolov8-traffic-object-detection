# YOLOv8-Based Object Detection System for Traffic Analysis

## Project Objective
The main objective of this project is to build an object detection system for traffic analysis using YOLOv8. The model is trained to detect common traffic vehicle classes from images and help identify objects in road scenes.

## Dataset Information
- Total images: 880
- Train images: 704
- Validation images: 176

### Dataset Classes
- Ambulance
- Bus
- Car
- Motorcycle
- Truck

## Model Details
- Model used: YOLOv8n
- Final training run used: 50 epochs

## Project Structure
- `model/` contains the final trained YOLO model
- `app/` contains the Streamlit app
- `outputs/` contains training results and prediction outputs
- `docs/` can be used for report files or extra documentation
- `code/` contains the notebook, dataset config, and prediction script

## Evaluation Outputs
The `outputs` folder includes important evaluation and result files such as:
- `results.png`
- `confusion_matrix.png`
- `confusion_matrix_normalized.png`
- `BoxPR_curve.png`
- `BoxP_curve.png`
- `BoxR_curve.png`
- `BoxF1_curve.png`
- `labels.jpg`

It also includes some sample predicted output images.

## How to Run the Streamlit App
Go to the `app` folder and use one of these options:

### Easy way
Double-click:
- `Open_Traffic_Detection_App.vbs`

This will open the Streamlit app without needing to type commands in CMD.

### Command way
If needed, you can also run:

```powershell
cd app
pip install -r requirements.txt
streamlit run app.py
```

## How to Run the predict_image.py Script
Go to the `code` folder and run:

```powershell
cd code
python predict_image.py
```

Then enter the full path of the image when the program asks for it. The predicted output image will be saved inside:

```text
outputs/demo_predictions
```

The script will also print the detected classes and confidence scores in the terminal.

## Limitations
One limitation of this project is that similar classes may sometimes be confused. For example, `car`, `truck`, `bus`, and `ambulance` can look similar in some traffic images, especially when the image is unclear, far away, or partly blocked.
