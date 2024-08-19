from pathlib import Path
from loguru import logger
import json


def process_corpus(comet_json_file, comet_file_key, llm_json_file, out_json_file):
    with open(comet_json_file) as f:
        data = f.read()
        comet_json = json.loads(data)
        comet_json = comet_json[comet_file_key]
    with open(llm_json_file) as f:
        data = f.read()
        llm_json = json.loads(data)

    assert len(comet_json) == len(llm_json)

    with Path(out_json_file).open("w") as f:
        fsum = .0
        for i in range(0, len(comet_json)):
            comet_ele = comet_json[i]
            assert llm_json[i]["ori_text"] == comet_ele["src"]
            llm_json[i]["COMET"] = comet_ele["COMET"]
            fsum += comet_ele["COMET"]
            if "errors" in comet_ele:
                llm_json[i]["comet_errors"] = comet_ele["errors"]
        json.dump(llm_json, f, ensure_ascii=False, indent=4)
    assert len(comet_json) > 0
    return fsum / len(comet_json)


def process_all(dir_path):
    path = Path(dir_path)
    ori_json_files = [file for file in path.rglob("*.json")]
    logger.info(f"ori_json_files: {ori_json_files}")
    for ori_json_file in ori_json_files:
        language = ori_json_file.stem
        score = process_corpus(f"ori_comet/{language}/comet.json", f"ori_comet/{language}/mt.txt", f"ori_json/{language}.json", f"merged_json/{language}.json")
        print(f"{language}, {score}")


process_all("ori_json")