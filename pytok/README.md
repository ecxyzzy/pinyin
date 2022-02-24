# pytok

`pytok` (**P**in**y**in **Tok**enizer) is a quick and dirty ETL script utilizing the [unihan-etl](https://github.com/cihai/unihan-etl) API. It takes in the `kMandarin` and `kHanyuPinyin` fields of the Unihan database, as per Unicode® Standard Annex #38, and tokenizes all listed readings of all characters into the initial (if applicable), the final, and the tone (if applicable), in accordance with the rules of Mandarin phonography.

The generated dataset in the repository, `pytok.json`, is further hand-curated to rectify any inconsistencies and duplicate entries in the automated ETL process.

## Setup and Execution

Set up a virtual environment (optional) and install dependencies from `requirements.txt`, then execute `pytok.py`.

## Assumptions and Limitations

`pytok` works based on a fixed list of finals and a fixed mapping of vowels. It assumes that each reading has zero or one initial(s), one final, and a tone. This covers the vast majority of valid readings, but outliers exist. If such a reading is encountered, the tokenization process will fail silently, and the character's pinyin will be recorded as `null`.

## Contributing

This script was kludged together in an afternoon. If you discover any issues or would like to contribute new features, please don't hesitate to open an issue/pull request!
