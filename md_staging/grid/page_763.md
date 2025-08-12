```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_763.jpeg
document_name: grid
page_number: 763
page_id: grid#page_763
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

| ReferencedFields | Saves a list of referenced field names used in the expression. Use semicolon as a delimiter to specify multiple fields. This list will be used by the engine to determine which cells to update when ListChanged event is triggered. |
| --- | --- |

## Overview

- You can add any number of expression fields to the table.
- Figure 306 illustrates the process.

## Content

### Expression Field Management

You can add any number of expression fields to the table. The following image depicts this.

![Figure 306: ExpressionFieldDescriptor Collection Editor](image_url)

### Programmatic Approach

#### ExpressionFieldDescriptor Collection Editor

This interface allows you to manage and define the properties of expression fields in the grid.

- **Members**:
  - `ExprWins`
  - `ExprLosses`

#### ExprLosses Properties

| Name | Value |
| --- | --- |
| Name | ExprLosses |
| ResultType | System.Double |
| Expression | `[losses]/100` |
| AllowTrimEnd | True |
| FieldPropertyType | System.Double |
| ForceImmediateS | False |
| Hide | False |
| ReferencedFields | losses |

### Programmatic

By using the `ExpressionFieldDescriptor Collection Editor`, you can programmatically define and manage expression fields, ensuring dynamic calculation and display in the grid control.

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid.Grouping

#### Class: ExpressionFieldDescriptor

##### Properties
- **Name**: string
- **ResultType**: Type
- **Expression**: string
- **AllowTrimEnd**: bool
- **FieldPropertyType**: Type
- **ForceImmediateS**: bool
- **Hide**: bool
- **ReferencedFields**: string

##### Methods
- **Update**(): Updates cells based on referenced fields when ListChanged event is triggered.

## Code Examples

### C#

```csharp
var exprLosses = new ExpressionFieldDescriptor
{
    Name = "ExprLosses",
    ResultType = typeof(double),
    Expression = "[losses]/100",
    AllowTrimEnd = true,
    FieldPropertyType = typeof(double),
    ForceImmediateS = false,
    Hide = false,
    ReferencedFields = "losses"
};
gridGroupingControl1.Expressions.Add(exprLosses);
```

### Remarks

Ensure that the referenced fields are correctly listed to maintain data consistency and accuracy when the grid updates dynamically.

## Page-level Navigation/TOC (if applicable)

- **ReferencedFields**
- **ExpressionFieldDescriptor Collection Editor**
- **Programmatic**

<!-- tags: [grid, windows forms, expression fields, Syncfusion, essential grid, ListChanged, referenced fields] keywords: [ReferencedFields, ExpressionFieldDescriptor, ExpressionFieldDescriptor Collection Editor, programmatically, dynamic calculation, ListChanged event, field properties] -->
```