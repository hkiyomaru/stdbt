import json
import os
import commands


class HandSelector:
    def __init__(self, path_to_data):
        self.get_json(path_to_data)
        self.selected_dataset = []

    def get_json(self, path_to_data):
        f = open(path_to_data)
        self.dataset = json.load(f)
        self.dataset_size = len(self.dataset)
        f.close()

    def show(self, image_path):
        commands.getoutput('xli ' + image_path)

    def hand_select(self):
        print "size of dataset:", self.dataset_size
        for i, data in enumerate(self.dataset):
            image_path = os.path.join('data', 'images', str(data['id'])+'.jpg')
            self.show(image_path)
            print "w:write, e:exclude -> ",
            while True:
                if self.judge(data):
                    break
                else:
                    continue
            print str(i), "/", str(self.dataset_size)

    def dump(self, path_to_sorted_data):
        f = open(path_to_sorted_data, 'wb')
        json.dump(self.selected_dataset, f)
        f.close()

    def judge(self, data):
        command = raw_input()
        if command == 'w':
            self.selected_dataset.append(data)
            return 1
        elif command == 'e':
            return 1
        else:
            return 0

    def evaluate(self):
        positive_num = 0
        negative_num = 0
        for data in self.selected_dataset:
            if data['positive'] - data['negative'] > 0:
                positive_num += 1
            else:
                negative_num += 1
        print "Total iamges:", len(self.selected_dataset)
        print "Positive images:", positive_num
        print "Negative images:", negative_num

if __name__ == '__main__':
    hs = HandSelector('data/_image_data.json')
    hs.hand_select()
    hs.dump('data/selected_image_data.json')
    hs.evaluate()
