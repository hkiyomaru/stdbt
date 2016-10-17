import urllib
import os


class ImageSaver:
    def __init__(self):
        self.init_dir()

    def __call__(self, id, url):
        resource = urllib.urlopen(url)
        path_to_image = os.path.join('data', 'images', str(id)+'.jpg')
        outfile = open(path_to_image, "wb")
        try:
            outfile.write(resource.read())
            outfile.close()
            return 1 # success(True)
        except:
            return 0 # failure(False)

    def init_dir(self):
        directory = 'data/images'
        try:
            os.makedirs(directory)
        except:
            pass
