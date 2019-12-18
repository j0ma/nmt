# note: this script must be run in the EVALB folder of the starter code

INFERENCE_OUTPUTS="../../post_processed_outputs"
TEST_LINEARIZED_TREES="../../../ptb_processed_data/test.lintree"

cd ../starter_code/EVALB

for file in $(ls $INFERENCE_OUTPUTS);
do
    echo "NEW: "$file
    ./evalb -e 50000 $TEST_LINEARIZED_TREES $INFERENCE_OUTPUTS/$file
done
