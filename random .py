import random

class randomgenerator:
    def __init__(self, start, end):
      self.start = start
      self.end = end

    def random_number(self):
          return random.randint(self.start, self.end)

rg = randomgenerator(1, 20)

print("Random number:", rg.random_number())
     

























