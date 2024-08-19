# Readme

## 模型
1. `https://huggingface.co/Unbabel/XCOMET-XL`
2. `https://huggingface.co/facebook/xlm-roberta-xl`
下载完后XCOMET-XL的配置文件`hparams.yaml`中的key`pretrained_model`修改为xlm-roberta-xl的下载路径

## 补丁
env 路径下`comet/lib/python3.11/site-packages/comet/cli/score.py` 如下修改
```
# model = load_from_checkpoint(model_path)
model = load_from_checkpoint(model_path, reload_hparams=True)
```
## 运行 
```
# 使用comet 进行打分. src.txt,mt.txt,ref.txt 以行为单位,每行为一个case
comet-score -s src.txt -t mt.txt -r ref.txt --model  .../XCOMET-XL/checkpoints/model.ckpt --to_json comet.json --gpus 1
```

```
# 在LLM打分结果的基础上补充comet分数请参考`run.sh` , 注意,需要先把LLM对各语言的翻译结果打包到一个文件夹中并命名为 `ori_json`
sh run.sh
```
