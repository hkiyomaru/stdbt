import json


class TopSelector:
    def __init__(self, path_to_data):
        self.get_json(path_to_data)

    def get_json(self, path_to_data):
        f = open(path_to_data)
        self.dataset = json.load(f)
        f.close()

    def sort(self, num_of_top):
        self.sorted_dataset = sorted(self.dataset, key=lambda k: k['positive']-k['negative'], reverse=True) # sort by polarity
        positive_dataset = self.sorted_dataset[:num_of_top]
        print "Lowest positive score:", positive_dataset[-1]['positive']
        negative_dataset = self.sorted_dataset[-num_of_top:]
        print "Lowest negative score:", negative_dataset[0]['negative']
        self.dump_dataset = positive_dataset + negative_dataset

    def dump(self, path_to_sorted_data):
        f = open(path_to_sorted_data, 'wb')
        json.dump(self.dump_dataset, f)
        f.close()


if __name__ == '__main__':
    ts = TopSelector('data/image_data.json')
    ts.sort(20000)
    ts.dump('data/_image_data.json')
