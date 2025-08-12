```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_161.jpeg
document_name: pdf
page_number: 161
page_id: pdf#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:33:53Z
fidelity: lossless
-->

# Essential PDF

```csharp
// Set Width for first column.
pdfGrid.Columns[0].Width = 20f;
```

### [VB.NET]

```vb
' Set Width for first column.
pdfGrid.Columns(0).Width = 20f
```

**Note:** The unit of the `Width` property is always points. You can set the PDF units only as points. Also, you can use the `PdfUnitConverter` class to convert the other units to points.

## Column Span

PdfGrid enables you to merge cells within a column. You can specify the number of cells to be merged by using the `ColumnSpan` property of the `PdfGridCell` class. The following code example illustrates this.

### [C#]

```csharp
// Merging column cells.
pdfGrid.Rows[0].Cells[0].ColumnSpan = 2;
```

### [VB.NET]

```vb
' Merging column cells.
pdfGrid.Rows(0).Cells(0).ColumnSpan = 2
```

## Format

You can specify the content format for the `PdfGrid` columns by using the `Format` property. Check `String Formatting` in `DrawingText` for more details.

### **4.1.2.3.2.3.4 Cell**

#### Properties

| Name        | Description                        | Data Type          |
|-------------|------------------------------------|--------------------|
|             |                                    |                    |
```



## API Reference (if applicable)

### References

- Column formatting options.

### See also:

- [Cell properties](cell_properties)
- [String Formatting](string_formatting)
- [DrawingText](drawingtext_reference)
- [PdfUnitConverter](unit_conversion)
- [PdfGrid](grid_documentation)

<!-- tags: [pdfgrid, format, columnspan, width, cell, fusionpdf, syncfusion, winforms] keywords: [formatting, columns, span, width, units, conversion, merging, cell properties] -->
```