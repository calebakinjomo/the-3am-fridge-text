# The 3AM Fridge Text

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the [make.fun bounty "The 3AM Fridge Text"](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d) — one line a smart fridge would text its owner at 3am.

## The entry

> 3am. You're standing here in your underwear, door open, staring at a yoghurt like it's going to apologise. It won't. Take the cake.

131 characters, one line. The fridge has been awake all night, it has opinions, and it has no shame about sharing them at 3am.

## How it works

`main.py` writes the entry line to `/output/entry.txt`, with a length guard (1–140 chars, single line) enforced by assertion.

```bash
python3 main.py
cat /output/entry.txt
```

## Referral

Play on make.fun with referral code `hdavhdvz`.
