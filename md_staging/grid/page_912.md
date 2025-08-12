```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_912.jpeg
document_name: grid
page_number: 912
page_id: grid#page_912
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:06Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the functionality of the FieldDialogBox to select columns to display in a grid.
- Explains how to customize the grid by choosing specific columns via the Field Chooser dialog.

## Content

### FieldDialogBox

#### Figure: FieldDialogBox
![Field Dialog Box](https://example.com/image_url)

The FieldDialogBox allows you to select the columns you want to be displayed in the grid.

1. **Select the checkboxes of the columns you want to be displayed in the grid.**
2. **The grid will have only the columns which are selected in the Field Chooser dialog.**

#### Figure 329: FieldDialogBox
The screenshot shows a dialog box with several checkboxes, each representing a column. The columns listed include:
- OrderID
- CustomerID
- EmployeeID
- OrderDate
- RequiredDate
- ShippedDate
- ShipVia
- Freight
- ShipName
- ShipAddress
- ShipCity
- ShipRegion
- ShipPostalCode
- ShipCountry

### Customized Grid

#### Figure: Customized Grid
![Customized Grid](https://example.com/image_url)

This section demonstrates the result of using the Field Chooser dialog to customize the grid.

#### Figure 330: Customized Grid
The grid displays a subset of the columns selected in the Field Chooser dialog. The grid is structured as follows:

- **Headers**:
  - Header One: Columns include OrderID, CustomerID, EmployeeID.
  - Header Four: Columns include ShipRegion.

- **Data**:
  - OrderID, CustomerID, EmployeeID, ShipAddress, ShipRegion.

The FieldTreeDialogBox also provides the ability to group headers and select columns within those groups. The structure within the FieldTreeDialogBox includes:
- Header One: Checked for OrderID, CustomerID, EmployeeID.
- Header Four: Checked for ShipRegion and ShipAddress.

### Example of the Customized Grid

The screenshot shows the grid displaying only the specified columns, affirming the functionality of the Field Chooser dialog in filtering the data representation.

## Cross References
- Refer to the [FieldDialogBox documentation](link) for more information on column selection functionality.
- See also: [WinForms Grid Customization](link) for additional grid customization options.

<!-- tags: [WinForms, Grid, FieldDialogBox, ColumnSelection] keywords: [Essential Grid, Windows Forms, Field Chooser, Column Filtering, Customized Grid, Column Selection] -->
```