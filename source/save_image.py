import json
from utils import ImageSaver

if __name__ == '__main__':
    saver = ImageSaver.ImageSaver()
    f = open('data/_image_data.json')
    dataset = json.load(f)
    f.close()

    for i, data in enumerate(dataset):
        if saver(data["id"], data["url"]):
            print "Success:", data["id"]
        else:
            print "Failure:", data["id"]
            print "Delete:", data["id"]
            dataset.pop(i)

    f = open('data/_image_data.json', 'wb')
    json.dump(dataset, f)
    f.close()
