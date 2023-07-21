from PIL import Image
#img  = Image.open(path)     
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
   
try: 
    img  = Image.open("/Users/markymarkscomputer/Desktop/Summer Projects/SummerProjects/typhlosion HGSS.png")
    img = img.rotate(180) 
    img.save("/Users/markymarkscomputer/Desktop/Summer Projects/SummerProjects/typhlosion HGSS.png")
except IOError:
    pass
# Use the above statement within try block, as it can 
# raise an IOError if file cannot be found, 
# or image cannot be opened.