```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_764.jpeg
document_name: grid
page_number: 764
page_id: grid#page_764
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to set up and use expression fields in the Essential Grid for Windows Forms.
- Explains how to define and add two expression fields to a Statistics table.
- Provides examples in both C# and VB.NET languages.

## Content

### Setting Expression Fields

Expression Fields can also be set through code. The following code example adds two expression fields to the Statistics table.

#### [C#]

```csharp
// Define expression fields.
ExpressionFieldDescriptor exp1 = new ExpressionFieldDescriptor("Winning %", "([wins] *100)/([wins]+[ties]+[losses])", "System.Double");
ExpressionFieldDescriptor exp2 = new ExpressionFieldDescriptor("Loosing %", "([losses] *100)/([wins]+[ties]+[losses])", "System.Double");

// Add the expression fields to the grid table.
this.gridGroupingControl1.TableDescriptor.ExpressionFields.AddRange(new Syncfusion.Grouping.ExpressionFieldDescriptor[] { exp1, exp2 });
```

#### [VB.NET]

```vb
' Define expression fields.
Dim exp1 As ExpressionFieldDescriptor = New ExpressionFieldDescriptor("Winning %", "([wins] *100)/([wins]+[ties]+[losses])", "System.Double")
Dim exp2 As ExpressionFieldDescriptor = New ExpressionFieldDescriptor("Loosing %", "([losses] *100)/([wins]+[ties]+[losses])", "System.Double")

' Add the expression fields to the grid table.
this.gridGroupingControl1.TableDescriptor.ExpressionFields.AddRange(New Syncfusion.Grouping.ExpressionFieldDescriptor() { exp1, exp2 })
```

### Visual Representation

The screen shot given below highlights these expression fields.

## Page-level Navigation/TOC
- See also: related topics on Essential Grid features.

<!-- tags: [Windows Forms, Essential Grid, Expression Fields, C#, VB.NET] keywords: [grid, window forms, essential grid, expression fields, code example, statistics table, AddRange] -->
```