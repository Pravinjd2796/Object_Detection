# # Install the necessary libraries
# !pip install ultralytics




import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')  # Use yolov8n.pt for YOLOv8 Nano, or choose a different model

def detect_objects(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_number = 0
    results = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform object detection
        detections = model(frame)
        for detection in detections.pandas().xyxy[0].to_dict(orient='records'):
            results.append({
                'frame': frame_number,
                'class': detection['name'],
                'confidence': detection['confidence'],
                'bbox': detection['xyxy']
            })
        
        frame_number += 1

    cap.release()
    return results

# from ultralytics import YOLO

# def detect_objects(video_path, conf_threshold=0.5, iou_threshold=0.4):
#     # Load YOLOv8 model (use a pre-trained model or your own)
#     model = YOLO('yolov8n.pt')
    
#     # Perform detection
#     results = model.predict(video_path, conf=conf_threshold, iou=iou_threshold)
    
#     detections = []
    
#     # Check the type of results
#     if isinstance(results, list):
#         for result in results:
#             if hasattr(result, 'pandas'):
#                 # Access results as a pandas DataFrame
#                 df = result.pandas().xyxy[0]
#                 for _, row in df.iterrows():
#                     detections.append({
#                         'class': row['name'],
#                         'confidence': row['confidence'],
#                         'bbox': [row['xmin'], row['ymin'], row['xmax'], row['ymax']],
#                         'frame': 0  # YOLOv8 might not provide frame information directly
#                     })
#             else:
#                 # Handle cases where result is not as expected
#                 detections.append({
#                     'class': 'unknown',
#                     'confidence': 0.0,
#                     'bbox': [0, 0, 0, 0],
#                     'frame': 0
#                 })
#     else:
#         # Handle cases where results are not in list format
#         print("Unexpected format of results.")
    
#     return detections
