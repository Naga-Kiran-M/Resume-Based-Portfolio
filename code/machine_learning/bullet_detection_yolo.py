# Bullet Hole Detection Using YOLO (Deep Learning)

import cv2
from ultralytics import YOLO

# Load YOLOv8 Pretrained Model
model = YOLO("yolov8n.pt")  # Using a pre-trained model

# Load Target Image
image_path = "assets/images/target.jpg"
image = cv2.imread(image_path)

# Perform Object Detection
results = model(image)

# Draw Bounding Boxes
for box in results.xyxy[0]:  # Iterate through detected objects
    x1, y1, x2, y2, confidence, cls = box
    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(image, f"Bullet Hole {confidence:.2f}", (int(x1), int(y1) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Save & Display Output
cv2.imwrite("assets/images/bullet_detection_output.jpg", image)
cv2.imshow("Bullet Hole Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
