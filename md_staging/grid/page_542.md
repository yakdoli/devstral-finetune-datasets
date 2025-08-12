```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_542.jpeg
document_name: grid
page_number: 542
page_id: grid#page_542
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes how to customize columns in the Grid Data Bound Grid.
- Provides instructions on using the GridBoundColumns collection to determine which data source columns are displayed.
- Offers guidance on setting column properties like backcolor and font.

## Content

### Customizing Columns in the Grid
**Figure 213: Table and Data Selected**

![Figure showing Table and Data Selected](https://i.imgur.com/decisionToUseItsUsableExt.png)

- To customize columns, open the **GridBoundColumns** collection by clicking that property in the Grid Data Bound Grid.
- With this editor, you can determine exactly which columns of the data source are displayed in the grid.
- You can also set the column properties like **backcolor** and **font**.

## API Reference
### GridBoundColumns Property
- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Type:** Collection of GridBoundColumn objects.
- **Description:** Allows control over the columns displayed in the grid and their properties.

## Code Examples
### Setting Column Properties
```csharp
// Example of setting backcolor and font for a column
GridBoundColumn col = gridModel.GridColumn["CustomerID"];

col.Backcolor = System.Drawing.Color.LightGray;
col.Font = new System.Drawing.Font("Arial", 10, System.Drawing.FontStyle.Bold);
```

## Cross References
- Refer to the Grid Data Bound Grid documentation for more information on column customization and properties.

<!-- tags: [product, syncfusion, essential-grid, gridboundcolumns, windowsforms, columns, customization, version11.4.0.26] keywords: [griddata, datacolumns, columnproperties, backcolor, font, table, dataselected] -->
```