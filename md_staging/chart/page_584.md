```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_584.jpeg
document_name: chart
page_number: 584
page_id: chart#page_584
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
series.CategoryLabels = sheet.Range("A1:A5")

' Make the chart as active sheet.
chart.Activate()

' Save the Chart book.
chartBook.SaveAs(exportFileName)
chartBook.Close()
ExcelUtils.Close()

' Launches the file.
System.Diagnostics.Process.Start(exportFileName)
```

## Sample

A sample demonstrating the above functionality is available in our installation at the following location:

```
"My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Chart.Windows\Samples\2.0\Export\Chart Export Data"
```

## 4.14.5 Exporting to PDF

The chart control can be exported into a PDF file as an image using Essential PDF. The chart control provides APIs to convert it to an image, while Essential PDF lets you insert this image into a Word Document file programmatically.

![Adobe Reader - chartexport.pdf screenshot showing chart](image.png)

<!-- tags: [windows forms, chart control, export, pdf, essential pdf, chart exporting] keywords: [chart, export, pdf, windows forms, essential studio, image export, api, document, word, programmatically, syncfusion] -->
```