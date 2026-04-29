import cv2, sys, numpy, os
cam = cv2.VideoCapture(0) # This is primary cam
#haar = cv2.CascadeClassifier(
#    cv2.data.haarcascades + "haarcascade_car_default.xml")
haar = cv2.CascadeClassifier('carcascade.xml')
dataset = "carss"
subdata = "cars"
path = os.path.join(dataset, subdata)
if not os.path.isdir(path):
    os.mkdir(path)
width, height = 100, 130
count = 1
c = 0
while count < 100 and c < 10:
    r, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting of clrs to gray make easier detection
    cars = haar.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)
        car = gray[y:y+h, x:x+w]
        carresized = cv2.resize(car, (width, height))
        cv2.imwrite('% s% s.png' %(path,count), carresized)
    count += 1
    c = len(cars)
    cv2.imshow('OpenCV', image)
    key = cv2.waitKey(10)
    if key == 27:
        break
cv2.destroyAllWindows()