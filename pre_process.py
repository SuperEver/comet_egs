from pathlib import Path
from loguru import logger
import json


def process_corpus(input_json_file, out_dir):
    print("input_json_file:", input_json_file)
    with open(input_json_file) as f:
        data = f.read()
    json_data = json.loads(data)
    logger.info(f"Datasize: {len(json_data)}")
    folder_path = Path(out_dir)
    folder_path.mkdir(parents=True, exist_ok=True)
    path_src = Path(out_dir) / "src.txt"
    path_ref = Path(out_dir) / "ref.txt"
    path_mt = Path(out_dir) / "mt.txt"
    file_src = path_src.open("w")
    file_ref = path_ref.open("w")
    file_mt = path_mt.open("w")
    for ele in json_data:
        line_src = ele["ori_text"]
        line_ref = ele["label"]
        line_mt = ele["predict"]
        assert "\n" not in line_src and "\n" not in line_ref and "\n" not in line_mt
        file_src.write(line_src + "\n")
        file_ref.write(line_ref + "\n")
        file_mt.write(line_mt + "\n")
    file_src.close()
    file_ref.close()
    file_mt.close()


def process_all(dir_path):
    path = Path(dir_path)
    ori_json_files = [file for file in path.rglob("*.json")]
    logger.info(f"ori_json_files: {ori_json_files}")
    for ori_json_file in ori_json_files:
        logger.warning(f"ori_json_file: {ori_json_file}")
        language = ori_json_file.stem
        dst_dir = f"ori_comet/{language}" 
        process_corpus(ori_json_file.resolve(), dst_dir)


process_all("ori_json")
