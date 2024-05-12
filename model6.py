import tetris_base as tb
import numpy as np
import model
import pandas as pd



### (Model 5) ###

model_6 = model.GeneticAlgorithm(num_of_generations=10,
                                 max_score=500000,
                                 calculate_next_move=True,
                                 heuristic_names=['aggregate_height',
                                                  'complete_lines',
                                                  'holes',
                                                  'bumpiness',
                                                  'four_rows'])

model_6.load_chromosomes("model4_chromosomes.csv")
model_6.train()
model_6.save_chromosomes("model6_chromosomes.csv")
model_6.save_history("model6_history.csv")

optimal_score = pd.read_csv("model6_history.csv")["Best Score"].max()


print(f"Optimal Score model 6: {optimal_score}")