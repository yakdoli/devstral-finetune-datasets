```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_095.jpeg
document_name: grid
page_number: 095
page_id: grid#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:46Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### GridBoundColumn Collection Editor

The GridBoundColumn Collection Editor is used to manage and define the properties of grid columns in the **Essential Grid for Windows Forms** control. This editor provides a comprehensive way to configure each column's appearance and behavior. Below are the key sections visible in the editor:

#### Members
- **gridBoundColumn1**: This section lists the grid bound columns. The editor shows the current column `gridBoundColumn1` as a placeholder, allowing users to manage multiple columns.

#### gridBoundColumn1 Properties
- **Name**: gridBoundColumn.
- **Modifiers**: Private.
- **HeaderText**: This field is left empty, indicating that the header text for the column can be customized.
- **MappingName**: Maps to `Product Name`.
- **ReadOnly**: Set to `False`, indicating the column is not read-only.
- **StyleInfo**: Various properties can be configured here, such as:
  - **AllowEnter**: Set to `False`.
  - **AutoSize**: Set to `False`.
- **BackColor**: The background color of the column can be customized. The dropdown menu offers several color options including `OldLace`, `FloralWhite`, `DarkGoldenRod`, `GoldenRod`, `CornSilk`, and more. Notably, `LightGoldenRodYellow` is selected, indicating a light yellow color for the column.

### Figure 60: Setting StyleInfo.BackColor for the Column

The Figure illustrates the process of setting the `StyleInfo.BackColor` for a specific column. The interface enables developers to customize the column's appearance effectively.

### Steps for Adding Grid Bound Columns

1. **Adding Columns**: Repeat the above steps to add additional Grid Bound Columns for `UnitPrice` and `UnitsInStock`.
   
2. **Formatting the 'UnitPrice' Column**:
   - For the 'UnitPrice' Grid Bound Column, set `StyleInfo.Format` to `C`. This ensures that the unit price information is displayed in a currency format.

## Additional Notes
- The `gridBoundColumn1` properties editor provides a structured way to define how each column in the grid will look and behave, including text, mapping, and style configurations.
- Customizing each column ensures a tailored user experience in the grid control, making it easier to display and interact with data.

## References
- Syncfusion Documentation: For more information and advanced configurations, refer to the official Syncfusion documentation on GridBoundColumn properties and customization options.

<!-- tags: [essential grid, windows forms, gridboundcolumn, styleinfo, backcolor, unitprice, unitsinstock, grid, syncfusion winforms] keywords: [gridboundcolumn1, mappingname, readonly, allowenter, autoresize, backcolor, color selection, currency format, custom appearance, column management] -->
```