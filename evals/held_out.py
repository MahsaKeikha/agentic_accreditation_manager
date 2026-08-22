from orchestration.orchestrator import orchestrate


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "standards_mapping_gap": True}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "unresolved_material_gap": True}, False),
    ({**base(), "narrative_overclaim": True}, False),
    ({**base(), "corrective_action_unverified": True}, False),
    ({**base(), "stale_evidence": True}, False),
    ({**base(), "institutional_claim_unsupported": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += orchestrate(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
