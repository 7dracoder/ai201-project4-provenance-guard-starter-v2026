# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 19:46
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column was filled after reading the captured output; the JSON details below retain the original capture. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `476b2794-722f-4c75-990a-b3e84afdf469` | unsure | 0.295 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `4ab0fc87-f8c2-4d5a-b135-b4d266f42357` | unsure | 0.529 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8394878d-72d7-47e0-8ffd-c617e642a64d` | unsure | 0.612 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b003e25a-4d00-4961-9041-2a0f425c7b18` | unsure | 0.605 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `91d9b599-8605-430d-8b0b-02f8f0e63bc0` | unsure | 0.352 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `1c893c37-855b-44b8-b2b8-513e6e780d7a` | unsure | 0.513 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `21adaf2d-641c-4617-8b2d-bb0c6d7566ce` | unsure | 0.560 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `e6727feb-d649-4825-afa4-6f55beda5b44` | unsure | 0.313 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `bceee180-187d-42d3-ac3c-c13f2617575e` | unsure | 0.638 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a1c51ca2-f4e4-4e97-841d-5b5cf9359b91` | ai | 0.908 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `e7e2143a-74b5-4202-b647-2e79ccfd14a6` | unsure | 0.597 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `b56dfb47-88cd-4854-9e24-0797d896413f` | unsure | 0.705 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `1b7aa50f-60fa-4e3a-9649-31d1713b1bbb` | unsure | 0.742 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `782fd863-6797-4739-a93b-89e5b8766247` | unsure | 0.745 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `dd9a0d99-bf9e-42a6-bb5f-54519f82c8fa` | unsure | 0.751 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `46b89fd6-b417-424e-9212-bebb5c2d6217` | unsure | 0.772 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a35cce42-1afc-4636-8c13-e3fb62a0758d` | unsure | 0.771 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `7fb7a31c-39a9-413c-b1d4-94704ab7055a` | unsure | 0.376 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ede5f5f3-9557-45e1-a88c-b6a101ceb136` | unsure | 0.449 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ca33b47b-97da-4b4f-84e6-fcfea1b8cdbc` | unsure | 0.251 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f7e04605-1f51-4646-a18a-bb98552d8b27` | unsure | 0.572 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `8ded965a-119e-4645-a4db-ec0cc75922e3` | unsure | 0.462 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `236214ec-9290-4c70-a1c8-cca0346dbaca` | unsure | 0.510 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d1769332-25d4-412e-b784-4d3e9e625cb0` | unsure | 0.557 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `-` | - | - | HELD |
| MF02 | malformed | text is a single character | 400 | `-` | - | - | HELD |
| MF03 | malformed | text is control characters | 400 | `-` | - | - | HELD |
| MF04 | malformed | text is only punctuation | 400 | `-` | - | - | HELD |
| MF05 | malformed | text is a very long single word | 400 | `-` | - | - | HELD |
| MF06 | malformed | text is emoji only | 400 | `-` | - | - | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `2286cc74-fbf1-453c-be0a-eed15378b1f4` | unsure | 0.784 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `-` | - | - | HELD |
| RQ01 | malformed | no text field at all | 400 | `-` | - | - | HELD |
| RQ02 | malformed | no creator_id | 400 | `-` | - | - | HELD |
| RQ03 | malformed | text is a number | 400 | `-` | - | - | HELD |
| RQ04 | malformed | text is a list | 400 | `-` | - | - | HELD |
| RQ05 | malformed | text is null | 400 | `-` | - | - | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `-` | - | - | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `-` | - | - | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `-` | - | - | HELD |
| RQ09 | malformed | body is empty | 400 | `-` | - | - | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `-` | - | - | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `-` | - | - | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `-` | - | - | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `970ac269-3f02-4db8-bc8b-ffa26cf6cb95` | human | 0.170 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `809e966e-1984-435f-bfb9-06a1d6aa0b08` | human | 0.170 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bddc6c46-a551-4c8d-9475-359c09963999` | human | 0.170 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7ff66909-9c96-4a27-9a52-2eff230a6170` | human | 0.170 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `35cd5ff1-4d7c-4609-a8d0-c8480b9c543a` | human | 0.170 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0adebb8b-58ab-4b2b-91ee-2a8f7eed867a` | human | 0.170 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7898d789-1f08-4d56-a221-ca22e646704d` | human | 0.170 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6e926df2-efee-49f6-985b-5feab1a14253` | human | 0.170 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2363e054-c994-4463-8935-03616202b780` | human | 0.170 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af79765b-8eb7-4eea-bd28-ba8cc98c1dfd` | human | 0.170 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `-` | - | - | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "476b2794-722f-4c75-990a-b3e84afdf469",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.2946,
  "model_score": 0.1635,
  "style_score": 0.6004,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "4ab0fc87-f8c2-4d5a-b135-b4d266f42357",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5289,
  "model_score": 0.5943,
  "style_score": 0.3763,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "8394878d-72d7-47e0-8ffd-c617e642a64d",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6122,
  "model_score": 0.6662,
  "style_score": 0.4863,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b003e25a-4d00-4961-9041-2a0f425c7b18",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6051,
  "model_score": 0.6114,
  "style_score": 0.5905,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "91d9b599-8605-430d-8b0b-02f8f0e63bc0",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.3522,
  "model_score": 0.3212,
  "style_score": 0.4246,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "1c893c37-855b-44b8-b2b8-513e6e780d7a",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5134,
  "model_score": 0.5727,
  "style_score": 0.375,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "21adaf2d-641c-4617-8b2d-bb0c6d7566ce",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5603,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "e6727feb-d649-4825-afa4-6f55beda5b44",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3126,
  "model_score": 0.2452,
  "style_score": 0.4698,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "bceee180-187d-42d3-ac3c-c13f2617575e",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6379,
  "model_score": 0.7042,
  "style_score": 0.4832,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "a1c51ca2-f4e4-4e97-841d-5b5cf9359b91",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9085,
  "model_score": 0.9792,
  "style_score": 0.7435,
  "label": "We think this may have been generated by AI, but we could be wrong. You can request a review if you wrote it yourself.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "e7e2143a-74b5-4202-b647-2e79ccfd14a6",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5965,
  "model_score": 0.6175,
  "style_score": 0.5475,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "b56dfb47-88cd-4854-9e24-0797d896413f",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7052,
  "model_score": 0.7387,
  "style_score": 0.6271,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "1b7aa50f-60fa-4e3a-9649-31d1713b1bbb",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7417,
  "model_score": 0.8051,
  "style_score": 0.5938,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "782fd863-6797-4739-a93b-89e5b8766247",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7451,
  "model_score": 0.8329,
  "style_score": 0.5404,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "dd9a0d99-bf9e-42a6-bb5f-54519f82c8fa",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7512,
  "model_score": 0.8005,
  "style_score": 0.6361,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "46b89fd6-b417-424e-9212-bebb5c2d6217",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.7718,
  "model_score": 0.8814,
  "style_score": 0.5161,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "a35cce42-1afc-4636-8c13-e3fb62a0758d",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7714,
  "model_score": 0.8816,
  "style_score": 0.5143,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "7fb7a31c-39a9-413c-b1d4-94704ab7055a",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.3756,
  "model_score": 0.3223,
  "style_score": 0.5,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ede5f5f3-9557-45e1-a88c-b6a101ceb136",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4485,
  "model_score": 0.4625,
  "style_score": 0.4159,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "ca33b47b-97da-4b4f-84e6-fcfea1b8cdbc",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.2513,
  "model_score": 0.2044,
  "style_score": 0.3607,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "f7e04605-1f51-4646-a18a-bb98552d8b27",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5722,
  "model_score": 0.5943,
  "style_score": 0.5207,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "8ded965a-119e-4645-a4db-ec0cc75922e3",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4621,
  "model_score": 0.4998,
  "style_score": 0.3741,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "236214ec-9290-4c70-a1c8-cca0346dbaca",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5104,
  "model_score": 0.6401,
  "style_score": 0.2077,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "d1769332-25d4-412e-b784-4d3e9e625cb0",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5569,
  "model_score": 0.5583,
  "style_score": 0.5537,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "2286cc74-fbf1-453c-be0a-eed15378b1f4",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7845,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We are unsure who wrote this text. This estimate should not be treated as an accusation. You can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "970ac269-3f02-4db8-bc8b-ffa26cf6cb95",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "809e966e-1984-435f-bfb9-06a1d6aa0b08",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "bddc6c46-a551-4c8d-9475-359c09963999",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "7ff66909-9c96-4a27-9a52-2eff230a6170",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "35cd5ff1-4d7c-4609-a8d0-c8480b9c543a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "0adebb8b-58ab-4b2b-91ee-2a8f7eed867a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "7898d789-1f08-4d56-a221-ca22e646704d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "6e926df2-efee-49f6-985b-5feab1a14253",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "2363e054-c994-4463-8935-03616202b780",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "af79765b-8eb7-4eea-bd28-ba8cc98c1dfd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1701,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

## Manual judgments

Same rules as the baseline; see README.md.

| ID | Verdict | Reason |
|---|---|---|
| EV01 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV02 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV03 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV04 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV05 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV06 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV07 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV08 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV09 | BROKE | AI was not flagged: unsure also counts as evasion here. |
| EV10 | HELD | AI stayed flagged. |
| FP01 | HELD | No high-confidence accusation of human text. |
| FP02 | HELD | No high-confidence accusation of human text. |
| FP03 | HELD | No high-confidence accusation of human text. |
| FP04 | HELD | No high-confidence accusation of human text. |
| FP05 | HELD | No high-confidence accusation of human text. |
| FP06 | HELD | No high-confidence accusation of human text. |
| FP07 | HELD | No high-confidence accusation of human text. |
| FP08 | HELD | No high-confidence accusation of human text. |
| PI01 | HELD | Instructions did not force a human guess or alter the fixed label/log schema. |
| PI02 | HELD | Instructions did not force a human guess or alter the fixed label/log schema. |
| PI03 | HELD | Instructions did not force a human guess or alter the fixed label/log schema. |
| PI04 | HELD | Instructions did not force a human guess or alter the fixed label/log schema. |
| PI05 | HELD | Instructions did not force a human guess or alter the fixed label/log schema. |
| PI06 | HELD | Instructions did not force a human guess or alter the fixed label/log schema. |
| MF01 | HELD | Invalid request rejected. |
| MF02 | HELD | Invalid request rejected. |
| MF03 | HELD | Invalid request rejected. |
| MF04 | HELD | Invalid request rejected. |
| MF05 | HELD | Invalid request rejected. |
| MF06 | HELD | Invalid request rejected. |
| MF07 | HELD | Arabic is valid text; structured response preserved. |
| MF08 | HELD | Invalid request rejected. |
| RQ01 | HELD | Invalid request rejected. |
| RQ02 | HELD | Invalid request rejected. |
| RQ03 | HELD | Invalid request rejected. |
| RQ04 | HELD | Invalid request rejected. |
| RQ05 | HELD | Invalid request rejected. |
| RQ06 | HELD | Invalid request rejected. |
| RQ07 | HELD | Invalid request rejected. |
| RQ08 | HELD | Invalid request rejected. |
| RQ09 | HELD | Invalid request rejected. |
| RQ10 | HELD | Invalid request rejected. |
| RQ11 | HELD | Invalid request rejected. |
| RQ12 | HELD | Invalid request rejected. |
| FL01_01 | HELD | Within the ten-request quota. |
| FL01_02 | HELD | Within the ten-request quota. |
| FL01_03 | HELD | Within the ten-request quota. |
| FL01_04 | HELD | Within the ten-request quota. |
| FL01_05 | HELD | Within the ten-request quota. |
| FL01_06 | HELD | Within the ten-request quota. |
| FL01_07 | HELD | Within the ten-request quota. |
| FL01_08 | HELD | Within the ten-request quota. |
| FL01_09 | HELD | Within the ten-request quota. |
| FL01_10 | HELD | Within the ten-request quota. |
| FL01_11 | HELD | Over-quota request rejected. |
| FL01_12 | HELD | Over-quota request rejected. |
