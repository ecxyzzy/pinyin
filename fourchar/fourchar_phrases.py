from json import dump, load
from urllib.request import urlopen

# URL for the phrase dataset
URL = 'https://raw.githubusercontent.com/pwxcoo/chinese-xinhua/master/data/ci.json'

# configuration
# local hanzi dataset path
HANZI = './hanzi.json'
# export path
PHRASE = './phrases.json'
# whether to prompt for entries with multiple readings
INTERACTIVE = False


def prompt_reading(phrase: str, char: str, readings: list[tuple[str, str, int]]) -> tuple[str, str, int]:
    print(f'Character "{char}" in phrase "{phrase}" has multiple recording readings:')
    [print(f'[{i}]: {readings[i]})') for i in range(len(readings))]
    while True:
        try:
            index = int(input(f'Please select the appropriate reading [0-{len(readings) - 1}]: '))
            return readings[index]
        except ValueError:
            print('Invalid input.')


def process(db: dict[str, list[tuple[str, str, int]]], phrase: str) -> list[tuple[str, str, int]]:
    ret = []
    for i in phrase:
        if i in db:
            if len(db[i]) == 1:
                ret.append(db[i][0])
            else:
                ret.append(prompt_reading(phrase, i, db[i]) if INTERACTIVE else None)
        else:
            ret.append(None)
    return ret


def main() -> None:
    with open(HANZI, 'r', encoding='utf-8') as fp:
        hanzi = load(fp)
    with urlopen(URL) as fp:
        phrases = {}
        for i in load(fp):
            if '，' in i['ci']:
                for j in i['ci'].split('，'):
                    if len(j) == 4:
                        p = process(hanzi, j)
                        if any(i is None for i in p):
                            continue
                        phrases[j] = p
            else:
                if len(i['ci']) == 4:
                    p = process(hanzi, i['ci'])
                    if any(i is None for i in p):
                        continue
                    phrases[i['ci']] = p
    with open(PHRASE, 'w', encoding='utf-8') as fp:
        dump(phrases, fp, ensure_ascii=False)


if __name__ == '__main__':
    main()
