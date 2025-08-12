```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: pdf
page_number: 141
page_id: pdf#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:47Z
fidelity: lossless
-->

## Essential PDF

```csharp
// Specifying Column name
pdfLightTable.Columns(2).ColumnName = "Student Name"
```

### StringFormat

The format of the data for a single column can be changed using the StringFormat property. Check String Formatting in [DrawingText](#DrawingText) for more details.

### Width

By default, all the columns in a PdfLightTable have equal width, and the columns automatically fill the entire width of the PdfLightTable. If the width of any of the column(s) is increased or decreased, the width of other columns changes appropriately.

To customize initial column widths, you can invoke the Width property for each column of the PdfLightTable. The following code snippet illustrates this:

```csharp
// Setting width for third column
pdfLightTable.Columns[2].Width = 10;
```

```vb.net
' Setting width for third column
pdfLightTable.Columns(2).Width = 10
```

**Note**: The unit of the Width property is always points. You can set the PDF units only as points. Also, you can use the [PdfUnitConverter](#PdfUnitConverter) class to convert the other units to points.

### Column Span

You can set column span in PdfLightTable using BeginRowLayout event. Check the following link for more details.

- [How To Implement Column Span In PdfLightTable?](#HowToImplementColumnSpanInPdfLightTable)

### Cell

You can specify the default cell style by using the DefaultStyle property. The style for the header cells is set by using the HeaderStyle property.

---

``` 
© 2013 Syncfusion. All rights reserved.   141 | Page 
```

<!-- tags: [pdf, column, stringformat, width, column span, cell, syncfusion, windows forms] keywords: [pdf, column properties, string formatting, column width, column span, cell style, default style, header style, pdflighttable] -->
``` 
