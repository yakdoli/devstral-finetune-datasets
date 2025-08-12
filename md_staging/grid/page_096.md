```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_096.jpeg
document_name: grid
page_number: 096
page_id: grid#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:22:12Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to set the `StyleInfo.Format` property for a specific grid bound column.
- Provides a visual guide on configuring grid columns using the GridBoundColumn Collection Editor.
- Explains the steps to apply formatting to a column, specifically the 'UnitPrice' column, displaying values in a specified currency format.

## Content

### Using the GridBoundColumn Collection Editor
The GridBoundColumn Collection Editor allows you to configure the properties of grid columns. In the screenshot below, we are focusing on setting the `StyleInfo.Format` property for `gridBoundColumn2`.

#### GridBoundColumn Collection Editor
- **Members**:
  - `gridBoundColumn1`
  - `gridBoundColumn2`
  - `gridBoundColumn3`
- **Properties** for `gridBoundColumn2`:
  - Enabled: `True`
  - FloatCell: `True`
  - FloodCell: `True`
  - Font: Not specified
  - **Format**: `C` (Currency format)
  - FormattedText: Not specified
  - HorizontalAlign: `Left`
  - HotkeyPrefix: `None`
  - ImageIndex: `None`
  - ImageList: `None`
  - ImageSizeMode: `CenterImage`
  - Interior: `Solid; Window`
  - MaskEdit: Not specified
  - MaxLength: `0`
  - MergeCell: `None`
  - NumericUpDown: Not specified

#### Setting the Format Property
To format the `UnitPrice` column to display values in currency format:
1. Open the GridBoundColumn Collection Editor.
2. Select `gridBoundColumn2`.
3. Navigate to the `Format` property and set it to `C` for currency format.
4. Click `OK` to apply the changes.

### Verifying the Format
- Compile and run the project to see the formatted Grid Data Bound Grid.
- The grid will display the columns in the order and format you specified.
- Observe the 'UnitPrice' column, which will now show values in the specified currency format.

## API Reference

### Properties
- **Enabled**: A boolean property indicating whether the column is enabled.
- **FloatCell**: A boolean property indicating whether the column supports floating-point values.
- **FloodCell**: A boolean property indicating whether the column supports flooded cells.
- **Font**: A property to define the font for the column.
- **Format**: A property to specify the format of the column's values (e.g., `C` for currency).
- **HorizontalAlign**: A property to set the horizontal alignment of the column's contents.
- **HotkeyPrefix**: A property to define the hotkey prefix for the column.
- **ImageIndex**: A property to specify the image index for the column.
- **ImageList**: A property to specify the image list for the column.
- **ImageSizeMode**: A property to define the sizing mode for images in the column.
- **Interior**: A property to define the interior style of the column.
- **MaskEdit**: A property to specify a mask for editing the column's values.
- **MaxLength**: A property to define the maximum length of the column's values.
- **MergeCell**: A property to specify if the column's cells can be merged.
- **NumericUpDown**: A property to specify if the column supports numeric up-down feature.

## Code Examples

### Example: Configuring GridBoundColumn Properties
```csharp
// Configuring gridBoundColumn2
gridBoundColumn2.Enabled = true;
gridBoundColumn2.FloatCell = true;
gridBoundColumn2.FloodCell = true;
gridBoundColumn2.Format = "C"; // Currency format
gridBoundColumn2.HorizontalAlign = HorizontalAlignment.Left;
```

### Running the Project
1. Compile the project.
2. Run the application to see the formatted Grid Data Bound Grid.
3. Verify that the 'UnitPrice' column displays values in the specified currency format.

## Cross References
- For more information on grid formatting and styling, refer to the GridStyler documentation.
- See also: GridBoundColumn, GridDataBoundGrid, GridStyleInfo, and related properties.

<!-- tags: [Syncfusion, Winforms, Grid, GridDataBoundGrid, gridBoundColumn, styling, formatting] keywords: [currency format, property editor, grid, winforms, styleinfo, gridboundcolumn collection editor] -->
```