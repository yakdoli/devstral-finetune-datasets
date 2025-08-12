```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: grid
page_number: 094
page_id: grid#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:22:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to add a `GridBoundColumn` to hold the `ProductName` column.
- Explains setting the back color for a column using the `StyleInfo` property.

## Content

### Adding a GridBoundColumn to hold the ProductName Column

#### Figure: GridBoundColumn Collection Editor
![](image.png)

* **Description:** The screenshot shows the GridBoundColumn Collection Editor in use. It illustrates the process of adding and configuring a `GridBoundColumn` to display the `ProductName` column. The dialog box includes options for members, properties, and mapping names, with `ProductName` selected as the `MappingName`.

#### Step-by-Step Guide
1. Open the GridBoundColumn Collection Editor.
2. Navigate to the `MappingName` property and select `ProductName`.
3. Select the `StyleInfo` property and set the back color for the column.

### Setting the Back Color for a Column

#### Instructions:
- **Step 3:** Select the `StyleInfo` property and set the back color for the column as shown in the following screenshot.

---

## API Reference

### `GridBoundColumn` Properties
#### 1. `MappingName`
- **Description:** Determines the data source property to which the column is bound.
- **Type:** String
- **Example:** `gridBoundColumn1.MappingName = "ProductName";`

#### 2. `StyleInfo`
- **Description:** Allows customization of the column's appearance, including back color, font, etc.
- **Type:** GridStyleInfo
- **Example:** 
  ```csharp
  gridBoundColumn1.StyleInfo.BackColor = System.Drawing.Color.LightBlue;
  ```

## Code Examples

#### Example: Setting the Back Color of a Column
```csharp
// Assuming gridBoundColumn1 is already added to the grid.
gridBoundColumn1.MappingName = "ProductName";
gridBoundColumn1.StyleInfo.BackColor = System.Drawing.Color.LightBlue;
```

---

## Page-level Navigation/TOC
- [Adding a GridBoundColumn to hold the ProductName Column](#add-gridboundcolumn)
- [Setting the Back Color for a Column](#set-back-color)

<!-- tags: [Essential Grid, Windows Forms, GridBoundColumn, ProductName, StyleInfo, MappingName] keywords: [GridBoundColumn, ProductName, StyleInfo, MappingName, back color, columns, grid, Windows Forms, essential grid] -->
```