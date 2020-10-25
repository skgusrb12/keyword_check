
import os
from args import parser
import shutil
from tools import load_txt


if __name__ == '__main__':

    args = parser.parse_args()

    path = args.script_list
    save_path = args.save_path
    copy_path = args.destination_path
    max_val = args.max_count


    script = list()

    for idx, script_list in enumerate(os.listdir(path)):

        print("step : %d / %d of total script list " %(idx+1, len(os.listdir(path))))

        shutil.copyfile(os.path.join(path, script_list), os.path.join(copy_path, script_list))
        script, is_keyword = load_txt(os.path.join(path, script_list), max_val)

        if is_keyword:
            f = open(os.path.join(save_path, script_list), 'w')

            for idx_line in range(len(script)):
                line = script[idx_line] + "\n\n"
                f.write(line)

            f.close()

        else:
            pass

    print('\nthe keyword checking is completed')