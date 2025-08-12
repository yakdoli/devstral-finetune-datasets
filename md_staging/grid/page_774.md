```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_774.jpeg
document_name: grid
page_number: 774
page_id: grid#page_774
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates adding record filters through code.
- Explores the use of expression fields and filter expressions.
- Highlights nested tables and setting record filters to child tables.

## Content

### Adding Record Filters Through Code

#### Figure: Adding Record Filters Through Code

![Figure 310: Adding Record Filters Through Code](#)

**Note:** Filter Expressions share the same format as in expression fields. For a list of valid expressions, refer to the **List of Filter Expressions**.

### Nested Tables

Record Filters can also be set to the nested tables by accessing the `RecordFilters` collection of the `ChildTableDescriptor`.

### C#

```csharp
FilterCondition cond = new FilterCondition(FilterCompareOperator.GreaterThan, 20);
RecordFilterDescriptor filter = new RecordFilterDescriptor("OrderID", cond);
this.gridGroupingControl.GetTableDescriptor("Orders").RecordFilters.Add(filter);
```

### VB.NET

```vb
Dim cond As FilterCondition = New FilterCondition(FilterCompareOperator.GreaterThan, 20)
Dim filter As RecordFilterDescriptor = New RecordFilterDescriptor("OrderID", cond)
Me.gridGroupingControl.GetTableDescriptor("Orders").RecordFilters.Add(filter)
```

## API Reference

### Namespace
- `Syncfusion.Windows.Forms.Grid`

### Class
- `GridGroupingControl`

### Methods
- `GetTableDescriptor(string tableName)`
- `Add(RecordFilterDescriptor filter)`

## Code Examples

### C# Example
```csharp
FilterCondition cond = new FilterCondition(FilterCompareOperator.GreaterThan, 20);
RecordFilterDescriptor filter = new RecordFilterDescriptor("OrderID", cond);
this.gridGroupingControl.GetTableDescriptor("Orders").RecordFilters.Add(filter);
```

### VB.NET Example
```vb
Dim cond As FilterCondition = New FilterCondition(FilterCompareOperator.GreaterThan, 20)
Dim filter As RecordFilterDescriptor = New RecordFilterDescriptor("OrderID", cond)
Me.gridGroupingControl.GetTableDescriptor("Orders").RecordFilters.Add(filter)
```

## Cross References
- See also: List of Filter Expressions.

<!-- tags: [product, module, control, api, version?], keywords: [Essential Grid, Windows Forms, RecordFilters, Nested Tables, Expression Fields, Filter Expressions, GridGroupingControl] -->
```