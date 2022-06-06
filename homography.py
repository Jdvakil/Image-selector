import cv2
import matplotlib.pyplot as plt


S = 9
B = 50

for i in range(1,4):
    img = cv2.imread(f'/Users/jayvakil/Documents/GitHub/Homography/{i}_cam{i-1}.jpg')
    img = img[:424, :550]
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 131, 15)
    _, _, boxes, _ = cv2.connectedComponentsWithStats(binary_img)
    boxes = boxes[1:]
    filtered_boxes = []
    for x,y,w,h,pixels in boxes:
        if pixels < 10000 and h < B and w < B and h > S and w > S:
            filtered_boxes.append((x,y,w,h))


    for x,y,w,h in filtered_boxes:
        cv2.rectangle(img, (x,y), (x+w,y+h), (5,5,255),2)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    

    
    