import tetris_base as tb
import numpy as np
import model
import pandas as pd


### (Model 4) ###

print("MODEL 4")

model_4 = model.GeneticAlgorithm(num_of_generations=10,
                                 max_score=100000,
                                 heuristic_names=['aggregate_height',
                                                  'complete_lines',
                                                  'holes',
                                                  'bumpiness',
                                                  'four_rows'])

model_4.init_chromosomes()
model_4.train()
model_4.save_chromosomes("model4_chromosomes.csv")
model_4.save_history("model4_history.csv")

optimal_score = pd.read_csv("model4_history.csv")["Best Score"].max()

print(f"Optimal Score model 4: {optimal_score}")
