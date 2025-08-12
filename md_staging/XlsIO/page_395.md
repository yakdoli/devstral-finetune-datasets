```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_395.jpeg
document_name: XlsIO
page_number: 395
page_id: XlsIO#page_395
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:30Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
shape.Fill.GradientStyle = ExcelGradientStyle.Horizontal
shape.Fill.GradientColorType = ExcelGradientColor.TwoColor
shape.Fill.ForeColorIndex = ExcelKnownColors.Red
shape.Fill.BackColorIndex = ExcelKnownColors.White
```

XlsIO also provides options to resize the comment size, and move/size with cell by using the `IsMoveWithCell` and `IsSizeWithCell` properties. You can also autofit the size of the comment by using the `AutoFit` property.

> **Note:** Currently it is not possible to insert preformatted RTF tags in Excel by using XlsIO.

## 4.6.2 Changes

Excel provides various options that can be used to protect a workbook or worksheet, or just a cell.

This section explains how the following features of Excel can be implemented by using XlsIO.

- Workbook Protection—This section explains how a workbook can be protected by using the Windows and Structure option of Excel.
- Worksheet Protection—This section explains how a worksheet can be protected with or without a password. It also explains how a particular element modification can be prevented.
- Edit Range—This section explains how to lock/unlock a particular range in a protected worksheet.

### 4.6.2.1 Workbook Protection

MS Excel provides the creator of a workbook the ability to protect the Structure and Windows of a workbook with a password. It includes the following options.

- **Protecting Structure**

  Worksheets and chart sheets in a workbook with protection cannot be moved, deleted, hidden, unhidden, or renamed, and new sheets cannot be inserted.

- **Protecting Windows**

<!-- tags: [XlsIO, workbook protection, worksheet protection, edit range, Excel, Syncfusion Winforms, version 11.4.0.26] keywords: [workbook protection, worksheet protection, edit range, XlsIO, Excel, Syncfusion, Winforms] -->
```