# Mandarin finals, sorted in descending order of length and ascending alphabetical order within the same length
__FINALS = [
    'iang', 'iong',
    'ang', 'eng', 'ian', 'iao', 'ing', 'ong', 'uai', 'uan',
    'ai', 'an', 'ao', 'ei', 'en', 'er', 'ia', 'ie', 'in', 'iu', 'ou', 'ua', 'ui', 'un', 'uo', 'üe',
    'a', 'e', 'i', 'o', 'u', 'ü'
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


def tokenize(pinyin: str) -> tuple[str, str, int] | None:
    """
    Given a string containing the pinyin representation of a Chinese character, return a 3-tuple containing its
    initial (``str``), final (``str``), and tone (``int; [0-4]``), or ``None`` if it cannot be properly tokenized.
    """
    initial = final = ''
    tone = 0
    for i in pinyin:
        if i in __TONED_VOWELS:
            tone = __TONED_VOWELS[i][1]
            pinyin = pinyin.replace(i, __TONED_VOWELS[i][0])
            break
    for f in __FINALS:
        if f in pinyin:
            final = f
            initial = pinyin.rstrip(f)
            break
    return (initial, final, tone) if final else None
