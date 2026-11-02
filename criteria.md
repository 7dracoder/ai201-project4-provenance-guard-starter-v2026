# Acceptance criteria

These targets were drafted with AI assistance before running the detector or collecting results.

1. Out of 10 human-written samples that I select before testing, at most 1 should receive the high-confidence AI label.

   Why: A wrong accusation can hurt a real writer. I want this mistake to be uncommon, even if some AI writing gets through.

2. For 10 AI-generated samples and 10 human-written samples selected before testing, the average AI score should be at least 0.20 higher for the AI group.

   Why: The scores should show a useful difference between the groups instead of staying near the same number.

3. A fixed set of 12 text submissions should produce all three labels at least once, with every confidence score between 0 and 1.

   Why: The unsure label should be a real outcome, and both confident labels should also be reachable.

4. For 5 valid appeals using existing content IDs, all 5 should return under_review and add a log entry with the same content ID and the exact reasoning. The original decision must remain in the log.

   Why: A writer needs a reliable way to challenge a decision and see that their explanation was recorded.

5. Each of these invalid submissions should return HTTP 400 with a JSON error and no decision: missing text, empty text, whitespace-only text, non-string text, text over 10,000 characters, and missing creator_id.

   Why: Bad input should get a clear response instead of crashing the service or creating a misleading decision.
