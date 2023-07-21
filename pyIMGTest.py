from PIL import Image
#img  = Image.open(path)     
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
   
try: 
    img  = Image.open("/Users/markymarkscomputer/Desktop/Summer Projects/SummerProjects/typhlosion HGSS.png")
    #img = img.rotate(180) 
    pixel_map = img.load()
    width,height = img.size
    for i  in range(width):
        for j in range(height):
            if(pixel_map[i,j]!=(255, 255, 255, 0)):
                if(pixel_map[i,j][0]!=16):
                    pixel_map[i,j]=(255, 255, 0, 255)
    #print(img.size)
    img.save("/Users/markymarkscomputer/Desktop/Summer Projects/SummerProjects/typhlosion HGSS edited.png")
except IOError:
    pass
# Use the above statement within try block, as it can 
# raise an IOError if file cannot be found, 
# or image cannot be opened.