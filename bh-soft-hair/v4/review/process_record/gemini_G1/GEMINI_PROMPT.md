# Prompt for Gemini: independent review of the soft-hair paper v4 r11

Paste everything below the line into Gemini, attaching every file in this folder (the PDF, the .tex, GROK_REVIEW_PACKET.md and the .txt files).

---

You are an independent reviewer for George Bressler. Attached are a physics paper (bh_soft_hair_v4_r11.pdf, with its LaTeX source) and a review packet (GROK_REVIEW_PACKET.md) that fixes the criteria in advance. The packet was written for a Grok review; apply the same criteria, priorities and reply template to yourself as a reviewer from a third model family (Google). You have not seen any other reviewer's findings, and you should not try to find them.

Rules:
1. Review only the attached bytes. The pinned SHA-256 values are: PDF f83639b2ebf2043705c62998cc84cebdaae24e12e256b17de15adf910baae5f9, tex fbd273d0c01c73ca93d33a56b299f75bdd0326ae485d38d56dfdbe1830818a77 (checked by Sparks before upload).
2. Use the packet's severity criteria (MUST-FIX a/b/c/d, SHOULD-FIX, NOTE) and its four priority areas first, then a general pass.
3. Attached supporting files (renamed .txt so they upload): the pre-registration, its input JSON, the frozen verdict script, the run output and result for the X24si/LVK ringdown test (section 7.1), and the GRACE script TMRB_GRACE_torsion_search_2026-04-27.py (section 8.1). The git history is NOT attached. Commit times recorded by Sparks from the repository: 76d92c7 (registration) 2026-11-18 16:05:55 UTC, d590909 (input transcription) 16:06:44 UTC, e16e6a6 (result) 16:07:18 UTC. Judge for yourself what those times can and cannot prove.
4. For outside sources (arXiv:2607.19293 GWTC-5.0, eq. 21-22 p.23 and p.24; Sen arXiv:1205.0971 eqs. 1.2-1.5), open them if you can and say so. If you cannot open them, write "I cannot check that from here". Do not answer from memory.
5. "Inconclusive" and "I cannot check that from here" are complete answers. Do not guess. Every number you report must come from a computation you show or a source you opened.
6. You provide decision support only; George makes the decisions.

Reply format, one block per finding:

Finding N
  Location:   section / equation / page (in the attached PDF)
  Severity:   MUST-FIX (a|b|c|d) | SHOULD-FIX | NOTE
  Claim in paper:
  Finding:
  Provenance: reasoning | retrieval (source opened: ...) | execution (computation shown)
  Proposed fix:
  Confidence: high | medium | low | inconclusive

Start with one line naming yourself (model name and version as you know it) and today's date. End with one line: what you learned, or the stuck point you are handing on.
