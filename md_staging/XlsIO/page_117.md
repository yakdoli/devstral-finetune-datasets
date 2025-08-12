```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: XlsIO
page_number: 117
page_id: XlsIO#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:56:13Z
fidelity: lossless
-->

# Essential XlsIO

At times, the text you enter in a cell will be wider than the cell. In such situations, the text may be hidden beyond the edge of the cell. Although one solution to this problem is to resize the cell, there are two additional solutions. They are, to Shrink the text to fit the cell, or Wrap the text so that it is displayed in multiple lines within the cell.

Yet another solution could be to merge multiple cells, so that the text can be fully displayed.

XlsIO allows to set these text control options by using the following APIs.

```csharp
[C#]

// Merging of Cells.
sheet.Range["A16:C16"].Merge();

// Wrapping Text.
sheet.Range["A14"].WrapText = true;
```

```vbnet
[VB.NET]

' Merging of Cells.
sheet.Range("A16:C16").Merge()

' Wrapping Text.
sheet.Range("A14").WrapText = True
```

## Orientation

The Orientation section enables you to bend the text to a fixed angle. There are two ways to set an angle. By dragging the small red diamond, one can specify the desired angle. You can also click one of the arrows of the Degrees spin button.

```csharp
[C#]

// Text Orientation Settings.
sheet.Range["B2"].CellStyle.Rotation = 60;
sheet.Range["B4"].CellStyle.Rotation = 90;
```

```vbnet
[VB.NET]

' Text Orientation Settings.
sheet.Range("B2").CellStyle.Rotation = 60;
```

## References
- [Syncfusion Winforms Documentation](https://www.syncfusion.com/documentation/windowsforms)

<!-- tags: [product, module, control, api, version?] keywords: [Excel, text formatting, XlsIO, text orientation, text wrapping, text merging, Syncfusion Winforms] -->
```