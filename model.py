import tetris_base as tb
import heuristic_functions
import random
import numpy as np

NUM_OF_GENES = 4
NUM_OF_CHROMOSOMES = 15
NUM_OF_EVOLUTIONS = 10

PERECENTAGE_OF_MUTATED = 0.2
PERECENTAGE_OF_SELECTION = 0.1

MAX_SCORE = 10000
GAME_MODE = 2

class Chromosome:
    def __init__(self,genes=None):
        self.genes = genes
        self.fitness_score = 0
        if genes == None:
            self.genes = []
            for i in range(NUM_OF_GENES):
                self.genes.append(random.randint(-10, 10))
        else:
            self.genes = genes
    
    def update_fitness_score(self, game_score):
        self.fitness_score = game_score
    
    def best_play(self,board,piece,next_piece):
        best_rotation = 0
        best_column = -1
        play_score = -10000000

        for column in range(-2, tb.BOARDWIDTH-2):
            for rot in range(len(tb.PIECES[piece['shape']])):
                # use calc_move_data 
                move_data = tb.calc_move_data(board, piece, column, rot)

                #if the move is valid
                if move_data['is_valid']:
                    # calculate the score for each rotation and return the best rotation and its score
                    temp_score = np.array(self.genes)
                    # dot multiplication baby
                    temp_score = np.dot(temp_score, np.array(list(move_data['cal_data'].values())))
                    # TODO: TEST IT LATER
                    # for the next_piece you could get the new_board from the first piece and recalculate the
                    # calc_move_data based on the next_piece
                    '''
                    if(next_piece != None):
                        for possible_col in range(-2,len(board[0])-2):
                            best_next_r , next_score = self.best_play(move_data['new_board'],next_piece,None,possible_col)
                            temp_score += next_score
                    '''
                    if temp_score > play_score:
                        play_score = temp_score
                        best_rotation = rot
                        best_column = column
                

        return {'best_column':best_column,'best_rotation': best_rotation, 'score': play_score}

'''
Objective function == Heuristic function
Initializes the chromosomes -> use chromosomes in obj function
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
        self.NUM_OF_GENERATIONS = num_of_generations
        self.optimal_chromosome = None

    
    
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
        
        # Return the best chromosome
        #TODO: make sure to return the best chromosome
        optimal_chromosome = sorted(self.chromosomes, key=lambda x: x.fitness_score, reverse=True)[0]
        return optimal_chromosome

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
            chrom_score = tb.run_game(GAME_MODE,chrom)
            chrom.update_fitness_score(game_score=chrom_score)

    def selection(self):
        # Update the chromosome list (delete the rest) ceil(Top 30%)
        # Normalize the fitness (1/(1+F_Obj(i)))
        # Total = Sum(the normalized fitness)
        # P[i] = F[i] / Total
        # max(P[i]) => The fittest
        # ==== Selection ====
        # use roulette wheel
        # calculate the cumulative probability
        # Generate random numbers [0,1]
        # If random number R[1] is greater than C[1] and smaller than C[2]  then select
        #   Chromosome[2] as a chromosome in the new population for next generation

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
