import tetris_base as tb
import numpy as np
import model
import pandas as pd


### Basic Model (Model 1) ###

print("MODEL 1")

model_1 = model.GeneticAlgorithm(num_of_generations=10,
                                 max_score=500000,
                                 heuristic_names=['aggregate_height', 'complete_lines', 'holes', 'bumpiness'])

model_1.init_chromosomes()
model_1.train()
model_1.save_chromosomes("model1_chromosomes.csv")
model_1.save_history("model1_history.csv")

optimal_score = pd.read_csv("model1_history.csv")["Best Score"].max()

print(f"Optimal Score model 1: {optimal_score}")









