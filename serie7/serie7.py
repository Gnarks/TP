from umage import * 
from copy import deepcopy
from math import sqrt

def greyscale(mat_img):
    new_img = []
    for row in mat_img:
        new_line = []
        for r,g,b in row:
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
    
def convolution(mat_img,mat):
    new_img = deepcopy(mat_img)
    mid = len(mat)//2
    for i in range(len(mat_img)):
        for j in range(len(mat_img[i])):
            r,g,b = 0,0,0
            for k in range(len(mat)):
                for m in range(len(mat[k])):
                    if not (i - mid+k < 0 or i -mid+k > len(mat_img)-1 or j-mid +m <0 or j-mid +m >len(mat_img[i])-1):
                        r_pos,g_pos,b_pos = mat_img[i - mid+k][j-mid +m]
                        r += r_pos * mat[k][m]
                        g += g_pos * mat[k][m]
                        b += b_pos * mat[k][m]
            new_img[i][j] = (max(min(r,255),0),(max(min(g,255),0)),(max(min(b,255),0)))
    return new_img
    
def sobel(mat_img):
    convX = [[-1,0,1],[-2,0,2],[-1,0,1]]
    convY = [[-1,-2,-1],[0,0,0],[1,2,1]]
    gX = convolution(mat_img,convX)
    gY = convolution(mat_img,convY)
    final = deepcopy(mat_img)
    for i in range(len(mat_img)):
        for j in range(len(mat_img[i])):
            r = int(sqrt((gX[i][j][0])**2 + (gY[i][j][0])**2))
            g = int(sqrt((gX[i][j][1])**2 + (gY[i][j][1])**2))
            b = int(sqrt((gX[i][j][2])**2 + (gY[i][j][2])**2))
            final[i][j] = (r,g,b)
    return final

def is_sym(mat_img):
    hori = True
    verti = True
    for i in range(len(mat_img)):
        for j in range(len(mat_img[i])):
            if mat_img[i][j] != mat_img[i][len(mat_img[i])-j-1]:
                verti = False
            if mat_img[i][j] != mat_img[len(mat_img)-i-1][j]:
                hori = False
    return hori,verti


def flou(img,r):
    new_img = deepcopy(img)
    total = 0
    neighbours = []
    for i in range(-r-1,r+1):
        for j in range(-r-1,r+1):
            if abs(i)+abs(j) <=2:
                neighbours.append((i,j))
                total+=1
    
    for i in range(len(img)):
        for j in range(len(img[i])):
            red,green,blue = 0,0,0
            for neighbour in neighbours:
                if not (i+neighbour[0] < 0 or i+neighbour[0]>len(img)-1 or j+neighbour[1] <0 or j+neighbour[1] >len(img[i])-1):
                    red+= img[i+neighbour[0]][j+neighbour[1]][0]                    
                    green+= img[i+neighbour[0]][j+neighbour[1]][1]
                    blue+= img[i+neighbour[0]][j+neighbour[1]][2]
                    
            new_img[i][j] = (red//total,green//total,blue//total)
    return new_img

first_im = load("NYC.jpg")
sobel_test = flou(first_im,2)
save(sobel_test,"flou")
