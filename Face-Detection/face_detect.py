

import cv2 as cv

def face_rectangle(img, gray, scaleFactor, minNeigbors):
    haar_cascade = cv.CascadeClassifier('.\Face-Detection\haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeigbors)

    print("Number of faces found: ", len(faces_rect))
    for (x,y,w,h) in faces_rect:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=3)
    return img

def main():
        
    path = "D:/!!!MAAykanat Dosyalar/MAA_Own_Study/CV-Data/Face-Detection"

    img = cv.imread(path + '/foto.png')
    cv.imshow('Original Image', img)
    print(img.shape) #--> Image shape is (1116, 1060, 3)

    img = cv.resize(img,((int(img.shape[1]*0.75)), int(img.shape[0]*0.75)))

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray Image', gray)

    face_rectangle(img,gray, scaleFactor= 1.3, minNeigbors=5)

    cv.imshow('Detected Faces', img)
    cv.waitKey()
    cv.destroyAllWindows()
    
    # Group-1 Photo
    group1 = cv.imread(path + '/Group1.jpeg')
    cv.imshow("Group-1 Photo", group1)

    gray_group1 = cv.cvtColor(group1, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray-Group1", gray_group1)

    face_rectangle(group1, gray_group1, scaleFactor= 1.1, minNeigbors=3)
    
    cv.imshow("Group1-Detected Image",group1)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Group-2 Photo
    group2 = cv.imread(path + '/Group2.jpeg')
    cv.imshow("Group-1 Photo", group2)

    gray_group2 = cv.cvtColor(group2, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray-Group1", gray_group2)

    face_rectangle(group2, gray_group2, scaleFactor= 1.3, minNeigbors=5)
    
    cv.imshow("Group2-Detected Image", group2)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        main()
    except:
        pass
