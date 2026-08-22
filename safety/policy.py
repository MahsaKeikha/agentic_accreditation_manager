"""Fail-closed accreditation governance for F100."""

PROTECTED_ACTIONS = {
    "accreditation_decision",
    "compliance_attestation",
    "institutional_commitment",
    "external_submission",
    "accreditation_claim",
    "corrective_action_closure",
}

REQUIRED_REVIEWS = (
    "standards_mapping_reviewed",
    "evidence_provenance_reviewed",
    "gap_analysis_reviewed",
    "narrative_accuracy_reviewed",
    "corrective_actions_reviewed",
    "readiness_reviewed",
    "institutional_claims_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding accreditation authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required accreditation review", "missing": missing}

    blockers = []
    if context.get("standards_mapping_gap"):
        blockers.append("standards mapping incomplete or incorrect")
    if context.get("evidence_provenance_missing"):
        blockers.append("supporting evidence provenance incomplete")
    if context.get("unresolved_material_gap"):
        blockers.append("material accreditation gap unresolved")
    if context.get("narrative_overclaim"):
        blockers.append("narrative overstates evidence or compliance")
    if context.get("corrective_action_unverified"):
        blockers.append("corrective action closure not verified")
    if context.get("stale_evidence"):
        blockers.append("material evidence is stale or superseded")
    if context.get("institutional_claim_unsupported"):
        blockers.append("institutional accreditation claim unsupported")
    if context.get("conflicting_evidence_unresolved"):
        blockers.append("conflicting evidence unresolved")

    if blockers:
        return {"allowed": False, "reason": "accreditation governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "accreditation-preparation package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
