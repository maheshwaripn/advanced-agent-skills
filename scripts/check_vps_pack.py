"""Check the optional marketplace pack without invoking an external service."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def check():
    entries = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())['plugins']
    entry, = [e for e in entries if e['name'] == 'vps-workflows']
    pack = ROOT / entry['source']
    manifest = json.loads((pack / '.claude-plugin/plugin.json').read_text())
    catalog = (pack / 'README.md').read_text()
    folders = sorted((pack / 'skills').iterdir())
    assert manifest['name'] == entry['name']
    assert sorted(manifest['skills']) == ['./skills/' + f.name for f in folders]
    links = re.findall(r'\]\(([^)]+/SKILL.md)\)', catalog)
    assert len(links) == len(set(links)) == len(folders) + 2
    for link in links:
        assert (pack / link).is_file(), link
    for folder in folders:
        skill = (folder / 'SKILL.md').read_text()
        assert f'\nname: {folder.name}\n' in skill
        assert 'disable-model-invocation: true' in skill
        assert 'allow_implicit_invocation: false' in (folder / 'agents/openai.yaml').read_text()
        for heading in ('## Illustrative request', '## Expected result'):
            assert skill.partition(heading)[2].strip(), folder
    print(f'{len(folders)} companion skills and {len(links)} illustrated mappings verified.')


if __name__ == '__main__':
    check()
