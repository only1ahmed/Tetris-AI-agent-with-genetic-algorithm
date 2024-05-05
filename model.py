import tetris_base
import heuristic_functions
import random

NUM_OF_GENES = 9
NUM_OF_CHROMOSOMES = 15
NUM_OF_EVOLUTIONS = 10

PERECENTAGE_OF_MUTATED = 0.2
PERECENTAGE_OF_SELECTION = 0.1

MAX_SCORE = 10000
AUTO_GAME = 3

class Chromosome:
    def __init__(self,genes,tetris_game):
        self.genes = []
        self.fitness_score = 0
        self.tetris_game = tetris_game
        if genes == None:
            for i in range(NUM_OF_GENES):
                self.genes.append(random.randint(-10, 10))
        else:
            self.genes = genes
    
    def update_fitness_score(self, heuristics, game_score):
        self.fitness_score = 0
        for i in range(NUM_OF_GENES):
            self.fitness_score += self.genes[i] * heuristics[i]
        self.fitness_score += game_score
    
    def best_play(self,board,piece,next_piece,column):
        best_rotation = 0
        play_score = -10000000

        # TODO: write formula
        for rot in range(self.tetris_game.PIECES[piece['shape']]):
            # use calc_move_data 
            # calculate the score for each rotation and return the best rotation and its score
            # dot multiplication baby
            # for the next_piece you could get the new_board from the first piece and recalculate the
            # calc_move_data based on the next_piece
            pass

        return best_rotation,play_score

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

    def __init__(self, num_of_generations,tetris_game):
        self.chromosomes = []   # List of Chromosomes
        self.chromo_scores = [] # Fitness Score for each Chromosome
        self.NUM_OF_GENERATIONS = num_of_generations
        self.optimal_chromosome = None
        self.tetris_game = tetris_game
    
    
    # NOTE: maybe try to take chromosoms as an input (not nessacary)
    def init_chromosomes(self):
        for i in range(NUM_OF_CHROMOSOMES):
            #TODO: Take Input from a file
            self.chromosomes.append(Chromosome(tetris_game=self.tetris_game))

    def train(self):
    
        for i in range(self.NUM_OF_GENERATIONS):
            self.cal_fitness()
            self.selection()
            offspring_chrom = self.crossover()
            offspring_chrom = self.mutate(offspring_chrom)
            self.replace(offspring_chrom)
        
        # Return the best chromosome
        #TODO: make sure to return the best chromosome
        optimal_chromosome = self.chromosomes[0]

    '''
    You will be given the
    current state of the board, the current piece to be played and the next piece, and what column I am
    thinking of playing it on. You will be asked to return what is the best rotation and its score. You can
    score each rotation and check who has highest and return it and its associated score.
    '''
    def cal_fitness(self):
        # Run the game for each chromosome and calculate the fitness score
        for chrom in self.chromosomes:
            #TODO: 
            data = self.tetris_game.run_game(AUTO_GAME,chrom)
            chrom.update_fitness_score(data)


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

    def save_chromosomes(self):
        pass


class AI:
    def computer_plays(self, board, piece, chromosom):
        pass

    def test_all_moves(self, board, piece, chromosom):
        pass

    def play_move(self, board, rotation, column):
        pass
