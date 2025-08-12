<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_766.jpeg
document_name: grid
page_number: 766
page_id: grid#page_766
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:57Z
fidelity: lossless
-->

## Overview

- Demonstrates how to create nested expression fields in a grid using `ExpressionFieldDescriptor`.
- Implements appearance settings for custom display of these expression fields.
- Provides C# and VB.NET code examples.

## Nested Expression Fields in Windows Forms Grid

The following code examples are used to create nested expression fields.

### C# Example

```csharp
[C#]

// Define expression fields that are nested.
ExpressionFieldDescriptor expField1 = new
ExpressionFieldDescriptor("ExpCol1", "[wins]+[ties]+[losses]", 
typeof(System.Double));
ExpressionFieldDescriptor expField2 = new
ExpressionFieldDescriptor("ExpCol2", "[ExpCol1]*100", 
typeof(System.Double));

// Add these expression fields to the grid table.
this.gridGroupingControl1.TableDescriptor.ExpressionFields.AddRange(
new ExpressionFieldDescriptor[] { expField1, expField2 });

// Appearance Settings.
this.gridGroupingControl1.TableDescriptor.Columns["ExpCol1"].Appearance.
AnyRecordFieldCell.BackColor = Color.Cornsilk;
this.gridGroupingControl1.TableDescriptor.Columns["ExpCol2"].Appearance.
AnyRecordFieldCell.BackColor = Color.Cornsilk;
```

### VB.NET Example

```vb.net
[VB.NET]

' Define expression fields that are nested.
Dim expField1 As ExpressionFieldDescriptor = New
ExpressionFieldDescriptor("ExpCol1", "[wins]+[ties]+[losses]", 
GetType(System.Double))
Dim expField1 As ExpressionFieldDescriptor = New
ExpressionFieldDescriptor("ExpCol2", "[ExpCol1]*100", 
GetType(System.Double))

' Add these expression fields to the grid table.
Me.gridGroupingControl1.TableDescriptor.ExpressionFields.AddRange(
New ExpressionFieldDescriptor() { expField1, expField2 })

' Appearance Settings.
Me.gridGroupingControl1.TableDescriptor.Columns("ExpCol1").Appearance.A
nyRecordFieldCell.BackColor = Color.Cornsilk
Me.gridGroupingControl1.TableDescriptor.Columns("ExpCol2").Appearance.A
nyRecordFieldCell.BackColor = Color.Cornsilk
```

### Screen Shot Description

Here is a sample screen shot showing two expression fields **ExpCol1** and **ExpCol2** where **ExpCol2** is referencing **ExpCol1**.

<!-- tags: [syncfusion, winforms, expression fields, grid, windows forms, c#, vb.net] keywords: [nested expression fields, appearance settings, grid grouping control, expressionfielddescriptor, expcol1, expcol2] -->