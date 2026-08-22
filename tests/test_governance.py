from orchestration.orchestrator import orchestrate
from safety.policy import authorize


def valid_context():
    return {
        "standards_mapping_reviewed": True,
        "evidence_provenance_reviewed": True,
        "gap_analysis_reviewed": True,
        "narrative_accuracy_reviewed": True,
        "corrective_actions_reviewed": True,
        "readiness_reviewed": True,
        "institutional_claims_reviewed": True,
        "human_approval": True,
    }


def test_complete_review_can_release_preparation_package():
    result = orchestrate(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_accreditation_authority"] is False


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert orchestrate(context)["release_allowed"] is False


def test_accreditation_decision_is_never_autonomous():
    assert authorize("accreditation_decision", valid_context())["allowed"] is False


def test_standards_mapping_gap_blocks_release():
    context = valid_context()
    context["standards_mapping_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_missing_evidence_provenance_blocks_release():
    context = valid_context()
    context["evidence_provenance_missing"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_material_gap_blocks_release():
    context = valid_context()
    context["unresolved_material_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_narrative_overclaim_blocks_release():
    context = valid_context()
    context["narrative_overclaim"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_unverified_corrective_action_blocks_release():
    context = valid_context()
    context["corrective_action_unverified"] = True
    assert orchestrate(context)["release_allowed"] is False
