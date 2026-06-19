class RandomNumberGenerator:
    def __init__(self, seed=None):
        # Set the seed for reproducibility
        self.seed = seed if seed is not None else int(1000 * time.time())
        self.m = 2 ** 32
        self.a = 1664525
        self.c = 1013904223

    def random(self):
        # Linear congruential generator formula
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m

    def randint(self, low, high):
        # Generate a random integer in the range [low, high]
        return low + int(self.random() * (high - low + 1))