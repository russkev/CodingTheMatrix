import sys
#sys.path.append('C:\\Users\\kev_k\\Documents\\Coursera\\CodingTheMatrix\\03_resources\\02_TheField')
sys.path.append('E:\\DOCS\\3D\\Resources\\Tutorials\\Coursera\\CodingTheMatrix\\03_resources\\02_TheField')
from plotting import plot

L = [2+2j, 3+2j]
plot(L)
from image import *
#I = color2gray(file2image('C:\\Users\\kev_k\\Documents\\Coursera\\CodingTheMatrix\\03_resources\\02_TheField\\img01.png'))
I = color2gray(file2image('E:\\DOCS\\3D\\Resources\\Tutorials\\Coursera\\CodingTheMatrix\\03_resources\\02_TheField\\img01.png'))
r = len(I)
c = len(I[0])

#Make an array with complex numbers that define the brightness of individual pixels
M = [x + y*1j for x in range(c) for y in range(r) if I[r - y - 1][x] < 120]

#plot takes an optional argument (2nd) that tells it the size to make the plot
#and another optional argument (3rd) that defines the size in pixels of the plot.

plot(M, max(r,c), 1)

#moves original up
plot({z+(1+2j) for z in L})

#moves picture to centre
plot([z - (c/2 + (r/2)*1j) for z in M], max(r,c), 1)