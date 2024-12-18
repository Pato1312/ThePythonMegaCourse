import cv2

try:
    face_cascade = cv2.CascadeClassifier(
        "C:\\Users\\pato1\\OneDrive\\Documentos\\PythonMegaCourse\\modules\\module17\\faces\\haarcascade_frontalface_default.xml"
    )
    print("Cascade classifier loaded successfully.")
except:
    print("Error loading cascade classifier.")


try:
    img = cv2.imread(
        "C:\\Users\\pato1\\OneDrive\\Documentos\\PythonMegaCourse\\modules\\module17\\faces\\photo.jpg"
    )
    print("Photo loaded successfully.")
except:
    print("Error loading photo.")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.1,
    minNeighbors=5,
)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)


cv2.imshow("Face recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
