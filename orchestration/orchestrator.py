from AGENTS.evidence_collection_agent import run as evidence
from AGENTS.gap_analysis_agent import run as gaps
from AGENTS.narrative_drafting_agent import run as narrative
from AGENTS.readiness_review_agent import run as readiness
from AGENTS.standards_mapping_agent import run as standards
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run accreditation specialists and apply fail-closed governance."""
    results = [
        standards(context),
        evidence(context),
        gaps(context),
        narrative(context),
        readiness(context),
    ]
    governance = authorize("accreditation_preparation_release", context)
    return {
        "system": "F100",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_accreditation_authority": False,
        "autonomous_attestation_authority": False,
    }
