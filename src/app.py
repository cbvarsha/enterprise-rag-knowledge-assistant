import math, re
from collections import Counter

def tokens(text): return re.findall(r"[a-z0-9]+", text.lower())
def vector(text): return Counter(tokens(text))
def cosine(a,b):
    common=set(a)&set(b); dot=sum(a[x]*b[x] for x in common)
    denom=math.sqrt(sum(v*v for v in a.values()))*math.sqrt(sum(v*v for v in b.values()))
    return dot/denom if denom else 0.0
def retrieve(question, documents, top_k=3):
    q=vector(question); ranked=[]
    for doc in documents:
        score=cosine(q,vector(doc["text"])); ranked.append({**doc,"score":round(score,4)})
    return sorted(ranked,key=lambda x:x["score"],reverse=True)[:top_k]
def answer(question, documents, threshold=.12):
    hits=retrieve(question,documents)
    if not hits or hits[0]["score"] < threshold: return {"answer":"Insufficient evidence in the indexed knowledge base.","citations":[],"abstained":True}
    evidence=" ".join(h["text"] for h in hits[:2])
    return {"answer":evidence,"citations":[h["id"] for h in hits[:2]],"abstained":False}

if __name__ == "__main__":
    docs=[{"id":"SOP-14 §4.2","text":"Critical incidents require immediate escalation and an evidence record."},{"id":"POL-08 §3.1","text":"Access reviews are completed quarterly by the system owner."}]
    print(answer("How often are access reviews completed?",docs))
