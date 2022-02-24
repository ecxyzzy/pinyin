from json import dump
from pinyintools import tokenize
from unihan_etl.process import Packager

# import/export options
FILENAME = 'hanzi.json'
OPTIONS = {
    'zip_path': './unihan.zip',
    'work_dir': './unihan/',
    'fields': ['kHanyuPinyin', 'kMandarin'],
    'format': 'python',
    'log_level': 'WARNING'
}


def process(char: dict) -> list[tuple[str, str, int] | None]:
    readings = []
    if 'kHanyuPinyin' in char:
        readings += [r for r in char['kHanyuPinyin'][0]['readings']]
        if ('kMandarin' in char) and (char['kMandarin']['zh-Hans'] not in char['kHanyuPinyin'][0]['readings']):
            readings.append(char['kMandarin']['zh-Hans'])
    else:
        readings.append(char['kMandarin']['zh-Hans'])
    return [tokenize(r) for r in readings]


def main() -> None:
    tokenized = {}
    p = Packager(OPTIONS)
    p.download()
    for c in p.export():
        tokenized[c['char']] = process(c)
    with open(FILENAME, 'w', encoding='utf-8') as fp:
        dump(tokenized, fp, ensure_ascii=False)


if __name__ == '__main__':
    main()
