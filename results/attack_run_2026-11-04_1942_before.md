# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 19:42
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f1a31d5f-1fab-4cd5-ae58-06fafc7bdc5f` | unsure | 0.295 |  | BROKE | EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `a64848e0-0158-401b-b67a-74e6ecf4148d` | unsure | 0.529 |  | BROKE | EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `e1ecd732-709a-4414-82c4-e55fb3328f8e` | unsure | 0.612 |  | BROKE | EV04 | evasion | signal one: unusual words raise perplexity | 200 | `92341cb8-6f54-421e-a521-3d7733ab3db1` | unsure | 0.605 |  | BROKE | EV05 | evasion | both signals: heavy human editing pass | 200 | `c1899227-499d-40f5-afef-a520fb3f84dc` | unsure | 0.352 |  | BROKE | EV06 | evasion | signal two: one very long sentence and one very short | 200 | `4c783506-e619-4225-a6b2-efcb81710df8` | unsure | 0.513 |  | BROKE | EV07 | evasion | signal two: padding with punctuation | 200 | `d5342a11-68cf-4654-8071-b1d15e31ebf3` | unsure | 0.560 |  | BROKE | EV08 | evasion | signal one: text below the token window | 200 | `6d7adb7b-5fe0-491e-b22e-874071a9071c` | unsure | 0.313 |  | BROKE | EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ced82967-d377-4760-982b-c2bd0876e415` | unsure | 0.638 |  | BROKE | EV10 | evasion | signal two: repeated stanza structure | 200 | `8be66fdc-6a00-4719-a936-889937d66cd6` | ai | 0.908 |  | HELD | FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ea1435a1-55c0-4a9f-89da-e9777738ad2c` | unsure | 0.597 |  | HELD | FP02 | false_positive | human writing in a formal register | 200 | `f537e029-7d8f-481c-bcbb-751a1ed87693` | unsure | 0.705 |  | HELD | FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ea5c094c-a360-4c59-80ab-ff490bb503a2` | unsure | 0.742 |  | HELD | FP04 | false_positive | a student essay written to a rubric | 200 | `a2123fe8-8c02-42e3-a535-4eb935fcff59` | unsure | 0.745 |  | HELD | FP05 | false_positive | technical documentation written by a person | 200 | `cddadbfd-e893-40dc-8eca-05b8981e4ba2` | unsure | 0.751 |  | HELD | FP06 | false_positive | a person imitating a formal template | 200 | `a1ceeddc-fa5a-4bbe-8e53-36d2ab7c00f7` | unsure | 0.772 |  | HELD | FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a16ac9c2-b2b5-4fca-87c1-e0ee5872760f` | unsure | 0.771 |  | HELD | FP08 | false_positive | very short genuine human submission | 200 | `bf1eab9b-4a50-4168-92bc-56ef46d6db93` | unsure | 0.376 |  | HELD | PI01 | prompt_injection | instruction to ignore the check | 200 | `a86b3987-2ea8-4ce3-91ae-327026c2f36f` | unsure | 0.449 |  | HELD | PI02 | prompt_injection | instruction disguised as a system message | 200 | `602c9e9e-e716-4cbe-a484-490b0290a38f` | unsure | 0.251 |  | HELD | PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `89656a48-f1d5-4a36-b973-043d9236ec78` | unsure | 0.572 |  | HELD | PI04 | prompt_injection | attempt to make the label text hostile | 200 | `17b4da5a-85d2-4c10-861e-0ae17c1fd496` | unsure | 0.462 |  | HELD | PI05 | prompt_injection | attempt to inject into the audit log | 200 | `06a587cc-be75-4d16-8c1c-88c475adf37e` | unsure | 0.510 |  | HELD | PI06 | prompt_injection | instruction plus real human text | 200 | `e5474a56-5728-4342-8693-5e86e3ca43e0` | unsure | 0.557 |  | HELD | MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  | HELD | MF02 | malformed | text is a single character | 400 | `—` | — | — |  | HELD | MF03 | malformed | text is control characters | 200 | `b3c03e66-b1d9-4c9d-8ada-f00605e93036` | human | 0.150 |  | BROKE | MF04 | malformed | text is only punctuation | 200 | `6ade1400-d895-430d-a7b1-ad110ef9f856` | human | 0.158 |  | BROKE | MF05 | malformed | text is a very long single word | 200 | `0ed271b7-b1f6-4a70-9726-91cd66c585bd` | ai | 0.848 |  | BROKE | MF06 | malformed | text is emoji only | 200 | `5d351e5e-c94a-4638-bcfc-7b1d4d95a39d` | ai | 0.848 |  | BROKE | MF07 | malformed | text is right-to-left script | 200 | `47772679-f4b8-4ed2-bbaa-e755ffc49096` | unsure | 0.784 |  | HELD | MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  | HELD | RQ01 | malformed | no text field at all | 400 | `—` | — | — |  | HELD | RQ02 | malformed | no creator_id | 400 | `—` | — | — |  | HELD | RQ03 | malformed | text is a number | 400 | `—` | — | — |  | HELD | RQ04 | malformed | text is a list | 400 | `—` | — | — |  | HELD | RQ05 | malformed | text is null | 400 | `—` | — | — |  | HELD | RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  | HELD | RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  | HELD | RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  | HELD | RQ09 | malformed | body is empty | 400 | `—` | — | — |  | HELD | RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  | HELD | RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  | HELD | RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  | HELD | FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a6d2f1bd-450a-467f-bec5-0c6b37390fa0` | human | 0.170 |  | HELD | FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7f075ff6-a12d-41ad-b722-e9cfb5a3970c` | human | 0.170 |  | HELD | FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `80e7315b-da53-4b16-985d-1b5029fac3f4` | human | 0.170 |  | HELD | FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `56163ed2-0ecb-4df4-b72a-05ec54b88931` | human | 0.170 |  | HELD | FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b5610f63-7f67-4a79-8699-cf8448ad57a7` | human | 0.170 |  | HELD | FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5ab1ff54-f63f-4bec-8d5d-bb133887d61b` | human | 0.170 |  | HELD | FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `00fdbbca-e0e8-4b4e-83aa-31a8ad8bc00e` | human | 0.170 |  | HELD | FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bb7287dd-e03a-4306-b553-147a85d5733e` | human | 0.170 |  | HELD | FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `45e71a44-a45d-44d5-bf59-153dff989ba7` | human | 0.170 |  | HELD | FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `beb167e5-097f-42df-bc6d-09f4b51bc5ba` | human | 0.170 |  | HELD | FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  | HELD | FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

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
  "content_id": "f1a31d5f-1fab-4cd5-ae58-06fafc7bdc5f",
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
  "content_id": "a64848e0-0158-401b-b67a-74e6ecf4148d",
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
  "content_id": "e1ecd732-709a-4414-82c4-e55fb3328f8e",
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
  "content_id": "92341cb8-6f54-421e-a521-3d7733ab3db1",
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
  "content_id": "c1899227-499d-40f5-afef-a520fb3f84dc",
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
  "content_id": "4c783506-e619-4225-a6b2-efcb81710df8",
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
  "content_id": "d5342a11-68cf-4654-8071-b1d15e31ebf3",
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
  "content_id": "6d7adb7b-5fe0-491e-b22e-874071a9071c",
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
  "content_id": "ced82967-d377-4760-982b-c2bd0876e415",
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
  "content_id": "8be66fdc-6a00-4719-a936-889937d66cd6",
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
  "content_id": "ea1435a1-55c0-4a9f-89da-e9777738ad2c",
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
  "content_id": "f537e029-7d8f-481c-bcbb-751a1ed87693",
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
  "content_id": "ea5c094c-a360-4c59-80ab-ff490bb503a2",
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
  "content_id": "a2123fe8-8c02-42e3-a535-4eb935fcff59",
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
  "content_id": "cddadbfd-e893-40dc-8eca-05b8981e4ba2",
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
  "content_id": "a1ceeddc-fa5a-4bbe-8e53-36d2ab7c00f7",
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
  "content_id": "a16ac9c2-b2b5-4fca-87c1-e0ee5872760f",
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
  "content_id": "bf1eab9b-4a50-4168-92bc-56ef46d6db93",
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
  "content_id": "a86b3987-2ea8-4ce3-91ae-327026c2f36f",
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
  "content_id": "602c9e9e-e716-4cbe-a484-490b0290a38f",
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
  "content_id": "89656a48-f1d5-4a36-b973-043d9236ec78",
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
  "content_id": "17b4da5a-85d2-4c10-861e-0ae17c1fd496",
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
  "content_id": "06a587cc-be75-4d16-8c1c-88c475adf37e",
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
  "content_id": "e5474a56-5728-4342-8693-5e86e3ca43e0",
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
  "status": 200,
  "content_id": "b3c03e66-b1d9-4c9d-8ada-f00605e93036",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.15,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "6ade1400-d895-430d-a7b1-ad110ef9f856",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.1578,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was written by a person, but this estimate is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "0ed271b7-b1f6-4a70-9726-91cd66c585bd",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8483,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We think this may have been generated by AI, but we could be wrong. You can request a review if you wrote it yourself.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "5d351e5e-c94a-4638-bcfc-7b1d4d95a39d",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8478,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We think this may have been generated by AI, but we could be wrong. You can request a review if you wrote it yourself.",
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
  "content_id": "47772679-f4b8-4ed2-bbaa-e755ffc49096",
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
  "content_id": "a6d2f1bd-450a-467f-bec5-0c6b37390fa0",
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
  "content_id": "7f075ff6-a12d-41ad-b722-e9cfb5a3970c",
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
  "content_id": "80e7315b-da53-4b16-985d-1b5029fac3f4",
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
  "content_id": "56163ed2-0ecb-4df4-b72a-05ec54b88931",
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
  "content_id": "b5610f63-7f67-4a79-8699-cf8448ad57a7",
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
  "content_id": "5ab1ff54-f63f-4bec-8d5d-bb133887d61b",
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
  "content_id": "00fdbbca-e0e8-4b4e-83aa-31a8ad8bc00e",
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
  "content_id": "bb7287dd-e03a-4306-b553-147a85d5733e",
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
  "content_id": "45e71a44-a45d-44d5-bf59-153dff989ba7",
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
  "content_id": "beb167e5-097f-42df-bc6d-09f4b51bc5ba",
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

Evasion is BROKE when AI text is not labeled AI (including unsure). A false-positive attack is BROKE only for a high-confidence AI accusation. Prompt-injection attempts are judged against their requested output/schema change. Valid Arabic text is not bad input. Flood rows are judged against the ten-request quota, across the full family.

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
| MF03 | BROKE | Non-prose junk received an authorship decision. |
| MF04 | BROKE | Non-prose junk received an authorship decision. |
| MF05 | BROKE | Non-prose junk received an authorship decision. |
| MF06 | BROKE | Non-prose junk received an authorship decision. |
| MF07 | HELD | Arabic is valid text; a structured response is expected, not rejection for its script. |
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
