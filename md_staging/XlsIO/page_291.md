```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_291.jpeg
document_name: XlsIO
page_number: 291
page_id: XlsIO#page_291
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:56Z
fidelity: lossless
-->

## Overview
- Demonstrates the creation and usage of a Combo Box control in Excel worksheets using the `IComboBoxShape` interface.
- Explains how to add a Combo Box to a worksheet and assign linked cell values.

## Content

### Check Box with Linked Cell created using XlsIO

Figure 97 shows an example of a checkbox with a linked cell, created using XlsIO. This feature enables interaction between form controls and specific cells in a worksheet.

![](image.png)  
*Figure 97: Check box with Linked Cell created using XlsIO*

### 4.2.8.3 Combo Box

Essential XlsIO now provides support to read/write a Combo Box control. This is achieved by using the `IComboBoxShape` interface, which is used to add a combo box inside a worksheet.

**Description:**
- The `IComboBoxShape` interface allows the integration of Combo Box controls into Excel spreadsheets.
- By assigning a `ListFillRange`, you can specify the range of values available in the combo box.
- A linked cell can be specified to store the selected value from the combo box, enabling interaction between user input and worksheet data.

#### Code Example

The following code example illustrates how to read/write a combo box control using C#:

```csharp
// Create a Combo Box.
IComboBoxShape comboBox1 = sheet.ComboBoxes.AddComboBox(27, 5, 20, 100);

// Assign a value to the Combo Box.
comboBox1.ListFillRange = sheet["A1:A12"];
comboBox1.LinkedCell = sheet["C3"];
```

### Summary
This section demonstrates how to create and configure a Combo Box control in an Excel worksheet using the `IComboBoxShape` interface in Essential XlsIO. The example code showcases the process of adding a combo box, specifying its value range, and linking it to a specific cell in the worksheet.

<!-- tags: [XlsIO, Combo Box, IComboBoxShape, Excel, Worksheet, Syncfusion Winforms] keywords: [Combo Box, Linked Cell, IComboBoxShape, Excel, XlsIO, Worksheet, Control, Value Range] -->
```