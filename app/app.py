from pathlib import Path

from PIL import Image
import streamlit as st
from ultralytics import YOLO


# Build a Windows-friendly path to the trained model.
APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR.parent / "model" / "best.pt"


@st.cache_resource
def load_model(model_path: Path) -> YOLO:
    """Load the YOLO model once and reuse it across Streamlit reruns."""
    return YOLO(str(model_path))


st.set_page_config(page_title="YOLOv8 Traffic Detection", layout="centered")

st.title("YOLOv8 Traffic Detection")
st.write(
    "Upload a traffic image to detect vehicles and traffic-related objects "
    "using the trained YOLOv8 model."
)

# Stop early with a clear message if the model file is missing.
if not MODEL_PATH.exists():
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

try:
    model = load_model(MODEL_PATH)
except Exception as exc:
    st.error(f"Failed to load model: {exc}")
    st.stop()

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:
    try:
        # Open the uploaded image and convert it to RGB for consistent inference.
        image = Image.open(uploaded_file).convert("RGB")

        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

        # Run object detection on the uploaded image.
        results = model(image)
        result = results[0]

        # Draw bounding boxes and class labels on the image.
        plotted_image = result.plot()
        plotted_image = Image.fromarray(plotted_image[:, :, ::-1])

        st.subheader("Detected Image")
        st.image(plotted_image, use_container_width=True)

        st.subheader("Detections")
        boxes = result.boxes

        if boxes is None or len(boxes) == 0:
            st.info("No objects were detected in this image.")
        else:
            for index, box in enumerate(boxes, start=1):
                class_id = int(box.cls[0].item())
                confidence = float(box.conf[0].item())
                class_name = model.names.get(class_id, str(class_id))
                st.write(f"{index}. {class_name} - confidence: {confidence:.2f}")

    except Exception as exc:
        st.error(f"Error while processing the image: {exc}")
else:
    st.info("Please upload a JPG or PNG image to start detection.")
