from pathlib import Path

from PIL import Image
from ultralytics import YOLO


def main():
    # Get the location of this script so relative paths work on Windows.
    script_dir = Path(__file__).resolve().parent
    model_path = script_dir.parent / "model" / "best.pt"
    output_dir = script_dir.parent / "outputs" / "demo_predictions"

    # Check that the trained model exists before trying to use it.
    if not model_path.exists():
        print(f"Error: model file not found at {model_path}")
        return

    # Ask the user to type or paste the image path.
    image_input = input("Enter the full path of the image: ").strip().strip('"')
    image_path = Path(image_input)

    # Check that the input image exists.
    if not image_path.exists():
        print(f"Error: image file not found at {image_path}")
        return

    try:
        # Load the trained YOLOv8 model.
        model = YOLO(str(model_path))
    except Exception as error:
        print(f"Error loading model: {error}")
        return

    try:
        # Run prediction on the selected image.
        results = model(str(image_path))
        result = results[0]
    except Exception as error:
        print(f"Error running prediction: {error}")
        return

    try:
        # Create the output folder if it does not already exist.
        output_dir.mkdir(parents=True, exist_ok=True)

        # Draw bounding boxes on the image and save the result.
        plotted_image = result.plot()
        saved_image_path = output_dir / f"predicted_{image_path.name}"
        Image.fromarray(plotted_image[:, :, ::-1]).save(saved_image_path)
    except Exception as error:
        print(f"Error saving output image: {error}")
        return

    print("\nPrediction completed successfully.")
    print(f"Saved output image to: {saved_image_path}")

    # Print detected classes and confidence scores in a simple format.
    boxes = result.boxes
    if boxes is None or len(boxes) == 0:
        print("No objects were detected in the image.")
        return

    print("\nDetected objects:")
    for index, box in enumerate(boxes, start=1):
        class_id = int(box.cls[0].item())
        confidence = float(box.conf[0].item())
        class_name = model.names.get(class_id, str(class_id))
        print(f"{index}. {class_name} - confidence: {confidence:.2f}")


if __name__ == "__main__":
    main()
