```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_132.jpeg
document_name: XlsIO
page_number: 132
page_id: XlsIO#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:58:02Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
sheet.Range("C4").BorderInside(ExcelLineStyle.Dash_dot, Color.Red)
```

## 4.1.1.5 Fill Settings

This section illustrates the fill settings available in Excel.

### Color

MS Excel provides support to format its cells, rows, and columns with various colors and patterns. This can be done by using the **Fill Color** button and an associated palette.

![Figure 42: Format Cells Dialog Box](https://via.placeholder.com/600)

A color is a 4-byte number of the format `00BBGGRR`, where `RR`, `GG`, and `BB` values are the Red, Green, and Blue values, each of which is between 0 and 255 (`&HFF`). If all component values are 0, the RGB color is 0, which is black. If all component values are 255 (`&HFF`), the RGB color is `16,777,215` (`&H00FFFFFF`), or white. All other color combinations of values for the red, green, and blue components.
```