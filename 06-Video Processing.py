import cv2

path = r"C:\Users\admin\Downloads\sample_video.mp4"

def play_video(delay, title):
    cap = cv2.VideoCapture(path)
    print(title + " - Press q to continue")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow(title, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Call function for different speeds
play_video(30, "Normal Speed")
play_video(100, "Slow Motion")
play_video(10, "Fast Motion")
