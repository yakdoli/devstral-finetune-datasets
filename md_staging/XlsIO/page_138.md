```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_138.jpeg
document_name: XlsIO
page_number: 138
page_id: XlsIO#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:41Z
fidelity: lossless
-->

## Essential XlsIO

### Applying Default style in XlsIO

XlsIO provides various ways to apply styles. The `IStyle` interface is used for creating styles. You can set the default styles created with groups of styles to a range of rows and columns. This is the most optimized approach to format rows and columns with large numbers of cells with the same styles.

Following code example illustrates how to create and apply default styles for a range of rows and columns.

#### C#

```csharp
// Define the default styles that need to be applied to rows and columns.
IStyle rowStyle = workbook.Styles.Add("RowStyle");
rowStyle.Color = Color.LightCoral;
IStyle columnStyle = workbook.Styles.Add("ColumnStyle");
columnStyle.Color = Color.Orange;

// Set Column Default Style
sheet.SetDefaultRowStyle(1, 2, rowStyle);

// Set Column Default Style
sheet.SetDefaultColumnStyle(1, 2, columnStyle);
```

#### VB.NET

```vb.net
' Define the default styles that need to be applied to rows and columns
Dim rowStyle As IStyle = workbook.Styles.Add("RowStyle")
rowStyle.Color = Color.LightCoral
Dim columnStyle As IStyle = workbook.Styles.Add("ColumnStyle")
columnStyle.Color = Color.Orange

' Set Column Default Style
sheet.SetDefaultRowStyle(1, 2, rowStyle)

' Set Column Default Style
sheet.SetDefaultColumnStyle(1, 2, columnStyle)
```

---

**Note**: Applying custom styles will override the original styles.

### See Also
```