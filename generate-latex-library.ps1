# Generate latex-library.json from the Drive folder
#
# Usage (from repo root):
#   pwsh -File ./generate-latex-library.ps1
# or
#   powershell -ExecutionPolicy Bypass -File ./generate-latex-library.ps1

$ErrorActionPreference = 'Stop'

# Resolve the Drive folder relatively so the script contains no non-ASCII path
# (Windows PowerShell 5.1 mis-decodes non-BOM UTF-8 string literals).
# Repo lives at: ...\Teaching materials CV education web at github\saq-questionnaire-main
# Target   lives at: ...\Teaching materials by LATEX          (sibling two levels up)
$SourceDir = (Resolve-Path (Join-Path $PSScriptRoot '..\..\Teaching materials by LATEX')).Path
$OutFile   = Join-Path $PSScriptRoot 'latex-library.json'

if (-not (Test-Path -LiteralPath $SourceDir)) {
    throw "Source folder not found: $SourceDir"
}

$extensions = @('.pdf', '.pptx', '.ppt', '.doc', '.docx', '.md', '.mp4')

$files = Get-ChildItem -LiteralPath $SourceDir -File -Recurse |
    Where-Object { $extensions -contains $_.Extension.ToLower() } |
    ForEach-Object {
        $relPath = $_.FullName.Substring($SourceDir.Length).TrimStart('\','/') -replace '\\','/'
        [PSCustomObject]@{
            name    = $_.Name
            path    = $relPath
            ext     = $_.Extension.ToLower().TrimStart('.')
            size    = [int64]$_.Length
            mtime   = $_.LastWriteTimeUtc.ToString("yyyy-MM-ddTHH:mm:ssZ")
        }
    } |
    Sort-Object name

# Preserve the previously-set drive_folder URL so re-running the script
# does not wipe out the user-configured share link.
$existingDriveUrl = '__SET_ME__'
if (Test-Path -LiteralPath $OutFile) {
    try {
        $prev = Get-Content -LiteralPath $OutFile -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($prev.drive_folder -and $prev.drive_folder -ne '__SET_ME__') {
            $existingDriveUrl = [string]$prev.drive_folder
        }
    } catch {
        # Old file was malformed; fall back to the sentinel.
    }
}

$payload = [PSCustomObject]@{
    source        = 'Teaching materials by LATEX'
    generated_at  = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    count         = $files.Count
    drive_folder  = $existingDriveUrl
    files         = @($files)
}

$json = $payload | ConvertTo-Json -Depth 4
[System.IO.File]::WriteAllText($OutFile, $json, [System.Text.UTF8Encoding]::new($false))

Write-Host ("Wrote {0} files to {1}" -f $files.Count, $OutFile)
