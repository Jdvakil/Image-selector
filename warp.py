import os
import matplotlib.pyplot as plt
import cv2
import numpy as np

RP07_RIGHT = np.array([[110,49],[192,63],[248,70],[117,205],[197,189],[252,178]],dtype=np.float32)
RP07_TOP = np.array([[97,67],[188,62],[279,62],[101,205],[194,201],[288,198]], dtype=np.float32)
RP07_LEFT = np.array([[302,132],[255, 161],[192,200],[267,34],[213,49],[138,70]],dtype=np.float32)

RP07_COORD ={
    'left': RP07_LEFT,
    'right': RP07_RIGHT,
    'top': RP07_TOP
}

ROBOT_CART_COORD = np.array([[0.7,-0.3],[0.7,0],[0.7,0.3],[0.25,-0.3],[0.25,0],[0.25,0.3]], dtype=np.float32)
robot_mm = np.array([[700,-300],[700,0],[700,300],[250,-300],[250,0],[250,300]], dtype=np.float32)
mark = ['left', 'right', 'top']

for i in mark:
    for j in mark:
        H, status = cv2.findHomography(RP07_COORD[i], RP07_COORD[j])
        cv2_img = cv2.imread(f'{os.getcwd()}/{i}.jpg',0)
        h, w = cv2_img.shape
        pts = np.float32([[0,0],[w-1,0],[w-1,h-1], [0,h-1]]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts, H)
        print(f"{i} - {dst}")
        im_warp = cv2.warpPerspective(cv2_img, H, (w,h))
        cv2.imshow(f"Source - {i}, dest - {j}",im_warp)
        #cv2.imwrite(f"warped_{i}.jpg", im_warp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
