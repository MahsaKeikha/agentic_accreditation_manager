from AGENTS.standards_mapping_agent import run as a
from AGENTS.evidence_collection_agent import run as b
from AGENTS.gap_analysis_agent import run as c
from AGENTS.narrative_drafting_agent import run as d
from AGENTS.readiness_review_agent import run as e
def orchestrate(context): return [a(context),b(context),c(context),d(context),e(context)]
