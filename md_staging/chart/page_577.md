```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_577.jpeg
document_name: chart
page_number: 577
page_id: chart#page_577
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to add and format text and charts in a document.
- Explains the process of saving and launching the document.
- Introduces exporting chart data into a grid cell using Essential Grid.

## Content

```vb
Dim section As IWSection = document.AddSection()
' Adding a paragraph to the section.
Dim paragraph As IWParagraph = section.AddParagraph()
' Writing text.
paragraph.AppendText("Essential Chart")
' Adding a new paragraph.
paragraph = section.AddParagraph()
paragraph.ParagraphFormat.HorizontalAlignment = Syncfusion.DLS.HorizontalAlignment.Center

' Inserting chart.
paragraph.AppendPicture(Image.FromFile(file))

' Save the Document to disk.
document.Save(exportFileName, Syncfusion.DocIO.FormatType.Doc)

' Launches the file.
System.Diagnostics.Process.Start(exportFileName)
```

A sample demonstrating the above is available in our installation at the following location:

```
"My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Chart.Windows\Samples\2.0\Export\Chart Export Data"
```

### 4.14.3 Exporting to Grid

The chart control can be exported into a grid cell (in Essential Grid) as an image using Essential Grid. The chart control provides APIs to convert it to an image, while the Grid will let you insert this image into any specific cell.

## API Reference (if applicable)
- Methods:
  - `AppendText(text As String)`
  - `AppendParagraph()`
  - `AppendPicture(image As Image)`
  - `Save(fileName As String, formatType As FormatType)`
  - Static methods like `Fromfile(file As String)`

## Code Examples (multi-language supported)
- **Visual Basic**
```vb
Dim section As IWSection = document.AddSection()
Dim paragraph As IWParagraph = section.AddParagraph()
paragraph.AppendText("Essential Chart")
paragraph = section.AddParagraph()
paragraph.ParagraphFormat.HorizontalAlignment = Syncfusion.DLS.HorizontalAlignment.Center
paragraph.AppendPicture(Image.FromFile(file))
document.Save(exportFileName, Syncfusion.DocIO.FormatType.Doc)
System.Diagnostics.Process.Start(exportFileName)
```

### Handling Export to Grid with Essential Grid
```vb
Dim chartImage As Image = chartControl.Image // Convert chart to image
gridControl.Cells[row, column].Image = chartImage // Insert into grid cell
```

## Cross References
- Refer to the chart control's API documentation for methods to convert the chart into an image.
- For grid-related operations, consult the Essential Grid documentation to learn how to insert images into grid cells.

<!-- tags: [syncfusion, windows forms, chart, grid, export, document, image export] keywords: [chart control, grid cell, Visual Basic, AppendText, AppendParagraph, AppendPicture, Save, Process.Start, Image, documentation, Essential Grid, row, column, API, image export] -->
```