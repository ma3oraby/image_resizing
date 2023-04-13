from PIL import Image 
import os 

#take image size from user 
fit_size = int(input("plz enter image size : "))

#locate output folder 
output_folder =  input("enter folder name you want to save : ")

#check if output folder is exist or create it 
if not os.path.exists(output_folder) : 
    os.mkdir(output_folder)

for file_name in os.listdir(('.')):
    if not file_name.endswith((".png" , ".jpg" , ".jpeg")): #check if the file is not image  
        continue

    ## open image , get image size  
    image = Image.open(file_name)
    width , height = image.size
    
    #check if image width & height > fit_size  
    if width > fit_size and height > fit_size : 
        if width > height :
            height = int((fit_size/width)*height)
            width = fit_size

        else :
            width = int((fit_size/height)*width)
            height = fit_size 

        ##resize images
        image = image.resize((width , height))
        print ('resizing : %s'  %(file_name))
        
    ##save resized images
    image = image.save(os.path.join(output_folder , file_name))

print ("Done resizing all Images ..")   

