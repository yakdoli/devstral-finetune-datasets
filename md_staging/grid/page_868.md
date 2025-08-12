```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_868.jpeg
document_name: grid
page_number: 868
page_id: grid#page_868
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Setting Conditional Formatting

### Overview
This section provides an example of how to set up conditional formatting for the GridControl in Syncfusion's Windows Forms. The steps include defining appearance and expressions for specific conditions.

### WinForms Conditional Formatting Example
The following C# code snippet demonstrates how to create two conditional format descriptors with specific styles applied to records based on conditions.

#### C# Example
```csharp
GridConditionalFormatDescriptor format1 = new GridConditionalFormatDescriptor();
format1.Appearance.AnyRecordFieldCell.Interior = new BrushInfo(Color.FromArgb(255, 191, 52));
format1.Appearance.AnyRecordFieldCell.TextColor = Color.White;
format1.Expression = "[CustomerID] LIKE 'A%'";
format1.Name = "ConditionalFormat 1";

// Apply the following style to the records whose ContactTitle = 'Sales Representative'.
GridConditionalFormatDescriptor format2 = new GridConditionalFormatDescriptor();
format2.Appearance.AnyRecordFieldCell.Font.Bold = true;
format2.Appearance.AnyRecordFieldCell.Interior = new BrushInfo(Color.FromArgb(102, 110, 152));
format2.Appearance.AnyRecordFieldCell.TextColor = Color.White;
format2.Expression = "[ContactTitle] LIKE 'Sales Representative'";
format2.Name = "ConditionalFormat 2";
```

#### VB.NET Example
```vb
'Apply the following style to the records whose CustomerID starts with 'A'
Dim format1 As GridConditionalFormatDescriptor = New GridConditionalFormatDescriptor()
format1.Appearance.AnyRecordFieldCell.Interior = New BrushInfo(Color.FromArgb(255, 191, 52))
format1.Appearance.AnyRecordFieldCell.TextColor = Color.White
format1.Expression = "[CustomerID] LIKE 'A%'";
format1.Name = "ConditionalFormat 1"

'Apply the following style to the records whose ContactTitle = 'Sales Representative'
Dim format2 As GridConditionalFormatDescriptor = New GridConditionalFormatDescriptor()
format2.Appearance.AnyRecordFieldCell.Font.Bold = True
format2.Appearance.AnyRecordFieldCell.Interior = New BrushInfo(Color.FromArgb(102, 110, 152))
format2.Appearance.AnyRecordFieldCell.TextColor = Color.White
format2.Expression = "[ContactTitle] LIKE 'Sales Representative'"
format2.Name = "ConditionalFormat 2"
```

### Adding the Descriptor to the TableDescriptor

#### C# Example
```csharp
this.gridGroupingControl.TableDescriptor.ConditionalFormats.Add(format1);
```

## Notes
This example shows how to set conditional formatting in the GridControl by applying specific styles to records based on predefined conditions. The expressions are used to determine which records should be formatted using the defined styles.

### Cross References
- See also: [Conditional Formatting in GridControl](#section-link)
- Further information: [Syncfusion Grid Documentation](#link-to-documentation)

<!-- tags: [syncfusion, gridcontrol, windowsforms, conditionalformatting, customization] keywords: [grid, conditional formatting, appearance, expression, font style, sales representative, customerid] -->
```
