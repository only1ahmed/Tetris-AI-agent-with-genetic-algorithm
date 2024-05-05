import computer_player
import tetris_base
import random

NUM_OF_GENES = 9
COUNT_OF_CHROMOSOMES = 15
NUM_OF_EVOLUTIONS = 10
PERECENTAGE_OF_MUTATED = 0.2
CHROMOSOMS = []


class Chromosom:
    def __init__(self, genes=None):
        self.Genes = []
        if genes == None:
            for i in rage(NUM_OF_GENES):
                self.Genes.append(random.randint(-1000, 1000))
        else:
            self.Genes = genes


# KHALED
# NOTE: maybe try to take chromosoms as an input (not nessacary)
def init_chromosoms(mode=None):
    for i in range(COUNT_OF_CHROMOSOMES):
        CHROMOSOMS.append(Chromosom())


# MOHSEN
# The main function for training the chromosomes
# Note: When using run_game() function, make sure to pass (False, chromosome)
def train():
    pass


# FAWZY
# Apply ecolution on chromosomes
def evolute():
    pass


# FAWZY
# Play the game and evaluate the final score of the given chromosom (The highest final score the better)
def evaluate(chromosom):
    pass


# OMAR
# Select the best suited chromosomes for the next stage of mating
def selection(scores):
    pass


# OMAR
# Mate chromosomes to get the new generation
def crossover():
    pass


# MOHSEN
# Mutate some of the chromosomes of the new generation
def mutate():
    pass
