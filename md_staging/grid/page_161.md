```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_161.jpeg
document_name: grid
page_number: 161
page_id: grid#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:28Z
fidelity: lossless
-->  

## Overview
- Demonstrates the Grid List Control cell type, available in the sample at the specified installation path.
- Details the Header cell type and its implementation, providing code examples in C# and VB.NET.

## Content

### 4.1.4.1.8 Header

The Header cell type displays static text similar to the standard CellType, but it can also have a button-like border with a depressed state. 

#### Setting the Cell Type to Header

The following code examples illustrate how to set the cell type to Header.

##### C#

```csharp
// Set Cell Type as "Header".
gridControl1[rowIndex, colIndex].Text = "HeaderText";

// Set Formatting properties.
gridControl1[rowIndex, colIndex].CellType = "Header";
gridControl1[rowIndex, colIndex].BackColor = Color.FromArgb(208, 208, 208);
```

##### VB.NET

```vb
' Set Cell Type as "Header".
gridControl1(rowIndex, colIndex).Text = "HeaderText"

' Set Formatting properties.
gridControl1(rowIndex, colIndex).CellType = "Header"
gridControl1(rowIndex, colIndex).BackColor = Color.FromArgb(208, 208, 208)
```

![Header Cells](Figure 84: Header Cells)

<!-- tags: Header, CellType, Grid List Control, GridControl1, Text, BackColor, C#, VB.NET, static text, button-like border, depressed state, implementation, sample path, header cells, Syncfusion Winforms, version 11.4.0.26 -->
```