#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path

RESULTS_PATH = Path("docs/benchmarks/results-template.csv")
CRITICAL_FIELDS = [
    "tension_logic(0-2)",
    "compression_behavior(0-2)",
    "fold_hierarchy(0-2)",
    "thickness_volume(0-2)",
    "artifact_resistance(0-2)",
]


def to_int(value: str) -> int:
    return int(value.strip())


def is_placeholder(row: dict) -> bool:
    return row.get("run_date", "").strip() == "YYYY-MM-DD"


def evaluate_row(row: dict) -> tuple[int, str]:
    total = sum(
        to_int(row[k])
        for k in row
        if k.endswith("(0-2)") and k not in {"max_score"}
    )
    critical_zero = any(to_int(row[field]) == 0 for field in CRITICAL_FIELDS)
    passed = total >= 17 and not critical_zero
    return total, "PASS" if passed else "FAIL"


def main() -> None:
    if not RESULTS_PATH.exists():
        raise SystemExit(f"Missing results file: {RESULTS_PATH}")

    rows = []
    with RESULTS_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if is_placeholder(row):
                continue
            rows.append(row)

    if not rows:
        print("No benchmark runs recorded yet (only template row found).")
        return

    per_scenario = defaultdict(list)
    pass_count = 0

    for row in rows:
        total, result = evaluate_row(row)
        scenario = f"{row['scenario_id']} - {row['scenario_name']}"
        per_scenario[scenario].append(total)
        if result == "PASS":
            pass_count += 1

    print("=== Fabric Physics Running Phase Summary ===")
    print(f"Total runs: {len(rows)}")
    print(f"Pass rate: {pass_count}/{len(rows)} ({(pass_count/len(rows))*100:.1f}%)")
    print("\nScenario averages:")
    for scenario, scores in sorted(per_scenario.items()):
        avg = sum(scores) / len(scores)
        print(f"- {scenario}: avg {avg:.2f} ({len(scores)} run(s))")


if __name__ == "__main__":
    main()
