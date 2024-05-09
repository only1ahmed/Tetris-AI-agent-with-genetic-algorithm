import tetris_base as tb
import numpy as np
import model

GA = model.GeneticAlgorithm(num_of_generations=2,
                            max_score= 1000,
                            calculate_next_move=False,
                            heuristic_names=['aggregate_height','complete_lines', 'holes', 'bumpiness','four_rows'])
GA.load_chromosomes("saved_chromosome.csv")
GA.train()
GA.save_history("training_history.csv")