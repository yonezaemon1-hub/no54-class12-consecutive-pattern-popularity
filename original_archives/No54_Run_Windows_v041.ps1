# No.54 v0.4.1 Windows reproduction launcher (PATH-SEPARATOR HOTFIX ONLY).
# Original No54_Audit_v04.zip is SHA256-pinned and NEVER modified.
# Applies a tightly scoped, 3-occurrence path normalization to the original
# v0.4 Python delta verifier IN MEMORY only. All other verifications are unchanged.
# PowerShell 5.1 compatible; no admin rights, network, installs, or publication.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$downloads = Join-Path $env:USERPROFILE 'Downloads'
$archivePath = Join-Path $downloads 'No54_Audit_v04.zip'
$expectedZipSha256 = '9fca07c3ce4f15bfa7c9022660cab8051a175149291a0c38e605dce1c5adc446'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss_fff'
$workDir = Join-Path $downloads ('No54_v041_WINDOWS_REPRO_' + $stamp)
$logPath = Join-Path $downloads ('No54_v041_WINDOWS_LOG_' + $stamp + '.txt')
$transcriptStarted = $false
$exitCode = 1
try {
    Start-Transcript -Path $logPath -ErrorAction Stop | Out-Null
    $transcriptStarted = $true
    Write-Host 'No54 v0.4.1 Windows path-separator hotfix. Original v0.4 ZIP is immutable.'
    if (-not (Test-Path -LiteralPath $archivePath -PathType Leaf)) {
        throw "FAIL-CLOSED: ZIP missing: $archivePath"
    }
    $zipSha = (Get-FileHash -LiteralPath $archivePath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($zipSha -cne $expectedZipSha256) {
        throw "FAIL-CLOSED: original ZIP SHA256 mismatch; got $zipSha"
    }
    Write-Host "PASS: original ZIP SHA256 $zipSha"

    $pyCmd = Get-Command 'python.exe' -ErrorAction Stop
    if ($pyCmd.CommandType -ne 'Application') { throw 'FAIL-CLOSED: python.exe not a native application' }
    $pyExe = $pyCmd.Source
    & $pyExe --version
    if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: python version command failed' }
    & $pyExe -I -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 2)'
    if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: Python 3.10+ required' }

    if (Test-Path -LiteralPath $workDir) { throw 'FAIL-CLOSED: work folder already exists' }
    Expand-Archive -LiteralPath $archivePath -DestinationPath $workDir -ErrorAction Stop
    $inner = Join-Path $workDir 'No54_v0.4_CLAUDE_DELTA_AUDIT_20261105'
    $manifest = Join-Path $inner 'SHA256SUMS_v0.4.txt'
    if (-not (Test-Path -LiteralPath $manifest -PathType Leaf)) { throw 'FAIL-CLOSED: missing manifest' }

    $seen = @{}
    foreach ($line in [System.IO.File]::ReadAllLines($manifest)) {
        if ($line -cnotmatch '^([a-f0-9]{64})  ((?:frozen_v0\.3/[A-Za-z0-9_./-]+)|(?:v0\.4/[A-Za-z0-9_.-]+)|RUN_WINDOWS_V04\.ps1)$') {
            throw "FAIL-CLOSED: malformed manifest row: $line"
        }
        $hash = $Matches[1]; $rel = $Matches[2]
        if ($rel -match '(^|/)\.\.(/|$)' -or $seen.ContainsKey($rel)) {
            throw "FAIL-CLOSED: duplicate/unsafe manifest path: $rel"
        }
        $seen[$rel] = $true
        $path = Join-Path $inner ($rel.Replace('/', [IO.Path]::DirectorySeparatorChar))
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "FAIL-CLOSED: missing $rel" }
        if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() -cne $hash) {
            throw "FAIL-CLOSED: original package hash changed: $rel"
        }
    }
    $files = @(Get-ChildItem -LiteralPath $inner -File -Recurse | Where-Object { $_.FullName -cne $manifest })
    if ($seen.Count -ne $files.Count) { throw 'FAIL-CLOSED: original archive inventory differs from manifest' }
    if ($seen.Count -ne 27) { throw 'FAIL-CLOSED: unexpected original manifest entry count' }
    Write-Host 'PASS: all 27 original package hashes and file inventory'

    # The helper is outside the original package. It normalizes three Path
    # string conversions IN MEMORY. The on-disk script, ZIP and manifest stay
    # byte-identical to the original v0.4 Claude-audited package.
    $helper = Join-Path $workDir 'verify_windows_path_only_v041.py'
    $helperSource = @'
import sys
from pathlib import Path
root = Path(sys.argv[1]).resolve()
original = root / 'v0.4' / 'verify_delta_v0.4.py'
raw = original.read_bytes()
needle_old = b'str(p.relative_to(OLD))'
needle_root = b'str(p.relative_to(ROOT))'
if raw.count(needle_old) != 2 or raw.count(needle_root) != 1:
    raise RuntimeError('FAIL-CLOSED: verifier does not have the expected three path-conversion sites')
fixed = raw.replace(needle_old, b'p.relative_to(OLD).as_posix()')
fixed = fixed.replace(needle_root, b'p.relative_to(ROOT).as_posix()')
assert fixed != raw
print('PASS: Windows path normalization in memory only; original verifier untouched')
code = compile(fixed.decode('utf-8'), str(original), 'exec')
exec(code, {'__file__': str(original), '__name__': '__main__'})
'@
    [System.IO.File]::WriteAllText($helper, $helperSource, (New-Object System.Text.UTF8Encoding($false)))
    & $pyExe -I $helper $inner
    if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: normalized v0.4 delta verifier failed' }

    $frozen = Join-Path (Join-Path $inner 'frozen_v0.3') 'frozen_v0.2'
    $brute = Join-Path $frozen 'No54_v0.1_VERIFY_20261105.py'
    $rational = Join-Path $frozen 'No54_v0.1_INDEPENDENT_ATTACK_20261105.py'
    & $pyExe -I $brute
    if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: brute force verifier failed' }
    & $pyExe -I $rational
    if ($LASTEXITCODE -ne 0) { throw 'FAIL-CLOSED: rational integral verifier failed' }
    Write-Host 'PASS: No54 v0.4.1 WINDOWS REPRODUCTION (path-separator fix only)'
    Write-Host 'NOTE: Mathematics and audited data unchanged; novelty INCONCLUSIVE; publication HOLD.'
    $exitCode = 0
} catch {
    Write-Host ('FAIL-CLOSED: ' + $_.Exception.Message) -ForegroundColor Red
} finally {
    if ($transcriptStarted) {
        try { Stop-Transcript | Out-Null } catch { Write-Host ('WARNING: stop transcript: ' + $_.Exception.Message) }
    }
    Write-Host "LOG: $logPath"
    Write-Host "EXTRACTED: $workDir"
}
exit $exitCode
