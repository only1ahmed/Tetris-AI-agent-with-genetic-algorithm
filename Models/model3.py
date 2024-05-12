import tetris_base as tb
import numpy as np
import model
import pandas as pd


### (Model 3) ###

print("MODEL 3")

model_3 = model.GeneticAlgorithm(num_of_generations=10,
                                 max_score=500000,
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

model_3.init_chromosomes()
model_3.train()
model_3.save_chromosomes("model3_chromosomes.csv")
model_3.save_history("model3_history.csv")

optimal_score = pd.read_csv("model3_history.csv")["Best Score"].max()

print(f"Optimal Score model 3: {optimal_score}")