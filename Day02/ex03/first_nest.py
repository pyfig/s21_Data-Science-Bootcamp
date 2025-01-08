import sys
import os

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
        def counts(self, data):
            heads = sum(1 for item in data if item[0] == 1)
            tails = len(data) - heads
            return heads, tails
        
        def fractions(self, heads, tails):
            total = heads + tails
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            return head_fraction, tail_fraction

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Please provide path to data file")
    
    research = Research(sys.argv[1])
    data = research.file_reader()
    print(data)
    
    calc = research.Calculations()
    heads, tails = calc.counts(data)
    print(heads, tails)
    
    head_fraction, tail_fraction = calc.fractions(heads, tails)
    print(head_fraction, tail_fraction)
        