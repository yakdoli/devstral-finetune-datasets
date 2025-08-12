```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_284.jpeg
document_name: pdf
page_number: 284
page_id: pdf#page_284
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:09Z
fidelity: lossless
-->

## Content

### Overview
- Steps to organize web deployment using Syncfusion OCR processor.
- Code examples for performing OCR on a complete PDF document in both C# and VB.

### 4.2.9.2.3 Web Deployment
Use the following steps to organize web deployment:
1. Place the **SyncfusionTesseract.dll** and **liblept168.dll** assemblies in the local system and provide an assembly path to the OCR processor.
2. Refer to the following assemblies to your project:
   - Syncfusion.Core.dll
   - Syncfusion.Compression.Base.dll
   - Syncfusion.Pdf.Base.dll
   - Syncfusion.OCRProcessor.Base.dll

### 4.2.9.3 Performing OCR for a Complete PDF Document
The following code example illustrates how to perform OCR for a complete PDF document.

#### C#
```csharp
//Initialize the OCR processor
using (OCRProcessor processor = new OCRProcessor(ocrBinariesPath))
{
    //Load a PDF document
    PdfLoadedDocument lDoc = new PdfLoadedDocument(fileName);
    //Set OCR language to process
    processor.Settings.Language = Languages.English;
    //Process OCR by providing the PDF document, data dictionary and language
    processor.PerformOCR(lDoc, tessDataPath);
    //Save the OCR processed PDF document in a disk
    lDoc.Save("Sample.pdf");
    lDoc.Close(true);
}
```

#### VB
```vb
'Initialize the OCR processor
Using processor As New OCRProcessor(ocrBinariesPath)
    'Load a PDF document
    Dim lDoc As New PdfLoadedDocument(fileName)
```

## API Reference
- **OCRProcessor**
  - **PerformOCR** (Method): Processes OCR on a PDF document.
  - **Settings.Language**: Property to set the OCR language.
  - **PdfLoadedDocument**: Class for loading PDF documents.

## Code Examples (multi-language supported)
- Both C# and VB examples are provided for initializing the OCR processor and performing OCR on a PDF document.

## Page-level Navigation/TOC (if applicable)
- This page provides detailed instructions for web deployment and performing OCR on PDFs using Syncfusion OCR processor.

<!-- tags: [syncfusion, ocr, pdf, web deployment, c#, vb] keywords: [web deployment, pdf document, ocr processor, syncfusion, libraries, initialization, perform ocr] -->
```