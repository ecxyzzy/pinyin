from json import dump
from types import NoneType
from typing import Dict, List, Tuple, Union
from unihan_etl.process import Packager

# Mandarin finals, sorted in descending order of length and ascending alphabetical order within the same length
FINALS = [
    'iang', 'iong',
    'ang', 'eng', 'ian', 'iao', 'ing', 'ong', 'uai', 'uan',
    'ai', 'an', 'ao', 'ei', 'en', 'er', 'ia', 'ie', 'in', 'iu', 'ou', 'ua', 'ui', 'un', 'uo', 'üe',
    'a', 'e', 'i', 'o', 'u', 'ü'
]

# Mandarin vowel data, mapped to the raw vowel and the tone number
TONED_VOWELS = {
    'ā': ('a', 1), 'á': ('a', 2), 'ǎ': ('a', 3), 'à': ('a', 4),
    'ē': ('e', 1), 'é': ('e', 2), 'ě': ('e', 3), 'è': ('e', 4),
    'ī': ('i', 1), 'í': ('i', 2), 'ǐ': ('i', 3), 'ì': ('i', 4),
    'ō': ('o', 1), 'ó': ('o', 2), 'ǒ': ('o', 3), 'ò': ('o', 4),
    'ū': ('u', 1), 'ú': ('u', 2), 'ǔ': ('u', 3), 'ù': ('u', 4),
    'ǖ': ('ü', 1), 'ǘ': ('ü', 2), 'ǚ': ('ü', 3), 'ǜ': ('ü', 4)
}

# import/export options
FILENAME = './pytok.json'
OPTIONS = {
    'zip_path': './unihan.zip',
    'work_dir': './unihan/',
    'fields': ['kHanyuPinyin', 'kMandarin'],
    'format': 'python',
    'log_level': 'WARNING'
}


def tokenize(pinyin: str) -> Union[Tuple[str, str, int] | NoneType]:
    initial = final = ''
    tone = 0
    for i in pinyin:
        if i in TONED_VOWELS:
            tone = TONED_VOWELS[i][1]
            pinyin = pinyin.replace(i, TONED_VOWELS[i][0])
            break
    for f in FINALS:
        if f in pinyin:
            final = f
            initial = pinyin.rstrip(f)
            break
    return (initial, final, tone) if final else None


def process(char: dict) -> List[Dict[str, Union[str | Union[Tuple[str, str, int] | NoneType]]]]:
    readings = []
    if 'kHanyuPinyin' in char:
        readings += [r for r in char['kHanyuPinyin'][0]['readings']]
        if ('kMandarin' in char) and (char['kMandarin']['zh-Hans'] not in char['kHanyuPinyin'][0]['readings']):
            readings.append(char['kMandarin']['zh-Hans'])
    else:
        readings.append(char['kMandarin']['zh-Hans'])
    return [{'char': char['char'], 'pinyin': tokenize(r)} for r in readings]


def main() -> None:
    tokenized = []
    p = Packager(OPTIONS)
    p.download()
    for c in p.export():
        tokenized += process(c)
    with open(FILENAME, 'w', encoding='utf-8') as fp:
        dump(tokenized, fp, ensure_ascii=False)


if __name__ == '__main__':
    main()
