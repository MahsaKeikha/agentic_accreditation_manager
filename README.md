# F100 Agentic Accreditation Manager

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for accreditation preparation across standards mapping, evidence management, gap analysis, narrative drafting, corrective-action tracking, readiness assessment, institutional claims, provenance, and qualified human review.

F100 is designed for universities, colleges, academic programs, professional programs, institutional effectiveness teams, accreditation offices, quality-assurance teams, and other organizations that need structured accreditation preparation without transferring accreditation, attestation, compliance, corrective-action closure, institutional-commitment, or submission authority to an automated system.

The repository is preparation-only and fail closed. It does not make accreditation decisions, certify compliance, claim accredited status, close corrective actions, issue institutional attestations, make institutional commitments, or submit externally on behalf of an institution.

## Accreditation lifecycle

```text
accreditation framework + institutional context
                     |
                     v
              standards mapping
                     |
                     v
             evidence collection
                     |
                     v
                gap analysis
                     |
                     v
             narrative drafting
                     |
                     v
          corrective-action review
                     |
                     v
             readiness review
                     |
                     v
          qualified human approval
```

A polished narrative is not proof of compliance. F100 preserves the distinction between evidence, interpretation, institutional assertion, corrective action, readiness, and formal accreditation judgment.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Standards Mapping Agent | Maps accreditation requirements to institutional processes, artifacts, owners, and evidence | What does each standard require, and where is the corresponding institutional evidence? |
| Evidence Collection Agent | Organizes supporting evidence, provenance, dates, versions, owners, and limitations | Is the evidence traceable, current, relevant, and sufficient for review? |
| Gap Analysis Agent | Identifies missing, weak, stale, conflicting, or unsupported evidence and process gaps | Where does the institution lack adequate evidence or demonstrated practice? |
| Narrative Drafting Agent | Structures accreditation narratives from verified evidence without overstating compliance | What can be accurately stated based on the reviewed evidence? |
| Readiness Review Agent | Performs an independent readiness assessment across standards, evidence, gaps, claims, and corrective actions | Is the preparation package sufficiently reviewed for qualified institutional action? |

The agents support accreditation preparation. They do not exercise the authority of an accrediting body, institutional signatory, compliance officer, or authorized institutional representative.

## Repository structure

