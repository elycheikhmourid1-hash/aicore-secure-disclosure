#!/usr/bin/env python3
"""AICore Secure Disclosure — supervised triage engine.
AI proposes severity and routing. A human officer confirms before any action.
"""

SEVERITY = {"critical": 5, "high": 4, "medium": 3, "low": 2, "info": 1}

def score_report(report):
    score = 0
    if report.get("auth_bypassed"): score += 3
    if report.get("data_exposure"): score += 2
    if report.get("rce"): score += 4
    if report.get("repro_steps"): score += 1
    if report.get("evidence"): score += 1
    sev = "critical" if score >= 7 else "high" if score >= 5 else "medium" if score >= 3 else "low" if score >= 2 else "info"
    return {"severity": sev, "score": score, "human_review_required": True, "action": "route_to_triage_officer"}

if __name__ == "__main__":
    sample = {"auth_bypassed": True, "data_exposure": True, "rce": False, "repro_steps": True, "evidence": True}
    print(score_report(sample))
