from json import dump, load
from pinyintools import tokenize_phrase
from urllib.request import urlopen

# URL for the idiom dataset
URL = 'https://raw.githubusercontent.com/pwxcoo/chinese-xinhua/master/data/idiom.json'

# export path
FILENAME = './idioms.json'


def main() -> None:
    with urlopen(URL) as fp:
        idioms = {}
        for i in load(fp):
            if '，' in i['word']:
                for j in zip(i['word'].split('，'), i['pinyin'].split('，')):
                    if len(j[0]) == 4:
                        idioms[j[0]] = tokenize_phrase(j[1].strip(' ').split(' '))
            else:
                if len(i['word']) == 4:
                    idioms[i['word']] = tokenize_phrase(i['pinyin'].split(' '))
    with open(FILENAME, 'w', encoding='utf-8') as fp:
        dump(idioms, fp, ensure_ascii=False)


if __name__ == '__main__':
    main()
