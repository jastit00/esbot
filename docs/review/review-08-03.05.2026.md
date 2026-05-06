# Review template (inspection / technical review)

**Project / product: ESBot: https://github.com/Mooh9876/esbot**  
**Review object(s): esbot documentation, requirements, tests and partial implementation**  
**Review type: Peer Review**  
**Date (planned / actual):27.04.2026/05.05.2026**
**Author(s): Mohammed Al-Otaibi, Nils-Konstantin Lutz, Alen Osmanagic, Dominic Sehorz** <!-- name(s) -->  
**Reviewers: Jakob Strauss, Yunis Ghazali, Vincent Kehl, Michaja Hummel** <!-- names -->

---

## 1. General instructions

The method peer review was chosen to enable a review without a meeting and asynchronous working. Furthermore its Ease-of-Use fit the low complexity of the review object
The review is based on the review template from the lecture

**Terminology**

| Acronym | Meaning |
|--------|---------|
| **MP** | Master Plan |
| **DS** | Data Summary |
| **LoF** | Level of Findings |
| **RR** | Review Report |

### Phases of a review / inspection

| Phase | Description |
|-------|-------------|
| **Planning** |  The review is planned: reviewers and dates are fixed. Part of the Group completes the Master Plan (MP) and identifies suitable inspection tasks. |
| **Kick-off**  | In the kick-off meeting, the master Plan is discussed with the whole group and changes are discussed and added to the Master Plan |
| **Individual preparation** | Each reviewer examines their  review objects. |
| **Review meeting** | Reviewers decide the status of each finding. Additional findings may be collected during the meeting. |
| **Reworking** | Rework is done by the Authors, the reviewers only provide a List of Findings      

---

## 2. Master Plan (MP)

### 2.1 Masterplan - header


| Field | Value |
|-------|-------|
| Review No. |REV-2026-001
| Project |esbot <!-- Project or product name (e.g. ESBot). --> |
| Project manager | Mooh9876 <!-- Name of project / product owner or PM. --> |
| Quality expert / manager | -<!-- Name of quality role if applicable;  else “—”. --> |
| Moderator | -<!-- Review moderator: owns process, schedule, consolidation. --> |
| Author(s) |  Mohammed Al-Otaibi, Nils-Konstantin Lutz, Alen Osmanagic, Dominic Sehorz <!-- Author(s) of the review object(s); main contact for rework. --> |


### 2.2 Review objects

<!-- List the specific artefacts under review (files, modules, documents, commits). Use Abbr. as a short label for each row (used in findings and assignments). Add rows if needed. -->

| # | Review objects | Abbr. |
|---|----------------|-------|
| 1 | `docs/spec/requirements.md` | requirements |
| 2 | `docs/spec/spec.md` | spec |
| 3 | `backend/app/models/`| models |
| 4 | `backend/tests/` | tests |
| 5 | `backend/features/*.feature` | feature |

### 2.3 Reference documents

<!-- List materials reviewers need for context (requirements baseline, architecture, API spec, course brief). Use Abbr. for cross-references. -->

| # | Reference documents | Abbr. |
|---|---------------------|-------|
| 1 | `docs/esbot.md` | esbot |
| 2 | `docs/spec/requirements.md` | requirements |
| 3 | `docs/spec/data-model.md` | datamodel |


### 2.4 Checklists / scenarios

<!-- Specify which checklists, reading guides, or test scenarios reviewers should follow (course checklist, OWASP skim, API contract checks). -->

| # | Checklists / scenarios |
|---|------------------------|
| 1 | **Requirements completeness :** Are all requirements uniquely numbered, testable, measurable, and consistent? |
| 2 | **BDD traceability :** Are all BDD scenarios traceable to requirements? Do scenarios follow the Given/When/Then format? |
| 3 | **Consistency :** Does the domain model match the specified requirements? Are all implemented features described in the spec? |
| 4 | **Code traceability :** Can unit tests and implementation be traced back to specific requirements? |



### 2.5 Reviewer assignment

<!-- Up to 10 reviewers: assign names and which chapters, objects, or checklists each person covers. Use Abbr. for initials or short IDs. -->

### **A review of a scenario always includes all review objects!**

| Reviewer | Names (and chapters / checklists or scenarios assigned to the review) | Name |
|:--------:|---------------------------------------------------------------------------|-------|
| 1 |   Code traceability | Michaja |
| 2 |  BDD traceability  | Jakob  |
| 3 | Consistency   |  Vincent |
| 4 |  Requirements completeness   | Jakob |


### 2.6 Kick-off

<!-- Optional but recommended: align on scope, Master Plan, and context before individual preparation. -->

| Date / time / location |
|------------------------|
|  27.04.2026 17:30 via Discord

### 2.7 Individual preparation

<!-- Planning figures for the preparation phase. “Optimal” rows support effort estimation (rate × time ≈ size). For documents without NLOC, substitute pages or words and state that in the Size unit cell. -->

| Individual preparation | Value | Unit |
|------------------------|-------|------|
| Submission of findings by | 05.05.2026<!-- Enter the deadline by which each reviewer submits findings to the moderator (date/time or rule such as “72h after kick-off”). --> |  |
| Size of review objects | Not measured<!-- Enter the total Non-Comment Lines of Code (NLOC) for code; for specification-only reviews, use pages or words and note the unit here. --> | NLOC |
| Optimal inspection rate | Not measured<!-- Target or measured inspection speed (e.g. NLOC per hour per reviewer). --> | NLOC/h |
| Optimal inspection time | ~4 for the whole team<!-- Planned total inspection time in hours (placeholder 0.00 until estimated or measured). --> | h |

