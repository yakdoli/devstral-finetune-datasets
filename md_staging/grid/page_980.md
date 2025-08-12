```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_980.jpeg
document_name: grid
page_number: 980
page_id: grid#page_980
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:49Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Enables the customization of grid column properties to control data interaction and display.
- Demonstrates setting the `AllowFilter` property for a specific column to enable filtering options.
- Highlights the `Company Name` column, showing how to configure filtering capabilities and view available filtering options.

## Content

### Setting AllowFilter property for 'Company Name' Column
The figure below illustrates configuring the `AllowFilter` property for the 'Company Name' column. This allows users to filter data based on specific values within this column.

**Figure 374: Setting AllowFilter property for 'CompanyName' Column**
\[Image description: The GridColumnDescriptor Collection Editor for the `gridGroupingControl1` is open. The `Company Name` column properties are being modified, with the `AllowFilter` property set to `True`. The grid view displays a collection of `GridColumnDescriptor` columns with mapping information to the underlying data source.\]

#### Key Points:
- The grid control is managing columns through the `GridColumnDescriptor` interface.
- The `Company Name` column is selected, and the properties window shows various settings including `MappingName`, `HeaderText`, and `AllowFilter`.
- Setting the `AllowFilter` property to `True` enables filtering functionality for this specific column.

### FilterBar drop down showing filtering options for the column 'Company Name'
Following the configuration of the `AllowFilter` property, the figure below displays the filtered options available for the `Company Name` column.

**Figure 375: FilterBar drop down showing filtering options for the column 'Company Name'**
\[Image description: The drop-down menu for the `Company Name` column in the grid control displays filtering options such as `(All)`, `(Custom...)`, `(Empty)`, and a list of unique company names (e.g., Charlotte Cooper, Shelley Burke, Regina Murphy, etc.). The grid control continues to reference the `gridGroupingControl1`, showing the filtering capability in action.\]

#### Key Points:
- The FilterBar drop-down provides users with a list of options to filter data by specific company names.
- Users can select from predefined company names or use custom filter options.
- This feature improves data navigation and retrieval efficiency in the grid.

### Expression Fields
The section introduces "Expression Fields," which likely discusses how to define customized fields or calculations within the grid, possibly to display derived values or to enhance filtering capabilities.

---

## API Reference
- **Namespace:** Syncfusion.Windows.Forms
- **Class:** GridGroupingControl
- **Properties:**
  - `AllowFilter`: Allows configuring filtering capabilities for specific columns.
  - `CompanyName`: Column name used as an example to demonstrate filtering functionality.

## Code Examples
- While specific code is not provided in the image, configuring the `AllowFilter` property would typically involve setting properties in C# as follows:
  ```csharp
  gridGroupingControl1.GridColumnDescriptors["CompanyName"].AllowFilter = true;
  ```

## Page-level Navigation/TOC (if applicable)
- No additional navigation or table of contents relevant to this page scope is present.

## Cross References
- See also: Other grid-related features such as grouping, column sorting, and conditional formatting for comprehensive data manipulation options.

<!-- tags: [grid, filter, column properties, winforms, syncfusion, gridGroupingControl] keywords: [gridGroupingControl1, AllowFilter, CompanyName, Filtering, Expression Fields] -->
```