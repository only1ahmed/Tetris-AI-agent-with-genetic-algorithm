import tetris_base as tb
import numpy as np
import model

# IF YOU WANT TO TRAIN 
# GA = model.GeneticAlgorithm(num_of_generations=2,
#                             max_score=10000,
#                             calculate_next_move=True,
#                             speed=30,

#                             heuristic_names=['aggregate_height','complete_lines', 'holes', 'bumpiness','four_rows'])
# GA.load_chromosomes("saved_chromosome.csv")
# GA.train()
# GA.save_history("training_history.csv")

# IF YOU WANT TO PLAY WITH A SINGLE CHROMOSOME
optimal_genes = [-6.03021361728919,1.842716403806107,-4.994838657280255,-2.581971055440853,-4.740969302492218]

chrom = model.Chromosome(heuristic_names=['aggregate_height','complete_lines', 'holes', 'bumpiness','four_rows'],
                         genes=optimal_genes,
                         calculate_next_move=False)

game_score = tb.run_game_ai(is_training=False,
                            chromosome=chrom,
                            max_score=10000,
                            is_score_limited=True,
                            is_piece_limited=False,
                            speed= 10)

chrom.save_history("chromosome_history.csv")