mkdir ./nmt_model_normed_bahdanau

python -m nmt.nmt \
    --attention=normed_bahdanau \
    --src=eng --tgt=lintree \
    --vocab_prefix=../ptb_processed_data/vocab  \
    --train_prefix=../ptb_processed_data/train \
    --dev_prefix=../ptb_processed_data/dev  \
    --test_prefix=../ptb_processed_data/test \
    --out_dir=./nmt_model_normed_bahdanau \
    --num_train_steps=8000 \
    --steps_per_stats=100 \
    --num_layers=2 \
    --num_units=128 \
    --dropout=0.2 \
    --metrics=bleu \
    --log_device_placement
