```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: grid
page_number: 157
page_id: grid#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:06Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Demonstrates how to configure a grid cell to display currency values.
- Includes setting the cell type, formatting properties, and style attributes.
- Examples provided in both C# and VB.NET.

## Content

### Cell Configuration for Currency Values

#### C#

```csharp
GridStyleInfo style = gridControl[row, 2];
style.CellType = "Currency";
style.Text = "$1.00";

// Set the clip mode.
style.CurrencyEdit.ClipMode = CurrencyClipModes.IncludeFormatting;

// Set formatting properties.
style.CurrencyEdit.CurrencyDecimalDigits = 2;
style.CurrencyEdit.CurrencyDecimalSeparator = ".";
style.CurrencyEdit.CurrencyGroupSeparator = ",";
style.CurrencyEdit.CurrencyGroupSizes = new int[] { 3 };
style.CurrencyEdit.CurrencyNegativePattern = 1;
style.CurrencyEdit.CurrencyNumberDigits = 27;
style.CurrencyEdit.CurrencyPositivePattern = 0;
style.CurrencyEdit.CurrencySymbol = "$";
style.CurrencyEdit.NegativeColor = System.Drawing.Color.Red;
style.CurrencyEdit.NegativeSign = "-";
style.CurrencyEdit.PositiveColor = System.Drawing.Color.Black;
style.FloatCell = true;
```

#### VB.NET

```vb
Dim style As GridStyleInfo = gridControl(row, 2)
style.CellType = "Currency"
style.Text = "$1.00"

' Set the clip mode.
style.CurrencyEdit.ClipMode = CurrencyClipModes.IncludeFormatting

' Set formatting properties.
style.CurrencyEdit.CurrencyDecimalDigits = 2
style.CurrencyEdit.CurrencyDecimalSeparator = "."
style.CurrencyEdit.CurrencyGroupSeparator = ","
style.CurrencyEdit.CurrencyGroupSizes = New Integer() { 3 }
style.CurrencyEdit.CurrencyNegativePattern = 1
style.CurrencyEdit.CurrencyNumberDigits = 27
style.CurrencyEdit.CurrencyPositivePattern = 0
style.CurrencyEdit.CurrencySymbol = "$"
style.CurrencyEdit.NegativeColor = System.Drawing.Color.Red
style.CurrencyEdit.NegativeSign = "-"
style.CurrencyEdit.PositiveColor = System.Drawing.Color.Black
style.FloatCell = True
```

### Explanation

- **CellType**: Sets the cell to display currency values.
- **Text**: Initializes the cell with a default currency value.
- **CurrencyEdit.ClipMode**: Ensures the currency formatting is preserved when editing.
- **Formatting Properties**: Configures the appearance of the currency values, including symbols, separators, and color coding for positive and negative values.
- **FloatCell**: Allows floating the cell for dynamic resizing.

## API Reference

### Namespaces and Classes

- **GridStyleInfo**: Represents the style attributes of a grid cell.
- **CurrencyClipModes**: Enumerates the modes for clipping currency formatting.
- **System.Drawing.Color**: Represents a color used for UI elements.
- **GridControl**: Primary control for displaying and managing grid data.

### Properties

- **CellType**: Gets or sets the type of the cell.
- **Text**: Gets or sets the text content of the cell.
- **CurrencyEdit**: Provides properties for configuring currency formatting.
  - **CurrencyDecimalDigits**: Number of decimal places to display.
  - **CurrencyDecimalSeparator**: Character used to separate decimals.
  - **CurrencyGroupSeparator**: Character used to separate groups of digits.
  - **CurrencyGroupSizes**: Array specifying the sizes of digit groups.
  - **CurrencyNegativePattern**: Determines how negative values are displayed.
  - **CurrencyNumberDigits**: Total number of significant digits.
  - **CurrencyPositivePattern**: Determines how positive values are displayed.
  - **CurrencySymbol**: Symbol used to denote currency.
  - **NegativeColor**: Color for negative values.
  - **NegativeSign**: Sign used for negative values.
  - **PositiveColor**: Color for positive values.
- **FloatCell**: Enables floating of the cell.

## Code Examples

The examples above demonstrate how to configure a grid cell to display currency values with specific formatting and style attributes. This ensures consistency and clarity in presenting financial data within a Windows Forms application.

## Related Documentation

Refer to the Syncfusion WinForms documentation for more information on grid controls and their configuration options.

<!-- tags: [syncfusion, winforms, grid, cell configuration, currency formatting] keywords: [gridstyleinfo, currencyedit, celltype, currencyformatting, floatcell] -->
```