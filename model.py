import tetris_base as tb
import heuristic_functions
import random
import numpy as np
import pandas as pd

NUM_OF_GENES = 4
NUM_OF_CHROMOSOMES = 15
NUM_OF_EVOLUTIONS = 10

PERECENTAGE_OF_MUTATED = 0.2
PERECENTAGE_OF_SELECTION = 0.3

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
        #Normalize the game score
        print(self.genes)
        print("Game Score: ",game_score)
        self.fitness_score = 1 / (1 + game_score)
    
    def best_play(self,board,piece,next_piece):
        best_rotation = 0
        best_column = -2 #
        play_score = 0

        for column in range(-2, tb.BOARDWIDTH - 3):
            for rot in range(len(tb.PIECES[piece['shape']])):
                # use calc_move_data 
                move_data = tb.calc_move_data(board, piece, column, rot)
                # fitness = w1 * h1(x) + w2* h2(x) ....
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
                
        piece['rotation'] = best_rotation
        piece['x'] = best_column
        piece['y'] = 0

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
            print("Training Generation: ", i,)
            self.cal_fitness()
            self.selection()
            print("--Best Score: ",self.chromosomes[0].fitness_score)
            offspring_chrom = self.crossover()
            offspring_chrom = self.mutate(offspring_chrom)
            self.replace(offspring_chrom)
        
        # Return the best chromosome
        #TODO: make sure to return the best chromosome
        optimal_chromosome = sorted(self.chromosomes, key=lambda x: x.fitness_score)[0]
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
            chrom_score = tb.run_game_ai(is_training=True,chromosome=chrom,speed=100)
            print("Chromosome Score: ",chrom_score)
            chrom.update_fitness_score(game_score=chrom_score)

    def selection(self):
        # Update the chromosome list (delete the rest) ceil(Top 30%)
        self.chromosomes = sorted(self.chromosomes, key=lambda x: x.fitness_score)
        self.chromosomes = self.chromosomes[int(len(self.chromosomes) * PERECENTAGE_OF_SELECTION):]

    def crossover(self): 
        # Return new chromosomes
        off_chroms = []
        num_of_offspring = NUM_OF_CHROMOSOMES - len(self.chromosomes)
        for i in range(len(self.chromosomes)):
            if(len(off_chroms) >= num_of_offspring):
                    break
            for j in range(i+1,len(self.chromosomes)):
                if(len(off_chroms) >= num_of_offspring):
                    break
                off_chroms.append(self.mating(self.chromosomes[i],self.chromosomes[j]))
        return off_chroms
    
    def mating(self,chrom1,chrom2):
        temp_gene_p1 = chrom1.genes 
        temp_gene_p2 = chrom2.genes
        gene_len = len(temp_gene_p1)
        off_gene = []
        #Multi Point Crossover
        #TODO: Try another one later
        for i in range(gene_len):
            if i % 2 == 0:
                off_gene.append(temp_gene_p1[i])
            else:
                off_gene.append(temp_gene_p2[i])
        return Chromosome(off_gene)

    def mutate(self,off_chroms):
        # mutated chromosomes
        # Set of off chromosomes
            # eliminate randomly
        num_of_mutated = int(len(off_chroms) * PERECENTAGE_OF_MUTATED)
        for i in range(num_of_mutated):
            rand_chrom = random.choice(off_chroms)
            rand_gene = random.randint(0,len(rand_chrom.genes)-1)
            rand_chrom.genes[rand_gene] += random.uniform(-0.1,0.1)         
        return off_chroms
    
    def replace(self,off_chroms):
        # Replace the 
        print(off_chroms)
        self.chromosomes = self.chromosomes + off_chroms

    def save_chromosomes(self):
        # Save the chromosomes to a file
        pass
