import math
from ultralytics import YOLO
import cv2
import cvzone
# import torch
from sort import *
import numpy as np

# print(torch.version.cuda)

ACCEPTABLE_CLASSES = ["person"]
VIDEO_SOURCE = "../Videos/people.mp4"
VIDEO_MASK = "../Masks/people.png"
VIDEO_GRAPHIC = "../Graphics/people.png"

# For a video
capture = cv2.VideoCapture(VIDEO_SOURCE)
mask = cv2.imread(VIDEO_MASK)

model = YOLO("../yolo_weights/yolov8l.pt")
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

limitsUp = [103, 161, 296, 161]
limitsDown = [527, 489, 735, 489]

totalCountUp = []
totalCountDown = []

while True:
    success, img = capture.read()
    imgRegion = cv2.bitwise_and(img, mask)
    graphic = cv2.imread(VIDEO_GRAPHIC, cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (730, 260))
    results = model(imgRegion, stream=True)

    detections = np.empty((0, 5))

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1
            class_name = classNames[int(box.cls[0])]
            confidence = math.ceil((box.conf[0] * 100))/100

            if class_name in ACCEPTABLE_CLASSES and confidence > 0.3:
                # SHow bounding rectangle
                cvzone.cornerRect(img, (x1, y1, w, h), l=10, t=2)
                # Show confidence and class name
                cvzone.putTextRect(
                    img,
                    f"{class_name} - {confidence}",
                    (max(0,x1), max(35, y1)),
                    scale=0.5,
                    thickness=1,
                    offset=3
                )
                detections = np.vstack((detections, np.array([x1, y1, x2, y2, confidence])))

    results_tracker = tracker.update(detections)

    cv2.line(img, (limitsUp[0], limitsUp[1]), (limitsUp[2], limitsUp[3]), (0, 0, 255), 5)
    cv2.line(img, (limitsDown[0], limitsDown[1]), (limitsDown[2], limitsDown[3]), (0, 0, 255), 5)

    for result in results_tracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2, id = int(x1), int(y1), int(x2), int(y2), int(id)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=10, t=2)
        cvzone.putTextRect(
            img,
            f"{id}",
            (max(0, x1), max(35, y1)),
            scale=1,
            thickness=1,
            offset=5
        )
        cx, cy = x1 + w//2, y1 + h//2
        cv2.circle(img, (cx, cy), 5, (0, 0, 255))

        if finish_line[0] < cx < finish_line[2] and finish_line[1] - 15 < cy < finish_line[1] + 15:
            if id not in total_cars:
                total_cars.append(id)
                cv2.line(img, (finish_line[0], finish_line[1]), (finish_line[2], finish_line[3]), (0, 255, 0), 5)

    # cvzone.putTextRect(
    #     img,
    #     f"Total: {len(total_cars)}",
    #     (50, 50),
    # )
    cv2.putText(img, str(len(total_cars)), (255, 100), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 250), 8)
    cv2.imshow("Image", img)
    cv2.waitKey(1)