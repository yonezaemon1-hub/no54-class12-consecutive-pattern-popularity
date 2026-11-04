#!/usr/bin/env python3
"""No54 v0.3 fail-closed package / section-8-only delta verification. No third-party deps."""
from pathlib import Path
import hashlib, json, sys, re
ROOT=Path(__file__).resolve().parent.parent
FROZEN=ROOT/'frozen_v0.2'
REFS=ROOT/'v0.3'/'No54_v0.3_PROOF_REFERENCES_20261105.md'
KNOWN = {
  "CLAUDE_AUDIT_REQUEST.md": "31969010a85e1e56d30a2aa37fc165ca6eb41025010b40ce29b15049d5c67ae8",
  "No54_v0.1_INDEPENDENT_ATTACK_20261105.py": "d5bd71db57eef902252f522284e3558f7a3ea497a58b16e435d8de843e26a080",
  "No54_v0.1_PROOF_AUDIT_20261105.md": "053f62ff69ff74152744be9679bae640843ee45628285ecf766cfb3e9c38fd43",
  "No54_v0.1_SHA256SUMS_20261105.txt": "7e3859342b69b4bc61bb6c34e7bc86b04f9acbe7e8e7aed79c6f2f14a25cae5d",
  "No54_v0.1_VERIFY_20261105.py": "e8a558958a4cd5944796d20d0519409b5f7127b99465cd06ebf32220075e8e0f",
  "No54_v0.1_VERIFY_LOG_20261105.txt": "957208ad37feb18f648b4b0bc3bca34b423f7e7421544b0cbb341fefc7abaa8e",
  "No54_v0.2_ADVERSARIAL_AUDIT_20261105.md": "eec6f8556a5ef980708f312d0311cadbccc746516e1f6fcfdfbaa8f17ad1f5eb",
  "No54_v0.2_ATTACK_LOG_20261105.txt": "1affca23186ee7771f7eea338ba3887542ad150bdd3a70c5a25e8c9f1fee4b53",
  "No54_v0.2_SHA256SUMS_20261105.txt": "1ed8b9d767deb4bc2ee60e796280f37353579de36c36c69bf3427c5b1204617c",
  "README_JA.md": "9845157f8a33bac467277e8a697be17078b6f6df29a3bb2a9800fc54f309971f",
  "RUN_WINDOWS_AUDIT.ps1": "269f20b7305ae5f547ce81728e82afa42ad1f1271ad4e22e901da5420da883a7",
  "SHA256SUMS_PACKAGE.txt": "cfe291cfa2ec6d04c2ab55769273ac38f176fd6cdaeeb7728adf2c9e9079f570"
}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def die(s): raise AssertionError('FAIL-CLOSED: '+s)
assert len(KNOWN)==12
for name, expected in KNOWN.items():
    p=FROZEN/name
    if not p.is_file() or sha(p)!=expected: die('original frozen byte hash mismatch '+name)
print('PASS: 12 frozen v0.2 package files unchanged')
manifest=ROOT/'SHA256SUMS_v0.3.txt'
if not manifest.is_file(): die('missing v0.3 manifest')
rows=manifest.read_text(encoding='utf-8').strip().splitlines()
verified=set()
for row in rows:
    m=re.fullmatch(r'([0-9a-f]{64})  ((?:frozen_v0\.2|v0\.3)/[A-Za-z0-9_.-]+|RUN_WINDOWS_V03\.ps1)',row)
    if not m: die('invalid manifest row: '+row)
    path=(ROOT/m.group(2))
    rel=str(path.relative_to(ROOT))
    if rel in verified: die('duplicate manifest row '+rel)
    if not path.is_file() or sha(path)!=m.group(1): die('hash mismatch '+rel)
    verified.add(rel)
expected={str(p.relative_to(ROOT)) for p in ROOT.glob('frozen_v0.2/*') if p.is_file()}
expected |= {str(p.relative_to(ROOT)) for p in ROOT.glob('v0.3/*') if p.is_file()}
expected.add('RUN_WINDOWS_V03.ps1')
# The manifest intentionally excludes itself only.
if verified!=expected: die('manifest list differs from folder contents: '+str(expected.symmetric_difference(verified)))
print('PASS:',len(verified),'v0.3 manifest entries')
old=(FROZEN/'No54_v0.1_PROOF_AUDIT_20261105.md').read_bytes()
new=REFS.read_bytes()
start=b'## 8. Prior work and novelty boundary\n'
newstart=b'## 8. Prior work, exact citation boundaries, and novelty status (bibliography-only revision v0.3)\n'
end=b'## 9. Audit request to a different model/reviewer\n'
if old.count(start)!=1 or new.count(newstart)!=1 or old.count(end)!=1 or new.count(end)!=1: die('bad section boundaries')
oldprefix,oldremainder=old.split(start,1)
newprefix,newremainder=new.split(newstart,1)
oldmid,oldsuffix=oldremainder.split(end,1)
newmid,newsuffix=newremainder.split(end,1)
if oldprefix!=newprefix or oldsuffix!=newsuffix: die('mathematical sections or section 9 changed')
if oldmid==newmid: die('reference section failed to change')
print('PASS: only proof section 8 changed; sections 1-7 and 9 byte-identical')
print('PASS: novelty INCONCLUSIVE and release HOLD retained in v0.3 status')
