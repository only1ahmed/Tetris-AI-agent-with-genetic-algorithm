import tetris_base as tb
import numpy as np
import model

#
genes = [5.387269303109375,3.8794766494803907,-3.6804923867413235,-6.709630184000435,8.339967392082738]
chrom = model.Chromosome(heuristic_names=['aggregate_height', 'complete_lines', 'holes', 'bumpiness', 'four_rows'],
                         genes=genes, calculate_next_move=True)
game_score = tb.run_game_ai(is_training=False,
                            chromosome=chrom,
                            max_score=700_000,
                            is_score_limited=True,
                            is_piece_limited=False,
                            speed=100000)

chrom.save_history("Models/optimal_6_hist.csv")
