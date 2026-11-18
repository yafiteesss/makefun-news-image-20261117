# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/yafiteesss/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/yafiteesss/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Sum up 17 November's world news in one image. A program that writes a 1024x1024 newspaper-style front page — six verified stories from Tuesday 17 November 2026 — to `/output/entry.png`.

## Run it

```sh
python3 main.py
# writes /output/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tgs239he&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>

## Stories in the image (Tuesday 17 November 2026)

1. US and Iran trade fire — US jets strike an Iranian missile site on Qeshm Island after Iran fires drones at a US radar in Bahrain
2. Kerch Bridge hit again — Ukrainian drones strike the Crimea bridge a second day; a road section falls into the strait
3. Nvidia records, Huang not back — revenue tops $115 billion, about double a year earlier; the board will not reinstate ousted CEO Jensen Huang
4. Trump heads to Asia — APEC summit in Shenzhen for talks with Xi Jinping and Vladimir Putin, after a Quad summit in Manila
5. EU states plan Rwanda return hub — Germany, Denmark, Austria, Greece and the Netherlands will send rejected asylum seekers to Rwanda
6. US loses measles-free status — after 26 years, amid 5,400 cases and 10 deaths

## Details

- Bounty: https://make.fun/bounty/news-image-20261117
- Deadline: 19 Nov 2026, 00:00 UTC = 19 Nov 2026, 07:00 WIB
- Prize: $250 total, shared by the 50 highest-ranked entries
- Entry: public GitHub repo, MIT license, `main.py` at root
- Image: 1024x1024 PNG, ~101 KiB (limit 1 MiB), 6 stories

## Local verification

```bash
python3 main.py
sha256sum /output/entry.png
python3 main.py
sha256sum /output/entry.png
```

Both runs must produce identical bytes. No network calls. `main.py` uses stdlib only (shutil/pathlib) and copies `entry.png` held in this repo.

`build_image.py` is the local builder (PIL) used to create `entry.png`; it is not needed at run time.
