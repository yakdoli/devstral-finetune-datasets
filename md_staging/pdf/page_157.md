```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: pdf
page_number: 157
page_id: pdf#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:41Z
fidelity: lossless
-->

# Essential PDF

```csharp
/* Set the header names.
collection(0).Value = "Header1"
collection(1).Value = "Header2"
collection(2).Value = "Header3"
collection(3).Value = "Header4"
``` 

## RepeatHeader

Header can be set to repeat on each page where PdfGrid is paginated. RepeatHeader property should be set to true to achieve this.

### [C#]

```csharp
pdfGrid.RepeatHeader = true;
```

### [VB.NET]

```vb
pdfGrid.RepeatHeader = True
```

## Style

You can specify the header style for the PdfGrid by using the PdfGridRowStyle or PdfGridCellStyle classes. The style applied at the collection will be applied to all rows in the header. Following code example illustrates how to specify the header style.

### [C#]

```csharp
// Applying header style.
pdfGrid.Headers.ApplyStyle(style);
```

### [VB.NET]

```vb
' Applying header style.
pdfGrid.Headers.ApplyStyle(style)
```

### Note: Styles for each PdfGridRow in Header can be individually applied using PdfGridRowStyle class.

Refer to the following topics for more details:  
- **PdfGridRowStyle**

## Reference

- **PdfGridRowStyle**

<!-- tags: [syncfusion, winforms, pdfgrid, header, repeatheader, style, pdfgridrowstyle, vb.net, csharp] keywords: [header names, header style, repeat header, pdfgrid, row style] -->
```