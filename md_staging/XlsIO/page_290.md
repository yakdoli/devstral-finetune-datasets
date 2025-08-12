```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_290.jpeg
document_name: XlsIO
page_number: 290
page_id: XlsIO#page_290
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:49Z
fidelity: lossless
-->

## Overview

- Essential XlsIO supports reading and writing of check boxes using the ICheckBoxShape interface to add and manipulate check boxes in a worksheet.
- The ICheckBoxShape interface facilitates creating check boxes with link to a specific cell.
- Examples are provided in both C# and VB.NET for creating and reading check boxes.

## Content

Essential XlsIO supports reading and writing of check boxes. This can be done by using the ICheckBoxShape interface, which is used to add a check box inside a worksheet.

### Code Examples

#### C# Example

```csharp
// Create a check box with cell link.
ICheckBoxShape chkBoxXlsIO = sheet.CheckBoxes.AddCheckBox(4, 4, 20, 75);
chkBoxXlsIO.Text = "XlsIO";
chkBoxXlsIO.CheckState = ExcelCheckState.Checked;
chkBoxXlsIO.LinkedCell = sheet["B4"];

// Read a check box.
ICheckBoxShape chkBoxXlsIO = sheet.CheckBoxes[0];
chkBoxXlsIO.Name = "chkBoxXlsIO";
```

#### VB.NET Example

```vb.net
' Create a check box.
Dim chkBoxXlsIO As ICheckBoxShape = sheet.CheckBoxes.AddCheckBox(5, 5, 20, 75)
chkBoxXlsIO.Text = "XlsIO"
chkBoxXlsIO.CheckState = ExcelCheckState.Checked
chkBoxXlsIO.LinkedCell = sheet("B4")

' Read a check box.
Dim chkBoxXlsIO As ICheckBoxShape = sheet.CheckBoxes(0)
chkBoxXlsIO.Name = "chkBoxXlsIO"
```

<!-- tags: [Essential XlsIO, ICheckBoxShape, ExcelCheckState, Check boxes, Check box interface, C#, VB.NET] keywords: [add checkbox, read checkbox, linked cell, check box interface, C# example, VB.NET example] -->
```