from PIL import Image
dir = "/home/pi/Desktop/raspi-cam/dad-test/"
fname="cat-spy_"
nimages = range(1,20,1)
compositeImage = Image.open(dir+fname+"%s.jpg" % 0)  #image 0 is base
compositeImage.putalpha(1)
blendedImage = Image.open(dir+fname+"%s.jpg" % 0)   #image 0 is base
blendedImage.putalpha(1)



for i in nimages:
    #bufImage = Image.open("fname%s.jpg" % i)
    currImage = Image.open(dir+fname+"%s.jpg" % i)
    currImage.putalpha(1)
    #alpha composite
    compositeImage = Image.alpha_composite(compositeImage, currImage)
    
    #blended image
    blendedImage = Image.blend(blendedImage, currImage, .1)

#save    
compositeImage.save(dir+"composite-test.jpg")
blendedImage.save(dir+"blended-test.jpg")


#show composites
compositeImage.show()
blendedImage.show()