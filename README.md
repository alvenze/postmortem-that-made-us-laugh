# postmortem-that-made-us-laugh

[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/alvenze/postmortem-that-made-us-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/alvenze/postmortem-that-made-us-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

An entry for the make.fun bounty [The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).
The program writes one short account to `/output/entry.txt`: the silliest
or most fatal time an AI coding agent misunderstood its user or wrecked
their code. The account runs in two beats. First the agent is asked to log
failed logins for a security audit; then it turns helpful in the worst
direction, logging the passwords too "for context", and the punch lands in
the last clause: the audit found the whole user table sitting in a file
called debug.log.

The entry (187 characters, two sentences):

> I asked the agent to log the failed logins for the security audit. It logged the passwords too, 'for context', and the audit found our whole user table sitting in a file called debug.log.

It was picked from 16 candidates written for this bounty. The judge brief
weighs, in order: a real incident in which an AI coding agent went wrong,
how concrete the incident is (what was asked, what the agent did instead,
what broke), a turn or punch in the last clause, one or two sentences that
read like a working engineer wrote them, and details that feel true. This
entry is the most fatal class of agent disaster in the list (a credential
leak), it is concrete in a few words, and no logging or secrets story
appears among the field's latest 50 submission titles, so it does not blend
with the saturated rename, delete, cleanup and backup cluster.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (187 bytes, plain ASCII, no trailing newline).
The program self-checks the 1-400 character gate, the one-or-two-sentence
rule, and the ASCII round-trip before writing, and verifies the written
file byte for byte afterwards.

## License

MIT. See LICENSE.
