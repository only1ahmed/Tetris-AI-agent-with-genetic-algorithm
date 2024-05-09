import tetris_base as tb
import numpy as np
import model

# IF YOU WANT TO TRAIN 
GA = model.GeneticAlgorithm(num_of_generations=2,
                            max_score= 1000,
                            calculate_next_move=False,
                            heuristic_names=['aggregate_height','complete_lines', 'holes', 'bumpiness'])
GA.init_chromosomes()
#GA.load_chromosomes("saved_chromosome.csv")
GA.train()
GA.save_chromosomes("chromosomes_test.csv")
GA.save_history("history_test.csv")
print(GA.optimal_chromosome.fitness_score)


# IF YOU WANT TO PLAY WITH A SINGLE CHROMOSOME
#optimal_genes = [-6.03021361728919,1.842716403806107,-4.994838657280255,-2.581971055440853,-4.740969302492218]

#chrom = model.Chromosome(heuristic_names=['aggregate_height','complete_lines', 'holes', 'bumpiness','four_rows'],genes=optimal_genes,calculate_next_move=False)
#game_score = tb.run_game_ai(is_training=False,
#                            chromosome=chrom,
#                            max_score=1000,
#                            is_score_limited=True,
#                            is_piece_limited=False,
#                            speed= 1000)
#
#chrom.save_history("chromosome_history.csv")