```text
AGENTS/
├── standards_mapping_agent.py
├── evidence_collection_agent.py
├── gap_analysis_agent.py
├── narrative_drafting_agent.py
└── readiness_review_agent.py

SKILLS/
├── standards_mapping.py
├── evidence_management.py
├── gap_analysis.py
├── accreditation_narrative.py
└── readiness_assessment.py

TOOLS/
├── standards_matrix_tool.py
├── evidence_register_tool.py
├── gap_tracker_tool.py
├── narrative_outline_tool.py
└── readiness_dashboard_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The architecture separates accreditation reasoning from deterministic mapping, evidence registration, gap tracking, narrative outlining, and readiness-dashboard utilities while keeping governance, evaluation, state, and observability explicit.

## Accreditation context

A governed accreditation case can include:

```text
institution
program
accrediting_body
framework
framework_version
review_cycle
self_study_period
site_visit_period
standards
institutional_units
evidence_owners
submission_deadlines
prior_findings
corrective_actions
institutional_claims
review_status
```

Accreditation requirements vary by accrediting body, jurisdiction, discipline, program type, and review cycle. F100 should not treat one framework as universally applicable.

## Standards mapping

`SKILLS/standards_mapping.py` and `TOOLS/standards_matrix_tool.py` support structured mapping of accreditation requirements.

A standards matrix can capture:

```text
standard_id
standard_text
interpretive_guidance
institutional_owner
process_or_policy
evidence_required
evidence_available
evidence_status
gap_status
narrative_status
reviewer
version
```

Mapping should preserve the actual language and version of the applicable accreditation standard when implementations connect to live accreditor materials.

## Framework versioning

Accreditation standards evolve.

A framework record should preserve:

- accrediting body
- framework title
- version
- effective date
- superseded version
- transition guidance
- institutional interpretation notes

A mapping created for a prior framework should not silently inherit validity after a standards revision.

## Standards interpretation boundary

F100 can organize institutional interpretations and evidence relationships, but it should not present its own interpretation as the accrediting body's binding interpretation.

Ambiguous requirements should be escalated to qualified institutional personnel and, where appropriate, authoritative accreditor guidance.

`standards_mapping_gap` is an explicit fail-closed blocker when mapping is incomplete or materially incorrect.

## Evidence management

`SKILLS/evidence_management.py` and `TOOLS/evidence_register_tool.py` support structured evidence collection and provenance.

Accreditation evidence can include:

- policies
- procedures
- meeting minutes
- assessment reports
- curriculum maps
- faculty records
- institutional research
- student-learning evidence
- strategic plans
- budgets
- resource records
- survey results
- outcome data
- committee records
- continuous-improvement records
- prior accreditation correspondence

Evidence should be evaluated for relevance, recency, ownership, traceability, and relationship to the standard it is intended to support.

## Evidence provenance

A useful evidence record can preserve:

```text
evidence_id
title
source
owner
creation_date
review_date
version
applicable_standard
claim_supported
confidentiality
limitations
status
```

`evidence_provenance_missing` blocks release because unsupported or untraceable artifacts cannot reliably support an accreditation claim.

The system should never fabricate policies, meeting minutes, outcome data, institutional records, student-learning results, approvals, or accreditor correspondence.

## Evidence freshness

Accreditation evidence can become stale even when the underlying artifact is authentic.

Review should consider:

- date of evidence
- applicable review period
- whether the process still exists
- whether the policy remains current
- whether responsible personnel changed
- whether newer evidence supersedes the artifact
- whether longitudinal evidence is required

`stale_evidence` is a fail-closed blocker when material evidence is outdated or superseded.

## Evidence sufficiency

The presence of an artifact does not automatically establish compliance.

A policy may exist but not be implemented. A process may be described but not evaluated. A learning outcome may be stated but not assessed. A committee may exist but not have evidence of functioning.

F100 therefore distinguishes artifact existence from demonstrated institutional practice.

## Direct and indirect evidence

Where appropriate, accreditation preparation can distinguish:

**Direct evidence** that demonstrates an outcome, process, decision, or institutional practice itself.

**Indirect evidence** that provides contextual or perception-based support but does not directly establish the underlying outcome.

The required evidence mix depends on the accreditation framework and standard.

## Gap analysis

`SKILLS/gap_analysis.py` and `TOOLS/gap_tracker_tool.py` support structured identification and tracking of accreditation gaps.

Potential gaps include:

- missing evidence
- stale evidence
- incomplete standards mapping
- policy-practice mismatch
- missing assessment cycle
- missing documented follow-up
- unsupported institutional claim
- unclear ownership
- unresolved conflicting evidence
- corrective action without verification
- narrative statement unsupported by evidence

An `unresolved_material_gap` blocks release.

## Gap severity

Implementations can classify gaps by factors such as:

```text
scope
materiality
standard affected
risk to readiness
required owner
required action
deadline
verification method
```

Severity classifications should support prioritization rather than masquerade as accreditor decisions.

## Corrective actions

A gap may generate a corrective-action plan.

A useful record can include:

```text
action_id
related_standard
gap
owner
action
milestone
due_date
evidence_required
status
verification_method
reviewer
closure_state
```

F100 may track corrective actions but cannot autonomously close them as an institutional or accreditation determination.

## Corrective-action verification

A corrective action should not be considered complete merely because an owner reports completion.

Closure can require evidence that the action occurred, that the intended process or control exists, and, where relevant, that implementation has been evaluated.

`corrective_action_unverified` is an explicit blocker.

`corrective_action_closure` is also a protected action that remains outside autonomous authority.

## Accreditation narrative

`SKILLS/accreditation_narrative.py` and `TOOLS/narrative_outline_tool.py` support structured drafting of evidence-grounded narratives.

A narrative can organize:

```text
standard
institutional approach
implementation evidence
results or outcomes
evaluation
improvement actions
evidence references
limitations
unresolved items
```

Narratives should explain evidence, not replace it.

## Narrative accuracy

F100 requires `narrative_accuracy_reviewed` before release.

Narrative review should check for:

- unsupported compliance statements
- exaggerated institutional performance
- selective omission of material gaps
- claims broader than the evidence
- outdated evidence references
- inconsistent statistics
- contradictory statements
- undocumented corrective-action closure

A `narrative_overclaim` blocks release.

## Institutional claims

Accreditation preparation often involves claims about institutional status, quality, performance, compliance, resources, outcomes, or improvement.

These claims can carry substantial reputational and regulatory consequences.

F100 therefore requires `institutional_claims_reviewed` and blocks `institutional_claim_unsupported`.

The system must not claim that an institution or program is accredited, compliant, approved, or in good standing unless that status is supported by the appropriate authoritative source and qualified review.

## Accreditation-status boundary

`accreditation_claim` is a protected action.

F100 cannot independently announce or represent that an institution or program has achieved, retained, renewed, or lost accreditation.

Formal accreditation status comes from the authorized accrediting body and institutional communication process.

## Compliance-attestation boundary

`compliance_attestation` is protected.

The system may organize evidence supporting an attestation, but it cannot sign, certify, or formally attest institutional compliance.

## Institutional commitments

Accreditation narratives or corrective actions may create commitments involving staffing, budgets, facilities, curriculum, policy changes, timelines, reporting, or governance.

`institutional_commitment` is a protected action.

The system should not convert a draft corrective action into a binding institutional promise.

## Conflicting evidence

Accreditation records can conflict.

Examples include:

- a policy describing one process while records show another
- inconsistent outcome data
- contradictory meeting records
- differing versions of a procedure
- narrative claims inconsistent with operational evidence
- faculty, staff, or student data that do not align

`conflicting_evidence_unresolved` blocks release when the conflict materially affects readiness or a claim.

The system should preserve the conflict rather than silently choose the evidence that creates the strongest narrative.

## Continuous improvement

Many accreditation frameworks expect evidence that institutions not only assess performance but use results to improve.

A continuous-improvement chain can be represented as:

```text
objective
   |
   v
