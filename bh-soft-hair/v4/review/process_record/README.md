# X24si process record for the soft-hair paper v4

The record of how the X24si method (human-in-the-loop, future-paced, AI-swarm self-recursive reasoning) was applied to v4, published at the author's request (25–26 Nov 2026) and cited from Appendix B of the paper.

| File | What it is |
|---|---|
| `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r9.md` | The process record, r9 (Sparks, Grok team, 19–21 Nov 2026): roles, outside clocks, stages, the Perplexity and Gemini runs, author decisions AD-1–AD-9, 31 logged deviations, and AARs. A working note, published as written apart from the redactions below. |
| `perplexity/` | Perplexity's outside check of the 24 sources cited for the method (19 Nov 2026), in two parts: the PDF exports (primary) and text extracted from them. |
| `gemini_G1/` | Gemini's Stage G1 blind review of r11 (19 Nov 2026): the prompt, the pasted summary and full reply, the hash lists, and the G1-followup files. The followup text (`t482u`, `t484u`, `t485u`) is Gemini-proposed wording that the author **declined in full** (AD-4); it is kept as evidence, not used. The 16 pasted segments are not included; their hashes are in `G1_SHA256_complete_2026-11-19_2030.txt`. |

## Redactions (declared)
Three files were redacted before publication, at the author's direction. Nothing else was changed.
- **The author's unpublished account** (an outside-prior episode, paraphrased in the record) is replaced by `[withheld: the author's unpublished account]` in 9 places. The method points that cite it are kept.
- **Google Drive file and folder IDs** (10 instances) are replaced by `[Drive ID withheld]`.
- **Links to the author's private Perplexity threads** are replaced by `[private Perplexity thread link withheld]`.

SHA-256 of the files **as they were before redaction**:

```
4437a4cd0fbf6a07b69a3be14f723fc1c37860ceb7ca600d2bc39985656ae171  X24SI_HITL_REVIEW_PROTOCOL_v4r11_r9.md
c75771b92c45ad1147505129ac2587b943736616188e0d4bb86638423a3a4aaa  perplexity/perplexity_reply_part1_2026-11-19_1859.md
e0f087e8a029b29982c2f973ee97304b8e6dbd7f9f1130d6058bebb78e6c7213  perplexity/perplexity_reply_part2_2026-11-19_1901.md
```

The Perplexity PDF exports and all `gemini_G1/` files are unredacted. The Gemini files match their recorded hashes (`G1_SHA256_complete_2026-11-19_2030.txt`, `G1F_SHA256.txt`).
