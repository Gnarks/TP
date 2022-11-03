from umage import * 
from copy import deepcopy

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
            #som = 0
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
    
first_im = load("pont.jpg")
#grey = greyScale(first_im)
conv = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]


save(convolution(first_im,conv),"test")
