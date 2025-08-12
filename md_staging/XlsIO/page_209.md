```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_209.jpeg
document_name: XlsIO
page_number: 209
page_id: XlsIO#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:28Z
fidelity: lossless
-->

# XlsIO

Essential XlsIO

## Content

### Overview
- This section demonstrates how to insert images, barcodes, and charts into an Excel document using the XlsIO library.
- It also explains how to extract images from an existing spreadsheet.

### Detailed Explanation

#### Inserting Images, Barcodes, and Charts
- Barcodes and Charts can be inserted in a spreadsheet by utilizing XlsIO's Image Insertion API's.
- The barcode/chart is rendered to an image using the Essential Barcode/ Essential Chart, and then inserted into the spreadsheet as an image.

#### Extracting Images
- XlsIO can extract images from an existing spreadsheet.

#### Example in Code

**C#**
```csharp
[C#]

// Read Image.
this.pictureBox1.Image = sheet.Pictures[0].Picture;
```

**VB.NET**
```vb
[VB.NET]

' Read Image.
Me.pictureBox1.Image = sheet.Pictures(0).Picture
```

### Summary
- The XlsIO library provides a robust set of tools for managing images, including the insertion and extraction of images, barcodes, and charts within Excel documents.

## API Reference

- **Namespace**: Essential.XlsIO
- **Class**: XlsIO
- **Methods**:
  - `InsertPicture()`: Inserts an image into the spreadsheet.
  - `ExtractPicture()`: Extracts an image from the spreadsheet.
- **Properties**:
  - `Pictures`: Collection of pictures in the spreadsheet.

## Code Examples

#### C# Example for Extracting an Image
```csharp
// Sample code
using Syncfusion.XlsIO;

// Initialize Excel Engine and Workbook
ExcelEngine engine = new ExcelEngine();
IApplication application = engine.Excel;
IWorkbook workbook = application.Workbooks.Open("Sample.xlsx");

// Get the first worksheet
IWorksheet sheet = workbook.Worksheets[0];

// Extract the first image from the worksheet
Image image = sheet.Pictures[0].Picture;

// Display the extracted image
this.pictureBox1.Image = image;
```

#### VB.NET Example for Extracting an Image
```vb
' Sample code
Imports Syncfusion.XlsIO

' Initialize Excel Engine and Workbook
Dim engine As New ExcelEngine()
Dim application As IApplication = engine.Excel
Dim workbook As IWorkbook = application.Workbooks.Open("Sample.xlsx")

' Get the first worksheet
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Extract the first image from the worksheet
Dim image As Image = sheet.Pictures(0).Picture

' Display the extracted image
Me.pictureBox1.Image = image
```

## Page-level Navigation/TOC (if applicable)
- Inserting Images, Barcodes, and Charts
- Extracting Images
- Code Examples
- Summary

## Cross References
- See also: Essential Barcode/ Essential Chart for detailed information on barcode and chart rendering.

<!-- tags: [xlsio, image insertion, barcode, chart, image extraction, c#, vb.net, syncfusion, winforms] keywords: [insertion, extraction, image, barcode, chart, api, c#, vb.net, spreadsheet, XlsIO] -->
```