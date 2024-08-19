#1. copy all llm result json to ori_json folder
mkdir -p ori_comet
mkdir -p merged_json
python pre_process.py
find ori_comet/* -type d -exec comet-score -s {}/src.txt -t {}/mt.txt -r {}/ref.txt --model  ~/models/XCOMET-XL/checkpoints/model.ckpt --to_json {}/comet.json --gpus 1 \;
python merge.py

