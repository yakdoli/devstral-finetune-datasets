```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_362.jpeg
document_name: pdf
page_number: 362
page_id: pdf#page_362
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:47:16Z
fidelity: lossless
-->

## Essential PDF

### 5.1.2.8 How to edit header in PdfGrid?

When data source is set to PdfGrid, captions from source will automatically add as header. This header can be edited to display any custom text.

**Note:** Editing text will affect only the PdfGrid and will not reflect in data source.

The following is the code snippet:

```csharp
// Edit cell value in header.
pdfGrid.Headers[0].Cells[0].Value = "Employee ID";
```

```vb.net
' Edit cell value in header.
pdfGrid.Headers(0).Cells(0).Value = "Employee ID"
```

### 5.1.2.9 How to set width for Table?

By default, both PdfLightTable and PdfGrid classes automatically calculate width if one is not specified during Draw. However, it is possible to specify width using one of the overloads in Draw method. The following is the code snippet.

```csharp
// Draw PdfLightTable with specified width.
pdfLightTable.Draw(pdfGraphics, PointF.Empty, width);
pdfLightTable.Draw(pdfGraphics, x_pos, y_pos, width);
pdfLightTable.Draw(pdfPage, x_pos, y_pos, width);
pdfLightTable.Draw(pdfPage, x_pos, y_pos, width, pdfLightTableLayoutFormat);

// Draw PdfGrid with specified width.
pdfGrid.Draw(pdfGraphics, PointF.Empty, width);
pdfGrid.Draw(pdfGraphics, x_pos, y_pos, width);
pdfGrid.Draw(pdfPage, x_pos, y_pos, width);
pdfGrid.Draw(pdfPage, x_pos, y_pos, width, pdfGridLayoutFormat);
```

```vb.net
' Draw PdfLightTable with specified width.
pdfLightTable.Draw(pdfGraphics, PointF.Empty, width)
```

---

``` 
© 2013 Syncfusion. All rights reserved. 362 | Page
```
``` 

<!-- tags: [product, syncfusion, winforms, essentialpdf, pdfgrid, pdflighttable, table, header, width, api] keywords: [syncfusion winforms, essentialpdf, pdfgrid, pdflighttable, table, header, width, editing header, setting width, data source, pdf, draw method, c#, vb.net, code snippet] -->
``` 
