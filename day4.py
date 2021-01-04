# OpenCV
import cv2 as cv
print(cv.__version__)

# mot so thao tac xu ly anh
image_path = "samedata/Dan.jpg"

# Hien thi anh
image_read = cv.imread(image_path)
cv.imshow('Hien thi anh', image_read)
cv.waitKey(0)

# Kiem tra kich thuoc anh
(h, w, d) = image_read.shape
print("rong={}, cao={}, sau={}".format(w, h, d))

# Thay doi kich thuoc anh
(h, w, d) = image_read.shape
r = 320.0 / w 
dim = (320, int(h * r))
resized = cv.resize(image_read, dim)
cv.imwrite('samedata/Dan1.jpg', resized)
