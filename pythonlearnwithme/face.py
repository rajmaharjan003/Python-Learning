import cv2

# Load cascade
face_cap = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
)

# Start camera (Windows stable mode)
video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, video_data = video_cap.read()

    if not ret:
        print("Failed to access camera")
        break

    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    faces = face_cap.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Live Face Detection", video_data)

    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()
cv2.destroyAllWindows()
