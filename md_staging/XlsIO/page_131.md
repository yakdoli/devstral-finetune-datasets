```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: XlsIO
page_number: 131
page_id: XlsIO#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:52Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
ExcelKnownColors.Blue
sheet.Range("A2").CellStyle.Borders(ExcelBordersIndex.EdgeTop).Color = ExcelKnownColors.Blue
```

![XlsIO with Border Settings](https://example.com/image.png)
*Figure 41: XlsIO with Border Settings*

You can also set the borders for a range as follows.

### Code Examples

#### [C#]

```csharp
sheet.Range["C2"].BorderAround();
sheet.Range["C4"].BorderInside(ExcelLineStyle.Dash_dot, Color.Red);
```

#### [VB.NET]

```vb
sheet.Range("C2").BorderAround()
```

## API Reference

### Methods

- `BorderAround()`: Sets a uniform border around the specified range.
- `BorderInside(ExcelLineStyle, Color)`: Sets an interior border with the specified line style and color.

## Cross References

See also:
- Excel Known Colors
- Excel Line Styles
- Excel Borders
```