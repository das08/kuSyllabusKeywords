import sys
import collections

import termextract.core
import termextract.japanese_plaintext
import re


def output(data):
    """
    処理結果を"jpn_plain_extracted.txt"に出力
    """
    outfile = open("jpn_plain_extracted.txt", "w", encoding="utf-8")
    data_collection = collections.Counter(data)
    tmp = set()
    for cmp_noun, value in data_collection.most_common():
        cmp_noun = termextract.core.modify_agglutinative_lang(cmp_noun)
        cmp_noun = re.sub(r"[./\[\]、。・．，①②③④⑤⑥⑦⑧⑨⑩ⅠⅡⅢⅣⅤⅥ]", "", cmp_noun)
        cmp_noun = re.sub(r"\d", "", cmp_noun)
        cmp_noun = cmp_noun.strip()
        if cmp_noun == "":
            continue
        if value > 2:
            tmp.add(cmp_noun)
        outfile.write(cmp_noun)
        outfile.write("\t")
        outfile.write(str(value))
        outfile.write("\n")
    key_list = list(tmp)

    outfile.close()
    return key_list


def genKeys(file):
    text = ""
    with open(f"{file}", "r", encoding="utf-8") as line:
        lectureName = line.readline()
        teacherName = line.readline()
        semester = line.readline()

        info = [lectureName, teacherName, semester]

        for _line in line:
            text += _line

    frequency = termextract.japanese_plaintext.cmp_noun_dict(text)
    lr = termextract.core.score_lr(frequency, lr_mode=1, average_rate=1)
    term_imp = termextract.core.term_importance(frequency, lr)
    return info, output(term_imp)


# keyList = getKeys("H524001")

