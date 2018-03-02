import PIL
import PIL.ImageDraw
import os.path

def changeImages(directory=None):
    if directory == None:
        directory = os.getcwd()
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    imageList, fileList = getImages(directory)
    fileName, fileType = os.path.splitext(fileList)
    newImage = FinalImage(imageList)
    newImage_fileName = os.path.join(new_directory, fileName + '.png')
    newImage.save(newImage_fileName)
    
def FinalImage(images):
    return images
    
def getImages(directory=None):
    """ Returns PIL.Image objects for all the images in directory.

    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a PIL.Image object for each image file in root_directory,     
    and a list with a string filename for each image file in root_directory
    """

    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified

    image_list=[] # Initialize aggregators
    file_list = []    


    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
