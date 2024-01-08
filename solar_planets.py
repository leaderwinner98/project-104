import cv2


img = cv2.imread("solar-system.jpg")


texts = {
    "Mercury": (50, 50),
    "Venus": (150, 150),
    "Earth": (250, 250),
    "Mars": (350, 350),
    "Jupiter": (450, 450),
    "Saturn": (550, 550),
    "Uranus": (650, 650),
    "Neptune": (750, 750)
}


for planet, pos in texts.items():
    cv2.putText(img, planet, pos, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


cv2.imshow("output", img)
cv2.waitKey(0)


cv2.imwrite("Solar_systemwithname.jpg", img)
