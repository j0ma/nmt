# note: this script must be run in the EVALB folder of the starter code

for file in $(ls ~/nmt/inference_outputs/);
do
    echo "NEW: "$file
    ./evalb -e 50000 ~/ptb_processed_data/test.lintree ~/nmt/inference_outputs/$file
done
