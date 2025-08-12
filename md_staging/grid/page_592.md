```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_592.jpeg
document_name: grid
page_number: 592
page_id: grid#page_592
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:26:55Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Overview of the Field Chooser dialog and its functionality in the Essential Grid for Windows Forms.

## Content

### Field Chooser Dialog

The Field Chooser dialog allows users to select which columns are displayed in the grid.

#### Figure 237: Field Chooser
- **Description:** The dialog lists all the column names with check boxes adjacent to them.
- **Example:** The grid displays various product-related fields such as ProductID, ProductName, SupplierID, CategoryID, etc.

#### Figure 238: FieldDialogBox
- **Description:** The FieldDialogBox lists column names with checkboxes to select which columns to display.
- **Example:** Columns like ProductID, ProductName, SupplierID, QuantityPerUnit, UnitPrice, etc., are shown with checkboxes.

#### Steps to Use the Field Chooser

1. **List of Column Names:** The dialog will list all the column names with check boxes adjacent to them.
   - **Example:** Column names include ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, etc.
2. **Selecting Columns:**
   - Select the checkboxes of the columns you want to be displayed in the grid.
3. **Result:** The grid will have only the columns which are selected in the Field Chooser dialog.

### Using the Field Chooser

#### Selecting Columns
- **Step 1:** Open the Field Chooser dialog.
- **Step 2:** Tick the checkboxes of the desired columns.
- **Step 3:** Click OK to apply the selection.

#### Grid Display
- The grid will update to show only the columns that have been selected in the Field Chooser dialog.

## API Reference

### Methods and Properties
- **Methods:**
  - `FieldChooser.ShowDialog()`: Displays the Field Chooser dialog.
- **Properties:**
  - `SelectedColumns`: A list of column names that are selected to be displayed.

## Code Examples

### C#

```csharp
// Example: Displaying the Field Chooser dialog
grid.FieldChooser.ShowDialog();
```

## Page-level Navigation/TOC
- **Steps to Use the Field Chooser**
- **Selecting Columns**
- **Grid Display**

## Cross References
- Refer to the Essential Grid section for more features and functionalities.

<!-- tags: [Syncfusion, Winforms, .NET, grid, fieldchooser] keywords: [fieldchooser dialog, columns, grid, windows forms, selection, checkboxes, display ] -->
```