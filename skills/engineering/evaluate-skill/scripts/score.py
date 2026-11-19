"""Usage: python3 score.py trials.csv (case,repeat,arm,verdict)."""
import csv
import json
import sys
from collections import Counter


def summarize(rows):
    pairs = {}
    for row in rows:
        case, repeat, arm, verdict = (row[k].strip() for k in ('case', 'repeat', 'arm', 'verdict'))
        if not case or not repeat or arm not in ('baseline', 'candidate') or verdict not in ('pass', 'fail'):
            raise ValueError('Expected a case, repeat ID, baseline/candidate arm and pass/fail verdict')
        pair = pairs.setdefault((case, repeat), {})
        if arm in pair:
            raise ValueError(f'Duplicate arm for {case}/{repeat}: {arm}')
        pair[arm] = verdict
    if not pairs:
        raise ValueError('No trials supplied')
    counts = Counter()
    regressions, incomplete = [], []
    for key, pair in sorted(pairs.items()):
        if len(pair) < 2:
            incomplete.append(key)
            continue
        counts['paired'] += 1
        for arm, verdict in pair.items():
            counts[arm] += int(verdict == 'pass')
        if pair['baseline'] == 'pass' and pair['candidate'] == 'fail':
            regressions.append(key)
    return dict(complete_pairs=counts['paired'], baseline_passes=counts['baseline'],
                candidate_passes=counts['candidate'], regressions=regressions, incomplete_pairs=incomplete)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    try:
        with open(sys.argv[1], newline='', encoding='utf-8-sig') as stream:
            print(json.dumps(summarize(csv.DictReader(stream)), indent=2))
    except (OSError, ValueError, KeyError, AttributeError) as exc:
        sys.exit(f'Invalid trial file: {exc}')
