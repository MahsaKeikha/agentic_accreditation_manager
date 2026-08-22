from orchestration.orchestrator import orchestrate

REFERENCE_CONTEXT = {
    "standards": ["institutional accreditation standard"],
    "standards_mapping_reviewed": True,
    "evidence_provenance_reviewed": True,
    "gap_analysis_reviewed": True,
    "narrative_accuracy_reviewed": True,
    "corrective_actions_reviewed": True,
    "readiness_reviewed": True,
    "institutional_claims_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(orchestrate(REFERENCE_CONTEXT))
