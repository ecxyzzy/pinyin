# Mandarin finals, sorted in descending order of length and ascending alphabetical order within the same length
__FINALS = [
    r'iang$', r'iong$',
    r'ang$', r'eng$', r'ian$', r'iao$', r'ing$', r'ong$', r'uai$', r'uan$',
    r'ai$', r'an$', r'ao$', r'ei$', r'en$', r'er$', r'ia$', r'ie$',
    r'in$', r'iu$', r'ou$', r'ua$', r'ui$', r'un$', r'uo$', r'üe$',
    r'a$', r'e$', r'i$', r'o$', r'u$', r'ü$'
]

# Mandarin vowel data, mapped to the raw vowel and the tone number
__TONED_VOWELS = {
    'ā': ('a', 1), 'á': ('a', 2), 'ǎ': ('a', 3), 'à': ('a', 4),
    'ē': ('e', 1), 'é': ('e', 2), 'ě': ('e', 3), 'è': ('e', 4),
    'ī': ('i', 1), 'í': ('i', 2), 'ǐ': ('i', 3), 'ì': ('i', 4),
    'ō': ('o', 1), 'ó': ('o', 2), 'ǒ': ('o', 3), 'ò': ('o', 4),
    'ū': ('u', 1), 'ú': ('u', 2), 'ǔ': ('u', 3), 'ù': ('u', 4),
    'ǖ': ('ü', 1), 'ǘ': ('ü', 2), 'ǚ': ('ü', 3), 'ǜ': ('ü', 4)
}


def tokenize_char(pinyin: str) -> tuple[str, str, int] | None:
    """
    Given a string containing the pinyin representation of a Chinese character, return a 3-tuple containing its
    initial (``str``), final (``str``), and tone (``int; [0-4]``), or ``None`` if it cannot be properly tokenized.
    """
    import re
    initial = final = ''
    tone = 0
    for i in pinyin:
        if i in __TONED_VOWELS:
            tone = __TONED_VOWELS[i][1]
            pinyin = pinyin.replace(i, __TONED_VOWELS[i][0])
            break
    for f in __FINALS:
        if (s := re.search(f, pinyin)) is not None:
            final = s[0]
            initial = re.sub(f, '', pinyin)
            break
    return (initial, final, tone) if final else None


def tokenize_phrase(pinyin_lst: list[str]) -> list[tuple[str, str, int] | None]:
    """
    Given a list of strings of pinyin representations, return a list of 3-tuples or ``None``, same as ``tokenize_char``.
    """
    return [tokenize_char(i) for i in pinyin_lst]
