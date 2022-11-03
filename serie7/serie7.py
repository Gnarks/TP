from umage import * 
from copy import deepcopy

def greyscale(mat_img):
    new_img = []
    for row in mat_img:
        new_line = []
        for column in row:
            r = column[0]
            g = column[1]
            b = column[2]
            v = int(r*0.2125 + 0.7154*g + 0.0721*b)
            new_line.append((v,v,v))
        new_img.append(new_line)
    return new_img

def greyScale(mat_img):
    new_img = deepcopy(mat_img)
    for i in range(len(mat_img)):
        for j in range(len(mat_img[i])):
            r = mat_img[i][j][0]
            g = mat_img[i][j][1]
            b = mat_img[i][j][2]
            v = int(r*0.2125 + 0.7154*g + 0.0721*b)
            new_img[i][j] = (v,v,v)
    return new_img
    
first_im = load("rainbow.jpg")
save(greyScale(first_im),"test")


