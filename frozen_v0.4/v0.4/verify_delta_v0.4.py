#!/usr/bin/env python3
"""No54 v0.4: fail-closed status-only delta and package integrity verification."""
from pathlib import Path
import hashlib, re, sys
ROOT=Path(__file__).resolve().parent.parent
OLD=ROOT/'frozen_v0.3'
PRE=OLD/'v0.3'/'No54_v0.3_PROOF_REFERENCES_20261105.md'
NOW=ROOT/'v0.4'/'No54_v0.4_PROOF_REFERENCES_STATUS_20261105.md'
PINNED={'RUN_WINDOWS_V03.ps1': 'e265ebc87e693091da50a86886a437dae4d0b5adfeffc22b4963072389aee149', 'frozen_v0.2/CLAUDE_AUDIT_REQUEST.md': '31969010a85e1e56d30a2aa37fc165ca6eb41025010b40ce29b15049d5c67ae8', 'frozen_v0.2/No54_v0.1_INDEPENDENT_ATTACK_20261105.py': 'd5bd71db57eef902252f522284e3558f7a3ea497a58b16e435d8de843e26a080', 'frozen_v0.2/No54_v0.1_PROOF_AUDIT_20261105.md': '053f62ff69ff74152744be9679bae640843ee45628285ecf766cfb3e9c38fd43', 'frozen_v0.2/No54_v0.1_SHA256SUMS_20261105.txt': '7e3859342b69b4bc61bb6c34e7bc86b04f9acbe7e8e7aed79c6f2f14a25cae5d', 'frozen_v0.2/No54_v0.1_VERIFY_20261105.py': 'e8a558958a4cd5944796d20d0519409b5f7127b99465cd06ebf32220075e8e0f', 'frozen_v0.2/No54_v0.1_VERIFY_LOG_20261105.txt': '957208ad37feb18f648b4b0bc3bca34b423f7e7421544b0cbb341fefc7abaa8e', 'frozen_v0.2/No54_v0.2_ADVERSARIAL_AUDIT_20261105.md': 'eec6f8556a5ef980708f312d0311cadbccc746516e1f6fcfdfbaa8f17ad1f5eb', 'frozen_v0.2/No54_v0.2_ATTACK_LOG_20261105.txt': '1affca23186ee7771f7eea338ba3887542ad150bdd3a70c5a25e8c9f1fee4b53', 'frozen_v0.2/No54_v0.2_SHA256SUMS_20261105.txt': '1ed8b9d767deb4bc2ee60e796280f37353579de36c36c69bf3427c5b1204617c', 'frozen_v0.2/README_JA.md': '9845157f8a33bac467277e8a697be17078b6f6df29a3bb2a9800fc54f309971f', 'frozen_v0.2/RUN_WINDOWS_AUDIT.ps1': '269f20b7305ae5f547ce81728e82afa42ad1f1271ad4e22e901da5420da883a7', 'frozen_v0.2/SHA256SUMS_PACKAGE.txt': 'cfe291cfa2ec6d04c2ab55769273ac38f176fd6cdaeeb7728adf2c9e9079f570', 'v0.3/CLAUDE_DELTA_AUDIT_REQUEST.md': '1ad0fc63cdaebcb124340f37c4e0250d4454c89c6c10b44364d16b55581f5b03', 'v0.3/DIFF_SECTION8_v0.2_to_v0.3.patch': '6d7def69fca8a0d9a8a359cb25a60604bc298bf6b579c52df52fd943ecd6b252', 'v0.3/No54_v0.3_PROOF_REFERENCES_20261105.md': 'a5c2e4f5ffc2338932455962470b8af3a6588c7c950df4c77a00c93c70ece82e', 'v0.3/STATUS_READ_FIRST_v0.3.md': '1a692a5a108f3338617a54ead8d12fac96dc4b5866f88ff347e6769b5885e192', 'v0.3/verify_delta_v0.3.py': 'bf66b34a64ba4fab877693184535489fd5d2245e9bc92a915b0e1ca3ee681cf1', 'SHA256SUMS_v0.3.txt': 'a1a3252882d5c9f21a0c3902c0e5b1858d78235a6d534fe162ae95dd6797776e'}
oldline=b'**Status:** Mathematical derivation drafted; independent AI audit **NOT PERFORMED**; novelty **INCONCLUSIVE**; human peer review **NOT PERFORMED**; publication **HOLD**.'
newline=b'**Status:** Mathematical derivation independently AI-audited (Claude v0.2 user-supplied report: MODEL / PROOF / COMPUTATION PASS; v0.3 differential audit PASS); novelty **INCONCLUSIVE**; human peer review **NOT PERFORMED**; publication **HOLD**.'
oldtheorem=b'**Theorem (candidate; requires independent audit).** For every integer `n >= 3`,'
newtheorem=b'**Theorem (independent AI mathematical audit reported PASS; novelty not established).** For every integer `n >= 3`,'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(ok,msg):
    if not ok: raise RuntimeError('FAIL-CLOSED: '+msg)
for rel, expected in PINNED.items():
    p=OLD/rel
    check(p.is_file() and sha(p)==expected, 'altered frozen v0.3 file: '+rel)
check(len({str(p.relative_to(OLD)) for p in OLD.rglob('*') if p.is_file()})==len(PINNED),'unexpected frozen file count')
check(set(str(p.relative_to(OLD)) for p in OLD.rglob('*') if p.is_file())==set(PINNED),'frozen inventory changed')
print('PASS: all 19 frozen v0.3 files unchanged')
rows=(ROOT/'SHA256SUMS_v0.4.txt').read_text(encoding='utf8').splitlines()
seen=set()
for row in rows:
    m=re.fullmatch(r'([0-9a-f]{64})  (frozen_v0\.3/[A-Za-z0-9_./-]+|v0\.4/[A-Za-z0-9_.-]+|RUN_WINDOWS_V04\.ps1)',row)
    check(m is not None,'bad SHA256 manifest row')
    rel=m.group(2)
    check(rel not in seen and '..' not in Path(rel).parts,'duplicate/unsafe manifest entry: '+rel)
    seen.add(rel)
    check((ROOT/rel).is_file() and sha(ROOT/rel)==m.group(1),'hash mismatch: '+rel)
expected=set(str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file())-{'SHA256SUMS_v0.4.txt'}
check(seen==expected, 'manifest incomplete / extra files: '+str(seen.symmetric_difference(expected)))
print('PASS:',len(seen),'v0.4 manifest hashes and exact inventory')
old=PRE.read_bytes();new=NOW.read_bytes()
check(old.count(oldline)==1 and old.count(oldtheorem)==1,'expected old status annotations not unique')
check(new==old.replace(oldline,newline).replace(oldtheorem,newtheorem),'non-status manuscript change')
check(b'novelty **INCONCLUSIVE**' in new and b'publication **HOLD**' in new,'hold/novelty not retained')
print('PASS: exactly two editorial lines changed, every other byte unchanged')
patch=(ROOT/'v0.4'/'DIFF_v0.3_to_v0.4.patch').read_text(encoding='utf8')
check(patch.count('\n@@ ')==2, 'expected two separate patch hunks')
print('PASS: v0.4 diff patch contains two hunks')
print('PASS: RELEASE HOLD, NOVELTY INCONCLUSIVE; Windows untested')
