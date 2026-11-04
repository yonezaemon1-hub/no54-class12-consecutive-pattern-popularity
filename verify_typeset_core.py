from pathlib import Path
import re,json,hashlib
base=Path(__file__).resolve().parent
package=base if (base/'paper').is_dir() else base/'publication_prepared'
p=package/'paper'
original=(p/'AUDITED_CORE_EXACT.md').read_text()
frozen=(package/'frozen_v0.4'/'v0.4'/'No54_v0.4_PROOF_REFERENCES_STATUS_20261105.md')
if frozen.exists():
    full=frozen.read_text()
    assert original==full[full.index('## 1.'):full.index('## 8.')]
published=(p/'No54_v1.0_PREPRINT_20261105.md').read_text()
body=published[published.index('## Definitions'):published.index('## Prior work')]
body=re.sub(r'\\needspace\{\d+\\baselineskip\}\n\n','',body)
for header in re.findall(r'^## \d+\. .*$',original,re.M):
    title=re.sub(r'^## \d+\. ','',header)
    body=body.replace('## '+title+'\n',header+'\n',1)
original_items=re.findall(r'`([^`]+)`',original)
mapping={x['audited_notation']:x['typeset_latex'] for x in json.loads((p/'NOTATION_TRANSCRIPTION.json').read_text())}
matches=list(re.finditer(r'\$\$([^$]+)\$\$|\$([^$]+)\$|`([^`]+)`',body))
assert len(matches)==len(original_items),(len(matches),len(original_items))
parts=[]; last=0
for old,m in zip(original_items,matches):
    kind='code' if m.group(3) is not None else 'math'
    rendered=m.group(1) or m.group(2) or m.group(3)
    expected=old if kind=='code' else mapping[old]
    assert rendered==expected,(old,rendered,expected)
    parts.extend([body[last:m.start()],'`'+old+'`']);last=m.end()
parts.append(body[last:])
reconstructed=''.join(parts)
assert reconstructed.strip()==original.strip(),'NON-NOTATION CORE TEXT CHANGED'
result={'result':'PASS','original_core_sha256':hashlib.sha256(original.encode()).hexdigest(),'notation_items_checked':len(matches),'sections_checked':7,'description':'Sections 1-7 reconstruct the exact frozen prose and every formula token, apart from heading numbering, typesetting delimiters and pagination commands.'}
if package!=base:
    (package/'TYPESET_CORE_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
