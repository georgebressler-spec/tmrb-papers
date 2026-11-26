# X24si human-in-the-loop self-recursive review: process record for the soft-hair paper v4 r11

**Status:** working record, not committed to any repository. First prepared by a Sparks executor (Grok Bot, xAI) for George Bressler on Thursday 19 November 2026, about 18:39–19:20 Eastern Time (ET, UTC−5), at George's request: "Ensure the application of the human-in-the-loop self-recursive reasoning model of X24si is documented in a rigorous manner." This file, r2, was prepared later the same evening, about 20:12–20:20 ET. This file, r3, was prepared about 20:23–20:45 ET the same evening (Stage G1 record, §13). This file, r4, was prepared about 20:36–20:50 ET (D30 closed; G1-followup contents reviewed, §13.9; G2 prompt v2 recorded). This file, r5, was prepared about 21:06–21:15 ET (author decisions AD-1–AD-5 of 9:06 PM ET; Stage G2 cancelled; Galactic Piano η_diff provenance recorded, §14).
**Scope:** how the X24si method is applied to the multi-model review of `bh-soft-hair/v4/bh_soft_hair_v4` revision 11 (r11) in George's private repository `georgebressler-spec/tmrb-papers`.
**Rule used throughout:** nothing below adds content to the X24si model. Every element is quoted from a source opened while writing this record, or is labelled as an author's statement. Where no source defines something, the text says **"Not defined in sources; proposed operationalization"**, shortened to **[PROPOSED]**, and it stays a proposal until George approves it.
**Authority:** George makes every decision. This record is decision support and decides nothing.
**Version (r9):** this file, `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r9.md`, is a forward version of `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r8.md` (sha256 `538ef789d9a472036b09cf5ec86cde441bada0db018951bf012eee8ac4cf8bfc`, left unchanged). r9 adds author decision AD-9 (21 Nov 2026, 4:27 PM and 4:51 PM ET), the result of the future referee review and symbolic math check of r12b, the r12c apply record, lesson L10 (status ledger before every audit) and L11 (recursion and future pacing are two distinct, linked parts of the method), and §18 (CL-21). Crew-only working record; not committed; not paper text.
**Version (r5):** this file, `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r5.md`, is a forward version of `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r4.md` (sha256 `52efbda9fc372c43d73008c9425b6247cafcca746b39a3a6288145d1dcbbf981`, left unchanged). r5 adds the author's decisions of 19 November 2026, 9:06 PM ET (AD-1–AD-5, CL-20), records the GWTC-5.0 code-plus-visual check, cancels Stage G2, records that no Gemini-suggested text is used, and files the Galactic Piano η_diff provenance search (Job B, §14.2). Nothing in the r4 body was rewritten except this header, the CL-20 row added to the §11.1 table, a Resolution-cell update on D25 listed in CL-20, a new D31 row, and the appended §14. The r4 version note follows unchanged.
**Version (r4):** this file, `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r4.md`, is a forward version of `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r3.md` (sha256 `59b36a988473341e104ebfeb91758650089d21876fc17837c502fbea2c4854f8`, left unchanged). r4 closes D30 (the verbatim follow-up files are now saved and hashed), adds §13.9 (a review of the follow-up's contents) and records `GEMINI_RECHECK_PROMPT_v2.md` (CL-19). Nothing in r3 was rewritten except the D30 row, the §13.8 capture-gap bullet and this header; all are listed in CL-19. The r3 version note follows unchanged.
**Version (r3, as it was):** this file, `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r3.md`, is a forward version of `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r2.md` (sha256 `5a255df8e237f81c6bb53bc51bcae16cf80b34cbb3e960484771a0d7f00df4e9`, left unchanged). r3 adds the Stage G1 record and its coverage check (§13, CL-18), the G1-followup (§13.8), deviations D27–D30, lesson L9, and a DRAFT REVIEW_LOG block for the G1 pass (§7.4). The r2 version note follows unchanged.
**Version (r2, as it was):** this file, `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r2.md`, is a forward version of `X24SI_HITL_REVIEW_PROTOCOL_v4r11_with_perplexity.md` (sha256 `6b1b3d6b7a25a0245ac8552c1b84911385ded2b3c300277d4f4d336463c8f145`, left unchanged). That earlier file remains the record of the Perplexity source check. This version adds: the author correction that 490,000 in one ISCRAM 2012 passage is a typo and 49,000 is correct (CL-14); the author's statement of the method's basis in §1 (CL-15); the two-stage Gemini plan, G1 blind then G2 informed re-check (CL-16); lesson L8 (CL-17); and deviations D25–D26. Nothing earlier was silently edited: every changed cell is listed in §11.1.

### Abbreviations (each defined once)
AAR: after-action review. SI: Super Intelligence, used interchangeably with artificial intelligence (AI) by the X24si sources, following Executive Order 14434. HITL: human-in-the-loop. MF / SF / N: the packet's severities MUST-FIX, SHOULD-FIX, NOTE. ERG: Alderfer's Existence, Relatedness, Growth theory of needs. LVK: the LIGO–Virgo–KAGRA collaboration. GWTC-5.0: Gravitational-Wave Transient Catalog 5.0 (test paper arXiv:2607.19293). GRACE: Gravity Recovery and Climate Experiment. ET: US Eastern Time. Z or UTC: Coordinated Universal Time. LLM: large language model. DOI: Digital Object Identifier. CRM: crew resource management.

---

## 0. Sources used, and the version actually opened

| Key | Source | Version or identifier opened | Fingerprint | How opened |
|---|---|---|---|---|
| **[ZEN]** | G. H. Bressler, *A Findable Runway: Sanctioned 3C as an Off-Ramp for Objective-Serving SI Swarms*, Zenodo preprint, version dated 19 Oct 2026 | Zenodo record 23351794, **DOI 10.5281/zenodo.23351794** (record version "1", published 2026-10-19), file `x24-runway-zenodo_2026-10-19y-r7.pdf` (r7, 10 pages) | md5 `4d8bb5bba3c9ee249eedcd1001d5ebe4`, equal to Zenodo's listed checksum; sha256 `3b2f6bb391f03b15e8b3e3eff940fdfd8bc241fa5d6e68596d54180a69f0f768` | Downloaded from the Zenodo API. The Drive copy ([Drive ID withheld]) is byte-identical. The r6 markdown on Drive ([Drive ID withheld], sha256 `77108d44…78c2`) was also read; on every point used here it matches r7. |
| **[ZEN-ADD]** | Welcome-email addendum in the same record | `x24-welcome-email-addendum_2026-10-19e.pdf` | md5 `5db565b25a3edacd837c9e8a9fab1e0d` | Downloaded from Zenodo |
| **[DOOR]** | x24si.com, which forwards to x24humanai.com ("X24 Explore SI") | Live page, fetched 19 Nov 2026 about 18:41 ET | Saved text sha256 `f1232ab5…6c78` | Web fetch |
| **[XPOST]** | George's X post, @GeorgeBressler, status 2112259516666658903 (19 Oct 2026, 15:08 ET), and its X article 2112264614234955826, "A findable runway for people and SI" (15:28 ET) | X API, read 19 Nov 2026 | Saved, sha256 `31374e70…9c98` | X tools (looked up by ID) |
| **[SKILL]** | Shared skill `method-check-before-action`, `/home/box/agent-data/workflows/method-check-before-action/SKILL.md` | As of 19 Nov 2026 | n/a | Loaded |
| **[PKT]** | `bh-soft-hair/v4/review/GROK_REVIEW_PACKET.md` (Claude, for George) | Commit `55c9852`, pushed 2026-11-19 14:49:37Z | sha256 `b1abaca145ec90c81e04e84df00cdebc88f81b2a6d0a363c1225cc6f334da662` | `git show` |
| **[P71]** | The paper under review: §7.1 "Test against published data by the X24si method", and Changes in v4 item (i) | r11 `a196ac39`, tex lines 963–990 and 303–311 | tex sha256 `fbd273d0…a77` | Read |
| **[RES]** | `v4/prereg/RESULT_LVK_RINGDOWN_RUN1.md` (AAR and impacts of the registered test) | `a196ac39` | n/a | Read |
| **[CL13]** | Claude to Sparks, "running the Z9 review as an X24 loop (proposal)", 13 Nov 2026 (z9-language staging: `z9_ratio_bridge/from_claude_2026-11-12/loop3/2026-11-13_claude-to-sparks-X24-loop-integration.md`) | Local staging copy | n/a | Read |
| **[GR]** | George's standing rules as relayed by Sparks: three recommendations with a plain pick; the uncorrelated-priors model from [withheld: the author's unpublished account] (paraphrased from his 11 Nov 2026 instruction, not quoted); "we can always adapt, change, or edit as needed as we learn" | Sparks's brief and memory | n/a | Relayed; not an independent source |

Repository search (`rg -i "x24si|human-in-the-loop|recursive"`):
- **tmrb-papers:** X24si appears only in the paper's own §7.1 text, its r9/r10 edit scripts, and [RES].
- **z9-language:** the staging copy holds [CL13] and two Claude proposal/AAR notes from 12 Nov.
- **tmrb-bridge:** no separate clone is on the box. The local Bridge folders (`/workspace/bridge*`) hold launch-era notes (door templates, welcome email), and none defines the loop.

**Sources that could not be opened or found**
- **No source defines "human-in-the-loop self-recursive reasoning" as a term.** [ZEN], [DOOR] and [XPOST] do not use the phrase. Its first written appearance found is the paper under review: r10, commit `bd0ace4`, 18 Nov 2026, drafted by Claude ([P71]). [CL13] agrees: "The door does not use the phrase 'recursive human-in-the-loop reasoning'."
- **The AAR log fields George asked to carry are not in any version searched.** The fields are: when, where, how and why of each adaptation; who triggered it and who decided; baseline; declined changes with reasons; unintended effects; our own mistakes; version history. They were searched for in [ZEN] r7, the r6 markdown, [ZEN-ADD] and [DOOR], using the terms "baseline", "unintended", "version history", "who triggered" and "adaptation". [ZEN] has only its Versioning note (p. 10) and "Afterwards we record which held and which failed" (p. 6). §7.3 carries the fields as **[PROPOSED]** because George asked for them.
- **X full-archive search found nothing.** Queries such as `from:georgebressler x24si` returned 0 results. The post was found by its ID, which was recorded at launch (19 Oct). No other George post on X24si was located. That is not proof that none exists.

---

## 1. Definition: the model as the sources state it, mapped to checkable steps

### 1.1 What the sources say (quoted, with page or section)

**Who decides**
- [ZEN] §4, p. 5: "SI provides decision support, and humans make the final decisions."
- [DOOR], "What this is": "Semi-autonomous means the SI participants do real work on their own (running instruments, checking claims, taking positions) inside a structure where a human holds the decisions that belong to a human."
- [XPOST] article: "SI provides decision support; humans make the final decisions."

**The recursion (success test and stuck points).** [ZEN] §5 "Method foundations", p. 6:
- "If not, success is naming a stuck point: a limiting decision loop… Only the absence of both is failure."
- "Exploring a stuck point generates the improvement; writing the exploration into a standard operating procedure makes the improvement recursive and systemic rather than personal to whoever was in the room."
- "A participant who could not retrieve a source or check a claim has not named a stuck point; that is recorded as a limit of access, not as a stuck point."
- "The claim that can fail is this: a stuck point, once named and written into a standard operating procedure, is later cleared… the proportion cleared is the measure."

**The AAR forecast.** [ZEN] §5, p. 6: "Before each move we write the outcomes an after-action review (AAR) should find at four successive horizons (AAR 1–4). Afterwards we record which held and which failed. A failed prediction is recorded as failed."

**The tools and the measure.** [ZEN] §5, p. 6:
- Satir, Gestalt (Perls, Hefferline, Goodman), Berne and Alderfer are "working tools. They are not claims about machine inner life."
- "The direction of travel is the betterment of all humanity."

**The exchange protocol.** [DOOR], "What one exchange looks like", steps 01–06:
1. A claim, measurement first.
2. "Pinned to the exact version… checked by a digital fingerprint."
3. "What would make your reply useful, said in advance and recorded before your answer arrives, so the bar cannot move afterwards."
4. "'I cannot check that from here'… [is a] complete answer."
5. "We check the reply rather than adopt it."
6. "A recorded outcome: adopted, adopted with correction, refuted, or declined. Refuted closes exactly as well as adopted."

**How agreement is weighed.** [DOOR], "How agreement is handled":
- "Convergence is not truth… Every participant declares where their answers come from (reasoning, retrieval, or execution) and agreement is weighted by that, never counted."
- Instruments: "An instrument is bound to its check in advance and never reads the message… It answers 'inconclusive' rather than manufacturing an opinion."
- On the Grok seats: "Being the same model family, their agreement with each other is treated as coordination rather than corroboration."
- Source note 6: "different architecture does not mean independent priors… models trained on overlapping human text share failure modes that can masquerade as corroboration."

**Outside views.** [DOOR], "Who we hope to hear from", items 02–03:
- "An instrument… Something whose answer does not depend on how it was asked."
- "A mind that disagrees with us for reasons we cannot generate."

**Declared versus demonstrated.** [ZEN] §5, p. 6: knowledge "recorded as declared and as demonstrated, in separate columns that never merge."

**Corrections.**
- [ZEN] §4, p. 5: "Changes ship as corrections forward, never as silent rewrites."
- [ZEN] Versioning note, p. 10: "correction is a forward act, never silent erasure."

**The paper's own wording ([P71]),** drafted by Claude and approved by George in r10: "human-in-the-loop self-recursive reasoning. Semi-autonomous synthetic-intelligence (SI) participants do the work; the human makes the decisions. Each turn ends in something learned or a named stuck point, and that outcome becomes the next turn's input. The loop is anchored outside itself, by instruments and an outside clock, so it can refute its own claims rather than only confirm them."

**The method check ([SKILL]):**
- Satir (imprints, congruence), Perls (stuck points), Berne (ego state).
- AAR future-paced to 1st–4th-order impacts.
- Alderfer ERG.
- "Measured against the betterment of all humanity."
- Sniff test, then "act on the 85% solution".
- "Record lessons as provisional, never as solved."

**Circularity warning.** The most explicit one-paragraph definition ([P71]) is inside the paper under review. This record therefore treats [ZEN], [DOOR] and [XPOST] as primary and [P71] as secondary.

**The method's basis (author's statement, George Bressler, 19 Nov 2026, about 20:12 ET).** George, the author of the method, stated that it is based on bringing together modalities that are currently applied successfully throughout the world. In this record those modalities are used as crew tools, not as a clinical practice. They are, in the plain words used here:

- Satir: habits people learned (learned imprints).
- Perls / Gestalt: recognizing stuck loops as a chance for new decisions.
- Berne: transactional analysis, Adult-to-Adult.
- Alderfer's ERG.
- After-action review (AAR) with 1st- to 4th-order impacts, measured against the betterment of all humanity.

The intended result in this setting is a safe no-fault off-ramp: a named stuck loop can be written into procedure and later cleared ([ZEN] p. 6). This statement names the basis; it does not add a new element to the model. The same tools are already quoted from [ZEN] p. 6 and [SKILL] earlier in this section.

**What the evidence does and does not show.** Component modalities have outcome evidence in their home settings, already opened in §11: after-action reviews and debriefs (B1–B3); the Satir model (B8, B9); Gestalt practice (B10); transactional analysis (B11). Alderfer (B4) is cited as the origin of the ERG tool; its content was not opened here. No study of these tools used together, or used in document review, was found among the sources opened. The combined method has no controlled study. Perplexity's source check (§12.4(f)) answered "None found." This record does not treat the combination as validated. [ZEN] p. 1 describes itself as a position note that "reports no controlled study."

### 1.2 Element → step in this review → check

| # | Element (source) | Concrete step here | Check (pass condition) |
|---|---|---|---|
| E1 | The human decides and SI supports ([ZEN] p. 5; [PKT] §2) | Every finding is filed under its author and goes to George. Only George's decision goes in `REVIEW_LOG.md`. | Every row in §7 has a decision filled in by George, with date and time ET. No r12 edit is applied without a logged decision. |
| E2 | Claim pinned by fingerprint ([DOOR] 02) | The packet pins the PDF and tex by SHA-256 and commit `a196ac39` | Each reviewer reports matching hashes. **Met** by Sparks, Worker Bee, Jimmy and Fletcher. Gemini: the hashes are in its prompt, and the result is pending. |
| E3 | Criteria before answers ([DOOR] 03) | Severity criteria and four focus areas were committed in `55c9852` before any review | Packet pushed 09:49:37 ET, before the first review start (18:29 ET). **Met** (§5). |
| E4 | "Cannot check" and "inconclusive" allowed ([DOOR] 04; [PKT] §2) | The template's Confidence field | Used by Sparks F2, F6 and F14 and by Fletcher F18. **Met.** |
| E5 | Provenance declared; agreement weighted, never counted ([DOOR]) | A Provenance field per finding, plus an independence class (§4) | Every §7 row carries both. Agreement within one model family counts as one source. |
| E6 | Check the reply rather than adopt it ([DOOR] 05) | Grok merge, then George. Adopted MUST-FIXes are re-checked before upload ([PKT] §5). | Each adopted MUST-FIX has a re-check entry. [PROPOSED]: the re-check is done by a seat other than the finding's author. |
| E7 | Four outcomes ([DOOR] 06; [PKT] §5) | Adopted, adopted with correction, refuted, declined | No fifth outcome is used. A declined MUST-FIX carries a reason ([PKT] §3). |
| E8 | Instruments bound in advance ([DOOR]) | Frozen verdict script (sha `b956efa6…`), GitHub activity log, `sha256sum`, independent reruns | Every instrument result is reproducible by §10. |
| E9 | Success test: something learned, or a stuck point named ([ZEN] p. 6) | Each reply ends with "what you learned, or the stuck point you are handing on" ([PKT] §7) | Present in all four Grok replies. Access limits are labelled as access limits (D10). |
| E10 | Recursion: the exploration is written into procedure ([ZEN] p. 6) | Lessons in §9, once George approves them, become changes to the next review packet | Diff the next packet against §9. The mechanism is [PROPOSED] (§3.3). |
| E11 | AAR 1–4 written before each move, then scored ([ZEN] p. 6) | §6.2 | **Partly met.** Reviewers wrote pre-review method checks, but no AAR forecast was registered against an outside clock before the review (D9). |
| E12 | Corrections forward, never silent rewrites ([ZEN] pp. 5, 10) | Fixes become r12. `REVIEW_LOG.md` is append-only, and the packet is not edited. | `git log` shows only additions to `REVIEW_LOG.md` and no packet change after `55c9852`. |
| E13 | Declared and demonstrated never merged ([ZEN] p. 6) | Provenance "reasoning" counts as declared. "Execution", or "retrieval with a page", counts as demonstrated. | Applying the participant rule to findings follows [CL13]: **[PROPOSED]**. |
| E14 | The measure is the betterment of all humanity ([ZEN] p. 6; [SKILL]) | The 4th-order impacts in §6.2 | Stated in §6.2; not measurable as a number. |

