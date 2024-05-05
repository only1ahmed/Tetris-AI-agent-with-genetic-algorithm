import tetris_base
import random

NUM_OF_GENES = 9
NUM_OF_CHROMOSOMES = 15
NUM_OF_EVOLUTIONS = 10

PERECENTAGE_OF_MUTATED = 0.2
PERECENTAGE_OF_SELECTION = 0.1

MAX_SCORE = 10000


class Chromosome:
    def __init__(self, genes=None):
        self.Genes = []
        if genes == None:
            for i in range(NUM_OF_GENES):
                self.Genes.append(random.randint(-1000, 1000))
        else:
            self.Genes = genes

'''
Initializes the chromosomes
Evolution (Training):
    Fitness for each chromosome(Population) (run_game)
    Selection ceil(Top 30%) 
    Crossover (Multi Point ) NOTE: maybe try to do weighted crossover
    Mutation (+- 0.1 or 0.3) 
    Replacement (Reintroduce)

'''
class GeneticAlgorithm:

    def __init__(self, num_of_generations):
        self.chromosomes = []   # List of Chromosomes
        self.chromo_scores = [] # Fitness Score for each Chromosome
        self.NUM_OF_GENERATIONS = num_of_generations
    
    
    # NOTE: maybe try to take chromosoms as an input (not nessacary)
    def init_chromosomes(self):
        for i in range(NUM_OF_CHROMOSOMES):
            #TODO: Take Input from a file
            self.chromosomes.append(Chromosome())

    def train(self):
    
        for i in range(self.NUM_OF_GENERATIONS):
            self.cal_fitness()
            self.selection()
            offspring_chrom = self.crossover()
            offspring_chrom = self.mutate(offspring_chrom)
            self.replace(offspring_chrom)


    def cal_fitness(self):
        pass

    def selection(self):
        # Update the chromosome list (delete the rest) ceil(Top 30%) 
        pass

    def crossover(self):
        # 1 2 3 4 = 6 off (4 C 2) 
        # Return new chromosomes
        pass

    def mutate(self,off_chroms):
        # mutated chromosomes
        pass
    
    def replace(self,off_chroms):
        pass


class AI:
    def computer_plays(self, board, piece, chromosom):
        pass

    def test_all_moves(self, board, piece, chromosom):
        pass

    def play_move(self, board, rotation, column):
        pass
