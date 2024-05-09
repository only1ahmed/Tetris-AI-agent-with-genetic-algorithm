import tetris_base as tb
import heuristic_functions as hf
import random
import numpy as np
import pandas as pd
import math

class Chromosome:
    def __init__(self,
                 genes = [],
                 calculate_next_move = False,
                 heuristic_names = hf.HEURISTIC_NAMES):
        self.NUM_OF_GENES = len(heuristic_names)
        self.NEXT_MOVE = calculate_next_move

        self.genes = genes
        self.fitness_score = 0
        self.game_score_history = []
        self.heuristic_names = heuristic_names

        if genes == []:
            self.genes = []
            for i in range(self.NUM_OF_GENES):
                self.genes.append(random.uniform(-10.0,10.0))
    
    def update_fitness_score(self, game_score):
        self.fitness_score = game_score

    def save_history(self,file_name="chromosome_game_score_history.csv"):
        history_df = pd.DataFrame(columns=['Move Number','Best Score'])
        for i, data in enumerate(self.game_score_history):
            history_df.loc[i] = [i,data]
        history_df.to_csv(file_name, index=False)


    def best_play(self,board,piece,next_piece):
        '''
        Returns the best play for the current piece and the score of the play
        '''
        best_rotation = 0
        best_column = -2 #
        play_score = -100000

        for column in range(-2, tb.BOARDWIDTH - 2):
            for rot in range(len(tb.PIECES[piece['shape']])):
                # use calc_move_data 
                move_data = tb.calc_move_data(board, piece, column, rot, heuristics_names=self.heuristic_names)
                
                #if the move is valid
                if move_data['is_valid']:
                    # calculate the score for each rotation and return the best rotation and its score
                    temp_score = np.array(self.genes)
                    temp_score = np.dot(temp_score, np.array(list(move_data['cal_data'].values())))

                    if(next_piece != None and self.NEXT_MOVE):
                        next_move_data = self.best_play(move_data['new_board'],next_piece,None)
                        temp_score += next_move_data['score']
                    
                    if temp_score > play_score:
                        play_score = temp_score
                        best_rotation = rot
                        best_column = column
                
        piece['rotation'] = best_rotation
        piece['x'] = best_column
        piece['y'] = 0

        return {'best_column':best_column,'best_rotation': best_rotation, 'score': play_score}


