import tetris_base as tb
import numpy as np
import model

GA = model.GeneticAlgorithm(num_of_generations=2,
                            max_score= 1000,
                            heuristic_names=['aggregate_height','complete_lines', 'holes', 'bumpiness',])
GA.load_chromosomes("new_chromosomes.csv")
GA.train()
GA.save_history()