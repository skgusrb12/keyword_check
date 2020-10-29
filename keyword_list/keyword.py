import os
import pandas as pd

def class_check(sentence, dict):
    result = sentence
    found = False
    for class_num in dict.keys():
        for keyword in dict[class_num]:
            if keyword in sentence:
                found = True
                result = '--<<'+str(class_num)+'>>--'+result

    return result, found


def load_dict(max_val):

    # load keyword
    violence_list = pd.read_excel('./keyword_list/load_keyword.xlsx', sheet_name=None)

    sheet_list = ['class_1(협박)', 'class_2(갈취)', 'class_3(직장)', 'class_4(기타)']
    keyword_cue = [idx for idx in range(len(violence_list))]

    for idx in range(len(violence_list)):
        violence_type = violence_list[sheet_list[idx]]
        keyword_list = violence_type[violence_type['count'] < max_val]

        keyword_cue[idx] = keyword_list['keyword']

    keyword_dict = {1: keyword_cue[0].tolist(), 2: keyword_cue[1].tolist(), 3: keyword_cue[2].tolist(),
            4: keyword_cue[3].tolist()}

    return keyword_dict


def data_candidate_search(download_path):
    class_format = '--<<'

    total = os.listdir(download_path)
    text_list = list()
    for file in total:
        if file.endswith('.txt'):
            text_list.append(file)

    for each in text_list:
        found = False

        refined_file_path = download_path + '(refined)' + each
        refined = open(refined_file_path, 'wt', encoding='utf-8')

        with open(download_path + each, 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                if class_format in line:
                    if not found:
                        found = True
                    refined.write(line)

                line = f.readline()
        if not found:
            os.remove(download_path + '(refined)' + each)

        refined.close()