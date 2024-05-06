import tetris_base as tb
import model
NUM_OF_GENERATIONS = 10
genetic_algorithm = model.GeneticAlgorithm(NUM_OF_GENERATIONS)
genetic_algorithm.init_chromosomes()
genetic_algorithm.train()