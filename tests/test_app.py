from src.app import retrieve, answer
DOCS=[{"id":"A","text":"Access reviews occur quarterly."},{"id":"B","text":"Incidents require escalation."}]
def test_retrieval_ranks_evidence(): assert retrieve("quarterly access review",DOCS)[0]["id"]=="A"
def test_abstains_without_evidence(): assert answer("holiday allowance",DOCS)["abstained"]
