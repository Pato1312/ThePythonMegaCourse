import cv2

video = cv2.VideoCapture(0)
fps = 1

while True:
    fps += 1
    check, frame = video.read()

    # gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRABANDO...", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
