import cv2

img = cv2.imread(r"C:\Users\admin\Downloads\image.jfif")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Image", gray)

    cv2.imwrite("gray_image.jpg", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
