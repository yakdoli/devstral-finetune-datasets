```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_781.jpeg
document_name: grid
page_number: 781
page_id: grid#page_781
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:29Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the functionality of FilterBars added to specific columns in the Customers table.
- Explains how to enable and customize filter conditions using the RecordFilterDescriptor collection editor.

## Content

### Customizing FilterBars

Figure 313 demonstrates the addition of FilterBars for the "CompanyName" and "ContactTitle" columns in a grid displaying customer data. The grid shows columns for CustomerID, CompanyName, ContactName, and ContactTitle, with 17 items listed. The "CompanyName" column includes a dropdown list with options such as "(All)", "(Custom...)", and various company names, indicating the filtering functionality. Similarly, the "ContactTitle" column has a consistent entry of "Sales Representative".

#### Enabling the FilterBar

When enabling the FilterBar, it adds options to show either **All** records or a **Custom** selection. Selecting the "Custom" option opens the RecordFilterDescriptor collection editor. This editor allows users to modify filter conditions or add additional filters as needed.

#### Custom Filter Conditions

By clicking the "Custom" option in the FilterBar dropdown, users access the RecordFilterDescriptor collection editor. Here, they can define specific criteria for filtering records based on their requirements. This feature enhances the flexibility and precision of filtering data within the grid.

```markdown
Figure 313: FilterBars added for "CompanyName" and "ContactTitle" Columns
```

### Example of Custom Filter Usage

The following example illustrates how the custom filter option can be utilized:

1. **Select Custom Option**: Click on the drop-down arrow in the FilterBar for the desired column (e.g., "CompanyName").
2. **Access Editor**: Choose the "Custom" option to open the RecordFilterDescriptor collection editor.
3. **Edit Conditions**: Define the specific conditions for filtering. For instance, selecting companies whose names contain "Delikatessen".
4. **Apply Filters**: Once conditions are set, apply the filters to see the filtered results in the grid.

## API Reference

### Classes and Methods

- **RecordFilterDescriptor**
  - **Properties**
    - **FilterConditions**: Allows defining the criteria for filtering records.
    - **CustomFilter**: Enables custom filtering based on specific conditions.

## Code Examples

### Example of Enabling Custom Filtering in Code

```csharp
using Syncfusion.Windows.Forms.Grid;

// Enable filter bar for a specific column
gridModel.allowFilterBar = true;

// Access the RecordFilterDescriptor collection editor
gridModel.filterBar.EditFilterDescriptor("CompanyName");

// Define custom filter conditions
gridModel.filterBar.SetFilterCondition("CompanyName", "Contains", "Delikatessen");
```

## Page-Level Navigation/TOC

- Overview
- Customizing FilterBars
- Example of Custom Filter Usage

## Cross References

- See also: Grid Control Documentation for detailed implementation of FilterBars and RecordFilterDescriptor editor in WinForms.
```

<!-- tags: [Syncfusion, WinForms, Grid, FilterBars, RecordFilterDescriptor] keywords: [Custom Filter, Filter Conditions, Grid Control, Custom Filtering, FilterBar, RecordFilterDescriptor Editor, Example Code] -->
```