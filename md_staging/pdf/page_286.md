```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_286.jpeg
document_name: pdf
page_number: 286
page_id: pdf#page_286
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:27Z
fidelity: lossless
-->

## OCRProcessor Sample Code Example

### C#

```csharp
// Save the OCR processed PDF document in a disk
lDoc.Save("Sample.pdf");
lDoc.Close(true);
}
```

### VB

```vb
Using processor As New OCRProcessor(ocrBinariesPath)
    'Load a PDF document
    Dim lDoc As New PdfLoadedDocument(fileName)
    'Set OCR language to process
    processor.Settings.Language = Languages.English
    Dim rect As New RectangleF(0, 100, 950, 150)
    'Assign rectangles to the page
    Dim region As New PageRegion()
    Dim pageRegions As New List(Of PageRegion)()
    region.PageIndex = 1
    region.PageRegions = New RectangleF() {rect}
    pageRegions.Add(region)
    processor.Settings.OCRPageRegion = pageRegions
    'Process OCR by providing the PDF document, data dictionary, and language
    processor.PerformOCR(lDoc, tessDataPath)
    'Save the OCR processed PDF document in a disk
    lDoc.Save("Sample.pdf")
    lDoc.Close(True)
End Using
```

## Note: Tesseract Binaries Location

**Note:** The Tesseract binaries, namely `SyncfusionTesseract.dll`, `liblept168.dll`, and language pack (tessdata), will be available in the following location:

```plaintext
<Installation Location>\Syncfusion\Essential Studio\<Version Number>\OCRProcessor
```

### References

- **Date:** © 2013 Syncfusion. All rights reserved.
- **Page Number:** 286

<!-- tags: [OCRProcessor, Tesseract, WinForms, Syncfusion, version 11.4.0.26] keywords: [OCR, PDF, Tesseract binaries, OCRPageRegion, PerformOCR, PageRegion, OCRProcessor, OCR, PDF document processing] -->
```