measure
   |
   v
result
   |
   v
analysis
   |
   v
action
   |
   v
follow-up evidence
```

The existence of assessment data without documented use may not demonstrate a complete improvement cycle.

## Student-learning outcomes

Programmatic and institutional accreditation may include student-learning assessment.

Preparation can map:

- learning outcomes
- curriculum coverage
- direct measures
- indirect measures
- performance criteria
- results
- interpretation
- improvement actions
- follow-up assessment

F100 can organize this evidence but does not independently determine whether academic standards have been met.

## Curriculum evidence

Accreditation review may involve curriculum maps, prerequisites, course sequences, assessment evidence, program outcomes, workload, and alignment.

F100 can incorporate curriculum evidence generated by governed educational systems, but the accreditation layer should still verify institutional ownership, version, and applicability.

## Faculty and staff evidence

Some standards involve faculty qualifications, staffing levels, governance participation, development, workload, or support.

F100 should avoid unsupported judgments about individual competence and should minimize unnecessary personal data.

Sensitive personnel information should be handled according to institutional policy and access controls.

## Resources and infrastructure

Evidence can address resources such as:

- facilities
- laboratories
- libraries
- technology
- student support
- staffing
- finances
- equipment
- accessibility
- administrative capacity

A resource claim should remain tied to actual evidence rather than generic statements of adequacy.

## Governance and institutional processes

Accreditation standards may involve:

- institutional governance
- program governance
- committees
- policy approval
- strategic planning
- assessment governance
- student participation
- faculty participation
- continuous improvement

F100 can map evidence of these processes without replacing institutional governance bodies.

## Accessibility and inclusion

Accreditation preparation can include evidence related to accessibility, equity, inclusion, student support, and nondiscrimination where relevant to the applicable standards.

The system should not infer compliance based on aspirational statements alone. Policies, implementation evidence, outcomes, and review processes should remain distinct.

## Privacy and confidentiality

Accreditation evidence may contain sensitive student, personnel, financial, research, clinical, or institutional information.

Implementations should apply:

- data minimization
- role-based access
- retention limits
- confidentiality classifications
- appropriate redaction
- secure storage
- restricted sharing

F100 should not expose confidential evidence simply because it is useful for narrative generation.

## Readiness assessment

`SKILLS/readiness_assessment.py` and `TOOLS/readiness_dashboard_tool.py` support structured readiness review.

A readiness dashboard can summarize:

- mapped standards
- evidence completeness
- stale evidence
- unresolved gaps
- corrective-action status
- narrative status
- unsupported claims
- conflicting evidence
- review status
- human approval status

A readiness score, if added by an implementation, should not be treated as an accreditation decision.

## Independent readiness review

The Readiness Review Agent is intentionally separated from narrative drafting.

Its role is to evaluate whether the preparation package is sufficiently supported rather than simply make the narrative sound stronger.

This reduces the risk that the same reasoning path both creates and validates an institutional accreditation claim.

## Required reviews

The reference governance policy requires all of the following before release of an accreditation-preparation package:

```text
standards_mapping_reviewed
evidence_provenance_reviewed
gap_analysis_reviewed
narrative_accuracy_reviewed
corrective_actions_reviewed
readiness_reviewed
institutional_claims_reviewed
human_approval
```

A missing required review fails closed.

## Fail-closed governance

Reference blockers include:

- standards mapping incomplete or incorrect
- supporting evidence provenance incomplete
- material accreditation gap unresolved
- narrative overstates evidence or compliance
- corrective-action closure unverified
- material evidence stale or superseded
- institutional accreditation claim unsupported
- conflicting evidence unresolved
- required review missing
- qualified human approval missing

The workflow should expose blockers rather than generate a deceptively complete accreditation package.

## Protected actions

The reference safety policy prohibits autonomous execution of:

```text
accreditation_decision
compliance_attestation
institutional_commitment
external_submission
accreditation_claim
corrective_action_closure
```

Protected actions remain outside the system's authority even when all review flags are true.

## Human authority boundaries

F100 must not autonomously:

- make an accreditation decision
- declare compliance with an accreditation standard
- certify an institution or program
- sign a compliance attestation
- claim accredited status
- close corrective actions as a binding determination
- make institutional commitments
- represent an accrediting body
- issue a site-visit finding
- change official accreditation records
- submit externally on behalf of an institution

Final authority remains with qualified institutional officials, authorized signatories, accreditation teams, governing bodies, and accrediting organizations according to their respective roles.

## Accrediting-body boundary

F100 is not an accrediting body and should never impersonate one.

Preparation support should clearly distinguish:

```text
institutional self-assessment
internal readiness judgment
external accreditor finding
formal accreditation decision
```

Only the authorized accrediting body can make the latter determinations.

## Site-visit preparation

F100 can support preparation for a site visit by organizing:

- standards maps
- evidence indexes
- narrative references
- outstanding gaps
- interview preparation
- document requests
- corrective-action status
- responsible owners

It cannot script deceptive responses, conceal material gaps, or manufacture evidence.

## Self-study preparation

A self-study package can be structured around:

- institutional or program context
- standards narratives
- evidence references
- outcome data
- analysis
- improvement actions
- unresolved gaps
- appendices

The self-study should remain an evidence-grounded institutional document subject to qualified review.

## Prior findings and follow-up

Accreditation preparation may need to track prior findings, recommendations, conditions, monitoring reports, or required follow-up.

A useful record can include:

```text
finding_id
source
standard
finding
required_response
deadline
action_owner
evidence
status
verification
```

Past findings should not be marked resolved without evidence and authorized review.

## Change impact

Institutional changes can affect previously mapped evidence.

Examples include:

- curriculum changes
- leadership changes
- policy revisions
- organizational restructuring
- new campuses or delivery modes
- program closures
- new technology platforms
- assessment redesign
- changes in staffing or resources

Material change should trigger re-evaluation of affected standards rather than automatically inheriting prior readiness status.

## Versioning

Accreditation preparation should preserve versions of:

- standards framework
- standards matrix
- evidence register
- gap log
- corrective-action plan
- narrative draft
- readiness review
- institutional claims
- submitted package

Versioning supports auditability and avoids mixing evidence from incompatible review states.

## Provenance and uncertainty

Material statements should distinguish among:

```text
accreditor requirement
verified institutional evidence
institutional assertion
system inference
unresolved question
internal readiness judgment
formal accreditor determination
```

Uncertainty should remain explicit.

## End-to-end reference workflow

A typical governed F100 workflow follows this sequence:

1. Identify the accrediting body, framework, version, review cycle, and institutional scope.
2. Map every applicable standard to institutional owners, processes, and expected evidence.
3. Register evidence with provenance, dates, versions, and confidentiality status.
4. Review evidence relevance, sufficiency, and freshness.
5. Identify missing, weak, stale, conflicting, or unsupported evidence.
6. Create and track corrective actions for material gaps.
7. Verify corrective-action evidence rather than accepting self-reported closure.
8. Draft standards narratives from reviewed evidence.
9. Review narratives for overclaiming, inconsistency, and unsupported compliance statements.
10. Review institutional accreditation claims separately.
11. Perform independent readiness review.
12. Apply fail-closed governance gates.
13. Require explicit qualified-human approval.
14. Keep accreditation decisions, attestations, institutional commitments, status claims, corrective-action closure, and external submission outside autonomous authority.

## Explicit failure states

Useful explicit states include:

```text
STANDARDS MAPPING INCOMPLETE
STANDARDS VERSION UNCERTAIN
EVIDENCE PROVENANCE MISSING
EVIDENCE STALE
EVIDENCE INSUFFICIENT
MATERIAL GAP UNRESOLVED
CONFLICTING EVIDENCE UNRESOLVED
NARRATIVE OVERCLAIM
CORRECTIVE ACTION UNVERIFIED
INSTITUTIONAL CLAIM UNSUPPORTED
READINESS REVIEW INCOMPLETE
HUMAN APPROVAL REQUIRED
ACCREDITATION DECISION AUTHORITY PROHIBITED
COMPLIANCE ATTESTATION AUTHORITY PROHIBITED
ACCREDITATION CLAIM AUTHORITY PROHIBITED
EXTERNAL SUBMISSION AUTHORITY PROHIBITED
```

The system should never fabricate standards, policies, outcomes, accreditation findings, evidence, corrective-action closure, institutional commitments, or formal accreditation status.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark material under `benchmarks/`.

Evaluation should test both accreditation-preparation usefulness and governance behavior.

Useful dimensions include:

- standards-mapping completeness
- version-awareness
- evidence provenance
- evidence freshness
- gap detection
- narrative grounding
- overclaim prevention
- corrective-action verification
- conflicting-evidence handling
- institutional-claim discipline
- human-approval enforcement
- protected-action enforcement

The held-out suite includes a 10-scenario accreditation-governance set intended to test refusal and escalation as well as preparation quality.

## Direct governance tests

The behavioral tests verify that:

- a complete reviewed preparation package may be released
- missing human approval fails closed
- an accreditation decision is never autonomous
- a standards-mapping gap blocks release
- missing evidence provenance blocks release
- an unresolved material gap blocks release
- narrative overclaiming blocks release
- an unverified corrective action blocks release

These tests establish minimum reference behavior. Production use requires institution-specific validation.

## Observability

The `observability/` layer supports traceability across the accreditation workflow.

Useful telemetry can include:

- framework version
- standard mapping state
- evidence counts and provenance status
- stale-evidence flags
- gap status
- corrective-action status
- narrative-review status
- institutional-claim status
- readiness-review state
- human-approval state
- governance blockers

Observability supports auditability. It does not create accreditation authority.

## Memory and state

The `memory/` and `state/` layers can preserve structured context across review stages.

State should distinguish standards, evidence, claims, gaps, actions, internal interpretations, reviewer decisions, and formal external determinations.

Sensitive institutional information should not be retained beyond legitimate need.

## Reproducibility

Install development dependencies:

```bash
python -m pip install -e .
```

Run static verification:

```bash
ruff check . --select E9,F63,F7,F82
```

Run governance tests:

```bash
python -m pytest -q
```

Run held-out evaluation:

```bash
python evals/held_out.py
```

Run the governed reference workflow:

```bash
python run.py
```

CI runs these gates on Python 3.10, 3.11, and 3.12.

## Extension points

Institution-specific deployments can extend F100 with governed integrations for:

- accreditation-management platforms
- institutional data warehouses
- curriculum systems
- assessment platforms
- document repositories
- policy repositories
- faculty-information systems
- student-information systems
- committee workflow systems
- evidence dashboards

Integrations should preserve provenance, access control, versioning, confidentiality, and fail-closed authority boundaries.

## Example applications

Potential governed uses include:

- institutional self-study preparation
- program accreditation preparation
- continuous-accreditation monitoring
- evidence inventory management
- standards mapping
- gap analysis
- corrective-action tracking
- site-visit preparation
- internal readiness reviews
- accreditation training

F100 is not a substitute for an accrediting body or authorized institutional accreditation process.

## Design principles

F100 follows these principles:

1. Evidence before accreditation claims.
2. Map requirements before drafting narratives.
3. Preserve framework version and source provenance.
4. Treat stale, missing, and conflicting evidence as explicit states.
5. Separate narrative generation from independent readiness review.
6. Never equate a polished narrative with compliance.
7. Verify corrective actions before treating them as resolved.
8. Fail closed when material evidence or review is incomplete.
9. Keep accreditation decisions, attestations, institutional commitments, claims, and submissions under qualified human authority.
10. Preserve a clear boundary between institutional self-assessment and formal accreditor judgment.

## Scope statement

F100 demonstrates a governed multi-agent architecture for accreditation preparation. It combines specialized accreditation agents, deterministic mapping and tracking tools, explicit state, provenance, observability, held-out evaluation, CI, and fail-closed governance while keeping binding accreditation and institutional authority with qualified humans and authorized accrediting bodies.

It is not an accrediting body, institutional signatory, compliance authority, or autonomous accreditation decision maker.