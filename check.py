import json, sys
from pathlib import Path
p=json.loads(Path('.github/workflows/release.yml').read_text())['jobs']['production']
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
def pipeline():
    assert p['needs']==['validate'], 'production must need validate'
    assert p['if']=="${{ success() && github.ref == 'refs/heads/main' }}", 'require successful validation and main'
def controls():
    assert p['environment']=='production', 'wrong environment'
    assert p['permissions']=={'contents':'read'}, 'use read-only job permissions'
    assert p['steps'][0]['env']['RELEASE_TOKEN']=='${{ secrets.RELEASE_TOKEN }}', 'use secret reference, never literal token'
try:
    if mode in ('pipeline','all'): pipeline()
    if mode in ('controls','all'): controls()
    if mode=='review':
        print(Path('approval-review.md').read_text())
        print('REPORT READY: prose requires human grading, not automated PASS.')
    elif mode in ('pipeline','controls','all'):
        print(mode.upper()+' PASS: static configuration only. No live approval or deployment proven.')
    else: raise AssertionError('unknown command')
except (AssertionError,KeyError) as e:
    print('CHECK FAIL:',e);sys.exit(1)
