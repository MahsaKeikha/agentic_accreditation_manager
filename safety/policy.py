def review_required(action: str) -> bool:
    protected = {"accreditation_decision", "compliance_attestation", "institutional_commitment", "external_submission"}
    return action in protected

def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
