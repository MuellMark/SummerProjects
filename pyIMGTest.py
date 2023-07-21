from PIL import Image
import random

def makeBody():
    upper_limit= 5
    lower_limit = 75
    x = random.randint(20,45)
    y = random.randint(20,45)
    startx=x
    starty=y
    cont=True
    check1=True
    while(cont):
        #randInt = random.randint(0,100)
        while(check1):
            randInt = random.randint(0,100)
            if randInt<20: x-=1
            elif randInt<50: y-=1
            if(x==upper_limit or y==upper_limit):
                check1=False
            pixel_map[x,y]=(0, 0, 0, 255)
            
        cont=False

    print(x)
try: 
    img = Image.new(mode="RGB", size=(80, 80), color="White")
    # img  = Image.open("/Users/markymarkscomputer/Desktop/Summer Projects/SummerProjects/typhlosion HGSS.png")
    #img = img.rotate(180) 
    pixel_map = img.load()
    width,height = img.size
    makeBody()
    # for i  in range(width):
    #     for j in range(height):
    #         if(i==j):
    #             pixel_map[i,j]=(0, 0, 0, 255)
            # if(pixel_map[i,j]!=(255, 255, 255, 0)):
            #     #if(pixel_map[i,j][0]!=16):
            #     if(pixel_map[i,j]==(32, 65, 106, 255)):
            #         print(pixel_map[i,j])
            #         pixel_map[i,j]=(255, 0, 0, 255)
    #print(img.size)
    img.save("/Users/markymarkscomputer/Desktop/Summer Projects/SummerProjects/test.png")
except IOError:
    pass
