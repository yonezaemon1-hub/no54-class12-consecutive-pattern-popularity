# No54 Windows PowerShell 5.1 audit. SHA256 fail-closed, then independent verification.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifest = Join-Path $base 'SHA256SUMS_PACKAGE.txt'
if (-not (Test-Path -LiteralPath $manifest -PathType Leaf)) { throw 'FAIL-CLOSED: no package SHA256 manifest' }
$count = 0
foreach ($line in [System.IO.File]::ReadAllLines($manifest)) {
    if ($line -notmatch '^([a-fA-F0-9]{64})  ([A-Za-z0-9_.-]+)$') { throw "FAIL-CLOSED: bad manifest line: $line" }
    $expected = $Matches[1].ToLowerInvariant()
    $name = $Matches[2]
    $path = Join-Path $base $name
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "FAIL-CLOSED: missing $name" }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($expected -cne $actual) { throw "FAIL-CLOSED: SHA256 mismatch $name" }
    $count += 1
}
if ($count -lt 10) { throw 'FAIL-CLOSED: too few checksums' }
Write-Host "PASS: $count file hashes verified"
& python -I (Join-Path $base 'No54_v0.1_VERIFY_20261105.py')
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: brute-force verification failed' }
& python -I (Join-Path $base 'No54_v0.1_INDEPENDENT_ATTACK_20261105.py')
if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: independent simplex verification failed' }
Write-Host 'PASS: No54 audit reproduction (Windows runner)'
