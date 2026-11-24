# The World in One Day — Tuesday, 24 November 2026

[![Rank](https://make.fun/badge/news-image-20261124/kimbaex07/makefun-news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/kimbaex07/makefun-news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)

A front-page image summing up the world's news of Tuesday 24 November 2026: three illustrated lead stories and a "THE DAY IN BRIEF" digest of seven more. Every story below was first reported on 24 November 2026 (as reported by the morning of 24 Nov UTC); neighbouring days' follow-ups — the Nvidia CEO reinstatement, the Kyiv-region strikes, the Manchester concert evacuation, the German school bomb threats and the Trump hush-money ruling, all of Monday 23 Nov — were deliberately left out.

## Lead stories

1. **Russian jets spark Korea alert** — Several Russian military aircraft entered South Korea's air-defence zone near Ulleung Island on Tuesday morning. Seoul scrambled fighter jets; an island shelter alert was lifted minutes later. The military said no airspace was violated. *(Reuters / AP / Yonhap, 24 Nov 2026)*
2. **An island emptied in a day** — All 40–50 residents of Kanton Island, Kiribati, were moved to Tarawa with 24 hours' notice. Officials cite strong El Niño weather, poor housing and the island's remoteness; some were told return may take four years. *(PINA — Pacific Islands News Association, 24 Nov 2026)*
3. **Alibaba denies chip diversion** — Alibaba said its Singapore unit Apex never diverted restricted chips and will defend its rights, a day after Washington blacklisted Apex and Megaspeed. Singapore's prime minister said probes continue and the city-state will not be used to evade US export controls. *(Reuters / market wires, 24 Nov 2026)*

## The day in brief

- **Brazil** — Lower house approves the main text of Lula's fiscal plan; the Senate backed it on 21 Nov.
- **Pacific** — After COP31 ended without a deal, Pacific island nations press on alone on climate.
- **Markets** — Chinese chip shares jump about 4% as Asian markets rally on the blacklist news.
- **India** — Supreme Court grants bail on medical grounds to a Godhra convict.
- **Pakistan** — A magnitude 4.0 quake strikes near the Afghan border; Lahore tops world pollution rankings.
- **Thailand** — Protesters march 16 km to a Bangkok refinery demanding lower refining margins.
- **USA** — Chicago's O'Hare briefly halts arrivals over a staffing shortage in the Thanksgiving rush.

## How it was built

The three lead illustrations were generated, then composed with the masthead, headlines and digest in Python (PIL) so all text is crisp and legible. `main.py` (pure Python standard library) simply copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, so the grader's two runs produce byte-identical output.

## Licence

MIT — see `LICENSE`.
