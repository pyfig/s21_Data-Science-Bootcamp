import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        with open(self.path, "r") as file:
            lines = file.readlines()
        
        start_idx = 1 if has_header else 0
        
        result = []
        for line in lines[start_idx:]:
            values = line.strip().split(',')
            result.append([int(values[0]), int(values[1])])
        
        return result

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(1 for item in self.data if item[0] == 1)
            tails = len(self.data) - heads
            return heads, tails

        def fractions(self):
            heads, tails = self.counts()
            total = heads + tails
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            return head_fraction, tail_fraction

    class Analytics(Calculations):
        def predict_random(self, n):
            predictions = []
            for _ in range(n):
                if randint(0, 1) == 0:
                    predictions.append([1, 0])
                else:
                    predictions.append([0, 1])
            return predictions

        def predict_last(self):
            return self.data[-1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Please provide the path to the data file")

    research = Research(sys.argv[1])
    data = research.file_reader()
    print("Data from file_reader():", data)

    analytics = Research.Analytics(data)

    heads, tails = analytics.counts()
    print("Counts from counts():", (heads, tails))

    head_fraction, tail_fraction = analytics.fractions()
    print("Fractions from fractions():", (head_fraction, tail_fraction))

    random_predictions = analytics.predict_random(3)
    print("Random predictions from predict_random():", random_predictions)

    last_prediction = analytics.predict_last()
    print("Last prediction from predict_last():", last_prediction)
