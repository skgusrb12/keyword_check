# keyword check

## 1. Introduction

**This project is simple code to extract the violence sentences in movie script with violence situation.**

We utilized this project on 2020 Artificial Intelligence (AI) Grand Challenge Speech Recognition(Track2) (http://www.ai-challenge.kr/sub0101) to construct a lot of dataset.


## 2. Run this project

Run script (Command Line)

```python
python ./main.py --script_list $SCRIPT_PATH --save_path $KEYWORD_SCRIPT_PATH \
--destination_path $COPY_PATH --max_count $MAX_COUNT
cmd /k
```

Here, 
- script_list : scripts of korean movies and drama
- save_path : script with violence keyword 
- destination_path : scripts without violence keyword
- max_count : the number of keyword count
