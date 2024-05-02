# Tetris-AI-agent-with-genetic-algorithm

There are 3 main files in this project:

## Tetris_base
This is the main file that contains the run_game function with both manual and AI modes.

It uses the Computer_player file for the AI mode.

It is where the game is actually gonna run.

You won't have to deal with this file at all except for debugging when running the game.

## Model
This file contains all the genetic algorithm logic, it uses Computer_player to test the chromosomes and evolute.

## Computer_player
This file contains all the AI player logic for making moves, which consists of:

- Using the chromosome as multipliers for ranking the moves based on the 9 evaluations

- Applying the move to the tetris board

- Evaluating the 9 measures that measures the move


### What and Who and How?

Our aim in this project is to try to do the best outstanding program that plays tetris with the given constraints, so the roles is gonna be more odd than our usual work.

There will be 2 types of roles in this project:

- Implementers

- Optimizers

#### Implementers
They are gonna be responsible of implementing the functions and comunicate with the optimizers to update them on their work

#### Optimizers
They are gonna make sure of the effeciency (both memory and time, but mainly time) and validity of the implemented functions, give feedback on how to enhance and optimize codes.

### Roles
There are two suggested role divisions:
#### First
- Wesam -> Optimzier
- Mohsen -> Implementer
- Fawzy -> Implementer
- Khaled -> Implementer
- Omar -> Implementer

#### Second
- Wesam -> 0.5 * Optimzier + 0.5 * Implementer
- Khaled -> 0.5 * Optimzier + 0.5 * Implementer
- Mohsen -> Implementer
- Fawzy -> Implementer
- Omar -> Implementer

We may vote for which you think is best.

**Final thing, search your name on the code to know what you should implement.**