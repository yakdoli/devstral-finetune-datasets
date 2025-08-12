```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_259.jpeg
document_name: XlsIO
page_number: 259
page_id: XlsIO#page_259
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:30Z
fidelity: lossless
-->

# Essential XlsIO

## Content

### Code Examples

[C#]
```csharp
// Change the range values that the Pivot Tables range refers to.
myWorkbook.Names["PivotRange"].RefersToRange = mySheet.Range["A1:D27"];
```

[Vb.NET]
```vb
' Change the range values that the Pivot Tables range refers to.
Private myWorkbook.Names("PivotRange").RefersToRange = mySheet.Range("A1:D27")
```

### Pivot Table Creation By Using MS Excel 2007

**In Excel, Pivot table can be inserted by selecting the PivotTable option from the Insert menu.**

**Figure 89: Create PivotTable Dialog Box**

![Create PivotTable Dialog Box](https://i.imgur.com/8W6K480.png)

**Excel automatically selects the entire range. However, it is possible to modify it if necessary. It also allows choosing where to place the PivotTable (New Worksheet is most commonly used to place the pivot table).**

## API Reference

- `myWorkbook.Names["PivotRange"].RefersToRange`: Sets the range that the Pivot Tables range refers to.
- `mySheet.Range["A1:D27"]`: Specifies the range of cells from "A1" to "D27".

## Code Examples

[C#]
```csharp
// Example of creating a PivotTable in C#
// Code snippet to demonstrate how to programmatically create a PivotTable
// using the specified range.

// Example of setting the range for the PivotTable
myWorkbook.Names["PivotRange"].RefersToRange = mySheet.Range["A1:D27"];
```

[Vb.NET]
```vb
' Example of creating a PivotTable in VB.NET
' Code snippet to demonstrate how to programmatically create a PivotTable
' using the specified range.

' Example of setting the range for the PivotTable
Private myWorkbook.Names("PivotRange").RefersToRange = mySheet.Range("A1:D27")
```

## Footer

© 2013 Syncfusion. All rights reserved. 259 | Page

<!-- tags: [xlsio, pivottable, range, excel, 2007, codeexamples, sdk繄cere']));
```