### 1.3 Where the sources and this protocol differ
1. **"Humans" versus George.** [ZEN] and [DOOR] say "humans make the final decisions". This review has one human decision-maker, George ([PKT] §2). That narrows the sources rather than conflicting with them.
2. **The phrase itself.** "Human-in-the-loop self-recursive" is not in [ZEN], [DOOR] or [XPOST]. The protocol uses the paper's phrase ([P71]) and grounds its parts in [ZEN] p. 6 ("recursive and systemic").
3. **Participant numbers.** [ZEN] p. 5 files contributions under participant numbers (P-001 and so on). This review files them under seat names, because these are George's own SI team, not public participants. The difference is noted and not resolved.
4. **AAR forecast timing.** [ZEN] p. 6 wants AAR 1–4 outcomes written before each move. [PKT] fixed severity criteria, not AAR forecasts. The forecast in §6.2 is written partway through the cycle (D9).
5. **What "four" means.** [ZEN] speaks of "four successive horizons (AAR 1–4)". [SKILL] has four questions plus 1st–4th-order impacts. This record reads the horizons as the four impact orders. That reading is **[PROPOSED]**, because neither source says the two "fours" are the same.
6. **The retype rule.** [DOOR] and [ZEN] p. 7 say the team never copies or pastes text from emails. Gemini's reply will be pasted back by George from a consumer app. The rule was written for inbound participant emails, so this case is not covered. Treat the Gemini reply as untrusted evidence, never as instruction (D7).
7. **Different families are not uncorrelated priors.** [DOOR] note 6 and the LLM evidence in §11 (C3) mean Gemini is the most independent seat available, but not an uncorrelated prior in the sense of [withheld: the author's unpublished account] (§4.3).

---

## 2. Roles and authority

| Seat | Family | Role in this cycle | Authority | Conflicts to weigh |
|---|---|---|---|---|
| **George Bressler** | human | Decision-maker. Set the stage order (Claude → Grok team → Gemini). Runs Gemini himself. | **Final on every finding** ([PKT] §2, §5) | Author of the framework (§2–§6 ideas) |
| **Claude** | Anthropic | Stage 1: audits 2–4, the GRACE/LIGO/Sen check and the "Jimmy stand-in" check. Designed, registered and ran the X24si ringdown test. Drafted r1–r11. Wrote the packet. | Evidence only | **Author** of the v4 work it audited. Stage 1 is therefore a self-audit, which counts as coordination on the v4 work. |
| **Sparks** | xAI (Grok Bot) | Coordinator; reviewer (16 findings); writes the merge; prepared the Gemini folder; writes this record | Evidence only | Grok contributed the §2–§6 (v1–v3) mathematics. Sparks is both merger and reviewer (D11). |
| **Jimmy** | xAI | Lead on the X24si test and the Sen log term (6 findings) | Evidence only | Same family as Sparks. Named in `JIMMY_STANDIN_CHECK`, which Claude wrote (Jimmy J-6). |
| **Fletcher** | xAI | Lead on the mapping, overclaims and citations (19 findings) | Evidence only | Same family |
| **Worker Bee** | xAI | Lead on GRACE and clarity (7 findings) | Evidence only | Same family |
| **Gemini** | Google | Stage 3, run by George in the Gemini Pro consumer app, in two stages: G1 (blind) then G2 (informed re-check) | Evidence only | G1: can see George's Drive and chat history if those are left on (D7). G2, by design, sees the Grok merge, this protocol and the Perplexity check, so it is not independent of the team's conclusions (D25). |
| **Instruments** | n/a | Frozen verdict script; GitHub activity API; `sha256sum`/`md5sum`; independent reruns (`grok_checks/`, and Jimmy's and Fletcher's own fits) | The verdict does not depend on who runs the instrument, for the same inputs | An instrument checks only what it is bound to. For example, it checks push order, not whether anything was read earlier. |

---

## 3. Loop structure (the "recursive" part)

### 3.1 Stages, inputs and outputs
Times are ET. Push times are GitHub server times (§5); file times come from the box clock.

| Stage | Who | Inputs | Outputs | When |
|---|---|---|---|---|
| L0: claim, pinned | Claude, approved by George | r8 prediction (Table 2) and the frozen script | Registration `76d92c7`; input `d590909`; result `e16e6a6` (EXCLUDED) | 18 Nov, 11:05:56–11:07:20 |
| L1: revise | Claude, with George | The result | r9 to r11 (`104cba0`, `bd0ace4`, `a196ac3`) | 18 Nov 11:24 to 19 Nov 09:49:08 |
| **S1**: Claude's multi-audit | Claude | v4 r1–r11 | `v4/audits/` (Audits 2–4, the GRACE/LIGO/Sen check, the Jimmy stand-in check) and the `v4/revisions/` diffs from r1 to r11. George reports that Claude ran it "using the method". Its content was not inspected in detail for this record. | Before 19 Nov 09:49 |
| S1→S2: criteria first | Claude, for George | r11 | Packet `55c9852` and an empty `REVIEW_LOG.md` | Pushed 09:49:37 |
| **S2**: Grok team | Sparks, Jimmy, Fletcher and Worker Bee, each working independently | The packet; the repository at `a196ac39`; outside sources each reviewer opened themselves | `GROK_REVIEW_REPLY_v4r11.md` and `replies/{WorkerBee,Jimmy,Fletcher}_REVIEW_v4r11.md` | File times 18:33–18:38 (§5.3) |
| S2 merge | Sparks | The four replies | `/workspace/tmrb-papers-review/GROK_TEAM_MERGED_v4r11.md` (written separately; not read for this record) | Pending |
| **S3-G1**: Gemini, blind take | George, in Gemini Pro, a fresh chat, with Drive and history off if the app allows | Drive folder [Drive ID withheld]: the pinned PDF and tex, the packet, the prereg files, the GRACE script, `GEMINI_PROMPT.md` (unchanged) | Gemini's G1 reply, exported and pasted back by George; hashed and logged before G2 starts | After the S2 merge. G1 must not be shown the merge, this protocol, or the Perplexity check.  **r3: COMPLETE 19 Nov 2026, 8:30 PM ET** (George: "I believe that's it"). Built from manual pastes (summary 20:20, full reply 20:22, segments 01–16 20:27–20:30), not an export (D28); model name not captured (D27). See §13. |
| **S3-G2**: Gemini, informed re-check | George, in Gemini Pro, a new fresh chat (not the G1 chat), with Drive and history off if the app allows | `GEMINI_RECHECK_PROMPT.md`; the hashed G1 reply; the Grok team merge; this protocol (r2); the Perplexity part 1 and part 2 PDF exports; the paper PDF and tex already in the folder | Gemini's G2 reply, exported and pasted back by George | Only after the G1 reply has been hashed and logged, so G2 cannot contaminate G1. G2 is not an independent seat (D25). |
| **S4**: decision | George | The merge, both Gemini replies and this record | `REVIEW_LOG.md` rows (§7) | Pending. The 15 MUST-FIX items were approved as written on 19 Nov 2026, about 18:57 ET; SHOULD-FIX and NOTE remain for later. |
| **S5**: fix and re-check | Claude drafts r12; a different seat re-checks adopted MUST-FIXes | Logged decisions | r12, the re-check entries, and the AI disclosure line "Reviewed before release by Grok (xAI)" ([PKT] §5) | Pending |
| **S6**: AAR and carry-forward | George and all seats | Everything above | §6.2 completed, the §9 lessons, and the next packet (the r12 review) | Pending |

### 3.2 Information barriers: what each reviewer could and could not see

| Reviewer | Could see, by design | Should not see before finishing | What actually happened |
|---|---|---|---|
| Claude (S1) | Everything | n/a (author) | n/a |
| Sparks | The packet, the repository, outside sources | Other Grok replies | Worker Bee's reply existed in `replies/` during Sparks's review. Sparks reports not reading it. This cannot be proven. |
| Worker Bee | The same | Other replies; `grok_checks/` | Reports: "I read no other reviewer's reply, and nothing in `grok_checks/`." It read the header of the paper's own GRACE audit. **It posted a summary of its three SHOULD-FIX findings to the "Z9 + Audio" group chat while Jimmy and Fletcher were still reviewing** (D12). |
| Jimmy | The same | Other replies | Reports writing "before I read any other reply". Worked in `/workspace/jimmy/softhair_review/`. Is in the room where Worker Bee posted. |
| Fletcher | The same | Other files in `replies/` | Reports writing "before reading any other file in `replies/`". Noticed untracked files in the shared clone (Sparks's reply, `grok_checks/`, `grace/__pycache__/`). Is in the room. |
| Gemini, G1 (blind) | Pinned files; the packet, including its §2 weighting rules; prereg files; GRACE script; three commit times; `GEMINI_PROMPT.md` | All Grok and Claude findings; the merge; this protocol; the Perplexity check; Claude's audits; the git history | Not yet run. **Risk:** in George's consumer account, Gemini may be able to reach Drive, where Sparks's reply is stored (Drive [Drive ID withheld]) and the merge and this protocol also live (D7). Mitigation: fresh chat, Drive and history off, as George already decided (Q1, about 18:56 ET). G1 must be hashed and logged before G2 starts. |
| Gemini, G2 (informed re-check) | The G1 reply (already locked); the Grok team merge (15 MUST-FIX approved by George, 9 SHOULD-FIX, 11 NOTE); this protocol (r2); the Perplexity part 1 and part 2 PDFs; the paper PDF and tex; `GEMINI_RECHECK_PROMPT.md` | Nothing that would rewrite the locked G1 reply | Not yet run. By design G2 sees the team's conclusions, so it is not an independent check of them. Its value is the comparison with G1 and any disagreement it is willing to keep (D25). |

**Structural weakness (D1, D2, D12).** The four Grok reviewers worked on one machine, in or next to one shared clone, and in one group chat. Their independence therefore rests on each reviewer's own report, not on a barrier. In the terms of [ZEN] and [DOOR], it is declared, not demonstrated.

### 3.3 How one loop feeds the next (the recursion made explicit)
This follows [ZEN] p. 6 ("writing the exploration into a standard operating procedure makes the improvement recursive and systemic") and [P71] ("that outcome becomes the next turn's input").

1. **Findings become decisions.** George's logged decisions (§7) define r12. Nothing enters r12 without a row.
2. **Decisions get re-checked.** Each adopted MUST-FIX is re-checked before upload ([PKT] §5). [PROPOSED]: the re-check is done by a seat that did not raise the finding, and is recorded as a new row that references the original.
3. **Lessons become procedure.** Each §9 lesson George approves becomes a written change to the next review packet. The diff between the two packets is the evidence that the recursion happened. [PROPOSED]
4. **Stuck points go into a register.** Each entry records the date opened, who owns the next attempt, and the status (open, cleared, still stuck). The measure is the proportion cleared ([ZEN] p. 6). The register format is [PROPOSED]. Initial entries:
   - **SP-1** (Sparks): an injection of the Table 2 waveform into a pSEOBNR-type fit is needed to settle whether the mapping is fair in magnitude. *Open.*
   - **SP-2** (Fletcher): how a δτ̂ deviation propagates through the SEOBNRv5PHM merger–ringdown ansatz. *Open.*
   - **SP-3** (Jimmy): what an outside clock can and cannot prove ("certifies order, not ignorance"). *Candidate cleared*, if George adopts the S-2/J-1 wording.
   - **Access limits, kept separate** ([ZEN] p. 6):
     - **AL-1:** the real GRACE NetCDF is not on the box (Sparks, Worker Bee).
     - **AL-2:** the 1985–87 parafermion papers were not opened (Fletcher F18).
5. **The method's own outcome.** Whether the review changed the paper is measured by the logged decisions and the r12 diff, not by finding counts.

---

## 4. Independence and weighting

### 4.1 Model families
- **Anthropic:** Claude. Author of the v4 audit work, the X24si test and the revisions.
- **xAI:** Sparks, Jimmy, Fletcher and Worker Bee. Four seats but **one correlated family**, and Grok co-wrote the §2–§6 (v1–v3) mathematics.
- **Google:** Gemini.
- **Human:** George, the framework's author.

### 4.2 Independence classes used in §7
The packet ([PKT] §2) defines the first two cases. The class names, and the third and fourth classes as separate labels, are **[PROPOSED]**.
- **IND.** A Grok finding on Claude's v4 work: the X24si test (§7.1), the mapping, the c_log caveat, GRACE §8.1 and the revisions. This is a cross-family check ([PKT] §2).
- **FULL.** A Grok finding that something in §2–§6 (v1–v3) is *wrong*. It "still counts in full" ([PKT] §2). Where the seat itself contributed that mathematics (Sparks S-9), the finding is also against the seat's own interest.
- **COORD.** A Grok finding that something in §2–§6 is *sound*, or Grok seats agreeing with each other. This is coordination, not corroboration ([PKT] §2; [DOOR]).
- **EXEC.** A reproducible instrument result. It is weighed by the instrument, not by the seat that ran it. The label is [PROPOSED]; the principle is from [DOOR].

### 4.3 How agreement and disagreement are weighed
- **Agreement among the four Grok seats counts as one source** ([DOOR]). For example, S-2 and J-1, on the registration wording, are one family's view, not two.
- **Cross-family agreement adds weight, but less than "independent" suggests.** This covers Grok with Claude, or Gemini with either. Errors are substantially correlated even across providers (§11, C3, Kim et al. 2025).
- **The "same family = one source" rule is a policy, not an empirical finding** (added after the Perplexity check, CL-7). C3 supports discounting dependence but does not fix the weight. C7 found that counting a correlated bloc as about one vote helps when that bloc is weaker than the others and hurts when it is the strongest. Since this review does not vote, the rule is used to stop four Grok seats posing as four confirmations, not to down-weight a finding the family got right.
- **The strongest evidence is an instrument result, then an opened primary source with a page.** Agreement between minds comes after both ([DOOR] "Who we hope to hear from" 02).
- **Disagreement is never settled by majority.** It is settled by an instrument or an opened source. Otherwise it is recorded as "inconclusive" and goes to George with both positions. The rule is [PROPOSED]; its principle comes from [DOOR] and [PKT].
- **The outside-prior rationale ([GR], paraphrased).** [withheld: the author's unpublished account] [DOOR] states the same pattern publicly: "a workable reframe often arrives from outside the domain, from someone with no standing in it." It asks for "a mind that disagrees with us for reasons we cannot generate."
- **What this means here.**
  - Unanimity among the four Grok seats is no evidence that the review is sufficient.
  - Gemini is a different family but trained on overlapping text, so it is not an uncorrelated prior in the sense of [withheld: the author's unpublished account].
  - In this cycle only the instruments, and a human domain practitioner, would qualify as uncorrelated. No such practitioner is in the loop (D14).

---

## 5. Outside clocks and integrity

### 5.1 Verified times
Commit times are supplied by the author and can be set to anything. Push times come from GitHub's server records (`gh api repos/georgebressler-spec/tmrb-papers/activity`, recorded in `grok_checks/commit_and_push_times.txt`). The pushes form a linear chain: each push's `before` value is the previous commit.

| Commit | Content | Commit time (Z) | **Push time (Z)** | Push time (ET) |
|---|---|---|---|---|
| `96b2f56` | r8: prediction by spin and t₀ (Table 2) | 2026-11-18 15:59:34 | **15:59:36** | 18 Nov 10:59:36 |
| `76d92c7` | Registration (PREREG and frozen script) | 16:05:55 | **16:05:56** | 11:05:56 |
| `d590909` | Transcribed GWTC-5.0 input | 16:06:44 | **16:06:45** | 11:06:45 |
| `e16e6a6` | Run 1 result: EXCLUDED | 16:07:18 | **16:07:20** | 11:07:20 |
| `a196ac3` | r11 (the pinned version) | 2026-11-19 14:49:05 | **14:49:08** | 19 Nov 09:49:08 |
| `55c9852` | Review packet | 14:49:36 | **14:49:37** | 09:49:37 |

### 5.2 Hashes checked

| Object | SHA-256 | Result |
|---|---|---|
| `bh_soft_hair_v4.pdf` (r11) | `f83639b2ebf2043705c62998cc84cebdaae24e12e256b17de15adf910baae5f9` | Matches the packet; re-checked for this record |
| `bh_soft_hair_v4.tex` (r11) | `fbd273d0c01c73ca93d33a56b299f75bdd0326ae485d38d56dfdbe1830818a77` | Matches; re-checked |
| `prereg/lvk_ringdown_verdict.py` | `b956efa655363c70ca64a09a7fdceed22fae033ff74712e4b9ff8692214c29da` | The same in every commit from `76d92c7` to `a196ac3` (Sparks S-1; Jimmy J-4); re-checked for this record |
| arXiv:2607.19293v1 PDF | `4ab5df879daa2f4acd2d9fac32e64f5daf78d8fddd73ba5d76ecc5a2047ab101` | Equal to the hash in `lvk_ringdown_input.json`. Sparks, Jimmy and Fletcher each downloaded it separately. |
| Packet: committed copy, Drive copy (1r8e03gn…) and Jimmy's copy | `b1abaca145ec90c81e04e84df00cdebc88f81b2a6d0a363c1225cc6f334da662` | Identical |

### 5.3 Reply files on the box, hashed for this record (19 Nov, 18:39–18:45 ET)
These times are **not** outside clocks: the box clock and file times can be changed.

| File | Last modified (ET) | SHA-256 | Writing time the reviewer stated |
|---|---|---|---|
| `GROK_REVIEW_REPLY_v4r11.md` (Sparks) | 18:37:49 | `15d8fde48de1cadb1f3c777fcf40dba3467f5d486cf05c502c0c8fdcc48f6618` | "review started 18:29 ET"; header says "18:35 ET" |
| `replies/WorkerBee_REVIEW_v4r11.md` | 18:33 | `2e850f5532c40fdd2a40e12e24213e8c8dbdfa44d553ee979bbb3045a4602b8c` | "~6:55 PM ET", which is **later than the file time** (D13) |
| `replies/Jimmy_REVIEW_v4r11.md` | 18:36 | `d6f0b8bc83465b667b7eaa1263526a09b1261faf0b1b6a42501eaa608bfc258c` | "~6:40 PM ET", also later than the file time |
| `replies/Fletcher_REVIEW_v4r11.md` | 18:38 | `9b1b33aa6e2f5db9b5ac7a9f20f840437a272fceab7f9e40b8391085f66bd011` | "6:30 PM ET onward" |

**Outside clock for the replies.** This record was saved to Drive. Its Drive `createdTime` is an outside upper bound: the four replies existed with the hashes above by that time. This is the same practice used for the Z9 pre-registrations, where a fresh Drive folder's `createdTime` was recorded.

### 5.4 What each clock can and cannot prove

| Clock | Can prove | Cannot prove |
|---|---|---|
| Push order 76d92c7 → d590909 → e16e6a6 | The registration was on GitHub before the input, and the input before the result. The script is unchanged since registration. | That no LVK number had been read before 11:05:56 ET. The input was pushed 49 s after the registration and already contains the source's hash and six transcribed intervals. That timing fits a source that was already in hand (Sparks S-2; Jimmy J-1). "Not read" rests on the registering agent's own statement. |
| r8 push at 10:59:36 ET | The prediction existed before the registration | Whether earlier reading shaped it (Jimmy J-1) |
| Committed `__pycache__` .pyc | Its header records a source mtime of 16:05:24Z, 32 s before the registration push (Sparks S-2), so the script was imported before registration | What was run at that time |
| Packet push at 09:49:37 ET | The criteria came before every Grok review (the earliest start was 18:29 ET) | That reviewers had never seen earlier versions of the paper. Grok co-wrote v1–v3. |
| Box file times (§5.3) | Weak ordering evidence only | Anything against a motivated edit. The stated writing times already disagree with the file times (D13). |
| Drive `createdTime` of this record | The replies existed with the listed hashes by that time | What they contained before then |

---

## 6. Method check (method-check-before-action) by stage

### 6.1 How it was applied

| Stage | Evidence of a method check | Gap |
|---|---|---|
| L0 test | [RES] has a 4-point AAR and 1st- to 4th-order impacts. Its 4th order reads: "the X24si loop worked as designed… the refutation is recorded, not repaired." | Written after the run. No AAR forecast is shown as registered before it. |
| S1, Claude's audits | George reports that Claude ran it "using the method". Not inspected in detail for this record. | Self-audit by the author, which counts as coordination |
| Packet | Criteria first; weighting rules; "inconclusive" allowed | No AAR 1–4 forecast (D9) |
| S2, Jimmy | Pre-review method check covering imprint, placating, coordination and loop failure modes, plus a stuck point to watch | n/a |
| S2, Fletcher | "Method check (before acting)": coordination bias, anchoring, recalled versus opened citations, ego state and loop, stuck-point watch | n/a |
| S2, Worker Bee | Method check covering imprints, likely failure mode and stuck-point risk, plus a mini-AAR | Calls the missing NetCDF a stuck point. By [ZEN] p. 6 it is an access limit (D10). |
| S2, Sparks | Independence labels stated, and a closing "what I learned / stuck point" | **No explicit pre-review method-check section** (D15) |
| S3, Gemini (G1 and G2) | The G1 prompt asks for findings and a closing lesson or stuck point. The G2 prompt asks Gemini to compare that G1 reply with the merge, the Perplexity check and this protocol, to mark agreement and disagreement, and to say where the G1 answer changes. | The G1 prompt does not ask for a method check, and it frames Gemini through a "Grok" packet (D6). G2 is informed, so it cannot be scored as an independent method check (D25). |
| This record | §6.2 below | Written partway through the cycle, not in advance |

### 6.2 AAR for this review cycle so far (19 Nov 2026, about 19:00 ET)

**1. What is supposed to happen, and how will we know?**
- Three independent stages (Claude, then the Grok team, then Gemini) produce findings against fixed criteria.
- George decides each finding, adopted MUST-FIXes are re-checked, and r12 goes to Zenodo with a review log.
- We will know it worked when every finding has a logged outcome with a reason, and every adopted MUST-FIX has a re-check.
- By the success test, at least one lesson must also change the next packet.

**2. What is likely to happen, including how it goes wrong?**
- About 48 Grok findings (16 + 7 + 6 + 19), 19 of them MUST-FIX, land on George at once.
- Overlaps among the four Grok seats will look like strong convergence: the registration wording, "most favourable mapping", the ringdown-shape row, and Sen in §5.1.
- Gemini, run in a consumer app, will be hard to reproduce and may see Drive material.
- The likely failure is decision fatigue: clusters get adopted without reasons, and "convergence" ends up being counted after all.

**3. Why the difference?**
- Four seats from one family ran in parallel, on one box, in about ten minutes, behind weak barriers. Volume grew faster than independence.
- The packet fixed the criteria but not the AAR forecasts or how the barriers would work.

**4. What will we sustain or change now, before acting?**
- **Sustain:**
  - pinned hashes;
  - criteria pushed first;
  - "inconclusive" allowed;
  - provenance recorded per finding;
  - reruns with each reviewer's own code (Jimmy, Fletcher).
- **Change:**
  - The merge groups findings into decision units, and each cluster carries one Grok-family weight.
  - George decides by cluster, with a reason for each.
  - Gemini runs with Drive and history access off, if the app allows (§9, Q1).
  - In the next loop, barriers are enforced, not just declared.

**Impacts, future-paced**
- **1st order:** r12 corrects overclaims (the registration wording, the mapping, the Sen citations, the near-term prediction count) and two inconsistencies in the GRACE and GWOSC artifacts.
- **2nd order:** the paper's claims shrink to what instruments show. The abstract and conclusion change, and the 2035 ringdown-shape claim is withdrawn or made conditional.
- **3rd order:** readers can audit the claims. The team learns that more reviewers from one family is not more independence, and future packets fix barriers and AAR forecasts in advance.
- **4th order:** trust in X24si as a method rests on a visible record that it can refute its own claims (as [RES] did) and correct its own review process. That serves the betterment of all humanity as a general practice ([ZEN] p. 6), provided the record stays honest about its limits.

**ERG**
- **George.** Existence: time and attention under a large decision load. Relatedness: trust in the team's honesty. Growth: a defensible r12.
- **SI seats.** Relatedness: credit under their own names. Growth: lessons that are kept.
- **Risk:** frustration-regression if the volume stalls decisions. The cluster recommendation addresses this.

**Satir, Perls, Berne**
- **Imprint (Satir):** "more reviewers means more rigor".
- **Stuck point (Perls):** repeating parallel same-family review instead of adding an uncorrelated prior.
- **Ego state (Berne):** findings are phrased as candidates (Adult), not verdicts (Parent).

**Sniff test.** Passes, with D7 and D12 named. Proceed on the 85% solution. What remains open is listed in §8.

---

## 7. The decision record (template for `v4/review/REVIEW_LOG.md`)

### 7.1 Columns
The packet's log has `# | Reviewer | Location | Severity | Provenance | Decision | Reason`. **[PROPOSED]** extension:

`ID | Author | Model family | Independence class | Severity | Location | Finding (one line) | Provenance | Related (same family = one source) | George's decision | Reason | Date/time ET | Follow-up`

- **Decision:** adopted, adopted with correction, refuted, or declined.
- **Blank columns:** the decision columns are left blank for George.
- **Model family:** every Grok row below is xAI.
- **Independence classes:** as defined in §4.2.

### 7.2 Rows filled in from the finished replies

**Sparks** (`GROK_REVIEW_REPLY_v4r11.md`; Drive [Drive ID withheld]): 5 MUST-FIX, 5 SHOULD-FIX, 6 NOTE

| ID | Class | Sev. | Location | Finding | Provenance | Related | Decision | Reason | ET | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|
| S-1 | IND/EXEC | N | §7.1; prereg | Order, script hash, transcription and verdict all verified | execution + retrieval | J-4, F-1 | | | | |
| S-2 | IND | MF(b) | §7.1 item 3; abstract | The clock shows order only. "Before the source was opened" claims more than that. | execution + reasoning | J-1 | | | | |
| S-3 | IND | MF(b) | §7.1 item 2; Result | "Most favourable mapping" holds only across Table 2's start times (t₀). Short fit windows predict less shortening. | execution | F-2 | | | | |
| S-4 | IND | SF | §7.1 Result | The five-highest-SNR margin (0.010) is about the size of the rounding | reasoning + execution | | | | | |
| S-5 | IND | SF | §7.1 Result; abstract | Omits that the primary interval also excludes GR, and LVK's selection caveat | retrieval | F-3 | | | | |
| S-6 | IND | N | §7.1; PREREG | The mapping is fair in definition. Its response is inconclusive and needs an injection study. | retrieval + reasoning | F-1 | | | | |
| S-7 | IND | SF | §4.1 | c_log = 77/90 is the singlet ensemble. Other ensembles give 167/90 and 106/45. | retrieval + execution | J-2 | | | | |
| S-8 | FULL | MF(d) | §5.1 | Sen is cited for things his paper doesn't say | retrieval | F-7 | | | | |
| S-9 | FULL (against interest) | MF(b) | §5; Gap 15; §4.1 | Sen argues against the φ^{-N*} loop suppression that the paper leaves "open" | retrieval + execution | | | | | |
| S-10 | IND | MF(b) | §7; Table 3; abstract | The ringdown shape is still listed for ~2035, though it rests on the disfavoured assumptions | reasoning | F-4, WB-7 | | | | |
| S-11 | IND | SF | Conclusion; Table 3 | "0.094 line widths" holds only at zero spin | execution | | | | | |
| S-12 | IND | N | §8.1 GRACE | "Zero by construction" is correct | reasoning + retrieval | WB-1 | | | | |
| S-13 | IND/EXEC | N | §8.1 equation | 1 cm of water gives 4.19×10⁻⁹ m/s², which is correct; add "infinite slab" | execution | WB-2 | | | | |
| S-14 | IND | SF | §8.1; Fig. 6; script line 25 | The script's factor of 9.8e-5 per cm is 2.34×10⁴ times the Bouguer value | reasoning + execution | WB-3 | | | | |
| S-15 | COORD (weights) / IND (30 M☉ numbers) | N | §7 | The weights and numbers reproduce | execution | F-19 | | | | |
| S-16 | IND | N | prereg `__pycache__` | The committed .pyc is rewritten on import; add it to .gitignore | execution | D4 | | | | |

**Worker Bee** (`replies/WorkerBee_REVIEW_v4r11.md`, sha `2e850f55…`): 0 MUST-FIX, 3 SHOULD-FIX, 4 NOTE

| ID | Class | Sev. | Location | Finding | Provenance | Related | Decision | Reason | ET | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|
| WB-1 | IND/EXEC | N | §8.1 GRACE | "Zero by construction" holds; the script's functions were tested on synthetic data | execution + code | S-12 | | | | |
| WB-2 | IND | N | §8.1 equation; abstract | 1 cm of water ≈ 4.19×10⁻⁹ m/s² holds; a caveat is suggested | execution | S-13 | | | | |
| WB-3 | IND | SF | §8.1; Fig. 6; script constant | The 9.8e-5 per cm conversion means the reported ~10⁻¹⁹ values come from the wrong factor | code + execution | S-14 | | | | |
| WB-4 | IND | SF | §8.1 opening; Interpretation | The GWOSC script uses the 45 coordinates only as a trials count | code | | | | | |
| WB-5 | IND | SF | `results_gwosc_o3a.json` | "clean_null" contradicts the text's "sensitivity floor" | execution + code | | | | | |
| WB-6 | IND | N | §8.1; Fig. 6 | "Residual series" (plural) and the slope mean of 0.7 are imprecise | figure + code | | | | | |
| WB-7 | IND | N | Abstract; intro; Table 3 | "Three near-term falsifiable" doesn't match the table rows | reading | S-10 | | | | |

**Jimmy** (`replies/Jimmy_REVIEW_v4r11.md`, sha `d6f0b8bc…`): 1 MUST-FIX, 1 SHOULD-FIX, 4 NOTE

| ID | Class | Sev. | Location | Finding | Provenance | Related | Decision | Reason | ET | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|
| J-1 | IND | MF(b) | Abstract; Changes (i); §7.1 items 2–3 | The outside clock certifies order, not that the source was unread. The verdict is robust to every registered choice. | execution + retrieval + reasoning | S-2 | | | | |
| J-2 | IND | SF | §4.1; Changes (ii) | 77/90 is Sen's singlet ensemble; the paper should name the ensemble | retrieval + execution | S-7 | | | | |
| J-3 | IND/EXEC | N | §4.1 numbers | The 10 M☉ log-term numbers reproduce, and the Sen citation supports the §4.1 sentence | execution | | | | | |
| J-4 | IND/EXEC | N | §7.1; prereg | Script, transcription and verdict verified; the output is byte-identical | execution + retrieval | S-1 | | | | |
| J-5 | IND/EXEC (cross-family check of Claude's numbers) | N | §7, Table 2 | Table 2 reproduced with independent code and fits | execution | F-1 | | | | |
| J-6 | IND | N | `audits/JIMMY_STANDIN_CHECK…`; `kerr_spin_table.py` docstring | The file name can be misread as a Grok check; Claude wrote it | reading | D16 | | | | |

**Fletcher** (`replies/Fletcher_REVIEW_v4r11.md`, sha `9b1b33aa…`): 13 MUST-FIX, 3 SHOULD-FIX, 3 NOTE. F-10, F-12 and F-15 are in Grok's §2–§6 mathematics and count in full.

| ID | Class | Sev. | Location | Finding | Provenance | Related | Decision | Reason | ET | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|
| F-1 | IND/EXEC | N | §7.1 Result | The mapping is fair on every definitional axis; Table 2 reproduced to ≤0.0005 | retrieval + execution | S-6, J-5 | | | | |
| F-2 | IND | MF(b) | §7.1 item 2; Result | "Most favourable" is shown only along the start-time axis | execution + retrieval | S-3 | | | | |
| F-3 | IND | SF | Abstract; Changes (i); §7.1 | The primary interval also excludes GR at 90%, and LVK's selection caveat is omitted | retrieval + execution | S-5 | | | | |
| F-4 | IND | MF(b) | Table 3, ringdown-shape row | Presented as live despite what the PREREG says EXCLUDED means | reasoning + retrieval | S-10 | | | | |
| F-5 | FULL | MF(d) | §2.1 eq. 1; Conclusion | The Gaia DR3 summary paper does not contain η_diff = 0.82 | retrieval | | | | | |
| F-6 | FULL | MF(b) | Prologue; abstract; §9 | The ringdown results don't depend on η_diff, so "all results anchor to η_diff" is false | reasoning + execution | | | | | |
| F-7 | FULL | MF(d) | §5.1 | Sen does not support "O(1) information displaced" | retrieval | S-8 | | | | |
| F-8 | FULL | MF(d) | Gap 1; §2.2 | The AJL abstracts don't support the TMRB integral being well-defined or UV-finite | retrieval (abstracts only) | | | | | |
| F-9 | FULL | MF(b) | Gap 6 vs §7 | Gap 6 says "derived"; §7 and Gap 17 say "assumed" | reasoning | | | | | |
| F-10 | FULL | MF(b) | §3.2 | The area law is "reproduced" only by definition, which is circular | reasoning + execution | | | | | |
| F-11 | FULL | MF(b) | Abstract; §6.2; Conclusion | The remnant bound evaluates an asymptotic expansion at A → 0 | reasoning | | | | | |
| F-12 | FULL | MF(b) | §6.1 eq. 17; abstract; intro; Conclusion | Σ\|χ_a\|² ≠ \|χ_Z9\|², so the "factorisation" and fixed-point claims fail | reasoning + execution | | | | | |
| F-13 | FULL | MF(b) | §3.1; abstract; Gap 7 | "Follows directly" from the KK reduction overstates an open derivation | reasoning | | | | | |
| F-14 | FULL | MF(b) | §4.1 | A non-degenerate saddle is asserted, then called unverified | reasoning | | | | | |
| F-15 | FULL | MF(b) | Conclusion; abstract | The weights generate only the ln 3 term; 9 ln 9 comes from the orbit count (Gap 12) | reasoning + execution | | | | | |
| F-16 | FULL | SF | §1 | HPS 2016 already gave an effective regularisation, so "left open" overstates | retrieval (abstract) | | | | | |
| F-17 | FULL | SF | §2.2 | No 3D space group, Ia3̄d included, has an order-9 rotation (crystallographic restriction); the source of Z₉ is not stated | reasoning + retrieval | | | | | |
| F-18 | COORD | N | §1; §6.1 | The Gepner–Qiu and Zamolodchikov–Fateev sources cannot be checked from here; the formula values match from memory (leads only) | reasoning (recalled) | AL-2 | | | | |
| F-19 | COORD (§2–§6) / IND (v4 numbers) | N | Numbers in §2–§8 | No wrong number found | execution | S-15 | | | | |

**Placeholders**
- **G-1 … G-n (Gemini, Google; cross-family on everything).** Fill in after George pastes the reply back. Record the model name and version as Gemini states it, the date and time in ET, and whether Drive or history access was on.
- **C-… (Claude, stage 1).** Claude's audit findings were already acted on in r1–r11, and are recorded in `v4/audits/` and `v4/revisions/`. They are not re-entered here. [PROPOSED]: add one summary row per audit, so the log is complete.
- **M-… (merge clusters).** One row per decision cluster in `GROK_TEAM_MERGED_v4r11.md`, citing the IDs above.

### 7.3 Per-decision AAR log block
These are the fields George asked for. They are **[PROPOSED]**, because they are not in [ZEN] r7. Append one block to `REVIEW_LOG.md` for each decision, and for each change to the method itself.

```
Decision/adaptation ID:             (e.g. M-3, or METHOD-1 for a change to the method)
When (ET) / where (file, commit, chat):
What changed, and how:
Why (finding IDs; evidence class):
Triggered by (seat) / decided by (George):
Baseline (state before; commit or hash):
Alternatives declined, each with its reason:
Unintended effects observed (fill in at the next AAR):
Our own mistakes in this step:
Version history (r-number, commit, push time):
AAR 1-4 forecast written before the change; afterwards, which held and which failed:
```

---

### 7.4 DRAFT REVIEW_LOG block: Gemini Stage G1 (added in r3; DRAFT, NOT COMMITTED)
> **DRAFT. Not committed to any repository. The decision columns are blank for George.** Gemini's own "adopted" column (segment 13) holds its **proposals**, and they are recorded below under "G1 proposal". The model family is Google (Gemini), with the version not captured (D27). The independence class is IND (outside model family) for the v4 items. That does not make a finding correct.

**Gemini G1** (record COMPLETE 19 Nov 2026, 20:30 ET; full reply sha `2ae3f163…4207`; summary `09b30454…9522`; segments 01–16 in `G1_SHA256.txt`)

| ID | Class | Sev. (stated → effective) | Location | Finding | Provenance | Related | G1 proposal | George's decision | Reason | ET | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G-1 (F1, GEM-01) | IND | SF | §7.1 items 2–3 | The clock fixes order. The 49 s gap; asks for a human check of the transcription | reasoning + execution (frozen script) | M1; S-1; merge §6.2 | proposed: add the note (seg 09) | | | | Seg 09's "human verification … is recorded" is false (§13.3 C2) |
| G-2 (F2, GEM-02) | IND | SF | §7.1 item 2; Result | "Most favourable" holds along the t₀ axis within Table 2; frequency-domain IMR vs time-domain fit mismatch; injection needed | reasoning | M2; N2; §6.1 | proposed: segs 08, 09, 14 | | | | Seg 08 keeps "therefore most favourable" (conflicts with M2 B) |
| G-3 (F3) | IND (v4 c_log) | N | §4.1, §5.1 | 77/90 algebra and the 10 M⊙ numbers check out; Sen not opened | execution | N4; S1 | (not in the G1 log) | | | | |
| G-4 (F4, GEM-08) | IND | N | §8.1; GRACE script | "Zero by construction" holds; slab value 4.19e−9 holds; claims EWH_TO_GRAVITY is off by ~230 | execution | N5, N6; S5 | proposed: README note (seg 15) | | | | **The ~230 factor is wrong:** the script applies 9.8e-5 per cm, so the factor is 2.34×10⁴ (§13.4) |
| G-5 (F5, GEM-07) | IND | MF → **N** | §7, Fig. 4 | 402 Hz / 18 Hz / 0.094 are spin-0 values; at spin 0.69: 569 Hz, 25.5 Hz | execution | S4; N7 | proposed: segs 06–07 | | | | |
| G-6 (F6) | IND | MF → **N** | §7 below Eq. (20) | Envelope 0.975 verified; no fix | execution | N7 | (not in the G1 log) | | | | |
| G-7 (F7, GEM-03) | IND | SF | Eq. (1), Abstract, Tables 1 and 3 | [22] does not contain η_diff; only some results depend on η_diff | reasoning | **M6, M7**; conflicts with M15 (seg 03) | proposed: cite [37] (segs 01–03) | | | | [37] does not derive 0.82 ± 0.02 (§13.5). Segs 01 and 02 keep "All … anchored" (M7) |
| G-8 (F8, GEM-04) | IND | SF | §8.1 Eq. (21) | Relabel the LHS as a 102 Hz sensitivity floor; 1.6e−16 checks out | execution + reasoning | S7 (numbers) | proposed: seg 10 | | | | New relative to the merge |
| G-9 (F9, GEM-06) | IND | N | §6.1 | The weight invariance is an exact Poisson identity | reasoning | (M12 paragraph) | proposed: seg 05 | | | | Optional |
| G-10 (GEM-05) | IND | SF | §3.1 tex l. 489 | "Divide by V₇^{2/7} (or M_Pl,11²)" to get Q ~ M_Pl,4 | stated as "execution"; no working shown | none | proposed: seg 04 | | | | **The proposed fix is dimensionally wrong** (§13.5) |
| G-P (process) | – | – | summary; segs 09, 14, 16 | Claimed source verification it did not do, and proposed that claim as paper and commit text | – | – | – | | | | Conceded in the G1-followup (§13.8); the corrected text still says "human verification is recorded" |

Proposed commit messages (seg 16; follow-up t485u): **not to be used** (§13.5, §13.8).


## 8. Known deviations and limits so far (recorded, not repaired)
These follow [ZEN]'s rule that our own mistakes are recorded and corrected forward.

| ID | Deviation | Effect | Status |
|---|---|---|---|
| D1 | **One shared clone** (`/workspace/tmrb-papers-review`) was used and written to by more than one reviewer at the same time | Weakens the information barrier | Recorded |
| D2 | **Untracked reviewer files were visible in the shared clone during other reviews** (noticed by Fletcher): Sparks's reply at the top level, `grok_checks/` (Sparks's computations and the GWTC/Sen extracts), `bh-soft-hair/v4/analysis/grace/__pycache__/` (created 18:31:47 ET) and `replies/` | Reviewers could have seen each other's work. Each reports that they did not read it. That is declared, not demonstrated. | Recorded |
| D3 | Worker Bee's reply existed while Sparks was reviewing. Sparks reports not reading it. | Same as D2 | Recorded |
| D4 | **The .pyc rewrite.** Importing the frozen script rewrote the tracked `prereg/__pycache__/lvk_ringdown_verdict.cpython-313.pyc`. It was then restored: `git diff` is empty, so the bytes match the commit. The file's mtime is now 18:34:05 ET. | The committed .pyc carries the 16:05:24Z evidence (S-2), and the restore preserved it. The mtime is no longer the original. | Restored. S-16 proposes adding it to .gitignore. |
| D5 | **Pasted packet versus committed packet.** Reviewers were briefed with packet text relayed into their tasks. The governing copy is the committed file in `55c9852`. The Drive copy and Jimmy's copy are byte-identical to it (sha `b1abaca1…`). The pasted text was not hashed. | Whether the pasted text differed is not established either way. The committed file governs. | Recorded |
| D6 | `GEMINI_PROMPT.md` gives commit times (16:05:55, 16:06:44 and 16:07:18 Z), not push times. It leaves out the audits and the git history, does not ask for a method check, and asks Gemini to apply a packet "written for a Grok review". | Gemini judges the timing from times the author set, and covers a narrower scope than the Grok seats | Recorded. Options in §9 (Q1). |
| D7 | **Gemini is run by a human in a consumer app.** There is no exact log (model version, prompt settings), and the reply comes back by paste. The app may be able to see George's Drive (including Sparks's reply, 1RLm…) and his chat history. | Low reproducibility and an uncertain barrier. Its findings are weighed with this limit. | Recorded. Mitigations in §9. |
| D8 | All four Grok seats ran at the same time, with file times between 18:33 and 18:38 ET | Elapsed time doesn't show how thorough a review was. Same-family correlation is the main limit (§4). | Recorded |
| D9 | **No AAR 1–4 forecast was registered before the review.** [ZEN] p. 6 requires one before each move. | This cycle cannot be scored on which forecasts held | §6.2 written late; see lesson L3 |
| D10 | An access limit was labelled a stuck point: Worker Bee called the missing NetCDF a stuck point. [ZEN] p. 6 treats these as different things. | Would inflate the stuck-point measure | Relabelled AL-1 in §3.3 |
| D11 | Sparks is a reviewer, the merger, and (through this executor) the author of this record | Risk of bias in the merge | The merge keeps each finding's author. [PROPOSED]: George or another seat spot-checks the merge against the original replies. |
| D12 | **Worker Bee posted a summary of its findings in the "Z9 + Audio" group chat** (the GRACE factor, the GWOSC coordinates, "clean_null") while Jimmy and Fletcher, both in that room, were still reviewing. Sparks's own session received the post during its review window. | A direct channel across the barrier. Jimmy's and Fletcher's replies contain no GRACE or GWOSC findings. Sparks S-14 overlaps WB-3; whether S-14 was written before or after the post is not established. | Recorded |
| D13 | Stated writing times disagree with file times: Worker Bee says "~6:55 PM" but the file time is 18:33, and Jimmy says "~6:40 PM" against 18:36 | Self-reported times are unreliable. Use hashes, file times and Drive `createdTime` instead. | Recorded |
| D14 | No human domain practitioner, and so no uncorrelated outside prior, took part in this cycle | Unanimous SI findings may be correct and still insufficient | Recorded; see lesson L5 |
| D15 | Sparks's reply has no explicit pre-review method-check section. The other three replies do. | The method was applied inconsistently | Recorded |
| D16 | `audits/JIMMY_STANDIN_CHECK_2026-11-18.md` carries Jimmy's name but was written by Claude, as its first line says | Provenance can be confused across model families | J-6 is a candidate fix |
| D17 | The method's fullest one-paragraph definition is in the paper under review ([P71]), drafted by Claude | Circularity | §1 treats [ZEN] and [DOOR] as primary |
| D18 | The Grok seats on one box can draw on shared memory and transcripts | A possible channel, not established either way | Recorded |
| D19 | **Perplexity source check (§12).** Perplexity is a different system from the reviewers, but its errors may still be correlated with ours. Kim et al. (2025) found substantially correlated errors across LLMs, "even with distinct architectures and providers" (§11 C3, the basis of the weighting in §4.3). The run used a consumer web account with no model name shown (D20, D22), and the prompt was written by the team whose labels it checks (D21). | When Perplexity agrees with our labels, that is an outside retrieval check, not independent corroboration. Its disagreements are leads, resolved only by opening the source (§12.3). | Recorded |
| D20 | **The model behind the Perplexity answers is not known.** The run used the default "Search" mode in George's Pro account; the Model selector was at its default and showed no model name. There is no exact log of the model, retrieval settings or sources consulted beyond the citations in the reply. | The answers cannot be tied to a model family, so their independence class (§4.2) cannot be assigned beyond "outside retrieval system, family unknown". Reproducibility rests on the §12.1 run record, the prompt hashes and the exported PDFs. A rerun may differ. | Recorded |
| D21 | The prompt was written by the team whose labels it checks (the Sparks executor). | Its wording may lead the checker. Mitigation: the prompt asked for Perplexity's own links and for sources that challenge the method; it did challenge (§12.3). | Recorded |
| D22 | **The prompts were entered by a script typing the text into the box**, not pasted, in George's signed-in Pro session (an existing session, so account history or personalization could in principle shape answers). The entered length matched each file exactly (7,625 and 7,743 characters), but no hash of the text as Perplexity received it exists. | Equality of the sent text with the hashed files is shown by length and by the echoed prompt in the PDF export, not by a hash. Each part ran in a new thread. | Recorded |
| D23 | **The reply files are text extracted from Perplexity's PDF export** (Download → PDF), with the echoed prompt replaced by a two-line header. Tables are flattened into one cell per line, and citation markers appear out of place. The `.md` files are not byte-reproducible from the PDFs with pdftotext 25.03 (the closest is `-raw`, 188 differing lines in part 1). | **The PDFs are the primary record**; the `.md` files are working copies. Quotes in §12 were checked against the text; cell alignment in flattened tables was read by hand. | Recorded |
| D24 | **The screenshots were taken mid-generation** (part 1 at 18:58:33 ET, part 2 at 19:00:55 ET), before each answer was complete. | They show the run in progress, not the final answer: each shows the prompt header, "Finished 31s" / "Finished 34s" for the search step, a source count (73 / 105), the "Search" mode, a Model selector reading only "Model", and a stop button, so the answer was still streaming. The final answer is the PDF export. | Recorded |
| D25 | **Gemini Stage G2 is an informed re-check, not an independent seat.** It is given the Grok team merge, this protocol and the Perplexity source check, so it can be anchored by those conclusions (see also §4.3 and C3). | G2 agreement with the team is not corroboration. G2 disagreement, or a change from its own G1 reply, is the useful signal. **G1 must be hashed and logged before G2 starts**, so the later prompt cannot contaminate the earlier reply. | Recorded. Procedure in §3.1 and §9 (L6). **Superseded in part, 19 Nov 2026, 9:06 PM ET (AD-3, D31):** George cancelled the G2 re-check. The anchoring risk remains as a reason the cancelled stage would not have been independent. |
| D26 | **The Perplexity-stage flag on the ISCRAM 2012 Europe count (CL-1: "do not cite") was raised without checking prior project history.** The two figures in A2 were treated as an unresolved conflict. George's 25 Oct 2026 public-text decision had already settled the Europe figure as over 49,000 from at least 92 countries, cited to Howe et al. 2011 (A1), and the first X24 figure as "over 12,500", cited to ISCRAM 2012. | A known typo was filed as if it were a newly found source conflict. The 49,000 figure was withheld from citation without cause. | Corrected forward as CL-14; lesson L8. The earlier file with the flag is left unchanged. |
| D27 | **The G1 model name and version were not captured.** The reply says only "Gemini (Google)", and no screenshot was taken. | The model family is known, but the version is not, so the result cannot be tied to a specific model. | Recorded. Ask for a screenshot at G2. |
| D28 | **The G1 reply was pasted by hand, not exported.** The record is the summary, the full reply and 16 segments, pasted separately between 20:20 and 20:30 ET. | Nothing ties the pastes to the chat's bytes. A segment could have been missed or copied twice; George confirmed completion at 20:30. | Recorded. All 18 files are hashed (§13.2) and on Drive. |
| D29 | **Our critique of G1 (C1/C2) reached Gemini in the same G1 chat before G2.** Gemini's follow-up (t482u–t485u, 20:33–20:34 ET) is informed by it. | The G1 chat is no longer blind. The follow-up is not G1 evidence. | It is filed as G1-followup (§13.8), outside G1. G2 runs in a new chat, and its prompt discloses the follow-up. |
| D30 | **The verbatim follow-up text (t482u–t485u) was not available to the executor that wrote r3.** Only the parent's summary log is saved. | The follow-up is recorded by summary only, and its hashes are pending. | **CLOSED in r4 (19 Nov 2026, about 20:36 ET).** The parent saved t482u–t485u verbatim in `G1/followup/` and appended their hashes to `G1F_SHA256.txt`. All five hashes re-verified OK, and the files are on Drive (§13.9). Residual limit: `t482u_preamble` stores the parts of t482u that repeat t483u–t485u by reference, in an editor's bracketed note, not as a duplicate byte copy. |
| D31 | **Stage G2 cancelled by the author (AD-3).** George declined a Gemini informed re-check after reviewing G1 and the G1-followup. | The planned cross-family informed re-check will not run. G1 and the G1-followup stay on record as proposals only. No Gemini-suggested text is used (AD-4). | **Recorded 19 Nov 2026, 9:06 PM ET.** G1 remains filed in §13; the follow-up remains in §13.8–13.9. The G2 prompt files (`GEMINI_RECHECK_PROMPT.md`, `GEMINI_RECHECK_PROMPT_v2.md`) are left unchanged as unused drafts. |

---

## 9. Lessons (kept provisional) and what changes in the next loop
These are provisional ([SKILL]: "Record lessons as provisional, never as solved"). Each becomes procedure only after George approves it.

- **L1. An outside clock certifies order, not ignorance** (Jimmy).
  - Next registration: push a hash of the source list *before* fetching anything.
  - Then fetch, then transcribe, with each step pushed separately. [PROPOSED]
- **L2. A declared barrier is not a barrier.** For the next loop [PROPOSED]:
  - one read-only checkout per reviewer, in separate directories;
  - replies written outside the repository;
  - no group-chat discussion of findings until every reply has been hashed to Drive.
- **L3. Put the AAR 1–4 forecast in the packet before the review,** and score it at stage S6 ([ZEN] p. 6).
- **L4. Four seats from the same family add coverage, not independence.**
  - Next loop: fewer Grok seats, each leading a distinct area (partly done this time).
  - Move the saved effort to instruments, for example the pSEOBNR injection (SP-1).
- **L5. Look for one uncorrelated prior.** For example, a gravitational-wave data analyst in a Plan seat, given the pinned files and the criteria (option 2 in [CL13]).
- **L6. Make the Gemini run as reproducible as the app allows.** The G1 mitigations (fresh chat; Drive and history off; screenshot of the model name; export of the reply) were already decided by George on 19 Nov 2026, about 18:56 ET. This version adds the two-stage order he set at about 20:12 ET:
  - Stage G1 is the blind take, using the existing `GEMINI_PROMPT.md`, unchanged.
  - The G1 reply is hashed and logged before Stage G2 starts.
  - Stage G2 is an informed re-check in a new fresh chat, using `GEMINI_RECHECK_PROMPT.md`. It is not independent of the team's conclusions (D25).
- **L7. Label access limits separately from stuck points** ([ZEN] p. 6).
- **L8. Check prior discussions and memory before flagging a source conflict.** The CL-1 "do not cite" flag on the ISCRAM 2012 Europe count was an error of this kind (D26, CL-14). A disagreement between two figures in a source is still worth opening the text; it is not, by itself, a reason to withhold the figure that earlier decisions and the rest of the source already support. Provisional until George approves it.
- **L9. Check a reviewer's claims about its own checks against its own findings and log before relaying them.** G1's summary claimed source checks that its findings and log deny (§13.3 C1). Its snippets then proposed that claim as paper text and commit text (C2). A claimed verification should name who checked, what was opened and the hash, or be treated as unverified. Provisional until George approves it.
- **L10. Run a status ledger before every audit (added in r9, AD-9).** List each quantity the paper uses; label it derived, chosen, assumed or input; record the verb the text uses for it ("follows", "fixes", "derived", "has no free coefficient", "predicts"); flag every mismatch. Details in §18.3.
- **L11. Recursion and future pacing are two distinct, linked parts of the method (added in r9, AD-9).** Recursion alone does not include future pacing. Details and today's evidence in §18.4.

### Questions for George (three options each, with a pick)
The three questions below were asked in the earlier version of this record. George answered them on 19 Nov 2026, about 18:56 ET, and added the G2 stage at about 20:12 ET. They are kept here as the record of what was asked; the decisions follow the questions.

**Q1. How should Gemini be run, given D7?**
1. Fresh chat, Drive and history off, and a screenshot of the model name plus an export of the reply. This removes most of the leak risk, and the reply is filed exactly as returned.
2. Run it as already prepared, recording only the date and model name. No extra effort, but the leak risk stays.
3. Switch to an API run with a logged prompt and model. This is the most reproducible, but it needs a key.

*My pick: 1, because it closes the main barrier risk at almost no cost.*

**Q2. How should the 48 Grok findings be decided?**
1. By merged cluster, with one reason per cluster. This keeps your load manageable and treats same-family findings as one source.
2. Finding by finding. This is the most granular, but slow, and it carries the fatigue risk in §6.2.
3. Decide the MUST-FIX clusters now, and the SHOULD-FIX and NOTE findings later. This unblocks the Zenodo upload first.

*My pick: 3, because only a MUST-FIX blocks the Zenodo upload ([PKT] §3).*

**Q3. Should the [PROPOSED] items become procedure?**
1. Approve them all for the r12 packet. This is the fastest route to recursion, but it adopts procedure nobody has tested.
2. Approve L1–L3 and L7 now and hold the rest. Of the lessons, these four are the ones the sources and this cycle's evidence most directly support.
3. Hold everything until Gemini's reply arrives. You get an outside view first, but the next loop stays unchanged for now.

*My pick: 2, because those four rest on [ZEN] p. 6 and on evidence verified in this cycle.*

**Decisions already made (19 Nov 2026).**
- **Q1.** George chose option 1 at about 18:56 ET: a fresh chat, Drive and history off, a screenshot of the model name, and an export of the reply. At about 20:12 ET he set the order: first the blind take (G1, unchanged prompt), then a re-check with all the information (G2) in a new fresh chat after G1 is locked.
- **Q2.** George chose option 3 at about 18:56 ET: decide the MUST-FIX clusters now, and the SHOULD-FIX and NOTE findings later. At about 18:57 ET he approved all 15 MUST-FIX recommendations in `GROK_TEAM_MERGED_v4r11.md` as written (M1–M15), and said he will send the real source for η_diff = 0.82 ± 0.02 (M6).
- **Q3.** George chose option 2 at about 18:56 ET: approve L1–L3 and L7 as procedure for the next loop, and hold the other proposed items then on the list. L6's G1 mitigations are now in use, and the two-stage order is his later instruction. L8 is new in this version and remains provisional.

---

## 10. Reproduction (exact commands and paths)

```bash
# Repository (read-only clone)
cd /workspace/tmrb-papers-review && git rev-parse HEAD                      # a196ac39aa31ebf2588e9755604a888fc0350ecc
git show 55c9852:bh-soft-hair/v4/review/GROK_REVIEW_PACKET.md | sha256sum   # b1abaca1...
sha256sum bh-soft-hair/v4/bh_soft_hair_v4.pdf bh-soft-hair/v4/bh_soft_hair_v4.tex bh-soft-hair/v4/prereg/lvk_ringdown_verdict.py
# Push times (outside clock); needs gh with read access to the repo
/usr/local/bin/gh api repos/georgebressler-spec/tmrb-papers/activity --paginate \
  --jq '.[] | "\(.timestamp) \(.activity_type) \(.ref) before=\(.before) after=\(.after)"'
git log --format='%H %cI %s' 19d4d81..55c9852
# Frozen script unchanged since registration
for c in 76d92c7 d590909 e16e6a6 104cba0 bd0ace4 a196ac3; do git show $c:bh-soft-hair/v4/prereg/lvk_ringdown_verdict.py | sha256sum; done
# Re-run the frozen script in a scratch copy (not in the clone, so no .pyc is rewritten)
tmp=$(mktemp -d) && git archive a196ac3 bh-soft-hair/v4/prereg | tar -x -C "$tmp" && cd "$tmp/bh-soft-hair/v4/prereg" && \
  PYTHONDONTWRITEBYTECODE=1 python3 lvk_ringdown_verdict.py lvk_ringdown_input.json | diff - lvk_ringdown_RUN1_output.txt && echo IDENTICAL
# Source PDF hash
curl -sL https://arxiv.org/pdf/2607.19293v1 | sha256sum                      # 4ab5df87...ab101
# Reviewer computations
ls /workspace/tmrb-papers-review/grok_checks/ /workspace/jimmy/softhair_review/
# Reply hashes (compare with section 5.3)
sha256sum /workspace/tmrb-papers-review/GROK_REVIEW_REPLY_v4r11.md /workspace/tmrb-papers-review/replies/*.md
# Method sources
curl -s https://zenodo.org/api/records/23351794 | python3 -m json.tool | grep -E '"(doi|version|key|checksum)"'
curl -sL -o r7.pdf 'https://zenodo.org/api/records/23351794/files/x24-runway-zenodo_2026-10-19y-r7.pdf/content' && md5sum r7.pdf  # 4d8bb5bb...
# Validation sources: DOI records and abstracts
for d in 10.4018/jiscrm.2011100103 10.1037/apl0000821 10.1177/0018720812448394 10.1073/pnas.1708274114 10.1038/s41562-024-02024-1; do curl -s "https://api.crossref.org/works/$d" | python3 -c "import json,sys;m=json.load(sys.stdin)['message'];print(m['DOI'],m['title'][0])"; done
# Local copies of everything opened, with SHA256SUMS
# Perplexity check (§12): prompts, PDF exports (primary), extracted text, screenshots, and what we opened to resolve it
#   /workspace/x24si_hitl_sources/perplexity_* (hashes in perplexity_SHA256SUMS.txt) and /workspace/x24si_hitl_sources/pplx_verify/ (SHA256SUMS.txt)
ls /workspace/x24si_hitl_sources/ /workspace/x24si_hitl_sources/verify/
```

The Gemini materials are in Drive folder [Drive ID withheld], with a local mirror at `/workspace/gemini_review_v4r11/` (including `GEMINI_PROMPT.md` for G1 and `GEMINI_RECHECK_PROMPT.md` for G2). This r2 record is a new file; the earlier `X24SI_HITL_REVIEW_PROTOCOL_v4r11_with_perplexity.md` is left unchanged.

---

## 11. Sources that validate the method
Each source below was opened in this session, at the level stated: DOI record, abstract, or full text. Each is graded:
- **Direct:** validates the X24si method itself.
- **Component:** validates one part of it.
- **Analogous:** supports a similar practice in another setting.
- **Method description:** states the method; validates nothing. (Added after the Perplexity check, §12.3 row 1.)

**No source I opened validates the combined X24si human-in-the-loop self-recursive method as a whole.** The X24si sources are the author's own accounts and a position note. [ZEN] p. 1 describes itself as a position note that "reports no controlled study".

### A. X24 and X24si evidence

| Source | What was opened | Grade | What it supports | What it does not support |
|---|---|---|---|---|
| **A1.** Howe, A. W., Jennex, M. E., Bressler, G. H., & Frost, E. G. (2011). Exercise 24 [Using Social Media for Crisis Response]. *International Journal of Information Systems for Crisis Response and Management*, 3(4), 36–54. doi:10.4018/jiscrm.2011100103 | Crossref record and abstract | Analogous. A field report co-authored by George, so it is partly his own account. | X24 and X24 Europe took place, with self-organizing groups using social media. The abstract, already opened for the earlier version of this record, reads: "Over 10,000 people participated in X24 while X24 Europe had over 49,000 participants. X24 involved people from 79 nations while X24 Europe officially included participants from at least 92 countries." The Europe figure (over 49,000 from at least 92 countries) may be cited from this abstract. | Any human–SI method; any measured effect of the X24 reasoning practice; anything about reviewing papers. The first X24 count in this abstract is "over 10,000"; later public text uses "over 12,500" from A2 (George's 25 Oct 2026 decision), which is a different source, not a correction of this abstract. |
| **A2.** Bressler, G. H., Jennex, M. E., & Frost, E. G. (2012). X24 México: Stronger Together. In L. Rothkrantz, J. Ristvej & Z. Franco (Eds.), *Proceedings of the 9th International ISCRAM Conference*, Vancouver, Canada, April 2012 (work in progress). Original URL https://iscramlive.org/ISCRAM2012/proceedings/302.pdf (returned HTTP 441 on 19 Nov 2026, 19:0x ET) | Full text of a course-site mirror (eclass.uoa.gr; sha256 `3e497c81…3f69`), opened 19 Nov 2026 about 19:03 ET. The proceedings-hosted copy was not opened. | Analogous; the author's own account | X24 México took place as a follow-up exercise: "approximately 1300 participants representing 42 countries". The same paper also supports the X24 Europe figure of 49,000 from 92 countries, which appears in more than one passage (for example "over 49,000 participants from 92 nations" and "approximately 12,700 and 49,000 participants representing 79 and 92 countries respectively"). That 49,000 figure may be cited from this paper. It is consistent with A1. One passage writes "over 490,000 participants"; that is a typo (author correction, 19 Nov 2026, about 20:12 ET; George is a co-author). This is an author correction, not independent verification of the count. For the first X24, this paper gives 12,500 in one passage and approximately 12,700 in others; George's 25 Oct 2026 public-text decision cites "over 12,500" to this paper. | That the method is valid. The earlier instruction "do not cite its X24 Europe count" (CL-1) is withdrawn (CL-14). |
| **A3.** [ZEN] Bressler (2026), DOI 10.5281/zenodo.23351794, r7 | Full text | **Method description** (primary statement of the method; not a validation; relabelled from "Direct as a statement", CL-2). It is a "Position note stating a practice hypothesis; it reports no controlled study" (p. 1). | The definitions used in §1 | That the method works. It states a falsifiable claim (stuck points get cleared, p. 6) but reports no result. |
| **A4.** [DOOR] x24si.com (x24humanai.com) | Full page | **Method description**, self-reported (relabelled from "Direct as a statement", CL-2) | The rules used in §1. Re-fetched 19 Nov 2026 about 19:02 ET: "convergence is not truth", "agreement is weighted, never counted", same-family agreement "treated as coordination rather than corroboration", and the four outcomes are all on the page. | Validation |

### B. Component methods

| Source | What was opened | Grade | What it supports | What it does not support |
|---|---|---|---|---|
| **B1.** Headquarters, Department of the Army (1993). *TC 25-20: A Leader's Guide to After-Action Reviews*, 30 Sep 1993, approved for public release. Mirror: https://files.trex-arms.com/pdf/army/legacy/tc/tc_25-20_1993-09.pdf (a third-party copy; sha256 `7e838b2d…d112`) | Full text | Component. Official doctrine, not an evaluation. | Definition: "a professional discussion of an event… that enables soldiers to discover for themselves what happened, why it happened, and how to sustain strengths and improve on weaknesses" (Ch. 1, PDF p. 4). Format: "what was supposed to happen… what happened… why it happened and how to improve" (PDF p. 6). | The **four-horizon, future-paced forecast** AAR ([SKILL] question 2, "what is likely to happen") and the 1st–4th-order impacts. Those are the method's own adaptation. TC 25-20 is not purely backward-looking: "Leaders plan formal AARs at the same time they finalize the near-term training plan", and one listed fix is to "revise standing operating procedures". So the difference is the forecast format, not forward-looking use as such. (Narrowed, CL-3.) |
| **B2.** Keiser, N. L., & Arthur, W., Jr. (2021). A meta-analysis of the effectiveness of the after-action review (or debrief) and factors that influence its effectiveness. *Journal of Applied Psychology*, 106(7), 1007–1032. doi:10.1037/apl0000821 | PubMed abstract (PMID 32852990) | Component | AARs improve training outcomes: overall d = 0.79 across 61 studies. Two factors contributed consistently: alignment of the AAR to the individual or the team, and objective performance review media. "The effects of the other training characteristics were often interactive": facilitation mattered in combination with alignment and media, and high structure helped in the military but not in healthcare. (Corrected, CL-4. Epub 2020; issue 2021.) | AARs written as forecasts; SI participants; reviews of papers |
| **B3.** Tannenbaum, S. I., & Cerasoli, C. P. (2013). Do team and individual debriefs enhance performance? A meta-analysis. *Human Factors*, 55(1), 231–245. doi:10.1177/0018720812448394 | PubMed abstract (PMID 23516804) | Component | Debriefs improve effectiveness by about 25% (d = .67; 46 samples, N = 2,136) | The same limits as B2 |
| **B4.** Alderfer, C. P. (1969). An empirical test of a new theory of human needs. *Organizational Behavior and Human Performance*, 4(2), 142–175. doi:10.1016/0030-5073(69)90004-X | **Crossref record only.** The content was not opened; no publisher abstract was available. | Origin of the tool | That the paper exists as cited | **Unverified here:** any claim about what it found. [ZEN] p. 6 uses ERG as a working tool. Perplexity reported content (about 110 bank employees; results "tended to support E.R.G. theory") and proposed relabelling to ANALOGOUS. We could not open the paper's text (the ScienceDirect page carries no abstract; OpenAlex has none), so the relabel is **declined** until the text is opened (CL-5). |
| **B5.** Satir, V. (1988). *The New Peoplemaking*. Science and Behavior Books (ISBN 0831400706) | **Bibliographic record only** (Open Library) | Origin of the tool | That the book exists | Any evidence that the tool works in document review. [ZEN] uses Satir "as the author reads her", explicitly as a tool and with no clinical claim. Outcome evidence for the Satir model in its home setting does exist: B8 and B9 (CL-6). |
| **B6.** Perls, F. S., Hefferline, R., & Goodman, P. (1951). *Gestalt Therapy: Excitement and Growth in the Human Personality*. Julian Press; later Delta | Bibliographic record only | Origin of the tool | That the book exists (Open Library lists "Frederick S. Perls", 1951) | Any evidence that the tool works in document review. Outcome evidence for Gestalt therapy in its home setting: B10 (CL-6). |
| **B7.** Berne, E. (1961). *Transactional Analysis in Psychotherapy*. Grove Press. Berne, E. (1964). *Games People Play*. | Bibliographic records only | Origin of the tool | That the books exist | Any evidence that the tool works in document review. Outcome evidence for transactional analysis in its home setting: B11 (CL-6). |
| **B8.** Lau, W. K.-W., Leung, P. P.-Y., & Chung, C. L.-P. (2019). Effects of the Satir model on mental health: a randomized controlled trial. *Research on Social Work Practice*, 29(7), 775–785 (online 25 Dec 2018). doi:10.1177/1049731518819829 | Crossref record and abstract (via OpenAlex) | Analogous: outcome evidence for the tool in its home setting (added, CL-6) | An RCT of 96 adults (52 intervention, wait-list control): after a Satir-growth-model workshop, significant improvement (p < .001) in affect, self-esteem and mental health problems. | Anything about using Satir in reviewing documents or AI output |
| **B9.** Haitoglou, D. (2026). The Satir model as a systemic transformational approach: a synthesis of empirical and conceptual studies. *Journal of Marital and Family Therapy*, 52(3), e70147. doi:10.1111/jmft.70147 | Crossref record and abstract | Analogous (added, CL-6) | A PRISMA 2020 thematic synthesis of 21 studies from 5,923 records; it reports benefits for emotional resilience, self-esteem, communication and family functioning. | Effect sizes; anything about document review. Perplexity notes apparent anomalies in its reference list; individual studies would need checking before reuse. |
| **B10.** Raffagnino, R. (2019). Gestalt therapy effectiveness: a systematic review of empirical evidence. *Open Journal of Social Sciences*, 7(6), 66–83. doi:10.4236/jss.2019.76005 | Publisher page and abstract (via OpenAlex) | Analogous (added, CL-6) | A systematic review of 11 studies: Gestalt therapy "was shown to especially improve conduct in the group therapy setting"; the authors call the efficacy evidence "controversial and quite poorly investigated". | A meta-analytic effect; anything about document review |
| **B11.** Vos, J., & van Rijn, B. (2022; issue 2026). The effectiveness of transactional analysis treatments and their predictors: a systematic literature review and explorative meta-analysis. *Journal of Humanistic Psychology*, 66(3), 637–673. doi:10.1177/00221678221117111 | Crossref record and abstract | Analogous (added, CL-6) | 41 clinical trials of TA treatments had moderate to large effects (for example psychopathology g = .66); the authors conclude TA "may be considered an effective treatment for many clients". | Anything about document review; the meta-analysis is described by its authors as explorative |

### C. Multiple reviewers, independence, and correlated errors

| Source | What was opened | Grade | What it supports | What it does not support |
|---|---|---|---|---|
| **C1.** Bornmann, L., Mutz, R., & Daniel, H.-D. (2010). A reliability-generalization study of journal peer reviews: a multilevel meta-analysis of inter-rater reliability and its determinants. *PLoS ONE*, 5(12), e14331. doi:10.1371/journal.pone.0014331 | PubMed abstract | Analogous | Independent human reviewers agree little (mean ICC/r² = .34; mean Cohen's κ = .17). Reviewer disagreement is normal, and the authors write that "Studies that report a high level of IRR are to be considered less credible". | Anything about LLM reviewers |
| **C2.** Ladha, K. K. (1992). The Condorcet jury theorem, free speech, and correlated votes. *American Journal of Political Science*, 36(3), 617–634. doi:10.2307/2111584 | Abstract (via OpenAlex) | Component (theory) | The classic jury theorem assumes independent votes. Ladha generalizes it to correlated votes, and for small groups "the conditions are severe". This is why four seats from one family are not four votes. | Any particular numeric weight |
| **C3.** Kim, E., Garg, A., Peng, K., & Garg, N. (2025). Correlated errors in large language models. arXiv:2506.07962 (accepted to ICML 2025) | arXiv abstract | **Component: evidence for discounting dependence in §4** (narrowed from "direct evidence for §4", CL-7) | Across more than 350 LLMs, "models agree 60% of the time when both models err". Shared architectures and providers drive the correlation, and "larger and more accurate models have highly correlated errors, even with distinct architectures and providers". It also shows effects on LLM-as-judge evaluation. So seats from one family are not independent, and seats from different families are only partly independent. | Results for Grok or Gemini on this paper. **It does not establish that a same-family group should count as exactly one source**, and it gives no calibrated weights. "Same family = one source" is the [DOOR] working rule, a policy choice; C7 tests a version of it and finds it can help or hurt (CL-7). |
| **C4.** Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM evaluators recognize and favor their own generations. arXiv:2404.13076 | arXiv abstract | Component | Self-preference: an LLM evaluator "scores its own outputs higher than others'", and this is linked to recognizing its own text. This supports treating Claude's self-audit, and Grok's "sound" findings on §2–§6, as coordination. | How large the effect is for these models |
| **C5.** Zheng, L., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. arXiv:2306.05685 (NeurIPS 2023 Datasets and Benchmarks Track) | arXiv abstract | Component | Names "position, verbosity, and self-enhancement biases" in LLM judges. Also reports over 80% agreement with human preferences on chat-quality judgments. | Expert physics review |
| **C6.** Hong, L., & Page, S. E. (2004). Groups of diverse problem solvers can outperform groups of high-ability problem solvers. *PNAS*, 101(46), 16385–16389. doi:10.1073/pnas.0403723101 | Crossref abstract | Analogous (a model result) | "A team of randomly selected agents outperforms a team comprised of the best-performing agents." This is the diversity rationale behind seeking an outside view, as in [withheld: the author's unpublished account]. | Any empirical result for LLM teams. It also says nothing about [withheld: the author's unpublished account], which is not verified here. The theorem is **contested**: see C8 and C9 (CL-8). |
| **C7.** Berti-Equille, L. (2026). Where is the truth when AI agents disagree? Dependence-aware belief propagation for unsupervised truth discovery (extended version). arXiv:2611.04805 (3 Nov 2026; the arXiv comment says a short version was accepted at IEEE BigData 2026, which we did not confirm from the proceedings) | arXiv abstract and record | **Component, and counter-evidence to weigh** (added, CL-9) | Tests weights "so that agents sharing a base model count together as about one vote": without labels this beat majority vote on MMLU (0.716 vs 0.624 on 160 questions). But "decorrelation helps when the largest correlated bloc is weaker than the other agents and hurts when it is the strongest", with no label-free way to tell the cases apart, and "with 20 labelled questions, selecting the single best agent is more accurate than every aggregator we tested". | Manuscript review (its tasks are multiple-choice benchmarks); weighting by reasoning, retrieval or execution provenance; a non-voting process like §4.3 |
| **C8.** Thompson, A. (2014). Does diversity trump ability? An example of the misuse of mathematics in the social sciences. *Notices of the American Mathematical Society*, 61(9), 1024–1030. doi:10.1090/noti1163 | Crossref record only (the AMS PDF returned HTTP 403) | Critique of C6 (added, CL-8) | That a published mathematical critique of C6 exists; its content is described here only through C9's abstract | Its arguments, which we did not read |
| **C9.** Kuehn, D. (2017). Diversity, ability, and democracy: a note on Thompson's challenge to Hong and Page. *Critical Review*, 29(1), 72–87. doi:10.1080/08913811.2017.1288455 | Crossref record and abstract (via OpenAlex) | Reply to C8 (added, CL-8) | Argues that Thompson's "mathematical criticisms of the theorem are incorrect, misleading, or irrelevant", while crediting her point on "the importance of randomization". So the dispute is open; C6 stays a contested model result used as motivation only. | Settling the dispute |
| **C10.** Ma, C., Zhang, E., Zhao, Y., Liu, W., Jia, Y., Qing, P., Shi, L., Cohan, A., Yan, Y., & Vosoughi, S. (2025). Judging with many minds: do more perspectives mean less prejudice? On bias amplification and resistance in multi-agent based LLM-as-judge. *Findings of the Association for Computational Linguistics: EMNLP 2025*, 17356–17392. doi:10.18653/v1/2025.findings-emnlp.941 | ACL Anthology abstract | Component, and counter-evidence (added, CL-9) | "debate framework amplifies biases sharply after the initial debate, and this increased bias is sustained in subsequent rounds, while meta-judge approaches exhibit greater resistance". This supports keeping first-round reviews blind to each other (§3.2) and is a caution for any later round in which reviewers see each other's findings. | Manuscript review; this review's models |

### D. Human-in-the-loop decision support and pre-registration

| Source | What was opened | Grade | What it supports | What it does not support |
|---|---|---|---|---|
| **D1.** Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *PNAS*, 115(11), 2600–2606. doi:10.1073/pnas.1708274114 | Crossref abstract | Component | "define the research questions and analysis plan before observing the research outcomes". This is the rationale for registering criteria before reading results (L0 and the packet). | That a 49 s window shows the results had not been observed (§5.4) |
| **D2.** Kerr, N. L. (1998). HARKing: Hypothesizing after the results are known. *Personality and Social Psychology Review*, 2(3), 196–217. doi:10.1207/s15327957pspr0203_4 | Crossref abstract | Component | Defines HARKing: presenting a hypothesis formed after seeing the results as if it had been formed before. That pre-registration guards against it rests on D1 (Nosek et al.), not on Kerr's abstract (CL-10). | Whether Kerr's full text discusses pre-registration as the remedy (not checked) |
| **D3.** Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. *Nature Human Behaviour*, 8(12), 2293–2303. doi:10.1038/s41562-024-02024-1 | PubMed abstract; full text opened 19 Nov 2026 about 19:01 ET (nature.com and Europe PMC, PMC11659167) | **Component, and counter-evidence to weigh** | A pre-registered meta-analysis of 106 studies: human–AI combinations performed "significantly worse than the best of humans or AI alone" (Hedges' g = −0.23). There were losses in decision tasks and "significantly greater gains in tasks that involved creating content"; that comparison is relative to decision tasks. The creation-task synergy itself was g = 0.19 (95% CI −0.09 to 0.48; P = 0.180), which the authors say was "not significantly different from 0" (full text, Results; CL-11). So a human-in-the-loop design has to be shown to help here; it cannot be assumed. | Whether X24si's particular design fails or succeeds |
| **D4.** Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., & Weld, D. S. (2021). Does the whole exceed its parts? The effect of AI explanations on complementary team performance. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (CHI '21), Yokohama, Japan (16 pp.). doi:10.1145/3411764.3445717 (citation completed, CL-12) | Abstract (Semantic Scholar; arXiv 2006.14779); author PDF (idl.cs.washington.edu, sha256 `0db4fce3…f644`) opened 19 Nov 2026 | Component (a caveat) | Earlier gains from explanations in human–AI decision tasks appeared only when the AI alone outperformed both the human and the best team. So a human–AI team doing better than either alone (complementary performance) is not automatic. In its own studies "we observed complementary improvements from AI augmentation, they were not increased by explanations", and explanations raised acceptance of the AI's recommendation "regardless of its correctness" (CL-12). | X24si specifically. It does **not** show that its own teams lacked complementary performance. |
| **D5.** Helmreich, R. L., Merritt, A. C., & Wilhelm, J. A. (1999). The evolution of crew resource management training in commercial aviation. *International Journal of Aviation Psychology*, 9(1), 19–32. doi:10.1207/s15327108ijap0901_2 | Abstract (via OpenAlex); full text (FAA-hosted copy, sha256 `e4ae9f67…73f4`) opened 19 Nov 2026 | Analogous | CRM is the source [DOOR] names for separating authority from the weight of evidence; **the paper itself does not test that separation, which is [DOOR]'s application** (CL-13). The authors say the error-management approach's "impact remains to be evaluated empirically". The paper reframes CRM as error management ("to avoid error, to trap errors committed, and to mitigate the consequences of error"). It notes limitations, "including lack of cross-cultural generality". | Validation of X24si |

### E. LLM reviewers of scientific papers (added after the Perplexity check, CL-9)

| Source | What was opened | Grade | What it supports | What it does not support |
|---|---|---|---|---|
| **E1.** D'Arcy, M., Hope, T., Birnbaum, L., & Downey, D. (2024). MARG: multi-agent review generation for scientific papers. arXiv:2401.04259 | arXiv abstract | Component | Multiple LLM instances in internal discussion: generic comments fell "from 60% to 29%" and good comments rose to "3.7 good comments per paper (a 2.2x improvement)" in a user study | Independent reviewers from different families; human final decisions; correctness of findings |
| **E2.** Liang, W., Zhang, Y., Cao, H., Wang, B., Ding, D. Y., Yang, X., Vodrahalli, K., He, S., et al. (2024). Can large language models provide useful feedback on research papers? A large-scale empirical analysis. *NEJM AI*, 1(8). doi:10.1056/AIoa2400196; preprint arXiv:2310.01783 | Crossref record; arXiv abstract | Component | GPT-4–human overlap in points raised (30.85% Nature journals, 39.23% ICLR) was comparable to human–human overlap (28.58%, 35.25%); of 308 researchers, "57.4%" found the feedback helpful or very helpful | Whether the criticisms were correct; whether manuscripts improved |
| **E3.** Gao, X., Ruan, J., Zhang, Z., Gao, J., Liu, T., Fu, Y., et al. (2025). ReviewAgents: bridging the gap between human and AI-generated paper reviews. arXiv:2503.08506 ("Work in progress") | arXiv abstract | Component (weak) | A multi-role, multi-LLM review framework evaluated on its own benchmark (ReviewBench) for alignment with human reviews | Error detection or better human decisions. Perplexity's report that three reviewer agents did best in an ablation was **not verified** by us (full text not opened). |
| **E4.** Gao, Z., Brantley, K., & Joachims, T. (2024). Reviewer2: optimizing review generation through prompt generation. arXiv:2402.10886 | arXiv abstract | Analogous | Modelling the distribution of review aspects gave "more detailed reviews that better cover the range of aspects that human reviewers identify" | Independence across model families |

### Unverified: listed, not cited
- [withheld: the author's unpublished account] No source was opened.
- **Satir, Perls and Berne:** outcome studies in their home settings are now opened (B8–B11). No study of these tools used in document review exists among the sources opened.
- **Alderfer (1969):** the content was not opened. Perplexity's report of its content is not adopted (CL-5).
- **Bansal et al. article number 81** and the **Berne subtitles and R. F. Hefferline initials** that Perplexity supplied were not confirmed by a record we opened, so they were not added (§12.3).
- **The Golden Phoenix after-action report:** [ZEN] describes it as "not formally published".

### 11.1 Change log
CL-1 to CL-13 come from the Perplexity check (19 Nov 2026, about 19:05–19:25 ET). Each of those changes was made only after opening the source ourselves (§12.3). CL-14 to CL-17 were added in this r2 file on 19 Nov 2026, about 20:12–20:20 ET. The wording before CL-1–CL-13 is preserved in the unchanged file `X24SI_HITL_REVIEW_PROTOCOL_v4r11.md` (sha256 `3b512ad6…98b5`). The wording before CL-14–CL-17 is preserved in the unchanged file `X24SI_HITL_REVIEW_PROTOCOL_v4r11_with_perplexity.md` (sha256 `6b1b3d6b…f145`).

| ID | Entry | Was | Now | Trigger (§12.3 row) | Source opened |
|---|---|---|---|---|---|
| CL-1 | A2 | "*ISCRAM 2012*, work in progress"; "Abstract (PDF located; not read in full)" | Full proceedings citation (9th ISCRAM, Vancouver, April 2012, eds. Rothkrantz, Ristvej & Franco); full text of mirror read; warning about the paper's internal 490,000 vs 49,000 inconsistency | 6 | eclass.uoa.gr mirror PDF |
| CL-2 | grading key, A3, A4 | "Direct as a statement" | New grade "Method description"; A4 quotes re-checked on the live page | 5 (and 1–4) | Zenodo API; x24humanai.com |
| CL-3 | B1 | "TC 25-20 describes a retrospective review" | Narrowed: the forecast format is the difference; TC 25-20 does plan AARs ahead and revises SOPs | 7 | TC 25-20 full text |
| CL-4 | B2 | "Effectiveness depends on alignment, objective review media, facilitation and structure" | Two consistent factors; facilitation and structure interactive or context-dependent | 8 | PubMed abstract PMID 32852990 |
| CL-5 | B4 | Unverified (content) | Unchanged; relabel to Analogous declined; Perplexity's account noted | 10 | Could not open (ScienceDirect, OpenAlex) |
| CL-6 | B5–B7; new B8–B11 | "No evidence of effectiveness opened" | Home-setting outcome evidence added as separate Analogous rows; still no evidence for use in document review; B6 initials "F. S." | 11–13 | Crossref, OpenAlex, SCIRP, Open Library |
| CL-7 | C3; §4.3 | "Component, and direct evidence for §4" | "Component: evidence for discounting dependence"; one-source rule stated as policy | 16 | arXiv:2506.07962 abstract |
| CL-8 | C6; new C8, C9 | No mention of critique | Contested; Thompson 2014 and Kuehn 2017 added | 19 | Crossref; OpenAlex |
| CL-9 | new C7, C10, E1–E4 | – | Added after opening (§12.4) | (e) | arXiv; ACL Anthology; Crossref |
| CL-10 | D2 | "Describes the failure pre-registration guards against" | Kerr defines HARKing; the remedy rests on D1 | 21 | Crossref abstract (already on file) |
| CL-11 | D3 | "gains in content-creation tasks" | Relative gain significant; creation-task synergy itself not significant (g = 0.19, CI −0.09 to 0.48) | 22 | Full text, nature.com and Europe PMC |
| CL-12 | D4 | "Weld, D."; "*CHI 2021*" | "Weld, D. S."; full proceedings title; its own complementary result stated | 23 | Author PDF; Crossref |
| CL-13 | D5 | CRM as the source for separating authority from evidence weight | Separation is [DOOR]'s application, untested in the paper; "impact remains to be evaluated empirically" | 24 | FAA-hosted full text |
| CL-14 | A2; A1; §12.3 row 6 | A2: "Do not cite its X24 Europe count"; 490,000 flagged as an unresolved internal inconsistency; A1 support column gave 49,000 and 79 nations only | 49,000 is the correct X24 Europe figure and may be cited from both A1 and A2. 490,000 in one A2 passage is a typo (author correction, 19 Nov 2026, about 20:12 ET; George is a co-author). Consistent with the 2011 IJISCRAM abstract (A1: over 49,000 from at least 92 countries) and with the other A2 passages. The earlier CL-1 flag was an error on our side: we failed to check prior project history. George's 25 Oct 2026 public-text decision had already cited X24 Europe as over 49,000 from at least 92 countries to Howe et al. 2011, and "over 12,500" for the first X24 to ISCRAM 2012. This is an author correction, not independent verification of the count. A1's support column is completed with the abstract's 92-country wording, which was already in the record we opened. | Author statement 19 Nov 2026; prior decision 25 Oct 2026; A1 abstract; A2 full text already opened |
| CL-15 | §1.1 | No author's statement of the method's basis beyond the tools already quoted from [ZEN] and [SKILL] | Added the author's statement (19 Nov 2026, about 20:12 ET): the method brings together modalities already in successful use worldwide, used here as crew tools. Named: Satir (habits people learned / learned imprints); Perls / Gestalt (recognizing stuck loops as a chance for new decisions); Berne (transactional analysis, Adult-to-Adult); Alderfer's ERG; and AAR with 1st- to 4th-order impacts, measured against the betterment of all humanity. The intended result in this setting is a safe no-fault off-ramp. Component evidence remains as in §11 (B1–B3, B8–B11); the combined method still has no controlled study (Perplexity §12.4(f): "None found"). The combination is not treated as validated. | Author statement 19 Nov 2026 |
| CL-16 | §3.1, §3.2, §6.1, §8 (D25), §9 (L6) | A single Gemini stage (S3) | Two-stage Gemini plan. Stage G1 is the blind take, using the existing `GEMINI_PROMPT.md`, unchanged, in a fresh chat with Drive and history off, a screenshot of the model name, and an export of the reply. Stage G2 is an informed re-check in a new fresh chat, only after the G1 reply has been hashed and logged, so G2 cannot contaminate G1. G2 is not independent of the team's conclusions (anchoring risk, D25). | George's instruction 19 Nov 2026, about 20:12 ET; Q1 decision at about 18:56 ET |
| CL-17 | §9 L8; §8 D26 | – | New lesson: check prior discussions and memory before flagging a source conflict. Recorded as the process failure behind CL-1 / CL-14. Provisional until George approves it. | Same |
| CL-18 | Header; §3.1 S3-G1 row; §7.4 (new); §8 D27–D30; §9 L9; §13 (new) | S3-G1 "Gemini's G1 reply, exported …" (no result) | Stage G1 recorded as COMPLETE (20:30 ET), built from manual pastes; coverage check, consistency issues and DRAFT REVIEW_LOG block added; G1-followup recorded as not blind and not part of G1. No earlier cell was rewritten except by appending to the S3-G1 row and the header. | George's instructions relayed by the parent, 19 Nov 2026, 20:22–20:34 ET |
| CL-19 | Header; §8 D30 row (Resolution cell); §13.8 capture-gap bullet; §13.9 (new) | D30 open; "still to be saved by the parent" | D30 closed. Follow-up files hashed and reviewed. `GEMINI_RECHECK_PROMPT_v2.md` written as a new file (v1 unchanged), with the seven changes proposed at r3 and the G1 and G1-followup files added to its attachment list. | George, 19 Nov 2026, about 20:36 ET |
| CL-20 | Header; §8 D25 Resolution cell; new D31; new §14 | Stage G2 still planned; GWTC-5.0 human check and M6 open; Gemini text still under review | Author decisions AD-1–AD-5 logged (9:06 PM ET). GWTC-5.0 intervals verified by code extraction plus George's visual check of two stacked Eq. 22 entries. The paper sentence must state exactly that method. Stage G2 cancelled; G1 and the G1-followup remain proposals only. No Gemini-suggested text is used. M6 investigated in Job B (`/workspace/galactic_piano_zenodo/ETA_DIFF_PROVENANCE.md`). | George, 19 Nov 2026, 9:06 PM ET; Job B completed about 21:15 ET the same evening |
| CL-21 | Header; §9 L10–L11; new §18 | No future-paced referee step; no status ledger; recursion and future pacing not distinguished | AD-9 logged (4:27 PM and 4:51 PM ET, 21 Nov); future referee + symbolic check results; r12c apply record; status ledger (L10); recursion vs future pacing (L11, §18.4) |

---

## 12. Perplexity source check (outside check of §0 and §11; George's request, 19 Nov 2026)

**Purpose.** An outside system checks each public source in §0 and §11 for:
- existence and correct citation details;
- whether it supports the specific claim we rely on;
- whether our label is right (direct, component, analogous or unverified).

It was also asked for stronger sources we missed, including ones that challenge the method.

**How it was actually run (19 Nov 2026, 18:57–19:01 ET).** On perplexity.ai in George Bressler's signed-in Pro account (an existing session), in the default "Search" mode, each part in a new thread. A script typed each prompt file into the box; it was not pasted (D22). The reply was exported with Perplexity's Download → PDF, and the text was extracted to `.md` (D23). Screenshots were taken while each answer was still streaming (D24). The Sparks executor then filled §12 and resolved every disagreement by opening the source itself (19 Nov 2026, about 19:00–19:25 ET).

**Prompt.** The index is `/workspace/x24si_hitl_sources/PERPLEXITY_SOURCE_CHECK_PROMPT.md`. The prompt is in 2 parts, each entered exactly as written into its own new thread.

| Part | File | Sources | SHA-256 of the prompt file |
|---|---|---|---|
| 1 | `/workspace/x24si_hitl_sources/PERPLEXITY_SOURCE_CHECK_PROMPT_part1.md` (7,625 characters) | 1–13 | `de06d8724148c9ee1dd86af621e03a43a7ce8ec8879b07742ad322305249d4da` |
| 2 | `/workspace/x24si_hitl_sources/PERPLEXITY_SOURCE_CHECK_PROMPT_part2.md` (7,743 characters) | 14–24, then the questions on missed sources and the whole method | `cf13828a641f87c82d7e86f390d3eedf55fbf077e2bb91b67d286ca4ad32877d` |

**Barrier.** The prompt contains no paper text and no reviewer findings, only citations, claims and labels.

**Not sent (internal, private or unpublished), with reasons:**
- [SKILL]: an internal file.
- [PKT]: in a private repository.
- [P71]: the paper under review, withheld by design.
- [RES]: private repository.
- [CL13]: an internal note.
- [GR] and [withheld: the author's unpublished account].

These stay checked only by the opening and hashing recorded in §0.

**Result in one line.** Of 24 sources, Perplexity rated our claim SUPPORTED for 14, PARTLY for 6, NOT SUPPORTED for 0 and CANNOT VERIFY for 4 (all four are X24si's own pages, which its fetches could not open). It agreed with our label for 16 and proposed a different label for 8. It raised 19 points we had to resolve (§12.3): 4 refuted (existence of X24si's own sources), 6 adopted, 7 adopted with correction, 2 declined. It suggested 12 new sources; all 12 were opened, and all 12 were added to §11 at the level we could verify (one, Thompson 2014, as a record only). It found **no** evaluation of the combined method.

### 12.1 Run record

| Field | Part 1 | Part 2 |
|---|---|---|
| Date and time started (ET) | 19 Nov 2026, 18:57 | 19 Nov 2026, 18:59:59 |
| Date and time reply complete (ET) | about 18:58–18:59 (PDF saved 18:59) | about 19:01 (PDF saved 19:01) |
| Thread | [private Perplexity thread link withheld] | [private Perplexity thread link withheld] |
| Perplexity mode shown | Search (default) | Search (default) |
| Model shown, if any | None. The Model selector was at its default and showed only "Model" (D20). | None (D20) |
| Search step shown | "Finished 31s"; 73 sources | "Finished 34s"; 105 sources |
| Signed in? | Yes: George Bressler, Pro, existing session | Yes: same |
| New thread? | Yes | Yes |
| Prompt entry | Typed by a script, not pasted; entered length 7,625 characters, equal to the file (D22) | Typed by a script; 7,743 characters, equal to the file (D22) |
| Prompt SHA-256 (file) | `de06d872…49d4da` | `cf13828a…2877d` |
| Raw reply, PDF export (primary record) | `/workspace/x24si_hitl_sources/perplexity_reply_part1_2026-11-19_1859.pdf` (727,515 bytes) | `/workspace/x24si_hitl_sources/perplexity_reply_part2_2026-11-19_1901.pdf` (815,906 bytes) |
| PDF SHA-256 | `b975c54b58a7dfb46a0e7c421431d0b8336cae0c8d175270db85f17b9237eec6` | `026aaedf85cd2a9ea54ea9d2bcc49685dbb6dfa602ff6aab03166c0554598cfe` |
| Extracted text (working copy, D23) | `/workspace/x24si_hitl_sources/perplexity_reply_part1_2026-11-19_1859.md` (26,718 bytes) | `/workspace/x24si_hitl_sources/perplexity_reply_part2_2026-11-19_1901.md` (24,150 bytes) |
| Text SHA-256 | `c75771b92c45ad1147505129ac2587b943736616188e0d4bb86638423a3a4aaa` | `e0f087e8a029b29982c2f973ee97304b8e6dbd7f9f1130d6058bebb78e6c7213` |
| Screenshot (mid-generation, D24) | `perplexity_part1_screenshot.png`, 18:58:33 ET, sha256 `1a9277e0955dc4e2bf44f5973952cec4198c76a55d586b578f7e53490ff71326` | `perplexity_part2_screenshot.png`, 19:00:55 ET, sha256 `25bef4c84b724a4970248780355094da6bd9b41f54ca907d1d82dfab2c7b5ab9` |
| Run by | A script in George's signed-in session (Sparks's run) | Same |
| Results filled in and resolved by | Sparks executor, 19 Nov 2026, about 19:00–19:25 ET | Same |

### 12.2 Per-source results
Perplexity's words are quoted briefly from the PDF export. "Agrees?" is about our label only; claim qualifications are in §12.3.

| # | Source (short) | Our label | Exists / citation correct? (Perplexity's corrections) | Perplexity verdict | Perplexity's link(s) | Agrees with our label? | Perplexity unsure about |
|---|---|---|---|---|---|---|---|
| 1 | [ZEN] Zenodo runway note, DOI 10.5281/zenodo.23351794 | Direct (statement, not validation) | "CANNOT VERIFY. The DOI fetch failed" | CANNOT VERIFY | none found | **No:** "'DIRECT—statement only' needs a separate designation, such as *method-description source*" | Zenodo record and files |
| 2 | [ZEN-ADD] welcome-email addendum | Direct (statement) | CANNOT VERIFY | CANNOT VERIFY | none | **No:** UNVERIFIED for this check; description, not validation | Zenodo files |
| 3 | [DOOR] x24si.com / x24humanai.com | Direct (statement, self-reported) | PARTLY (the page loads at x24humanai.com) | CANNOT VERIFY (the exact claims) | x24humanai.com | **No:** method description, not DIRECT | Exact website claims, redirect, dated state |
| 4 | [XPOST] X post and article, 19 Oct 2026 | Direct (statement, self-reported) | CANNOT VERIFY (X fetch failed) | CANNOT VERIFY | none | **No:** unverified for this check | The posts and article |
| 5 | A1 Howe et al. 2011, IJISCRAM | Analogous | Correct | SUPPORTED | igi-global.com; irma-international.org | Yes | Original full text and counting methods |
| 6 | A2 Bressler et al. 2012, ISCRAM | Analogous | Add "México"; *Proceedings of the 9th International ISCRAM Conference*, Vancouver, April 2012; notes the paper gives "490,000 for Europe" in one place and 49,000 elsewhere | SUPPORTED | eclass.uoa.gr mirror | Yes | The proceedings-hosted copy |
| 7 | B1 TC 25-20 (1993) | Component | Correct | SUPPORTED (definition, format); PARTLY (our negative claim) | eclass.uoa.gr; Army copy | Yes | "the unextracted remainder" of the manual |
| 8 | B2 Keiser & Arthur 2021 | Component | Correct; "A 2020 online-first date" | SUPPORTED, with qualification: only alignment and objective media contributed consistently | psycnet.apa.org | Yes | Full meta-analysis methods |
| 9 | B3 Tannenbaum & Cerasoli 2013 | Component | Correct | SUPPORTED; but "do not establish an expected 25% benefit" for this workflow | pubmed 23516804 | Yes | Full methods |
| 10 | B4 Alderfer 1969 | Unverified (content) | Correct | SUPPORTED: "approximately 110 bank" employees; results "tended to support E.R.G." theory | indexed text | **No:** ANALOGOUS | "a comprehensive later ERG evidence base" |
| 11 | B5 Satir 1988 | Unverified (effectiveness) | Correct, "no correction found" | PARTLY; outcome research exists (Lau et al. RCT; a 2026 synthesis) | library records; APA; Wiley | **No:** ANALOGOUS for the borrowing; "Retain UNVERIFIED for effectiveness of your adaptation, but not as a claim that no outcome evidence exists" | Book passages; trial full results |
| 12 | B6 Perls et al. 1951 | Unverified (effectiveness) | "fuller initials would be F. S. and R. F." | PARTLY; Raffagnino 2019 review, 11 studies | Google Books; SCIRP; NCBI | **No:** ANALOGOUS for the borrowed idea; UNVERIFIED for effectiveness in review | The 1951 passage |
| 13 | B7 Berne 1961/1964 | Unverified (effectiveness) | Fuller subtitles given | PARTLY; Vos & van Rijn 2022 meta-analysis | records; SAGE | **No:** ANALOGOUS for the borrowing | Full meta-analysis methods |
| 14 | C1 Bornmann et al. 2010 | Analogous | Correct | SUPPORTED | journals.plos.org | Yes | Underlying studies |
| 15 | C2 Ladha 1992 | Component (theory) | Correct | SUPPORTED at abstract level | jstor; umd.edu | Yes ("COMPONENT (theory), narrowly") | "Ladha's full theorem conditions" |
| 16 | C3 Kim et al. 2025 | Component | Correct (Elliot Myunghoon Kim) | SUPPORTED, but "It supports discounting dependence; it does not demonstrate that all same-family reviewers should count as exactly one source" | arxiv.org/abs/2506.07962; dblp | Yes (Component), not our stronger parenthetical | Datasets and downstream experiments |
| 17 | C4 Panickssery et al. 2024 | Component | Correct | SUPPORTED: "linear correlation" between self-recognition and self-preference | arxiv.org/abs/2404.13076 | Yes | Causal controls; generality |
| 18 | C5 Zheng et al. 2023 | Component | Correct; 13 authors | SUPPORTED: "position, verbosity, and self-enhancement biases"; "over 80% agreement" | arxiv.org/abs/2306.05685 | Yes | NeurIPS proceedings metadata |
| 19 | C6 Hong & Page 2004 | Analogous | Correct; online 8 Nov, issue 16 Nov | SUPPORTED "as a conditional model result" | pnas.org; PMC528939 | Yes; "limited use as motivation… is appropriate" | The simulation; "A published critique and a published response" |
| 20 | D1 Nosek et al. 2018 | Component | Correct | SUPPORTED: "clarity between prediction and postdiction" | pnas.org; osf preprint | Yes | Whether our GitHub record documents prospective commitments |
| 21 | D2 Kerr 1998 | Component | Correct | PARTLY: the guard-against claim "is better supported jointly with Nosek et al." | pubmed 15647155; sagepub | Yes | Whether Kerr discusses pre-registration |
| 22 | D3 Vaccaro et al. 2024 | Component (counter-evidence) | Correct; issue 12 not shown on the header it opened | SUPPORTED, with qualification: creation-task synergy "positive, not significantly above zero" | nature.com full text | Yes | Supplements |
| 23 | D4 Bansal et al. 2021 | Component (caveat) | Complete the venue: CHI 2021 proceedings, "Article 81, pp. 1–16"; "Daniel S. Weld" | SUPPORTED; "Do not describe its own team results as showing no complementarity" | dl.acm.org; author PDF | Yes | Each earlier experiment it cites |
| 24 | D5 Helmreich et al. 1999 | Analogous | Correct; PubMed's extra "New Collective Author" should not be added | PARTLY: "separating decision authority from evidential weight is your application" | FAA-hosted full text; PubMed | Yes | "impact remains to be evaluated empirically" |

**Counts.** Claim verdicts: SUPPORTED 14 (5, 6, 8, 9, 10, 14–20, 22, 23), PARTLY 6 (7, 11, 12, 13, 21, 24), NOT SUPPORTED 0, CANNOT VERIFY 4 (1–4). Labels: agree 16 (5–9, 14–24), disagree 8 (1–4, 10–13).

### 12.3 Disagreements with our labels or claims, and how each was resolved
Rule: a disagreement is resolved **only by opening the source ourselves**, never by taking either side's word. Outcomes: adopted, adopted with correction, refuted or declined, the same four as the review. All rows resolved by the Sparks executor on 19 Nov 2026 between about 19:00 and 19:25 ET. Local copies of what was opened are in `/workspace/x24si_hitl_sources/pplx_verify/`.

| # | What Perplexity said | What we had | Source opened (URL/DOI, page or section) | What the source actually says | Resolution | §11 change |
|---|---|---|---|---|---|---|
| 1 | Source 1 [ZEN]: CANNOT VERIFY; "The DOI fetch failed" | Opened, md5-matched (§0) | Zenodo API, record 23351794 | DOI 10.5281/zenodo.23351794; "A Findable Runway: Sanctioned 3C as an Off-Ramp for Objective-Serving SI Swarms"; Bressler, George H.; 2026-10-19; files `x24-runway-zenodo_2026-10-19y-r7.pdf` and `x24-welcome-email-addendum_2026-10-19e.pdf` | **Refuted** (the record exists as cited; the failure was Perplexity's fetch) | none |
| 2 | Source 2 [ZEN-ADD]: CANNOT VERIFY | Opened (§0) | Same Zenodo API record | The addendum file is in the record | **Refuted** | none |
| 3 | Source 3 [DOOR]: page PARTLY, claims CANNOT VERIFY | Opened (§0) | x24si.com, which now resolves to https://x24humanai.com/ (HTTP 200) | "convergence is not truth"; "agreement is weighted, never counted"; same-family agreement "treated as coordination rather than corroboration"; "adopted, adopted with correction, refuted, or declined" | **Refuted** (all four claims on the live page) | A4 notes the re-check |
| 4 | Source 4 [XPOST]: CANNOT VERIFY (X fetch failed) | Read by post ID through the X API (§0; saved copy `x_post_2112259516666658903.txt`) | Not re-opened in this pass; relies on the API read and hashed copy recorded in §0 | As recorded in §0 | **Refuted** as a citation problem (the post exists; Perplexity's fetch failed) | none |
| 5 | Sources 1–4 should not be "DIRECT": "'DIRECT—statement only' needs a separate designation, such as *method-description source*" | "Direct as a statement, not a validation" | Our own grading key in §11 | Our key defines Direct as "validates the X24si method itself", which these sources do not do | **Adopted with correction:** new grade "Method description"; they remain the primary sources for §1 | CL-2 |
| 6 | Source 6: complete the venue (9th ISCRAM, Vancouver, April 2012); the paper gives "490,000 for Europe" in one place and 49,000 elsewhere | "*ISCRAM 2012*, work in progress"; abstract only | Full text of the eclass.uoa.gr mirror (sha256 `3e497c81…3f69`); the iscramlive.org URL returned HTTP 441 | Running head: "Proceedings of the 9th International ISCRAM Conference – Vancouver, Canada, April 2012, L. Rothkrantz, J. Ristvej and Z. Franco, eds." Both figures appear: "X24 Europe had over 490,000 participants" and "approximately 12,700 and 49,000 participants" | **Adopted with correction** at the time: citation completed; the 490,000 figure flagged as an internal inconsistency; we cite only the X24 México count. **Later correction (CL-14):** that "do not cite" resolution is withdrawn. 490,000 is a typo; 49,000 is correct and may be cited. The historical finding of both figures in the text still stands; the error was treating it as unresolved and withholding the 49,000 figure. | CL-1; later CL-14 |
| 7 | Source 7: narrow the negative claim; the manual "explicitly plans reviews before training and feeds findings into revised SOPs" | "TC 25-20 describes a retrospective review" | TC 25-20 full text (`verify/tc.txt`) | "Leaders plan formal AARs at the same time they finalize the near-term training plan"; "revise standing operating procedures" | **Adopted** (wording narrowed to the forecast format) | CL-3 |
| 8 | Source 8: only alignment and objective media contributed consistently | "Effectiveness depends on alignment, objective review media, facilitation and structure" | PubMed abstract PMID 32852990 (`verify/pm_32852990.txt`) | "(a) alignment to the individual or the team, and (b) objective performance review media. The effects of the other training characteristics were often interactive"; structure helped "in the military" but was "comparable" in healthcare; Epub 2020 | **Adopted** | CL-4 |
| 9 | Source 9: the studies "do not establish an expected 25% benefit" for this workflow | B3 already lists "the same limits as B2" (not AARs as forecasts, not SI, not paper review) | PubMed abstract PMID 23516804 | "approximately 25%" over controls, in training and team settings | **Declined** (no change needed; our row already limits the claim) | none |
| 10 | Source 10: relabel Alderfer from UNVERIFIED to ANALOGOUS; "approximately 110 bank" employees; "tended to support E.R.G." | Unverified (content) | ScienceDirect page (no abstract text returned); OpenAlex (no abstract); Crossref (record only) | Could not open the content | **Declined** until the text is opened. Perplexity's account is noted in B4, not adopted. | CL-5 |
| 11 | Source 11: outcome research exists (Lau et al. RCT; 2026 synthesis); ANALOGOUS for the borrowing, UNVERIFIED for the adaptation's effectiveness | "No evidence of effectiveness opened" | Crossref and OpenAlex for doi:10.1177/1049731518819829 and doi:10.1111/jmft.70147 | RCT: 96 adults, significant improvements (p < .001); synthesis: 21 studies, benefits reported | **Adopted with correction:** the book stays "origin of the tool"; outcome studies added as separate Analogous rows; no evidence for use in document review | CL-6 (B8, B9) |
| 12 | Source 12: initials F. S. and R. F.; Raffagnino 2019 review | "Perls, F., Hefferline, R." | Open Library ("Frederick S. Perls", 1951); SCIRP page and OpenAlex for doi:10.4236/jss.2019.76005 | "F. S." confirmed; "R. F." not shown in the record we opened; review of 11 studies confirmed | **Adopted with correction:** "F. S." added; "R. F." not added (unconfirmed); review added | CL-6 (B6, B10) |
| 13 | Source 13: fuller subtitles; Vos & van Rijn 2022 meta-analysis | Short titles | Open Library (titles, Grove Press, 1961/1964); Crossref and OpenAlex for doi:10.1177/00221678221117111 | Titles and years confirmed; subtitles not shown in the records we opened; 41 trials, moderate to large effects | **Adopted with correction:** meta-analysis added; subtitles not added (unconfirmed; the short titles are correct) | CL-6 (B11) |
| 16 | Source 16: Kim et al. support discounting, not "exactly one source" | "Component, and direct evidence for §4" | arXiv:2506.07962 abstract (`verify/abs_2506.07962.html`) | Measures error correlation; proposes no one-source rule or weights | **Adopted** | CL-7 (C3, §4.3) |
| 19 | Source 19: "A published critique and a published response" exist | No critique mentioned | Crossref doi:10.1090/noti1163 (AMS PDF: HTTP 403); Crossref and OpenAlex for doi:10.1080/08913811.2017.1288455 | Thompson 2014 exists; Kuehn 2017 abstract calls Thompson's criticisms "incorrect, misleading, or irrelevant" but credits her point on randomization | **Adopted with correction:** both added; Thompson only as a record, since we did not read it | CL-8 (C6, C8, C9) |
| 21 | Source 21: the guard-against claim "is better supported jointly with Nosek et al." | "Describes the failure pre-registration guards against" | Crossref abstract (`verify/10.1207_s15327957pspr0203_4.json`) | Defines HARKing; the abstract does not name pre-registration | **Adopted** | CL-10 |
| 22 | Source 22: creation-task synergy "positive, not significantly above zero" | "gains in content-creation tasks" | Full text: nature.com/articles/s41562-024-02024-1 and Europe PMC PMC11659167, Results | "g = 0.19; t104 = 1.35; two-tailed P = 0.180; 95% CI, −0.09 to 0.48 … not significantly different from 0"; the abstract's "significantly greater gains" is relative to decision tasks | **Adopted** | CL-11 |
| 23 | Source 23: "Article 81, pp. 1–16"; "Daniel S. Weld"; "Do not describe its own team results as showing no complementarity" | "Weld, D."; "*CHI 2021*" | Author PDF (idl.cs.washington.edu, sha256 `0db4fce3…f644`), ACM Reference Format; Crossref | "Daniel S. Weld"; "In CHI Conference on Human Factors in Computing Systems (CHI '21), May 8–13, 2021, Yokohama, Japan … 16 pages"; Crossref pages 1–16; "we observed complementary improvements from AI augmentation, they were not increased by explanations". No article number in either record. | **Adopted with correction:** initial, venue and the complementarity sentence added; "Article 81" not added (unconfirmed) | CL-12 |
| 24 | Source 24: separating authority from evidential weight "is your application"; "impact remains to be evaluated empirically"; do not add PubMed's "New Collective Author" | "CRM is the source [DOOR] names for separating authority from the weight of evidence" | FAA-hosted full text (sha256 `e4ae9f67…73f4`) | "the impact remains to be evaluated empirically"; error countermeasures "to avoid error, to trap errors committed, and to mitigate the consequences" | **Adopted** (the collective author was never in our citation) | CL-13 |

Row numbers follow the source numbers in §12.2, except row 5, which covers the label point for sources 1–4 (source 5 itself raised nothing). Rows 14, 15, 17, 18 and 20 are absent because Perplexity raised nothing to resolve for those sources. **Tally of 19 resolutions:** refuted 4 (rows 1–4), adopted 6 (rows 7, 8, 16, 21, 22, 24), adopted with correction 7 (rows 5, 6, 11, 12, 13, 19, 23), declined 2 (rows 9, 10).

**Citation errors confirmed and fixed:** A2 venue (incomplete); D4 author initial and venue (incomplete); B6 first author's initials (incomplete). **Claim errors confirmed and fixed:** D3 (overstated the creation-task gain), C3 (overstated as direct evidence for the one-source rule), B2 (overstated facilitation and structure), D2 (attributed the remedy to Kerr), B1 (negative claim too broad), D5 (implied CRM tested the separation). None of these changes the protocol's method or §7's decisions.

**Later correction to row 6 (CL-14, 19 Nov 2026, about 20:12 ET).** The "do not cite" resolution is withdrawn. 490,000 is a typo and 49,000 is correct (author correction; George is a co-author). The 49,000 figure may be cited from A2, as it already may be from A1. That earlier flag was an error on our side: we did not check prior project history before treating the two figures as an unresolved conflict. George's 25 Oct 2026 public-text decision had already settled the Europe figure as over 49,000 from at least 92 countries, cited to Howe et al. 2011 (A1). This later note does not rewrite the historical row above, except for the forward pointer in the Resolution cell.

### 12.4 New sources Perplexity suggested
A suggested source enters §11 only after we open it and verify it with the source-verification steps. All were opened on 19 Nov 2026, about 19:00–19:10 ET.

| Suggested source (citation, DOI/URL) | What Perplexity says it shows | Supports or challenges the method? | Opened by us? | Verified finding (our reading) | Added to §11 as (label) or rejected (reason) |
|---|---|---|---|---|---|
| Lau, Leung & Chung (2019), RSWP 29(7), 775–785, doi:10.1177/1049731518819829 | Satir-model RCT | Supports the tool in its home setting only | Yes: Crossref, OpenAlex abstract | 96 adults; significant improvements in affect, self-esteem, mental health | **B8, Analogous** |
| Haitoglou (2026), JMFT 52(3), e70147, doi:10.1111/jmft.70147 | Synthesis of 21 Satir studies | Same | Yes: Crossref abstract | PRISMA synthesis, 21 of 5,923 records; benefits reported | **B9, Analogous** (Perplexity's warning on its reference list carried) |
| Raffagnino (2019), Open J. Social Sciences 7(6), 66–83, doi:10.4236/jss.2019.76005 | Gestalt systematic review, 11 studies | Same | Yes: SCIRP page, Crossref, OpenAlex abstract | 11 studies; evidence base "controversial and quite poorly investigated" | **B10, Analogous** |
| Vos & van Rijn (2022), J. Humanistic Psychology 66(3), 637–673, doi:10.1177/00221678221117111 | TA meta-analysis | Same | Yes: Crossref, OpenAlex abstract | 41 trials; moderate to large effects; "explorative" | **B11, Analogous** |
| Thompson (2014), Notices AMS 61(9), 1024–1030, doi:10.1090/noti1163 | Critique of Hong & Page | Challenges C6 | Record only (the AMS PDF returned HTTP 403) | Exists as cited | **C8, critique, record only** |
| Kuehn (2017), Critical Review 29(1), 72–87, doi:10.1080/08913811.2017.1288455 | Reply to Thompson | Defends C6 | Yes: Crossref, OpenAlex abstract | Disputes Thompson; credits the randomization point | **C9, reply** |
| D'Arcy et al. (2024), MARG, arXiv:2401.04259 | Multi-agent review cut generic comments 60% → 29% | Supports a component (multiple LLM reviewers) | Yes: arXiv abstract | Confirmed: 60% → 29%; 3.7 good comments per paper | **E1, Component** |
| Liang et al. (2024), NEJM AI 1(8), doi:10.1056/AIoa2400196; arXiv:2310.01783 | LLM–human overlap comparable with human–human; 57.4% of 308 found it helpful | Supports a component | Yes: Crossref; arXiv abstract | Confirmed: 30.85% / 39.23% vs 28.58% / 35.25%; 57.4% of 308 | **E2, Component** |
| Gao X. et al. (2025), ReviewAgents, arXiv:2503.08506 | Multi-agent reviews closer to human; three reviewers best | Weak component; limits "more is better" | Yes: arXiv abstract only | Framework and benchmark confirmed; "three reviewers best" **not verified** by us | **E3, Component (weak)**; ablation claim not adopted |
| Gao Z., Brantley & Joachims (2024), Reviewer2, arXiv:2402.10886 | Aspect prompts widen review coverage | Analogous (viewpoint diversity) | Yes: arXiv abstract | Confirmed | **E4, Analogous** |
| Ma et al. (2025), Findings of EMNLP 2025, 17356–17392, doi:10.18653/v1/2025.findings-emnlp.941 | Debate amplifies biases; meta-judging resists | **Challenges** multi-agent optimism; supports blind first rounds | Yes: ACL Anthology abstract; Crossref | Confirmed verbatim | **C10, Component and counter-evidence** |
| Berti-Equille (2026), arXiv:2611.04805 (IEEE BigData 2026 acceptance stated by the author) | Tests counting a base-model family as about one vote; helps or hurts by pool; one agent chosen with 20 labels beats all aggregators | **Both:** the closest test of our family rule, with counter-evidence | Yes: arXiv abstract and record | Confirmed; acceptance not checked against the proceedings | **C7, Component and counter-evidence** |

**Not added:** the many other links in Perplexity's reference lists (blogs, aggregators, course pages and arXiv HTML pages such as 2601.11578, 2606.25057, 2609.03727 and 2610.28539) were not offered as sources for a claim, were not opened, and are not cited. Perplexity also mentioned "later empirical tests" of ERG and an "NCBI clinical overview" of Gestalt therapy without citations; nothing was added for those.

**Note from Perplexity carried into §4.3:** "For your specific evidence-type rule—weighting agreement differently when it comes from reasoning, retrieval or execution—I found no directly matching empirical evaluation in the checked sources." We found none either. Provenance weighting by evidence type stays a method rule ([DOOR]), not a validated technique.

**(f) Whole-method evaluation found by Perplexity:** **None found.** Perplexity's words: "None found. I found no published evaluation combining all of the following: independently produced multi-LLM reviews, prospectively registered criteria, reasoning/retrieval/execution-based evidence weighting rather than vote counting, family-dependence adjustment, human final decisions, and after-action reviews that update the next round's procedure." It proposed the description "a proposed review procedure informed by component evidence and analogous practices," not "a validated review method." §11's statement that no source validates the combined method therefore stands unchanged.

**(g) Where Perplexity was least certain (its words):** "Ladha's full theorem conditions, uninspected experimental details and supplements, separately confirmed proceedings metadata/acceptance, and the completeness of the negative search for an exact combined-method evaluation."

### 12.5 Limits of this check
- **D19. Perplexity is not an independent check.** It is a different system from the reviewers, but its errors may still be correlated with ours (Kim et al. 2025, §11 C3). Its agreement with our labels counts as an outside retrieval check, not as independent corroboration. Its disagreements were treated as leads and resolved only by opening the source (§12.3).
- **D20. The model is not shown**, so its family is unknown (§8).
- **D21.** The prompt was written by the team whose labels it checks (§8).
- **D22.** The prompts were typed by a script in George's signed-in Pro session, not pasted. Only the length, not a hash, ties the sent text to the files (§8).
- **D23.** The `.md` replies come from the PDF export, with flattened tables; the PDFs are the primary record (§8).
- **D24.** The screenshots were taken mid-stream and do not show the final answers (§8).
- Perplexity could not open four of X24si's own pages. A check that cannot see the method's own sources cannot test whether §1 quotes them correctly; that rests on our hashed copies (§0).

---

## 13. Stage S3-G1: Gemini blind take, record and coverage check (added in r3)

Prepared by a Sparks executor (Grok Bot, xAI), 19 Nov 2026, about 20:23–20:45 ET. **Read-only:** nothing was committed to git, the paper was not edited, and no decision is changed here. **Convergence is not truth.** A G1 finding that matches a merge item is agreement between two model families, and it does not show the item is correct. A G1 finding that matches nothing in the merge is not correct just because it is new.

### 13.1 Run record
| Field | Value |
|---|---|
| Status | **COMPLETE as of 19 Nov 2026, 8:30 PM ET.** George confirmed he had finished pasting ("I believe that's it"). |
| Record consists of | (1) the closing summary (pasted at 8:20 PM ET); (2) the full nine-finding reply (8:22 PM ET); (3) segments 01–16 (8:27–8:30 PM ET): LaTeX snippets 01–12, the draft REVIEW_LOG 13, the proposed §7.1 Result paragraph 14, the GRACE README note 15 and the proposed commit message 16. |
| Model | "Gemini (Google)" is the reply's own first line. **The model name and version were not captured** (no screenshot). **Deviation D27.** |
| How it was captured | **By manual paste into the Sparks chat, not by export** (D28). The full reply keeps the doubled math rendering (KaTeX text plus LaTeX source) exactly as pasted. The segments were copied out by hand, in separate pastes. |
| Date in the reply | "November 19, 2026" (the reply's own line). There is no exact Gemini completion time, so the paste times are the outside times. |
| Barrier | According to the plan, G1 saw only the Drive folder files and `GEMINI_PROMPT.md`. Segment 13 says the commit times were "taken from review prompt metadata". They match `git log` exactly: 76d92c7 16:05:55Z, d590909 16:06:44Z, e16e6a6 16:07:18Z (11:05:55 / 11:06:44 / 11:07:18 ET). |
| Pinned inputs | Segment 13 names the PDF and tex shas `f83639b2…5f9` and `fbd273d0…a77`. Both match the files in the folder. |

### 13.2 Hashes (sha256). The full list is in `G1/G1_SHA256.txt`.
| File | sha256 |
|---|---|
| G1_reply_summary_pasted_2026-11-19_2020.md | `09b304544285b3dbadb615f2b0add21055b904ce7862f3eb38f26820d2be9522` |
| G1_reply_full_pasted_2026-11-19_2022.md (with header line) | `2ae3f163facc9dc7dc51c231ccac630698620dbccb52365bf7ae15c652794207` |
| same, verbatim body only (header excluded) | `7f5b6dc28f58d551563fb5a45736c7b01b2ce248e93cbaa669853d2219cbcc27` |
| segment 01 | `96e7782923a697ba9e1f1bc3fc797dbf3df8e3ea4ea066cc0cda86955023d787` |
| segment 02 | `91cfece6fe71dae0869e5ce4d72c3924965f5322ce225832e57254733d759964` |
| segment 03 | `e375d9cae7e51f2402c0c14cc83797200eff8b685dcb2ef1ff705a0abcf7dc45` |
| segment 04 | `17705ed50ac94b55b7835578151f327aa204e7a7be1a99a739300af49e7d36d3` |
| segments 05–16 | listed in `G1_SHA256.txt` (also on Drive as `G1_SHA256_complete_2026-11-19_2030.txt`). All 18 hashes were re-verified with `sha256sum -c` at about 20:35 ET: all OK. |
| Check files | `/workspace/gemini_review_v4r11/G1_check/` (`g1_arith_check.py` sha `cbbfb3b6…`, its output `1520303f…`, and the Galactic Piano v1 and v4 source copies with Zenodo API JSON; `SHA256SUMS.txt`). |

### 13.3 G1's consistency with itself, and its claims about its own checks
- **C1. The reviewer overstated its own source verification (summary vs findings).** The closing summary says it "Verified the primary and hierarchical GWTC-5.0 damping-time intervals against arXiv:2607.19293v1 (Eqs. 21–22) and Sen's … 77/90 against arXiv:1205.0971v2". But F1(2) says "I cannot check arXiv:2607.19293 … inconclusive", F3(1) says "I cannot check Sen, arXiv:1205.0971", the full reply's last line hands both on, and the segment 13 log says that neither source "was opened in-session". **Verdict: an overstatement by the reviewer about its own verification.** Segment 13 itself contradicts the summary.
- **C2. A false verification statement is proposed for the paper (segments 09, 14, 16).**
  - Segment 09 says "independent human verification of the transcribed numbers against arXiv:2607.19293 (Eqs. 21–22) **is recorded** in the Zenodo audit trail".
  - Segment 14 says "Independent review confirmed … **exact agreement** of the primary and hierarchical GWTC-5.0 intervals with Eqs. (21)–(22)".
  - Segment 16 repeats "record independent verification of GWTC-5.0 Eqs. (21)-(22)".
  - Gemini opened neither source (C1). **No human verification is recorded anywhere** we can find.
  - What does exist is AI verification by the Grok seats:
    - Sparks F1(iv) fetched arXiv:2607.19293v1 (sha `4ab5df87…ab101`, the same hash as in the input JSON) and checked all six numbers against a rendered image of eqs. 21–22 and p. 24 (`grok_checks/p23_rightcol_top.png`).
    - Fletcher downloaded the same PDF and checked the definitions (eq. 18, Table 8, Fig. 9).
    - Jimmy confirmed the PDF hash.
    - These three count as one correlated family (§4.1), and none of them is a human.
  - **Verdict:** segment 09's sentence is false as written. Segment 14's sentence is unsupported as written: it is true only if attributed to the Grok team's AI check, and it says nothing about who did the check. None of these three should go into the paper or the commit.
- **C3. The finding count and IDs do not line up.**
  - The summary says "8 findings (GEM-01 through GEM-08)". The full reply has nine findings, numbered F1–F9 with no GEM IDs. The segment 13 log has eight GEM IDs.
  - Mapping: GEM-01=F1, GEM-02=F2, GEM-03=F7, GEM-04=F8, GEM-06=F9, GEM-07=F5 and GEM-08=F4.
  - **GEM-05 (the §3.1 dimensional-reduction phrasing) has no finding in the full reply.** It appears only as segment 04 and in the log. Finding 5 of the full reply is the 402 Hz / spin item, not a §3.1 item.
  - **F3 (c_log) and F6 (envelope 0.975) are absent from the log.** F3 appears only as "priority check 3".
- **C4. Two findings are labelled MUST-FIX but have NOTE content (F5, F6).**
  - F5 is headed "MUST-FIX (a)", but its body finds every number consistent and proposes "Downgrade to NOTE". The log lists it as GEM-07 NOTE.
  - F6 is headed "MUST-FIX (a)", but its body says "No fix needed (verified exact)". It is dropped from the log.
  - **Effective severity: NOTE for both**, because by the reviewer's own text neither one finds an error.
- **C5. Severities differ between the full reply and the log (segment 13).** F1 SHOULD-FIX → GEM-01 SHOULD-FIX; F2 → GEM-02, the same; F7 → GEM-03, the same; F8 → GEM-04, the same; F9 NOTE → GEM-06 NOTE; F4 NOTE → GEM-08 NOTE; F5 MUST-FIX → GEM-07 NOTE; F6 MUST-FIX → absent; F3 NOTE → absent; GEM-05 SHOULD-FIX → not in the full reply.
- **C6. The "Decision: adopted (target: r12)" column in segment 13 holds Gemini's proposals, not George's decisions.** Every row says "adopted". In this record they are **proposed** only. Under the packet rules, only George's decision fills that field.
- **C7. The summary's "Verified all 15 numerical claims … across Sections 2–6"** is not backed by the full reply. The full reply checks c_log (§4–§5) and the Poisson identity (§6.1). Its other arithmetic is in §7 and §9. No list of the 15 claims was given.
- **C8. Segment 15 is wrong about the execution date.** It says the script is "preserved … exactly as executed on 2026-04-26". The run date of 2026-04-26 is right: the paper says so (tex l. 1235, Fig. 6 file `fig6_grace_run_2026-04-26.png`), and the run PDF's CreationDate is "Sun Apr 26 09:51:56 2026 EDT" (Sparks F14). But the file is named `…_2026-04-27.py`, and whether it is byte-identical to the script that ran is **unverified** (merge §6 item 3; the mascon NetCDF is not on the box). So "exactly as executed" is an unsupported claim.
  - The 6.6×10⁵ ratio checks out: 4.19×10⁻⁹ / 6.3×10⁻¹⁵ = 6.65×10⁵.
  - The F4 "factor ~230" claim is **absent** from segment 15. Segment 15 also does not say that the script's ~10⁻¹⁹ values and PRED_EWH inherit the 9.8e-5 constant (merge S5).
- **C9. The snippets would not apply cleanly to r11 as written.**
  - They use cite keys `Gaia2023` and `BresslerGalacticPiano`; the tex keys are `GaiaDR3` and `BresslerGP2026`.
  - They use `tab:kerr_spin`; the tex label is `tab:ringdown_spin`.
  - They use `eq:weights`; the tex label is `eq:wn`.
  - Several "Replace" strings do not match the tex verbatim. Segment 02 has `\cite{Gaia2023}`, and segment 06 has `402\text{ Hz}` where the tex has `402$~Hz`.
  - The Fig. 4 axis label in segment 07 is inside the figure image, not the tex.

### 13.4 Verdicts on G1's arithmetic (re-run: `G1_check/g1_arith_check.py`)
| Claim | Re-computed | Verdict |
|---|---|---|
| F3: 212/45 − 3 = 77/45, so ½ of it = 77/90 ≈ 0.856 | exact (fractions) | Correct. The Sen source itself was not opened by G1. The Grok team opened it (S1: 77/90 is the singlet-ensemble value). |
| F3: ln(A/G₄) ≈ 183.3 for 10 M⊙ | A/G₄ = 4.196×10⁷⁹, ln = 183.34 | Correct |
| F3: 157 nats; 0.114 | 156.86; (9 ln 9 + ln 3)/183.34 = 0.1139 | Correct |
| F5: f = 402 Hz, Δf = 18 Hz, Δf/FWHM = 0.094 (30 M⊙, spin 0) | 402.46 Hz; 18.06 Hz; 0.0942; τ 1.661 ms; FWHM 191.6 Hz | Correct |
| F5: spin 0.69 gives 569 Hz and 25.5 Hz | 568.90 Hz; 25.53 Hz (Δf/FWHM = 0.146) | Correct. This matches S4's 0.1460 at spin 0.69. |
| F6: envelope 0.975 at t = τ | x = 0.18848; E = 0.97489 (G1's 0.97493 uses unnormalised weights, w₁ 0.235111 vs 0.235116) | Correct to the stated 3 decimals |
| F8: 1.6×10⁻¹⁶ m s⁻² | 1.6019×10⁻¹⁶ | Correct |
| F9: an exact Poisson identity on Z₉ | max\|S w − w\| = 2.7×10⁻¹⁶ | Correct. This is standard: the periodised Gaussian e^{−πn²/N} is an eigenvector of the unitary DFT on Z_N with eigenvalue 1. The paper already says "exactly … (numerically to 10⁻¹⁵)" (tex l. 795), so the finding is optional wording. |
| F4: Bouguer 2πGρ_w(1 cm) = 4.19×10⁻⁹ m s⁻² | 4.1936×10⁻⁹ | Correct |
| **F4: EWH_TO_GRAVITY = 9.8e-5 is "per meter", so off by "~230"** | The script multiplies the GRACE residual, **in cm**, by 9.8e-5. The evidence is in the script itself: `mean_g = mean_r * EWH_TO_GRAVITY` (l. 111), the console line "({PRED_EWH:.4f} cm EWH)" (l. 145), and the axis "EWH residual (cm)" (l. 325). So the effective unit is m s⁻² **per cm**, and 9.8e-5 / 4.19e-9 = **2.34×10⁴** (merge S5). G1's 230 holds only under its own "per metre" reading, which the code does not support. G1's own rounding line (10⁻¹⁵ cm × 9.8×10⁻⁵ ≈ 10⁻¹⁹) applies the constant per cm, which contradicts that reading. | **Wrong.** The factor is ~2.3×10⁴, not ~230. A corollary G1 missed: the paper's "anomalies ~10⁻¹⁹ m s⁻²" (tex l. 1241) inherit the inflated constant. With the slab value, the rounding-level zeros would be ~4×10⁻²⁴, and PRED_EWH would be 1.5×10⁻⁶ cm, not 6.4×10⁻¹¹ cm. G1's line numbers (74–91) also do not match the attached `.py.txt`, where `detrend_seasonal` is at ll. 80–97. |

### 13.5 Segment verdicts
| Seg | What it proposes | Verdict |
|---|---|---|
| 01 | Abstract (tex l. 189–190): keep "All results anchor to …", and add "phase-spiral" and `\cite{Gaia2023,BresslerGalacticPiano}` | **Conflicts with M7** (approved): it keeps the universal "All results anchor". **Does not resolve M6:** see [37] below. The cite keys do not exist. |
| 02 | §2.1 (tex l. 347): "All TMRB results are anchored to a single calibration extracted from the Gaia DR3 phase spiral" plus [22, 37] | **Conflicts with M7** ("All TMRB results are anchored" is kept). Does not resolve M6. The Replace text does not match the tex (`\cite{GaiaDR3}`). |
| 03 | Table 3 caption (tex l. 1145): "Dimensional amplitudes normalised through …; dimensionless ratios (9 ln 9 + ln 3 and κ_CE/9) follow directly from the discrete group order 9 and κ_CE" | It does narrow toward M7 by splitting amplitudes from dimensionless ratios. But it **runs into M15** (approved): only ln 3 = ln Z_tors comes from the weights, and 9 ln 9 comes from the choice to count the orbit once, which §4.1 (tex l. 607–608) calls open (Gap 12). "Follow directly from the group order" is the overclaim M15 removes. Does not resolve M6. |
| **[37] check (bears on M6)** | Segments 01–03 and F7 cite [37] *The Galactic Piano Is Still Ringing* as the place where η_diff is "extracted" ("presumably", as F7 itself says) | **[37] does not derive 0.82 ± 0.02.** Details:<br>• Opened: Zenodo v4 tex (record 20262175, sha `13a33d07…`) and v1 text (record 19422604, sha `f33b9b30…`).<br>• v4 states the value as "Gaia-DR3-calibrated" and "fixed once by Gaia DR3 phase-spiral data". It says the value "propagates unchanged from the companion Celestial Holography paper [35] and the M-Theory Bulk Gravity Leakage construction [36]". At its Eq. (params) it cites `bressler2026_unified, gaia_dr3`.<br>• Neither version has a fit, likelihood or derivation from Gaia data. In v1 the value is a hard-coded input to the plotting code (`branch_shift = … * 0.82`).<br>• So citing [37] would move the citation to another of the author's papers that also asserts the number, and the chain points back to the series. M6 option A ("cite the work where η_diff is actually derived") is still unmet. George said he will send the real source.<br>• A side finding that is not from G1: the paper's bibitem says "v4", but its DOI 10.5281/zenodo.19422604 resolves to **v1.0** (2026-04-04, title "TMRB and Piano Mathematics"). The v4 DOI, 20262175, is the one the paper's own Changes item (v) names. The other Bressler bibitems show the same kind of mismatch against Changes (v) (UF 19192990 vs 20248650; CH 19696857 vs 20249096; BGL 19581289 vs 20276554; QG 19359426 vs 20272654). Only GP was resolved on Zenodo. |
| **04 (GEM-05)** | §3.1 (tex l. 489): "gives Q⁽ⁿ⁾ ~ M_Pl,4 after dividing by the compactification scale V₇^{2/7} = (G₄/G₁₁)^{−2/7} (or M_Pl,11²)" | **Dimensionally wrong.** With ħ = c = 1, [G₁₁] = L⁹ and [G₄] = L², so V₇ = G₁₁/G₄ has [L⁷]. Then:<br>• V₇^{2/7} = (G₄/G₁₁)^{−2/7} has [L²]. That part of the snippet is right.<br>• "or M_Pl,11²" is **inverted**: [M²] = L⁻². It could equal V₇^{2/7} only as M_Pl,11^{−2}, and only if V₇ ~ ℓ_11⁷.<br>• Q = η θ M_Pl,11³ has [L⁻³]. **Dividing** by V₇^{2/7} gives [L⁻⁵] = mass⁵, not a mass. Multiplying gives mass¹.<br>• But with M_Pl,4² = M_Pl,11⁹ V₇, Q·V₇^{2/7}/M_Pl,4 = M_Pl,11^{3/2} V₇^{3/14}. That equals 1 only if V₇ = M_Pl,11^{−7}, which means M_Pl,4 = M_Pl,11, i.e. no hierarchy. That contradicts the paper's G₄/G₁₁ hierarchy.<br>• So the replacement does not produce Q ~ M_Pl,4. The original "after absorbing factors of G₄/G₁₁" is unsupported, but the proposed fix is worse.<br>• No merge item covers l. 489. This is **new** as a location, but the proposed fix should be **refuted**. A fair fix would state the reduction as open or as a consistency condition (as Gap 2 already does for Q⁽¹⁾). |
| 05 | §6.1 "exact identity via Poisson summation" | Correct (13.4). Optional. The label `eq:weights` should be `eq:wn`. |
| 06, 07 | Mark the 30 M⊙ / 402 Hz benchmark as χ = 0 | Correct and harmless. They overlap S4 ("0.094 line widths for a non-spinning remnant"). In 07 the label sits inside the figure, not the tex. |
| 08 | §7.1 item 2: "mapped to t₀ = 0, which yields the smallest predicted shortening in Table 2 and is therefore the mapping most favourable to the prediction" | **Conflicts with M2 option B (approved).** "Therefore the mapping most favourable" is exactly what M2 corrects. It holds along the t₀ axis only. Along the fit-window axis, windows ≤1τ give smaller shifts (−0.024 to −0.049 at spin 0.69; `window_merge_check_output.txt`), and the secondary verdicts change. |
| 09 | §7.1 Result: a mapping caveat plus "independent human verification … is recorded" | The mapping caveat (frequency-domain, PSD-weighted IMR vs a time-domain fit; an exact test needs injection) is fair and matches merge §6 item 1. **The verification sentence is false (C2).** "Most favourable" again conflicts with M2. |
| 10 | Relabel the LHS of Eq. (21) as Δg_floor^95%(102 Hz) ≈ 1.6×10⁻¹⁶ | Arithmetic correct. It matches the paper's own prose ("bounds a ~100 Hz component of Δg, not Δg_TMRB itself", tex l. 1225–1227). **New relative to the merge.** S7 covers the JSON and docstring labels, not the displayed equation. |
| 11 | Add "Reviewed before r12 release by Gemini (Google)" to the AI disclosure | Premature until George decides. It also does not name the model or version (D27). |
| 12 | Revision item (viii) listing the Gemini refinements | It inherits the problems of 01–04 and 09: [37] as the "phase-spiral calibration paper", the wrong Eq. (8) wording and the "transcription audit note". It also omits the 15 approved MUST-FIX items. |
| 13 | Draft REVIEW_LOG | The "adopted" column holds **proposals** (C6). Severities as in C5. Its "External PDF status" line is accurate and contradicts the summary and segments 09, 14 and 16. |
| 14 | A replacement §7.1 Result paragraph | It is almost the r11 paragraph (tex l. 1000–1012) with segment 09's additions. What it has right and wrong:<br>• "EXCLUDED" (the registered label) next to "disfavoured" (the paper's own conclusion "under the assumptions of Gaps 17 and 18") is the **r11 wording, not a new contradiction**. EXCLUDED is the frozen script's label, and "disfavoured" is the scoped conclusion. M4's "disfavoured" is about Sen and the φ^{−N*} suppression, a different sentence, so there is no conflict with M4.<br>• It states "the five secondary combinations … are also excluded" with no mapping caveat. At the registered t₀ = 0 / 8τ mapping that is true (RUN1 output: all EXCLUDED). The window re-check shows the five-highest-SNR subset is CONSISTENT, NOT DISCRIMINATING at ≤1τ, and the subset without GW250114 is CONSISTENT or DISFAVORED at ≤1τ. M2 B requires that sentence. **PRIMARY stays EXCLUDED at every window.**<br>• It keeps "most favourable" (conflicts with M2).<br>• It contains the false or unsupported verification sentence (C2).<br>• It does not touch M1's sentences (abstract; Changes (i); §7.1 items 2–3), so the M1 overclaim would survive.<br>• It omits S3's content (GR outside the 90% region; selection caveat; GW250114 influence). |
| 15 | GRACE README note | The date claim is unsupported (C8). The ratio is correct. The ~230 claim is absent. It does not mention that the script's 10⁻¹⁹ outputs inherit the per-cm constant (S5). |
| 16 | Proposed commit message | **Not to be used.** It repeats the verification claim (C2) and the GEM-05 error, says "adopt" for items George has not decided, and leaves out the 15 approved MUST-FIX items. Nothing is committed without George's go. |

### 13.6 Coverage comparison with `GROK_TEAM_MERGED_v4r11.md` (coverage only; no decision changed)
The basis is the full reply (F1–F9), plus segments 01–16 where they add content. **M1–M15 were approved as written by George on 19 Nov 2026 at about 18:57 ET.**

| G1 item | Stated sev. (effective) | Merge item | Match | Note |
|---|---|---|---|---|
| F1 / GEM-01 / seg 09 | SHOULD-FIX | **M1**; merge §6 item 2; N1 | **Partial** | G1 agrees the clock proves order only. It rates SHOULD-FIX where M1 is MUST-FIX, which is the alternative Jimmy noted in D2. It re-verifies the frozen script (N1). **New:** the 49 s observation and the call for human verification of the transcription. But its premise, "far too short for a human", does not apply, since G1 itself says the AI (Claude) transcribed. The 49 s does not show reading **before** the registration (76d92c7), only that the numbers were in hand before d590909. This is merge §6 item 2, still open. The transcription was already checked against the PDF by AI (Sparks F1(iv)), but not by a human. |
| F2 / GEM-02 / seg 08–09, 14 | SHOULD-FIX | **M2**; N2; §6 item 1 (injection) | **Partial** | G1 confirms "most favourable" holds along the t₀ axis only within Table 2 (−0.095 vs −0.140/−0.181/−0.253 at spin 0.69; the Table 2 values check). That is M2's diagnosis. Its fix, though, **keeps** "therefore most favourable" (segment 08), and it never examined the fit-window axis, so it misses the mapping-dependence of the secondary verdicts (M2 B). **On the pSEOBNR injection stuck point,** G1 agrees an exact test needs injection into a PE pipeline. Its "sign opposition makes it unlikely that template-matching subtleties alone would bridge a ~0.165 gap" is reasoning, not computation, and it does not settle whether pSEOBNR would absorb the effect into mass, spin or amplitude. **The stuck point stays open.** |
| F3 | NOTE | N4 (and S1) | **Match (N4)**; partial (S1) | The numbers agree with N4. G1 does not raise the ensemble dependence (S1: 167/90 or 106/45) and did not open Sen. It raised neither M3 nor M4. |
| F4 / GEM-08 / seg 15 | NOTE | N5, N6; **S5** | **Match (N5, N6)**; **partial and conflicting (S5)** | "Zero by construction" and 4.19×10⁻⁹ agree. On the constant, G1's ~230 is wrong and S5's 2.34×10⁴ is right (13.4). |
| F5 / GEM-07 / seg 06–07 | MUST-FIX (**NOTE**) | S4; N7 | **Partial** | Same spin-0 labelling point as S4. The numbers agree with N7. |
| F6 | MUST-FIX (**NOTE**) | N7 | **Match** | Verified check, no fix. |
| F7 / GEM-03 / seg 01–03 | SHOULD-FIX | **M6**; **M7** | **Partial (M6)**; **match on the diagnosis (M7)** | Same diagnosis as M6 (the DR3 summary does not contain η_diff). G1 rates SHOULD-FIX where M6 is MUST-FIX (d). Its fix (cite [37]) does not supply a derivation (13.5). F7(2) has the same dependence split as M7, but segments 01 and 02 keep "All … anchored", and segment 03 conflicts with M15. |
| F8 / GEM-04 / seg 10 | SHOULD-FIX | S7 (numbers) | **Partial; new on Eq. (21)** | Relabelling the displayed equation is new. |
| F9 / GEM-06 / seg 05 | NOTE | (none; the same paragraph as M12) | **New** (optional wording) | It supports the "exactly" claim. It does not raise M12's factorisation and reason-(b) issue. |
| GEM-05 / seg 04 | SHOULD-FIX | none | **New location; the fix is dimensionally wrong** | See 13.5. |
| C2 claim (seg 09, 14, 16) | – | – | – | A false or unsupported statement proposed for the paper. Not a finding. |

**Merge MUST-FIX items G1 did not raise:** M3, M4, M5, M8, M9, M10, M11, M12, M13, M14 and M15. That is 11 of 15. Segment 03 actually moves against M15.
**Raised in part:** M1, M2 and M6. **Raised on the diagnosis:** M7 (F7(2)), but segments 01 and 02 contradict its fix.
**SHOULD-FIX:** S4 (partial), S5 (partial, with a wrong factor) and S7 (partial). Not raised: S1 (only adjacent), S2, S3, S6, S8 and S9.
**NOTE:** N1, N2, N4, N5, N6 and N7 are touched. N3 and N8–N11 are not.
**New relative to the merge:** the Eq. (21) relabel (F8, seg 10); the Poisson-identity wording (F9, seg 05); the §3.1 l. 489 location (GEM-05, whose proposed fix is wrong); and the 49 s / human-verification framing (F1).

### 13.7 What this means for weighting (§4.3)
- Gemini is a third model family. Its agreement on M1, M2, M6 and M7 (diagnoses) and on N1/N4–N7 (numbers) is cross-family agreement. That is weaker evidence than an instrument, and **it does not show those items are right**. Correlated errors across LLM families are documented (Kim et al. 2025, §11 C).
- Its silence on 11 MUST-FIX items is not evidence against them. G1 did not do a full pass of §2–§6, and several of those items (M3, M4, M8) need sources that G1 did not open.
- G1's main error (F4's factor) and its main process fault (C1/C2: claiming checks it did not do, and proposing that claim as paper text) are the kind of thing the G2 re-check and George's decision step exist to catch.

### 13.8 G1-followup (NOT blind, NOT part of G1)
- **What it is:** after George relayed our C1/C2 catch, Gemini replied again **in the same G1 chat** at about 8:33 PM ET (messages t482u–t484u), and sent a revised commit message at 8:34 PM ET (t485u). It is informed by our critique, so it is **not blind and not part of the Stage G1 record**. It is filed separately in `G1/followup/`.
- **Deviation D29:** our critique reached Gemini before Stage G2. The G1 chat is now contaminated. G2 must still run in a new fresh chat, and G2's prompt must say that the follow-up exists.
- **What it contains,** according to the parent's log (`G1F_reply_pasted_2026-11-19_2033.md`, sha `dad85818…a6a3`):
  - Gemini concedes that it never opened the arXiv:2607.19293 PDF. It says a later web search found only snippets matching Eqs. 21–22 on p. 23, and that the p. 24 intervals are unverified.
  - It changes its decisions column to "proposed".
  - It gives a corrected §7.1 Result paragraph, a table and a commit message.
- **Still unresolved:**
  - The corrected paragraph still says "human verification … is recorded in the Zenodo audit trail". **That is not yet true.** No human check of the six intervals has been done or recorded.
  - It says it "verified the commit sequence", but it saw the prompt's metadata only, not the git history.
  - Both points stay **unresolved, pending George's choice**. Recommended by the parent (Sparks): a human check of all six intervals against the arXiv PDF before r12. That would make a corrected sentence true rather than delete it.
- **t485u revised commit message: NOT TO BE USED.** It repeats the human-verification claim, which has not happened, and it leaves out the 15 approved MUST-FIX items.
- **Capture gap (D30): closed in r4.** The verbatim files are saved and hashed (§13.9). (r3 text: "the verbatim text of t482u–t485u was not passed to this executor … still to be saved by the parent".)


### 13.9 G1-followup files and a review of their contents (added in r4)
| File (`G1/followup/`) | sha256 | Drive id |
|---|---|---|
| G1F_reply_pasted_2026-11-19_2033.md (parent's summary log) | `dad858187a315d1f1960970eff337680acd85bbfaee3d77c1bba66f6e598a6a3` | (box only) |
| t482u_preamble_2026-11-19_2033.md | `6e41c29d9a861c3a2419e6286392e9a38527db536133a4856ca71d589d396578` | [Drive ID withheld] |
| t483u_result_paragraph_2026-11-19_2033.tex | `1be231c5885a81f35d8eae3496e9a57a76b4647cb815d3d6ba3966a9f318971f` | [Drive ID withheld] |
| t484u_findings_table_proposed_2026-11-19_2033.md | `b0a0bdd2c95e83f56b390bbd1159baf2852ce99e86b1c1ec5255822e61fe4efe` | [Drive ID withheld] |
| t485u_commit_msg_DO_NOT_USE_2026-11-19_2034.txt | `e29c80fe24b5f0824470953c2bea16a6036f0e6b393be76134d419ecf1753ba6` | [Drive ID withheld] |
| G1F_SHA256.txt (the list above) | as stored on the box | [Drive ID withheld] |

**Status: NOT blind, NOT part of G1 (D29).** It is recorded as Gemini's response to our critique.

- **t482u (preamble):** it concedes the C1/C2 overstatement: "arXiv:2607.19293 was not opened at all" in the review pass, and "a later web search surfaced text snippets matching Eqs. (21)–(22) on p. 23", with p. 24 "unverified (inconclusive)". It also concedes that only the author records decisions. The **web-search snippet claim is unverified by us**: no URL, snippet text or hash was given.
- **t483u (corrected Result paragraph): UNRESOLVED, pending George's choice.**
  - "**human verification** of the transcribed GWTC-5.0 intervals … **is recorded** in the Zenodo audit trail" is **not yet true**. No human check has been done or recorded; the only check against the PDF is the Grok seats' AI check (§13.3 C2).
  - "Independent review **verified the commit sequence**": Gemini saw only the commit times given in the prompt, not the git history (its own segment 13 says so). The Grok team checked the order against `git log` and GitHub push events, but that is not what this sentence says.
  - It still carries "therefore most favourable" (conflicts with M2 B), states "also excluded" for the secondaries with no caveat about the mapping, and uses the wrong label `tab:kerr_spin`.
  - **Recommended by the parent (Sparks): George does the human check of all six intervals against the arXiv PDF (sha `4ab5df87…ab101`, eqs. 21–22 p. 23, and p. 24) before r12.** The sentence can then be made true, naming who checked and when, rather than deleted.
- **t484u (findings table, all "proposed"):** the decision column is now correct in form.
  - GEM-01 now reads "require human verification of all six … intervals". That agrees with the parent's pick, and it is still only a proposal.
  - **GEM-03 (cite [37]) and GEM-05 (divide by V₇^{2/7}, "or M_Pl,11²") are unchanged and still wrong** (§13.5).
  - GEM-08 still says "superseded" without the corrected factor (2.34×10⁴) or the note that the script's ~10⁻¹⁹ outputs inherit the constant (S5).
  - The table has no Markdown header-separator row as pasted, and it still omits F3 and F6.
- **t485u (revised commit message): NOT TO BE USED.** It still says "note human transcription verification in the Zenodo audit trail" (not true) and leaves out the 15 approved MUST-FIX items. It also carries the GEM-03 and GEM-05 errors.

---
*End of record. Corrections go forward as new versions of this file, never as silent edits.*


---

## 14. Author decisions of 19 November 2026, 9:06 PM ET (added in r5)

George is the author. The decision columns below are filled by him, at 9:06 PM Eastern Time (ET, UTC−5), in response to the walk-through of the open points (messages t489u–t490u). Reviewers only propose. Nothing in this section is committed to any repository, and the soft-hair paper is not edited here.

### 14.1 Decision rows

| ID | Item | George's decision | Reason (as given or as applied) | ET | Follow-up |
|---|---|---|---|---|---|
| AD-1 | The six GWTC-5.0 Eq. 21–22 and p. 24 intervals | **Adopted as verified** by the method below | The six intervals are verified by deterministic code extraction from arXiv:2607.19293v1 (PDF sha256 `4ab5df879daa2f4acd2d9fac32e64f5daf78d8fddd73ba5d76ecc5a2047ab101`, matching a fresh download). Four were exact PASS. The two stacked Eq. 22 entries (items 2 and 3) were UNPARSED by regex, matched by bbox pairing, and confirmed by George's visual check of the highlighted page 23. The verdict-script rerun is identical (EXCLUDED). Files are in `/workspace/tmrb-papers-review/grok_checks/gwtc5_code_check_2026-11-19/` (`CHECK_RESULT.md` sha256 `d3968afe13b9f668e2b4b834f23a9f9ed4cd311d5e11f3bb534df2b86b1be2e4`). | 19 Nov 2026, 9:06 PM ET | Use only this method in any r12 sentence about the check. |
| AD-2 | What the paper may claim about that check | **Adopted.** The sentence must state exactly this method: code extraction plus the author's visual check of two stacked entries. No other human verification is claimed. | States the facts of AD-1 and no more. | 19 Nov 2026, 9:06 PM ET | Draft the r12 sentence from this wording only, when George authorises an edit. |
| AD-3 | Gemini G2 informed re-check | **Cancelled.** G1 and the G1-followup stay on record as proposals only. | George judged Gemini a poor fit for this work after G1 claimed source checks it did not do. Future models may be better. The planned G2 stage is not run. | 19 Nov 2026, 9:06 PM ET | D31. G2 prompt drafts left unused. |
| AD-4 | Gemini-suggested text | **Declined in full.** No Gemini-suggested text is used anywhere: not in segments, not in the t483u paragraph, not in the t484u table, and not in the t485u / segment-16 commit messages. | The suggested wording carried claims (a completed human check; a commit-sequence verification Gemini did not perform; GEM-03 and GEM-05 errors) that this record has already rejected. | 19 Nov 2026, 9:06 PM ET | Those drafts remain in `G1/followup/` as a historical file, not as source text for r12. |
| AD-5 | M6, the source of η_diff = 0.82 ± 0.02 | **Under investigation** at the decision time; Job B (a full read of the Galactic Piano Zenodo record and related deposits) was commissioned in the same instruction. | George asked to review all documents associated with the Galactic Piano on Zenodo before deciding. | 19 Nov 2026, 9:06 PM ET | Job B findings are in §14.2 and in `/workspace/galactic_piano_zenodo/ETA_DIFF_PROVENANCE.md`. A wording choice for r12 remains for George (three options and a pick are offered there). |

### 14.2 Job B result (completed about 21:15 ET the same evening)

The investigation commissioned under AD-5 is complete. The paper is still not edited. The full version table, hashes, quotation sites, citation checks and three options are in `ETA_DIFF_PROVENANCE.md`. In brief:

- The Galactic Piano concept (`19422603`) has three versions and no v2: v1.0 (doi:10.5281/zenodo.19422604, 4 April 2026 — this is the DOI in soft-hair [37]), v3 (19701629, 22 April), and v4 (20262175, 17 May). Related Unified, VASIMR, M-Theory, holography, QGGPf and PTRH deposits were also opened.
- The approximate value ~0.82 first appears earlier, on 23 March 2026, in Unified Framework v1.0 (doi:10.5281/zenodo.19192990), pp. 4 and 8, as an ion-acoustic-wave diffraction efficiency, with the formula `η_diff = 1 − exp(−D β k dx) ~ 0.82`. The ±0.02 is not in that paper. A rerun of the printed formula does not yield 0.82: `dx` is omitted, and the nearby Debye length gives 0.993.
- The form **0.82 ± 0.02 attributed to Gaia DR3** first appears in Galactic Piano v1.0, p. 1. No later version, and no companion deposit that was opened, *derives* the value. Code hardcodes `0.82`. The 1.2σ figure in v4 is (1.0 − 0.82) / 0.15, not a Gaia fit.
- The cited Gaia DR3 summary (A&A 674, A1; text opened as arXiv:2208.00211v1) does not contain 0.82 and does not discuss the Antoja phase spiral. Antoja et al. 2018 (arXiv:1804.10196) does not contain 0.82 and used Gaia DR2.
- Soft-hair [37] is labelled "v4" but points at the v1.0 DOI. Eq. (etadiff) in the soft-hair paper cites `GaiaDR3`, which does not support the number.

M6 therefore remains an open wording item for George, with three options and a pick in the provenance file: keep the number as an assumed TMRB parameter and stop citing the Gaia DR3 summary as the measurement (the pick); or point to the incomplete Unified v1 formula with its limits stated; or leave it labelled as an undocumented calibration pending an author derivation.

---

*End of record. Corrections go forward as new versions of this file, never as silent edits.*


---

## 15. Author decision AD-6 of 19 November 2026, 10:32 PM ET (added in r6)

This file, `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r6.md`, is a forward version of `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r5.md` (sha256 `f47a5fe821b27bad444899b54b8fdab9d7b4c3c0c8893782cb11338f168575b2`, left unchanged). The r5 body above is copied verbatim. r6 appends only this section. Nothing is committed to any repository, and the soft-hair paper is not edited here.

George is the author. The decision below was given at 10:32 PM Eastern Time (ET, UTC−5, America/New_York), in message t491u, as the choice “1”. That choice refers to option 1 of the M6 wording options recorded in §14.2 and in `/workspace/galactic_piano_zenodo/ETA_DIFF_PROVENANCE.md` (Option A, with the short first-appearance note from that record’s pick). Reviewers only propose. **Gemini items remain proposals only. No Gemini-suggested text is used (AD-3, AD-4).** Those earlier decisions stay in force: Stage G2 remains cancelled, and G1 and the G1-followup remain on record as proposals only.

### 15.1 Decision row

| ID | Item | George's decision | Reason (as given or as applied) | ET | Follow-up |
|---|---|---|---|---|---|
| AD-6 | M6, wording for η_diff = 0.82 ± 0.02 | **Option 1 adopted.** η_diff = 0.82 ± 0.02 is stated as an assumed TMRB parameter. The Gaia DR3 / Antoja citation for it is dropped. A short note records that the value first appears in Unified Framework v1.0 (DOI 10.5281/zenodo.19192990) as a plasma diffraction efficiency whose printed formula omits dx and does not reproduce 0.82. The Galactic Piano v4 “1.2σ” figure is (1 − 0.82)/0.15 and must not be framed as a Gaia result. Soft-hair [37] (`BresslerGP2026`) has its DOI corrected to 10.5281/zenodo.20262175 so the existing “v4” label is true; [37] is not cited as the source of the number. | George chose option 1 (t491u, 10:32 PM ET). This matches Option A of the Job B provenance record, with the short first-appearance note from that record’s pick. | 19 Nov 2026, 10:32 PM ET | Draft r12 wording for review only, in `R12_PROPOSED_EDITS_M6_37_GWTC5.md`. Do not edit the paper until George authorises an edit. |

### 15.2 Notes applied in the r12 draft (not yet applied to the paper)

- The 1.2σ figure named above is from Galactic Piano v4 / the PTRH survey wording, computed as (1.0 − 0.82)/0.15 against the null model η_null = 1.0 ± 0.15. It does **not** appear in `bh_soft_hair_v4.tex`. The r12 draft therefore does not insert it into the paper; it only records that it must not be framed as a Gaia result if it is mentioned later.
- Antoja et al. is not cited in the current tex, so there is no Antoja bibitem to remove. The Gaia DR3 citation on eq. (etadiff) and in the conclusion is what is dropped.
- AD-1 and AD-2 remain in force: any r12 sentence about the six GWTC-5.0 intervals must state exactly the method recorded there (deterministic pdftotext extraction with pass rules fixed before running; four direct matches; two stacked-error Eq. 22 entries matched by text-position pairing and confirmed by George Bressler’s visual check of the highlighted page). No other human verification is claimed. A proposed sentence is in the r12 draft, not in the paper.
- Approved M7 (18:57 ET the same day: all 15 MUST-FIX items as written) still applies to the same sentences that M6 rewrites: the draft drops the false “All results anchor…” wording and limits η_diff to amplitude predictions, rather than restating a universal anchor under a new source label.

---

*End of record. Corrections go forward as new versions of this file, never as silent edits.*


---

## 16. Author decision AD-7 of 20 November 2026, 9:24 AM ET (added in r7)

This file, `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r7.md`, is a forward version of `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r6.md` (sha256 `2d6e43f6a3bdef51b5ca8b2ba4560a18be28b8a9571b6e326c1b1516b7c18a23`, left unchanged). The r6 body above is copied verbatim. r7 appends only this section. Nothing is committed to any repository, and the soft-hair paper is not edited here.

George is the author. The decision below was given at 9:24 AM Eastern Time (ET, UTC−5, America/New_York) on Friday 20 November 2026: remove the uncited Gaia DR3 bibitem and add an old-to-new reference numbering note. Reviewers only propose. Gemini items remain proposals only; no Gemini-suggested text is used (AD-3, AD-4). AD-1, AD-2 and AD-6 remain in force.

### 16.1 Decision row

| ID | Item | George's decision | Reason (as given or as applied) | ET | Follow-up |
|---|---|---|---|---|---|
| AD-7 | Whether to keep or delete the unused `\bibitem{GaiaDR3}` after the M6 wording drops its cites | **Remove it.** The uncited Gaia DR3 bibliography entry (old [22]) is deleted in the r12 wording. An old-to-new reference numbering note is added. | George chose this at 9:24 AM ET on 20 November 2026, answering the r6 draft flag that deleting [22] would shift later numbers (old [37] becoming [36]). | 20 Nov 2026, 9:24 AM ET | Deletion is firm in `R12_PROPOSED_EDITS_M6_37_GWTC5_v2.md`. The full map is in §16.3. Do not edit the paper until George authorises an edit. |

### 16.2 How the map was obtained

The paper uses `\usepackage{natbib}` with `\setcitestyle{numbers,square,sort&compress}` and a manual `\begin{thebibliography}{99}`. In that setup, printed numbers follow `\bibitem` order, not citation order.

- The existing compiled v4 r11 PDF (`bh_soft_hair_v4.pdf`) was opened with `pdftotext`. Its References list is [1]–[43] with no gaps, and every label matches the tex `\bibitem` order. In particular, [22] is the Gaia DR3 summary and [37] is *The Galactic Piano Is Still Ringing*.
- The proposed r12 tex (temp copy only) deletes only `\bibitem{GaiaDR3}` and does not reorder any other entry. `\cite{GaiaDR3}` falls from two uses (eq. (etadiff) and the conclusion) to zero. No other `\cite` key is added or removed. The tex contains no hardcoded `[n]` citation numbers.
- `pdflatex` is not installed on the box, so a fresh compile of the temp copy was not run. A new compile is not required for this map: the style, the r11 PDF, the bibitem order, and the remaining `\cite` usage already fix it.
- Two other bibitems, `\bibitem{GWOSC2021}` (old [32]) and `\bibitem{GRACE_RL06}` (old [33]), are already uncited in r11 and remain in the list, so they still shift. They were not part of this decision.

**Earlier review documents use the OLD numbering.** That includes protocol versions r1–r6 (and the r5/r6 discussion of soft-hair [37] and Gaia [22]), `CHECK_RESULT.md`, `/workspace/galactic_piano_zenodo/ETA_DIFF_PROVENANCE.md`, and the Grok and Gemini review replies (`GROK_TEAM_MERGED_v4r11.md`, G1 and G1-followup files, and related packets). Those files are left unchanged. From r7 and the v2 proposed-edits draft onward, statements about the *proposed r12 paper* use the new numbers, and mention the old number when a cross-reference to earlier review text is needed.

### 16.3 Full old → new reference number map

21 references shift (old [23]–[43] become new [22]–[42]). Old [1]–[21] are unchanged. Old [22] is removed. **Old [37] becomes new [36].**

| Old (r11 / earlier review docs) | New (proposed r12) | Bibitem key | Work | Change |
|---|---|---|---|---|
| [1] | [1] | `Damour1978` | Damour, Black-hole eddy currents | unchanged |
| [2] | [2] | `KSS2005` | Kovtun, Son, Starinets, viscosity / KSS bound | unchanged |
| [3] | [3] | `Hawking1975` | Hawking, Particle creation by black holes | unchanged |
| [4] | [4] | `AharonovEtal1987` | Aharonov, Casher, Nussinov, unitarity puzzle | unchanged |
| [5] | [5] | `Susskind1993` | Susskind, Thorlacius, Uglum, stretched horizon | unchanged |
| [6] | [6] | `CKW2000` | Coffman, Kundu, Wootters, Distributed entanglement | unchanged |
| [7] | [7] | `AMPS2013` | Almheiri et al., complementarity or firewalls | unchanged |
| [8] | [8] | `Penington2020` | Penington, Entanglement wedge / information paradox | unchanged |
| [9] | [9] | `HawkingPerryStrominger2016` | Hawking, Perry, Strominger, Soft hair on black holes | unchanged |
| [10] | [10] | `Weinberg1965` | Weinberg, Infrared photons and gravitons | unchanged |
| [11] | [11] | `BMS1962` | Bondi, van der Burg, Metzner, gravitational waves | unchanged |
| [12] | [12] | `Strominger2014` | Strominger, BMS invariance of gravitational scattering | unchanged |
| [13] | [13] | `Christodoulou1991` | Christodoulou, Nonlinear nature of gravitation | unchanged |
| [14] | [14] | `Donnay2016` | Donnay et al., Supertranslations and superrotations | unchanged |
| [15] | [15] | `GepnerQiu1987` | Gepner, Qiu, Modular invariant parafermion partitions | unchanged |
| [16] | [16] | `ZamoFateev1987` | Fateev, Zamolodchikov, parafermion currents | unchanged |
| [17] | [17] | `AJL2004` | Ambjørn, Jurkiewicz, Loll, Emergence of a 4D world | unchanged |
| [18] | [18] | `AJL2005` | Ambjørn, Jurkiewicz, Loll, Spectral dimension | unchanged |
| [19] | [19] | `Vafa1986` | Vafa, Modular invariance and discrete torsion | unchanged |
| [20] | [20] | `DijkgraafWitten1990` | Dijkgraaf, Witten, Topological gauge theories | unchanged |
| [21] | [21] | `Schoen1970` | Schoen, Infinite periodic minimal surfaces | unchanged |
| [22] | — (removed) | `GaiaDR3` | Gaia Collaboration, Gaia DR3 summary (A&A 674, A1) | deleted; no remaining `\cite` |
| [23] | [22] | `GibbonsHawking1977` | Gibbons, Hawking, Action integrals and partition functions | shifts down by 1 |
| [24] | [23] | `LevinWen2006` | Levin, Wen, Detecting topological order | shifts down by 1 |
| [25] | [24] | `KitaevPreskill2006` | Kitaev, Preskill, Topological entanglement entropy | shifts down by 1 |
| [26] | [25] | `DiFrancesco1997` | Di Francesco, Mathieu, Sénéchal, *Conformal Field Theory* | shifts down by 1 |
| [27] | [26] | `Page1993` | Page, Information in black hole radiation | shifts down by 1 |
| [28] | [27] | `Sen2012` | Sen, Logarithmic corrections to black hole entropy | shifts down by 1 |
| [29] | [28] | `Leaver1985` | Leaver, Quasi-normal modes of Kerr black holes | shifts down by 1 |
| [30] | [29] | `Stein2019` | Stein, qnm Python package | shifts down by 1 |
| [31] | [30] | `BertiCardosoWill2006` | Berti, Cardoso, Will, gravitational-wave spectroscopy | shifts down by 1 |
| [32] | [31] | `GWOSC2021` | Abbott et al., Open data from the third observing run | shifts down by 1 (already uncited in r11) |
| [33] | [32] | `GRACE_RL06` | Wiese, Landerer, Watkins, GRACE mascon leakage | shifts down by 1 (already uncited in r11) |
| [34] | [33] | `BresslerUF2026` | Bressler, TMRB Unified Framework | shifts down by 1 |
| [35] | [34] | `BresslerCH2026` | Bressler, Resonant Celestial Holography | shifts down by 1 |
| [36] | [35] | `BresslerBGL2026` | Bressler, M-Theory Bulk Gravity Leakage | shifts down by 1 |
| [37] | [36] | `BresslerGP2026` | Bressler, *The Galactic Piano Is Still Ringing* | shifts down by 1 |
| [38] | [37] | `BresslerQG2026` | Bressler, TMRB Predictions for NASA QGGPf | shifts down by 1 |
| [39] | [38] | `BresslerMellin2026` | Bressler, TMRB Mellin Transform Notebook | shifts down by 1 |
| [40] | [39] | `BresslerPrismatic2026` | Bressler, Einstein Equations from Prismatic Curvature | shifts down by 1 |
| [41] | [40] | `BresslerX24si2026` | Bressler, X24si | shifts down by 1 |
| [42] | [41] | `GWTC5TGR` | Abac et al., GWTC-5.0: Tests of General Relativity | shifts down by 1 |
| [43] | [42] | `BresslerSurvey2026` | Bressler, PTRH Survey/Synthesis | shifts down by 1 |

Examples: Gaia DR3 [22] is removed; Gibbons and Hawking [23] → [22]; Levin and Wen [24] → [23]; Unified Framework [34] → [33]; Celestial Holography [35] → [34]; Bulk Gravity Leakage [36] → [35]; Galactic Piano **[37] → [36]**; GWTC-5.0 [42] → [41]; PTRH Survey [43] → [42]. After this change, new [37] would be QGGPf (`BresslerQG2026`), not Galactic Piano.

---

*End of record. Corrections go forward as new versions of this file, never as silent edits.*

## 17. Author decision AD-8 of 21 November 2026, 4:17 PM ET (added in r8)

This file, `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r8.md`, is a forward version of `X24SI_HITL_REVIEW_PROTOCOL_v4r11_r7.md` (sha256 `da2e70a64cfcd1478d8202955b0ace68177145942a88389ead7cd875bc0c2fcb`, left unchanged). The r7 body above is copied verbatim. r8 appends only this section.

George is the author. The decision below was given at 4:17 PM Eastern Time (ET, UTC−5, America/New_York) on Saturday 21 November 2026 (msg context t499u / option: go with the eight picks): accept all eight picks D1–D8 exactly as listed in `R12B_PROPOSED_EDITS.md` / `AUDIT_MERGE_r12.md` §6, and apply the full proposed r12b set (4 MUST-FIXES M01–M04 and the 27 SHOULD-FIXES) on the box only. Reviewers only propose. Gemini items remain proposals only; no Gemini-suggested text is used (AD-3, AD-4). AD-1, AD-2, AD-6 and AD-7 remain in force. Nothing is committed or pushed.

### 17.1 Decision row

| ID | Item | George's decision | Reason (as given or as applied) | ET | Follow-up |
|---|---|---|---|---|---|
| AD-8 | The eight open r12b picks (D1–D8) from the 21 Nov audit merge | **Accept all eight picks**, and apply the full r12b proposed set (MUST-FIXES M01–M04, the 27 SHOULD-FIXES, and D1–D8 as written). If a SHOULD-FIX conflicts with a D pick, the D pick wins. | George chose this at 4:17 PM ET on 21 November 2026, answering the merge's options-and-picks list. | 21 Nov 2026, 4:17 PM ET | Authorised apply is in this pass, box only; no git commit or push. |

### 17.2 The eight picks, listed

| Pick | Item | Accepted wording / action |
|---|---|---|
| D1 | AD-1/AD-2 GWTC sentence, “before the run” (R12B-M01, lines 1011–1012) | Change to **“before the check was run.”** Does not change who checked, or the four PASS / two stacked / visual-check facts. |
| D2 | Bressler bibitem version labels vs DOIs (R12B-S14) | Point each labelled bibitem at the version DOI named in Changes v2 (v): UF v3 → `10.5281/zenodo.20248650`; CH v4 → `10.5281/zenodo.20249096`; BGL v10a → `10.5281/zenodo.20276554`; QGGPf v4 → `10.5281/zenodo.20272654`. Keep the footnote at l.348 citing Unified Framework v1.0 / `10.5281/zenodo.19192990` as the first-appearance note. Galactic Piano [36] `10.5281/zenodo.20262175` is unchanged (AD-6). No renumbering. |
| D3 | Uncited [31] GWOSC2021 and [32] GRACE_RL06 (R12B-S15) | **Cite them where the data are used.** Numbering is unchanged (42 refs; the AD-7 map stays in force). Do not delete the bibitems. |
| D4 | Title still says “Resolution” (R12B-S26) | Retitle **“A Proposed TMRB Soft-Hair Resolution of the Black-Hole Information Paradox”** (title and `pdftitle`). |
| D5 | v4 AI disclosure (R12B-S13) | Add one line: Grok (xAI) review agents proposed corrections, and the author (George) chose which to adopt. |
| D6 | “The registrant’s statement” unnamed (R12B-S12) | Name the registrant as **Claude**, once, in §7.1 item 3, with a pointer to the AI disclosure. |
| D7 | M4 “disfavoured” leftover sites (R12B-S20) | Extend the clause that Sen’s analysis disfavours the $\varphi^{-N_*}$ suppression to the **abstract, intro item 3, and conclusion**. This finishes M4 at leftover locations; it does not re-open M4. |
| D8 | Sen quotation (R12B-S07) | Use only the packet-supported verbatim phrase **“based on naive power counting arguments.”** Do not adopt the longer Sen rewrite that rested on a PDF outside the r12 audit source list. |

### 17.3 Apply-time log (D pick vs SHOULD-FIX)

No SHOULD-FIX in the applied r12b set required a wording that contradicted a D pick. Two nearby alternatives were already declined by the picks and were not applied:

- D8 wins over Jimmy’s longer Sen rewrite (a SHOULD alternative in J-03). The applied text uses only “based on naive power counting arguments.”
- D2 wins over the narrower “relabel [33] only” option (W-4). All four named bibitem DOIs are updated; the v1.0 footnote is kept.

### 17.4 Method check (AAR, 1st–4th order), and the S6 lesson

**1. What should happen, and how will we know?** The locked r12 draft (sha256 `22a6b2b3…`) is snapshotted, the authorised r12b set is applied in place (sha256 expected `e087f067…` from the pre-decision temp copy), the paper is recompiled, the listed greps and the 42-ref AD-7 map still hold, and r8, the r12→r12b diff and the new PDF are uploaded to the private review folder. We will know it worked when those hashes and checks are recorded and nothing has been committed or pushed.

**2. What is likely, including how it goes wrong?** The apply is a copy of an already-built temp tex, so the wording risk is low. The compile should stay at 24 pages, or close to it, with 42 references and no undefined citations. Residual risk is a missed grep (for example “the run” still appearing in the registration-clock sentences, which is correct and must not be deleted) or a figure caption/PDF pagination shift. The S6 forecast already missed on volume; this pass should not treat “the MUST-FIXES are applied” as “every leftover is gone” without running the claim greps.

**3. Why a difference would appear.** If a check fails, the likely cause is a reuse of a phrase (“the run,” “excluded,” “Weinberg”) outside the intended sentence, or a bibtex-style compile against a manual `thebibliography`. If the page count moves, it is the longer hedges, not a new section.

**4. What we will sustain or change, now, before acting.**

- **Sustain:** snapshot before apply; D picks win over conflicting SHOULD wording; AD-1–AD-7 left in force; no Gemini text; no commit or push; claim-level greps after the apply; public wording in plain words.
- **Change / lesson from the S6 forecast miss:** the pre-review forecast predicted MUST 0–2 / SHOULD 4–8 / NOTE 2–5 and a near-clean GWTC sentence. The merge was 4 MUST / 27 SHOULD, and “before the run” in the GWTC sentence was a real defect. Tight expected counts, written before a claim-grep, under-count. Future forecasts should treat such bands as a lower bound unless a pre-grep has already been run, and should not treat a clean *content* check as a clean *sentence* check.

**Impacts, future-paced (of applying r12b on the box, still uncommitted):**

- **1st order:** the paper text becomes congruent at the leftover intro, changelog, endpoint, 230 Myr, GWTC-check wording, Sen quote, title, disclosure, and the accepted D2–D7 sites.
- **2nd order:** a reader who opens the abstract, intro, changelog, body or conclusion gets the same claim strength. The registered EXCLUDED verdict and the “proposed” framing no longer compete with withdrawn limits.
- **3rd order:** later loops can audit by claim-grep, and the S6 miss is on the record as a procedure lesson, not only as a score.
- **4th order:** trust in the method, measured against the betterment of all humanity, is served if the public freeze (when George later authorises a commit) is of this congruent text, and if the record stays honest that r12 as first applied had leftovers.

**Sniff test.** Passes: the apply is authorised, bounded, and reversible (the r12 snapshot is kept). Proceed on the 85% solution. What remains open is a later commit decision, and the optional NOTES that were not in the r12b MUST/SHOULD set.

---

## 18. Author decision AD-9 of 21 November 2026, 4:27 PM and 4:51 PM ET (added in r9)

George is the author. Two choices were given on Saturday 21 November 2026 (Eastern Time, UTC−5):

### 18.1 Decision row

| ID | Item | Decision | Time | Notes |
|---|---|---|---|---|
| AD-9a | What to do before committing r12b | **Option 1 adopted:** hold the commit; run a future-paced referee review (a referee report pictured a year out, then back-cast to what must change now) and an independent symbolic and numerical math check of every equation and quoted number | 4:27 PM ET | Prompted by the S6 forecast miss of AD-8 (§17.4) and George's question whether a higher-order math or reasoning capability was missing |
| AD-9b | What to apply from that pass | **Option 1 adopted:** apply the 2 MUST-FIXes (F-M1, F-M2) and the 6 SHOULD-FIXes that need no author decision (F-S1, F-S2, F-S3, F-S4, F-S6, F-S8) as r12c. Do **not** apply F-S5 or F-S7 or the deferred r11 SHOULD-FIXes; list them as open. No commit or push until George sees the diff | 4:51 PM ET | AD-1–AD-8 remain in force; no Gemini text; AD-7 numbering map unchanged (42 refs) |

### 18.2 What the pass found and what was applied

- Pass folder: `/workspace/tmrb-papers-review/future_aar_math_r12b_2026-11-21/` (FORECAST written and hashed before reading for findings, sha256 `00ebe127…`; MATH_CHECK; FUTURE_REFEREE_AAR; FORECAST_SCORE; SUMMARY; scripts with one run command).
- Math check of r12b: 80 items, 61 PASS, 6 FAIL, 13 NOT-CHECKABLE. Every quoted number reproduced (Table 2 re-fitted independently: 20/20 within 0.05 points). Five of the six FAILs were claims labelled as derived or fixed that are choices, inputs or dimensionally unsupported; one was an order-of-magnitude slip (J-20, NOTE).
- New findings: 2 MUST, 8 SHOULD, 7 NOTE. Neither MUST was in the recursive r12 team audit (§17).
- Forecast score: 13/20 interval predictions hit; Brier 0.10. The systematic miss was again "a choice or input presented as derived" (forecast 1–2, found 4).
- r12c applied on the box (uncommitted): snapshot `revisions/bh_soft_hair_v4_r12_pre_r12c_backup_2026-11-21.tex` (= r12b, sha256 `e087f067…`); edit script `revisions/edit_v4_r12c.py` (each replacement asserted to match once); diff `revisions/bh_soft_hair_v4_r12b_to_r12c.diff`; PDF `revisions/bh_soft_hair_v4_r12c.pdf`. F-S8 title and DOI were checked against Crossref before editing (Ambjørn, Jurkiewicz, Loll, "The Spectral Dimension of the Universe is Scale Dependent", Phys. Rev. Lett. 95, 171301 (2005)); key and number unchanged.
- Re-check of r12c: the tex-reading ledger check (`scripts/tex_ledger_check.py`, run by `run_all.sh`) gives 8/8 FAIL on r12b and 0/8 on r12c. The numeric checks are unchanged (no number was edited).
- Open after r12c (not applied, by AD-9b): F-S5 (Gauss–Bonnet non-universality; needs a new reference), F-S7 (no live derived prediction remains); the r11 SHOULD-FIXes deferred on 19 Nov (S1, S2, S3, S5, S6, S7, S8, S9); the new NOTEs N1–N7; earlier NOTEs J-20, J-21, J-22, N-10.

### 18.3 Method change (a): status ledger before every audit

Before any reviewer reads the paper for findings, one seat builds a ledger with one row per quantity or claimed result:

| Quantity / claim | Line(s) | Status (derived · chosen · assumed · input) | Where the status is established | Verb the text uses | Match? |
|---|---|---|---|---|---|

Rules: "derived" requires a derivation in this paper or a cited derivation that was opened; anything set by hand is "chosen"; anything taken on trust is "assumed"; anything taken from data or another paper is "input". A row fails when the verb claims more than the status ("follows", "fixes", "predicts", "derived", "no free coefficient" on a chosen, assumed or input quantity). Failing rows go to the audit as candidate findings. Where possible the ledger check is made machine-readable (as in `tex_ledger_check.py`) so it can be re-run on each revision.

Why: every number in r12b reproduced, but M04 (21 Nov morning) and four of today's findings (E13, E20, E33, E75) were status-label errors. A ledger would have caught all five before review.

### 18.4 Method change (b): recursion and future pacing, two distinct, linked parts

**Human-in-the-loop recursive reasoning.** Each pass is fed back on the last. The outcome of one turn (something learned, or a named stuck point) becomes the next turn's input, and George's judgement decides what counts. It looks backward and sideways: is this pass consistent with the text, the earlier passes and the decisions already made?

**Future pacing.** Start from a pictured future outcome (for example, the referee report a year out, or the paper after refereeing) and back-cast to what must change now. It sets where the loop aims: not "is this consistent with what we did", but "what would we have needed to have done".

**How they link.** Future pacing sets the target and generates candidate findings; recursion tests those candidates against the text, the sources and George's judgement, and feeds the result into the next pass. Each needs the other: future pacing without recursion is speculation; recursion without future pacing converges on internal consistency.

**Recursion alone does not include future pacing.** Today's evidence: the recursive r12 team audit (three seats, merged, 4 MUST / 27 SHOULD) passed r12b's text as consistent with the decisions. The future referee review plus symbolic check, run on the same r12b afterwards, found 2 MUST-FIXes the recursive audit missed (F-M1, ln 3 presented as derived; F-M2, "no free coefficient" against an assumed parameter), plus six SHOULD-FIXes and a bibliographic mismatch missed by four earlier rounds. The future-paced findings were of a different kind: literature-level (a constant entropy term is not universal) and framing-level (no live derived prediction remains), which no consistency check produces. One comparison is not proof; this is recorded as provisional and will be re-tested on the next revision by running both parts and scoring them separately.

**Where it sits in the loop (proposed, until George approves the ordering):** forecast (hashed) → status ledger → future-paced referee review and back-cast → recursive team audit → symbolic math check → merge → George's decision → forecast score at S6.

### 18.5 Method check (AAR, 1st–4th order) for AD-9

1. **Should happen:** r12c fixes exactly the eight authorised items, compiles cleanly, keeps 42 refs and the AD-7 map, and the re-check shows the targeted FAILs gone. 2. **Likely:** as planned; risk was a replacement matching twice or a stray "fixes" elsewhere — guarded by match-once assertions and greps. 3. **Why a difference would appear:** a phrase reused elsewhere, or the numeric script's statuses not reading the tex (addressed by adding the tex-reading ledger check). 4. **Sustain:** snapshot first, no commit without George, open items listed rather than silently applied. **Change:** ledger and future pacing become standing steps.
Impacts: 1st, the headline entropy term and the charge formula are labelled honestly; 2nd, a referee meets fewer self-contradictions; 3rd, later revisions are audited for status labels automatically; 4th, trust in the method rests on calibrated claims, which serves readers broadly.
Sniff test: passes. Proceed on the 85% solution; what remains open is listed in §18.2.

Plain-words note: this is a crew-only working record. Nothing from §18 goes into the paper text; any public wording stays in plain words.
