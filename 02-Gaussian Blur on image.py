import cv2

img = cv2.imread(r"C:\Users\admin\Downloads\image.jfif")

if img is None:
    print("Image not found")
else:
    blur = cv2.GaussianBlur(img, (5,5), 0)

    cv2.imshow("Blur Image", blur)

    cv2.imwrite("blur_image.jpg", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
