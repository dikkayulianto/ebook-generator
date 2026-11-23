param(
    [string]$inputPath,
    [string]$outputPath
)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0 # wdAlertsNone

try {
    $fullIn = [System.IO.Path]::GetFullPath($inputPath)
    $fullOut = [System.IO.Path]::GetFullPath($outputPath)
    
    # Open(FileName, ConfirmConversions, ReadOnly, AddToRecentFiles)
    $doc = $word.Documents.Open($fullIn, $false, $false, $false)
    
    # Format document margins & orientation
    $doc.PageSetup.TopMargin = $word.CentimetersToPoints(2.0)
    $doc.PageSetup.BottomMargin = $word.CentimetersToPoints(2.0)
    $doc.PageSetup.LeftMargin = $word.CentimetersToPoints(2.5)
    $doc.PageSetup.RightMargin = $word.CentimetersToPoints(2.0)
    
    # wdFormatXMLDocument = 16 (.docx)
    $doc.SaveAs2($fullOut, 16)
    $doc.Close([ref]$false)
    Write-Output "SUCCESS: Converted to DOCX: $fullOut"
} catch {
    Write-Output "ERROR: $($_.Exception.Message)"
} finally {
    $word.Quit()
}
