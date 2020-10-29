SCRIPT_PATH='./script_list'  #path should be end with '/'
KEYWORD_SCRIPT_PATH='./save_list/keyword'  #path should be end with '/'
COPY_PATH='./save_list/original'  #txt file of urls you prepared

MAX_COUNT=30

python ./main.py --script_list $SCRIPT_PATH --save_path $KEYWORD_SCRIPT_PATH \
--destination_path $COPY_PATH --max_count $MAX_COUNT
cmd /k
