
from keyword_list.keyword import load_dict


def load_txt(filename, max_val):

    try:
        f = open(filename, 'rt', encoding='utf-8')
        script_cue = list()

        while True:
            line = f.readline()

            if not line:
                break

            line = line.strip()
            keyword_set = load_dict(max_val)
            re_line, is_keyword = check_keyword(line, keyword_set)
            script_cue.append(re_line)

        f.close()

    except:

        is_keyword = False
        print('error')

    return script_cue, is_keyword


def check_keyword(sentence, keyword_list):

    script = sentence
    is_keyword = False

    for class_type in keyword_list.keys():
        for keyword in keyword_list[class_type]:
            if keyword in sentence:

                pos_keyword = script.find(keyword)
                is_keyword = True

                script = script[:pos_keyword] + '<<< class : '+str(class_type) + ', keyword : ' + keyword + ' >>>' + script[pos_keyword:]

    return script, is_keyword

