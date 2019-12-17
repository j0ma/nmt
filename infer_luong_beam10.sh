MODEL_FOLDER="nmt_model_luong_beam10"
INPUT_FILE="../ptb_processed_data/test.eng"
OUTPUT_FILE="./inference_outputs/luong_beam10_test_output"

python -m nmt.nmt \
    --out_dir=$MODEL_FOLDER \
    --inference_input_file=$INPUT_FILE \
    --inference_output_file=$OUTPUT_FILE

