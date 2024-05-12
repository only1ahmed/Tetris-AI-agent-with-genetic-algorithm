import tetris_base as tb
import numpy as np
import model
import pandas as pd



### (Model 5) ###

model_5 = model.GeneticAlgorithm(num_of_generations=10,
                                 max_score=500000,
                                 calculate_next_move=True,
                                 heuristic_names=['aggregate_height',
                                                  'complete_lines',
                                                  'holes',
                                                  'bumpiness',
                                                  'hole_segments',
                                                  'max_height',
                                                  'empty_columns',
                                                  'one_rows',
                                                  'two_rows',
                                                  'three_rows',
                                                  'four_rows'])

model_5.init_chromosomes()
model_5.train()
model_5.save_chromosomes("model5_chromosomes.csv")
model_5.save_history("model5_history.csv")

optimal_score = pd.read_csv("model5_history.csv")["Best Score"].max()


print(f"Optimal Score model 5: {optimal_score}")