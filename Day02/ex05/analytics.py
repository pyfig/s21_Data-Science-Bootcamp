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
                    predictions.append([1, 0]) # орел  
                else:
                    predictions.append([0, 1]) # орешко  
            return predictions

        def predict_last(self):
            return self.data[-1]

        def save_file(self, data, file_name, extension):
            with open(f"{file_name}.{extension}", "w") as file:
                file.write(data)
