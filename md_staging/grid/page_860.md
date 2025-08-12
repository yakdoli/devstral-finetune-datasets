```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_860.jpeg
document_name: grid
page_number: 860
page_id: grid#page_860
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:17Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to customize the appearance of a Grid in WinForms by setting interior colors for specific columns.

## Content

### Customizing Grid Column Appearance

The following code examples show how to create `GridColumnDescriptor` objects and customize the interior colors for specific columns in the grid.

#### C#
```csharp
desc1.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.FromArgb(237, 240, 246));
GridColumnDescriptor desc2 = new GridColumnDescriptor();
desc2.MappingName = "SupplierID";
desc2.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.FromArgb(218, 229, 245));

GridColumnDescriptor desc3 = new GridColumnDescriptor();
desc3.MappingName = "CategoryID";
desc3.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.FromArgb(102, 110, 152));

GridColumnDescriptor desc4 = new GridColumnDescriptor();
desc4.MappingName = "QuantityPerUnit";
desc4.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.FromArgb(252, 172, 38));
```

#### VB.NET
```vb
Dim desc1 As GridColumnDescriptor = New GridColumnDescriptor
desc1.MappingName = "ProductName"
desc1.Appearance.RecordFieldCell.Interior = New BrushInfo(Color.FromArgb(237, 240, 246))

Dim desc1 As GridColumnDescriptor = New GridColumnDescriptor
desc1.MappingName = "ProductName"
desc1.Appearance.RecordFieldCell.Interior = New BrushInfo(Color.FromArgb(218, 229, 245))

Dim desc1 As GridColumnDescriptor = New GridColumnDescriptor
desc1.MappingName = "SupplierID"
desc1.Appearance.RecordFieldCell.Interior = New BrushInfo(Color.FromArgb(102, 110, 152))

Dim desc1 As GridColumnDescriptor = New GridColumnDescriptor
desc1.MappingName = "QuantityPerUnit"
desc1.Appearance.RecordFieldCell.Interior = New BrushInfo(Color.FromArgb(252, 172, 38))
```

Given below is a sample screen shot.

---

## API Reference

### GridColumnDescriptor
- **MappingName**: Specifies the name of the property or field in the data source to bind to the column.
- **Appearance.RecordFieldCell.Interior**: Sets the interior color of the record cells in the column.

### Color.FromArgb
- Creates a `Color` object from the specified ARGB components.

## Code Examples

### C#
```csharp
// Initialize GridColumnDescriptor for ProductName
desc1.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.FromArgb(237, 240, 246));

// Initialize GridColumnDescriptor for SupplierID
desc2.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.FromArgb(218, 229, 245));

// Initialize GridColumnDescriptor for CategoryID
desc3.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.FromArgb(102, 110, 152));

// Initialize GridColumnDescriptor for QuantityPerUnit
desc4.Appearance.RecordFieldCell.Interior = new BrushInfo(Color.FromArgb(252, 172, 38));
```

### VB.NET
```vb
' Initialize GridColumnDescriptor for ProductName
desc1.Appearance.RecordFieldCell.Interior = New BrushInfo(Color.FromArgb(237, 240, 246))

' Initialize GridColumnDescriptor for SupplierID
desc1.Appearance.RecordFieldCell.Interior = New BrushInfo(Color.FromArgb(218, 229, 245))

' Initialize GridColumnDescriptor for CategoryID
desc1.Appearance.RecordFieldCell.Interior = New BrushInfo(Color.FromArgb(102, 110, 152))

' Initialize GridColumnDescriptor for QuantityPerUnit
desc1.Appearance.RecordFieldCell.Interior = New BrushInfo(Color.FromArgb(252, 172, 38))
```

<!-- tags: [syncfusion, winforms, grid, customization, appearance, column, color, interior] keywords: [GridColumnDescriptor, MappingName, Interior, Color, ARGB, customization, appearance, grid column] -->
```