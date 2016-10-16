import urllib
import os

class ImageSaver:
    def __init__(self):
        self.init_dir()

    def __call__(self, id, url):
        resource = urllib.urlopen(url)
        outfile = open('data/images/'+str(id)+'.jpg', "wb")
        try:
            outfile.write(resource.read())
            outfile.close()
            return 1
        except:
            return 0

    def init_dir(self):
        directory = 'data/images'
        try:
            os.makedirs(directory)
        except:
            pass
