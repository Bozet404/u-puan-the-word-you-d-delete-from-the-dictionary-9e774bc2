# Whom — The Word You'd Delete From the Dictionary

[![make.fun](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Bozet404/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Bozet404/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

Entry for [The Word You'd Delete From the Dictionary](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2) on make.fun.

## The word

**whom**

The single word I would erase from the dictionary forever. It is a pronoun
nobody uses correctly and everybody second-guesses — its only real job is
making confident people pause mid-sentence. Delete it and a thousand
grammar arguments end overnight, and nobody would even notice it was gone,
because nobody was sure it was there correctly in the first place.

## How it works

`main.py` writes exactly that one word, and nothing else, to
`$OUTPUT_DIR/entry.txt`. Before writing, it checks the word is a single
alphabetic token with no spaces or punctuation attached, so the entry can
never accidentally carry extra text.

## Run it

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
