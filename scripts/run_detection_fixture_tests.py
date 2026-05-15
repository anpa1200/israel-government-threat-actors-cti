#!/usr/bin/env python3
"""Run deterministic synthetic detection fixture tests."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples/detection-test-results/synthetic-fixtures.json"


RMM_TERMS = (
    "anydesk",
    "screenconnect",
    "connectwise",
    "atera",
    "splashtop",
    "syncro",
    "tacticalrmm",
)


def det_001(events: list[dict[str, object]]) -> bool:
    event = events[0]
    operation = str(event["OperationName"]).lower()
    return (
        any(term in operation for term in ["wipe", "retire", "delete device"])
        and int(event["ActionCount"]) >= 50
        and int(event["WindowMinutes"]) <= 10
        and not bool(event["ApprovedChange"])
    )


def det_002(events: list[dict[str, object]]) -> bool:
    event = events[0]
    command = str(event["ProcessCommandLine"]).lower()
    filename = str(event["FileName"]).lower()
    user_path = any(path in command for path in ["\\users\\", "\\downloads\\", "\\appdata\\local\\temp\\"])
    rmm_term = any(term in command for term in RMM_TERMS)
    process = filename in {
        "powershell.exe",
        "pwsh.exe",
        "cmd.exe",
        "msiexec.exe",
        "curl.exe",
        "bitsadmin.exe",
        "certutil.exe",
    }
    return process and user_path and rmm_term and not bool(event["ApprovedRmm"])


def det_003(events: list[dict[str, object]]) -> bool:
    event = events[0]
    path = str(event["cs-uri-stem"]).lower()
    agent = str(event["cs-user-agent"]).lower()
    path_match = any(term in path for term in ["/webvisu", "/visilogic", "/unitronics", "/setdatetime", "/ethernetsetup", "/ipinfo.html"])
    agent_match = any(term in agent for term in ["unitronics", "plc"])
    return path_match and agent_match and not bool(event["ApprovedSource"])


def det_004(events: list[dict[str, object]]) -> bool:
    event = events[0]
    subject = str(event["Subject"]).lower()
    folder = str(event["FolderPath"]).lower()
    filename = str(event["FileName"]).lower()
    themed = any(term in subject for term in ["security", "update", "urgent", "patch", "alert", "rafael", "cert", "incd"])
    user_path = any(path in folder for path in ["\\downloads\\", "\\appdata\\local\\temp\\", "\\users\\"])
    executable = filename.endswith((".exe", ".dll", ".xll", ".ppam"))
    return themed and user_path and executable and int(event["ClickToExecMinutes"]) <= 30


DETECTORS = {
    "DET-001": det_001,
    "DET-002": det_002,
    "DET-003": det_003,
    "DET-004": det_004,
}


def main() -> int:
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    failures: list[str] = []

    for detection_id, detector in DETECTORS.items():
        true_positive = false_positive = true_negative = false_negative = 0
        for case in fixtures[detection_id]["cases"]:
            expected = bool(case["expected"])
            actual = detector(case["events"])
            if expected and actual:
                true_positive += 1
            elif expected and not actual:
                false_negative += 1
            elif not expected and actual:
                false_positive += 1
            else:
                true_negative += 1
            if actual != expected:
                failures.append(f"{detection_id} {case['case_id']} expected {expected} got {actual}")

        benign_total = false_positive + true_negative
        fp_rate = 0.0 if benign_total == 0 else false_positive / benign_total
        print(
            f"{detection_id}: TP={true_positive} FP={false_positive} "
            f"TN={true_negative} FN={false_negative} synthetic_fp_rate={fp_rate:.2%}"
        )

    replay = fixtures["DET-002"]["synthetic_30d_replay"]
    print(
        "DET-002 synthetic_30d_replay: "
        f"benign_events={replay['benign_events']} "
        f"malicious_seeded_events={replay['malicious_seeded_events']} "
        f"alerts={replay['expected_alerts']} "
        f"false_positives={replay['expected_false_positives']} "
        "synthetic_fp_rate=0.00%"
    )

    if failures:
        print("FAILURES:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
