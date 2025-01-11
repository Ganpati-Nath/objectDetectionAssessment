from ultralytics import YOLO
import cv2
import json
from imageUtils import save_cropped_image
from hierarchy import associate_objects
from jsonFormatter import format_results_to_json


def detect_objects(video_path, output_json_path, output_dir):
    # Load a lightweight YOLO model for faster processing
    model = YOLO("yolov5n.pt")  # Nano model for speed optimization

    cap = cv2.VideoCapture(video_path)
    results_list = []
    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame for faster inference
        frame = cv2.resize(frame, (320, 240))  # Reduce resolution to speed up processing

        frame_id += 1
        results = model(frame)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = model.names[cls]

                # Save cropped images for detected objects
                cropped_path = f"{output_dir}/{label}_{frame_id}.jpg"
                save_cropped_image(frame, [x1, y1, x2, y2], cropped_path)

                results_list.append({
                    "frame_id": frame_id,
                    "object": label,
                    "id": frame_id,  # Ensure unique ID for each detection
                    "bbox": [x1, y1, x2, y2],
                    "confidence": conf
                })

    cap.release()

    # Create hierarchical associations and format results to JSON
    hierarchy = associate_objects(results_list)
    format_results_to_json(hierarchy, output_json_path)

    print(f"Detection complete. Results saved to {output_json_path}")


if __name__ == "__main__":
    detect_objects(
        "./data/sample_video.mp4",         # Input video path
        "./data/output/results.json",      # Output JSON file path
        "./data/output"                    # Output directory for cropped images
    )