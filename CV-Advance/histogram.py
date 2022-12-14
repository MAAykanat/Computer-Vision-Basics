### Used image, video and gif dataset is taken from Kaggle and link is below
### |--------------------------------------------------------------------------------| ###
### https://www.kaggle.com/datasets/bulentsiyah/opencv-samples-images?resource=download
### |--------------------------------------------------------------------------------| ###

    ###NOTES###
       
    ###SOURCES###
    
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def saveGraph(figure, title, xlab, ylab, xlim, savePath):
    #Saving matplolib graph to file
    plt.figure()
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xlim)
    plt.plot(figure)
    plt.savefig(savePath)

def main():
    path = "put location to this string"
    savePath= os.getcwd() + "/CV-Advance/Histogram-Results"

    img = cv.imread(path + "/data/fruits.jpg")
    cv.imshow("Original-Image", img)

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Gray-Image", gray)

    blank = np.zeros(img.shape[:2], dtype='uint8')
    cv.imshow("Blank", blank)

    mask = cv.circle(blank, center=(blank.shape[1]//2, blank.shape[0]//2), radius=120, color=255, thickness=-1)

    # masked = cv.bitwise_and(img,img, mask=mask)
    # cv.imshow("Masked", masked)

    #Gray-Scale Histogtam
    gray_hist = cv.calcHist([gray], [0], mask=None,histSize=[256],ranges=[0,256])
    gray_hist_mask = cv.calcHist([gray], [0], mask=mask,histSize=[256],ranges=[0,256])

    saveGraph(figure=gray_hist, title="Gray-Scale Histogram", xlab="Bins", ylab="# of pixels", xlim=[0,256], savePath=savePath+"/Gray-Scale Histogram.png")
    saveGraph(figure=gray_hist_mask, title="Masked Gray-Scale Histogram", xlab="Bins", ylab="# of pixels", xlim=[0,256], savePath=savePath+"/Masked Gray-Scale Histogram.png")

    #Colour Histogram
    color= ('b','g','r')

    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    for i,col in enumerate(color):
        color_hist=cv.calcHist([img], [i], mask=None, histSize=[256], ranges=[0,256]) 
        plt.xlim([0,256])
        plt.plot(color_hist,col)
    plt.savefig(savePath + "/Color Histogram.png")

    cv.waitKey()
    cv.destroyAllWindows()

if __name__=='__main__':
    try:
        main()
    except:
        pass