class GeneticAlgorithm:
    '''
    what kind of data do i need to collect:
    1. Optimal Chromosome that got me the highest score
    2. Progress of the chromosome while playing 
        - So in other words Generation Chromosome Genes  
    
    '''

    def __init__(self, 
                 num_of_generations=10, 
                 num_of_chromosomes=15,  
                 perecentage_of_mutated=0.2, 
                 perecentage_of_selection=0.35, 
                 max_score = 100_000, max_piece = 500, 
                 limit_score = True, limit_piece = False,
                 calculate_next_move = False, 
                 heuristic_names=hf.HEURISTIC_NAMES):
        
        self.NUM_OF_GENERATIONS       = num_of_generations
        self.NUM_OF_CHROMOSOMES       = num_of_chromosomes
        self.NUM_OF_GENES             = len(heuristic_names)
        self.PERECENTAGE_OF_MUTATED   = perecentage_of_mutated
        self.PERECENTAGE_OF_SELECTION = perecentage_of_selection
        self.MAX_SCORE                = max_score
        self.MAX_PIECE                = max_piece
        self.LIMIT_SCORE              = limit_score
        self.LIMIT_PIECE              = limit_piece
        self.NEXT_MOVE                = calculate_next_move
        self.HEURISTIC_NAMES          = heuristic_names


        self.chromosomes = []   # List of Chromosomes
        self.optimal_chromosome = None
        self.training_history = []


    
    def load_chromosomes(self,file_name):
        # Load the chromosomes from a file
        '''
        The format of the file should be a csv file with the following columns:
        '''
        chromo_df = pd.read_csv(file_name)
        for _, row in chromo_df.iterrows():
            row = row.to_list()
            self.chromosomes.append(Chromosome(heuristic_names=self.HEURISTIC_NAMES,genes=row,calculate_next_move=self.NEXT_MOVE))
        
        return self.chromosomes
                
    def save_chromosomes(self,file_name = "chromosomes.csv"):
        # Save the chromosomes to a file
        chromo_df = pd.DataFrame(columns=self.HEURISTIC_NAMES)
        for i, chrom in enumerate(self.chromosomes):
            chromo_df.loc[i] = chrom.genes
        chromo_df.to_csv(file_name, index=False)

    def save_history(self,file_name = "training_history.csv"):
        # Save the training history to a file
        history_df = pd.DataFrame(columns=['Generation','Best Score']+self.HEURISTIC_NAMES)
        for i, data in enumerate(self.training_history):
            history_df.loc[i] = data
        history_df.to_csv(file_name, index=False)

    

    def init_chromosomes(self):
        for i in range(self.NUM_OF_CHROMOSOMES):
            self.chromosomes.append(Chromosome(heuristic_names=self.HEURISTIC_NAMES,calculate_next_move=self.NEXT_MOVE))

    def train(self):

        self.optimal_chromosome = None
        best_score = -10000
        for i in range(self.NUM_OF_GENERATIONS):
            print("Training Generation: [", i,"/ ",self.NUM_OF_GENERATIONS,"]")
            self.cal_fitness()
            self.selection()
            temp_row = [i , self.chromosomes[0].fitness_score]
            temp_row = temp_row + self.chromosomes[0].genes
            self.training_history.append(temp_row)
            if self.chromosomes[0].fitness_score > best_score:
                self.optimal_chromosome = self.chromosomes[0]
                best_score = self.chromosomes[0].fitness_score
            offspring_chrom = self.crossover()
            offspring_chrom = self.mutate(offspring_chrom)
            self.replace(offspring_chrom)




        #self.optimal_chromosome = sorted(self.chromosomes, key=lambda x: x.fitness_score, reverse = True)[0]
        print("Training Completed")
        print("Optimal Chromosome: ",self.optimal_chromosome.genes)
        tb.check_quit()
        return self.optimal_chromosome

    '''
    You will be given the
    current state of the board, the current piece to be played and the next piece, and what column I am
    thinking of playing it on. You will be asked to return what is the best rotation and its score. You can
    score each rotation and check who has highest and return it and its associated score.
    '''
    def cal_fitness(self):
        # Run the game for each chromosome and calculate the fitness score
        for chrom in self.chromosomes:
            chrom_score = tb.run_game_ai(is_training=True,chromosome=chrom,max_score=self.MAX_SCORE)
            chrom.update_fitness_score(game_score=chrom_score)

    def selection(self):
        # Update the chromosome list (delete the rest) ceil(Top 30%)
        self.chromosomes = sorted(self.chromosomes, key=lambda x: x.fitness_score, reverse = True)
        self.chromosomes = self.chromosomes[0:max(2, int(math.ceil(len(self.chromosomes) * self.PERECENTAGE_OF_SELECTION)))]

    def crossover(self): 
        # Return new chromosomes
        off_chroms = []
        num_of_offspring = self.NUM_OF_CHROMOSOMES - len(self.chromosomes)
        while (len(off_chroms) < num_of_offspring):
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
        total_fitness = chrom1.fitness_score + chrom2.fitness_score
        off_gene = np.array(temp_gene_p1)*(chrom1.fitness_score/total_fitness) \
                  + np.array(temp_gene_p2)*(chrom2.fitness_score/total_fitness)
        off_gene = off_gene.tolist()
        return Chromosome(heuristic_names=self.HEURISTIC_NAMES,genes=off_gene,calculate_next_move=self.NEXT_MOVE)

    def mutate(self,off_chroms):
        # mutated chromosomes
        # Set of off chromosomes
            # eliminate randomly
        num_of_mutated = int(len(off_chroms) * self.PERECENTAGE_OF_MUTATED)
        for i in range(num_of_mutated):
            randi = random.randint(0,(self.NUM_OF_GENES * len(off_chroms))-1)
            off_chroms[randi//self.NUM_OF_GENES].genes[randi % self.NUM_OF_GENES] += random.uniform(-0.1,0.1)         
        return off_chroms
    
    def replace(self,off_chroms):
        # Replace the 
        self.chromosomes = self.chromosomes + off_chroms
