import math
from find_poker_hand import find_poker_hand
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
# capture = cv2.VideoCapture("../Videos/motorbikes-1.mp4")


model = YOLO("../yolo_weights/playingCards.pt")
classNames = [
    '10C', '10D', '10H', '10S',
    '2C', '2D', '2H', '2S',
    '3C', '3D', '3H', '3S',
    '4C', '4D', '4H', '4S',
    '5C', '5D', '5H', '5S',
    '6C', '6D', '6H', '6S',
    '7C', '7D', '7H', '7S',
    '8C', '8D', '8H', '8S',
    '9C', '9D', '9H', '9S',
    'AC', 'AD', 'AH', 'AS',
    'JC', 'JD', 'JH', 'JS',
    'KC', 'KD', 'KH', 'KS',
    'QC', 'QD', 'QH', 'QS'
]

while True:
    success, img = capture.read()
    results = model(img, stream=True)
    hand = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w , h))
            class_name = classNames[int(box.cls[0])]
            confidence = math.ceil((box.conf[0] * 100))/100
            cvzone.putTextRect(
                img,
                f"{class_name} - {confidence}",
                (max(0,x1), max(35, y1)),
                scale=0.7,
                thickness=1
            )
            hand.append(class_name)
    # print(hand)
    hand = list(set(hand))
    if len(hand) == 5:
        result = find_poker_hand(hand)
        cvzone.putTextRect(
            img,
            f"Your Hand: {result}",
            (100, 100),
            scale=2,
            thickness=5
        )
        for i, card in enumerate(hand):
            cvzone.putTextRect(img, card, (50 + i * 100, 50), scale=1, thickness=2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)