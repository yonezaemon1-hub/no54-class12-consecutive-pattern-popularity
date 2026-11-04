# No54 v0.3 PowerShell 5.1 fail-closed check; Windows not tested in authoring container.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifest = Join-Path $base 'SHA256SUMS_v0.3.txt'
if (-not (Test-Path -LiteralPath $manifest -PathType Leaf)) { throw 'FAIL-CLOSED: missing SHA256SUMS_v0.3.txt' }
$count = 0
foreach ($line in [System.IO.File]::ReadAllLines($manifest)) {
  if ($line -cnotmatch '^([a-f0-9]{64})  (frozen_v0\.2|v0\.3)/([A-Za-z0-9_.-]+)$') { throw "FAIL-CLOSED: malformed hash line $line" }
  $hash = $Matches[1]
  $sub = $Matches[2]
  $name = $Matches[3]
  $path = Join-Path (Join-Path $base $sub) $name
  if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "FAIL-CLOSED: missing $sub/$name" }
  if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() -cne $hash) { throw "FAIL-CLOSED: hash mismatch $sub/$name" }
  $count++
}
if ($count -lt 15) { throw 'FAIL-CLOSED: insufficient hashes' }
Write-Host "PASS: $count v0.3 hashes"
& python -I (Join-Path (Join-Path $base 'v0.3') 'verify_delta_v0.3.py')
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: delta check failed' }
& python -I (Join-Path (Join-Path $base 'frozen_v0.2') 'No54_v0.1_VERIFY_20261105.py')
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: brute-force check failed' }
& python -I (Join-Path (Join-Path $base 'frozen_v0.2') 'No54_v0.1_INDEPENDENT_ATTACK_20261105.py')
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: rational integral check failed' }
Write-Host 'PASS: No54 v0.3 Windows audit suite'
