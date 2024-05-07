import tetris_base as tb
import numpy as np
import model
NUM_OF_GENERATIONS = 20
GA = model.GeneticAlgorithm(NUM_OF_GENERATIONS)
GA.init_chromosomes()
GA.train()
