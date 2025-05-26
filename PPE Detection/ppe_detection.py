import math

from ultralytics import YOLO
import cv2
import cvzone

import torch
print(torch.version.cuda)

# For webcam
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

# For a video
# capture = cv2.VideoCapture("../Videos/ppe-2-1.mp4")


model = YOLO("../yolo_weights/ppe.pt")
classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

SAFE_COLOR = (0, 255, 0)
SAFE_CLASSES = ['Hardhat', 'Mask', 'Safety Vest']
UNSAFE_COLOR = (0, 0, 255)
UNSAFE_CLASSES = ['NO-Hardhat', 'NO-Mask', 'NO-Safety Vest']
NORMAL_COLOR = (255, 0, 0)

while True:
    success, img = capture.read()
    results = model(img, stream=True)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1

            class_name = classNames[int(box.cls[0])]
            confidence = math.ceil((box.conf[0] * 100))/100

            if confidence > 0.5:
                if class_name in SAFE_CLASSES:
                    chosen_color = SAFE_COLOR
                elif class_name in UNSAFE_CLASSES:
                    chosen_color = UNSAFE_COLOR
                else:
                    chosen_color = NORMAL_COLOR

                cvzone.cornerRect(img, (x1, y1, w, h), colorR=chosen_color)
                cvzone.putTextRect(
                    img,
                    f"{class_name} - {confidence}",
                    (max(0,x1), max(35, y1)),
                    scale=0.7,
                    thickness=1,
                    colorR=chosen_color,
                    colorT=(255,255,255)
                )

    cv2.imshow("Image", img)
    cv2.waitKey(1)