### 2.8 Review meeting

| Date / time / location |
|------------------------|
| 05.05.2026 on Discord<!-- e.g. 2026-04-25 10:00 CET, Room Y / video link --> |

### 2.9 Additional milestones (optional)

<!-- Not in the classic Masterplan sheet; useful for ESBot course tracking (rework, closure). -->

| Milestone | Planned date / time | Actual date / time |
|-----------|---------------------|---------------------|
| End of individual preparation | 04.05.2026 <!-- same as or before “Submission of findings by” --> | |

---

## 3. List of findings (LoF)

Use one row per finding. Extend the table if your course requires extra columns.

Suggested values: **Type** — defect, question, suggestion; **Severity** — blocking, major, minor, editorial (define team scale); **Status** — open, accepted, rejected, deferred, fixed (update through meeting and rework).

| ID | Location (file / section / module) | Summary | Type | Severity | Status | Owner | Notes / meeting decision |
|----|-------------------------------------|---------|------|----------|--------|-------|--------------------------|
| F-001 | `user_session.py` | How should FR5 be implemented? UserSession has no user identifier. | question | minor | open | — | FR5 not fully reflected in domain model |
| F-002 | `message.py`, `requirements.md`, `spec.md` | `Message.role` ("user"/"bot") is not defined anywhere in requirements or spec | defect | minor | open | — | Role concept missing in specification |
| F-003 | `requirements.md`  | FR2: "Contextualized answers" is not measurable or testable. No acceptance criterion defined.                 | defect     | major    | open   | —     | Add concrete criterion, e.g. answer must reference course material |
| F-004 | `requirements.md`  | NFR2:  "Intuitive and easy to use" is not measurable or testable. No usability metric provided.                 | defect     | major    | open   | —     | Replace with a measurable metric  |
| F-005 | `requirements.md`  | NFR4 "Multiple concurrent users" is not measurable. No minimum number of users specified.                     | defect     | major    | open   | —     | Define a concrete load target, e.g. ≥ 50 concurrent users |
| F-006 |`requirements.md`   | NFR5 "Stored securely" is not testable. No encryption standard, access control policy, or compliance requirement is mentioned. | defect     | minor    | open   | —     | Specify security mechanism |
| F-007 | `requirements.md`  | NFR1 response time of 2 seconds does not specify conditions, e.g. under what load or for what request type. | defect     | minor    | open   | —     | Add conditions, e.g. "under normal load of 50 users, 95th percentile" |
| F-008 | `backend/tests/*` | FR1 (Ask Questions), FR2 (Provide Answers), FR7 (Chat Interface), and FR8 (AI Integration) have no corresponding unit tests. Requirements exist but have no test coverage. | defect  | major   | open   | —     | Add tests that exercise the question-answering and chat flows, or document why they are excluded from unit testing |
| F-009 | `test_user_session.py`, `test_quiz_request.py` | FR5 (Retrieve Sessions) is not covered by any test. Sessions can be stored (FR4) but there is no test verifying that a previous session can be retrieved by a user. | defect  | minor    | open   | —     | Add a test for session retrieval to establish traceability to FR5                           |
| F-010 | `backend/features/*`        | All scenarios require a registered and logged-in student as a precondition, but no requirement in requirements.md defines user registration or authentication.  | question | minor    | open   | —     | Clarify whether authentication is an implicit requirement; if so, add it to requirements.md                     |


---

## 4. Data Summary (DS)

<!-- Key metrics for this review. Fill after preparation and/or after rework. -->

| Metric | Value | Notes |
|--------|-------|-------|
| Size of review object | 7 testfiles, 3 BDD feature files, 6 Data model files,  10+ documentation/specification files<!-- e.g. pages, LOC, #requirements --> | <!-- --> |
| Preparation effort (hours, optional) | ~4h <!-- per role --> | teamwide preparation effort<!-- --> |
| Number of findings (initial) | 10 | <!-- --> |
| Number of findings after meeting | 10 | <!-- --> |
| Rework effort (hours, author) | ~30min<!-- --> | minor additions to test template<!-- --> |
| Re-inspection required? | no<!-- yes / no --> | LoF can be passed to authors<!-- --> |

---

## 5. Review Report (RR)

### 5.1 Summary

<!-- Short executive summary: object reviewed, outcome, overall quality impression. -->

### 5.2 Review outcome

- **Review object state after review:** <!-- e.g. accepted with changes, requires re-inspection, not accepted -->
- **Major risks or themes:** <!-- bullet list -->

### 5.3 Decisions and follow-up

| Topic | Decision | Responsible | Due date |
|-------|----------|-------------|----------|
| <!-- --> | <!-- --> | <!-- --> | <!-- --> |

### 5.4 Positive observations (optional)

<!-- What was done well; good practices worth keeping. -->

### 5.5 Lessons learned (optional)

<!-- Process improvements for the next review. -->

### 5.6 Sign-off

| Role | Name | Signature / date |
|------|------|------------------|
| Moderator | <!-- --> | <!-- --> |
| Author | <!-- --> | <!-- --> |

*Claude Sonnet 4.6 was used in formulating Findings and Scenarios, and for Formatting* 
