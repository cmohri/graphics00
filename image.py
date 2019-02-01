import math

f = open("image.ppm", "w+")
f.write("P3\n500 500\n255\n")

for i in range(500):    
    for j in range(500):
         s = str(i% 255) + " " + str(j%255) + " 0 "
         f.write(s)
    f.write("\n")

f.close()


f = open("image2.ppm", "w+")
f.write("P3\n400 400\n255\n")

for i in range(400):
    for j in range(400):
        if i % 20 == 0 or i%20 == 1:
            s = "255 255 255 "
        elif j % 20 == 0 or j%20 == 1:
            s =	"255 255 255 "
        else:
            s = "0 0 0 "
        f.write(s)

f.close()


f = open("circle.ppm", "w+")
f.write("P3\n1000 1000\n255\n")

centerx = 250
centery = 250

for i in range(1000):
    for j in range(1000):
        val = round(math.sqrt( (i-centerx)**2 + (j-centery)**2))
        which_c = int(val / 255)
        val %= 255
        if which_c % 3 ==  0:
            s = str(int(val)) + " 0 0 "
        elif which_c %3==  1:
            s = "0 " + str(int(val)) + " 0 "
        else:
            s = "0 0 "+ str(int(val)) + " "        
        f.write(s)

f.close()
