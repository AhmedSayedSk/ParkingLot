import sys
import cv2 as cv
import numpy as np


# contributor: Menna & Abdullah

def main(argv):
    #file = 'Empty1.jpg'
    file = 'Empty2.jpg'
    #file = 'Empty3.png'
    #file = 'empty_lot.jpg'

    # load the input image
    img = cv.imread(file, cv.IMREAD_GRAYSCALE)

    # Check if image is loaded fine
    if img is None:
        print('Error opening image!')
        print('Usage: hough_lines.py [image_name -- default ' + file + '] \n')
        return -1

    dst = cv.Canny(img, 250, 350, None, 3)
    # here i can change the value of the min and max gradients depending on the brightness of the image
    cv.imshow ("canny", dst)
    # Copy edges to the images that will display the results in BGR
    new_dst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    dstP = np.copy(new_dst)
    # using HoughLinesP function to get the lines detected with both the start and the end points
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)


    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(dstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 6, cv.LINE_AA)
            #print(l[0], "  ", l[1], "  ", l[2], "  ", l[3])
    # cv.LINE_AA >> gives anti-aliased line which looks great for curves.

    # show input image and output image
    cv.imshow("Source", img)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", dstP)

    # save the output image (used to record the output only - and - not a must in the main algorithm)
    #cv.imwrite("Empty1_r.jpg", dstP)
    #cv.imwrite("Empty2_r.jpg", dstP)
    #cv.imwrite("Empty3_r.jpg", dstP)
    #cv.imwrite("empty_lot_r.jpg", dstP)

    cv.waitKey()
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
