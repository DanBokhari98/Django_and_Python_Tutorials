import cv2
print(cv2.CASCADE_SCALE_IMAGE)
face_cascade = cv2.CascadeClassifier('C:\\Users\\HD PC\\Desktop\\Danish\\opencv\\data\\haarcascadeshaarcascade_frontalface_default.xml')
#color =  cv2.cvtColor('C:\\Users\\HD PC\\Desktop\\Danish\\opencv\\modules\\videoio\\src\\cap_winrt')
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Input', frame)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
