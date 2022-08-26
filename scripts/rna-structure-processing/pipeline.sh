# Find multiple solutions
./find_more_lines.sh > multi_solutions.txt
# Split lines of multiple solutions
./split_multi_seq.sh
# Make bpseqs
./rnastructure_bpseq.sh
# Copy canonical targets
../validation/copy_canonical_targets.sh
# Filter canonical pairings
./filter_bpseq.sh


# Run validation
# Extract best inf using notebook
# ./copy_best_preds.sh
