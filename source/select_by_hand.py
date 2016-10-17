import json
import commands

class HandSelector:
    def __init__(self, path_to_data):
        self.get_json(path_to_data)

    def get_json(self, path_to_data):
        f = open(path_to_data)
        self.dataset = json.load(f)
        self.dataset_size = len(self.dataset)
        f.close()

    def show(self, image_path):
        commands.getoutput('xli ' + image_path)

    def hand_select(self):
        self.selected_dataset = []
        print "size of dataset:", self.dataset_size
        for i, data in enumerate(self.dataset):
            image_path = 'data/images/' + str(data['id']) + '.jpg'
            self.show(image_path)
            print "0:ok, 1:ng -> ",
            while True:
                if self.judge(data):
                    break
                else:
                    continue
            print str(i), "/", str(self.dataset_size)

    def dump(self, path_to_sorted_data):
        f = open(path_to_sorted_data, 'wb')
        json.dump(self.dump_dataset, f)
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


if __name__ == '__main__':
    hs = HandSelector('data/image_data.json')
    hs.hand_select()
    hs.dump()
