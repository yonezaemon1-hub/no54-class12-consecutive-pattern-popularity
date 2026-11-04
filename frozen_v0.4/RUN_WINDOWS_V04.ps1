# No.54 v0.4 PowerShell 5.1 audit suite; NOT YET TESTED ON WINDOWS.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifest = Join-Path $base 'SHA256SUMS_v0.4.txt'
if (-not (Test-Path -LiteralPath $manifest -PathType Leaf)) { throw 'FAIL-CLOSED: missing SHA256SUMS_v0.4.txt' }
$seen = @{}
foreach ($line in [System.IO.File]::ReadAllLines($manifest)) {
    if ($line -cnotmatch '^([a-f0-9]{64})  ((?:frozen_v0\.3/[A-Za-z0-9_./-]+)|(?:v0\.4/[A-Za-z0-9_.-]+)|RUN_WINDOWS_V04\.ps1)$') { throw "FAIL-CLOSED: invalid manifest line: $line" }
    $hash = $Matches[1]; $rel = $Matches[2]
    if ($rel -match '(^|/)\.\.(/|$)' -or $seen.ContainsKey($rel)) { throw 'FAIL-CLOSED: unsafe or duplicate path' }
    $seen[$rel] = $true
    $path = Join-Path $base ($rel.Replace('/',[IO.Path]::DirectorySeparatorChar))
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "FAIL-CLOSED: missing $rel" }
    if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() -cne $hash) { throw "FAIL-CLOSED: hash mismatch $rel" }
}
$all = @(Get-ChildItem -LiteralPath $base -Recurse -File | Where-Object { $_.FullName -ne $manifest })
if ($seen.Count -ne $all.Count) { throw 'FAIL-CLOSED: unexpected extra or missing files' }
Write-Host "PASS: $($seen.Count) SHA256 hashes"
& python -I (Join-Path (Join-Path $base 'v0.4') 'verify_delta_v0.4.py')
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: v0.4 delta verifier failed' }
& python -I (Join-Path (Join-Path (Join-Path $base 'frozen_v0.3') 'frozen_v0.2') 'No54_v0.1_VERIFY_20261105.py')
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: direct enumeration verifier failed' }
& python -I (Join-Path (Join-Path (Join-Path $base 'frozen_v0.3') 'frozen_v0.2') 'No54_v0.1_INDEPENDENT_ATTACK_20261105.py')
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: rational integral verifier failed' }
Write-Host 'PASS: No54 v0.4 Windows audit suite'
