import tetris_base as tb
import numpy as np
import model
import pandas as pd


### (Model 2) ###

print("MODEL 2")

model_2 = model.GeneticAlgorithm(num_of_generations=10,
                                 max_score=500000,
                                 heuristic_names=['one_rows', 'two_rows', 'three_rows', 'four_rows'])

model_2.init_chromosomes()
model_2.train()
model_2.save_chromosomes("model2_chromosomes.csv")
model_2.save_history("model2_history.csv")

optimal_score = pd.read_csv("model2_history.csv")["Best Score"].max()

print(f"Optimal Score model 2: {optimal_score}")
