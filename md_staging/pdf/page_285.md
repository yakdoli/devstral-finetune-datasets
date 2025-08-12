```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_285.jpeg
document_name: pdf
page_number: 285
page_id: pdf#page_285
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:16Z
fidelity: lossless
-->

```csharp
' Set OCR language to process
processor.Settings.Language = Languages.English

' Process OCR by providing the PDF document, data dictionary, and language
processor.PerformOCR(lDoc, tessDataPath)

' Save the OCR processed PDF document in a disk
lDoc.Save("Sample.pdf")
lDoc.Close(True)
End Using
```

## 4.2.9.4 Perform OCR for a Specific Region of PDF Document

The following code example explains how to perform OCR for a specific region of the PDF document.

```csharp
[C#]
// Initialize the OCR processor
using (OCRProcessor processor = new OCRProcessor(ocrBinariesPath))
{
    // Load a PDF document
    PdfLoadedDocument lDoc = new PdfLoadedDocument(fileName);

    // Set OCR language to process
    processor.Settings.Language = Languages.English;
    RectangleF rect = new RectangleF(0, 100, 950, 150);

    // Assign rectangles to the page
    PageRegion region = new PageRegion();
    List<PageRegion> pageRegions = new List<PageRegion>();
    region.PageIndex = 1;
    region.PageRegions = new RectangleF[] { rect };
    pageRegions.Add(region);
    processor.Settings.OCRPageRegion = pageRegions;

    // Process OCR by providing the PDF document, data dictionary, and language
    processor.PerformOCR(lDoc, tessDataPath);
}
```

<!-- tags: [syncfusion-sdk, perform OCR, Syncfusion Winforms, specific region, PDF document, OCR processor] keywords: [OCR, PDF document, specific region, OCR processor, OCR language, OCRPageRegion, performOCR] -->
```