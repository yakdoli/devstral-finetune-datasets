```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_975.jpeg
document_name: grid
page_number: 975
page_id: grid#page_975
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:29Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the functionality of sorting in the grid control.
- Highlighting the sorted columns within the grid.
- Visual representation using the SortColumnDescriptor Collection Editor.

## Content

### Figure: Sorted Grid highlights the Sorted Columns

#### First Image: gridGroupingControl1*
This section illustrates a grid displaying suppliers, showcasing highlighted sorted columns.

**Sorting Details**:
- **SupplierID**: 29 items are listed.
- **Company Name**: Highlighted as the sorting column.
- **Contact Name**: Shown in an active state for interaction.
- **Contact Title**: Includes titles such as Sales Manager, Marketing Manager, etc.

The grid includes data like:
- **SupplierID**: 4, 24, 13, etc.
- **Companies and Contacts**: Tokyo Traders, New Orleans Cajun Deli, Nord-Ost-Fisch Handels, etc.
- **Contact Roles**: Marketing Manager, Sales Representative, etc.

### Sorting Properties (Right-side panel)
- **DataMember**: Empty
- **DataSource**: Empty
- **DesignTime**: SortMapping is set to False
- **Grouping Control**: 
  - AllowSetCur: False
  - AutoPopulat: True
  - BackColor: Windo
  - BlinkTime: 0
  - BorderStyle: FixedSingle
  - Font: Verdana, 8

### Second Image: TableDescriptor
This shows the gridGroupingControl1* with detailed table descriptor settings in a popup window named **SortColumnDescriptor Collection Editor**.

**Sorting Columns Editor Details**:
- **Members**: CompanyName is listed as a primary member.
- **Company Name properties**:
  - **Name**: CompanyName
  - **SortDirection**: Ascending

**TableDescriptor Settings**:
- **AllowEdit**: True
- **AllowNew**: True
- **AllowRemove**: True
- **Appearance**: Appearance settings available.
- **ChildGroupOpt**: Grouped Column options are listed.
- **Count**: Counts for Total Columns, Visible Columns, and other settings.

### Interaction Elements:
- **SortColumnDescriptor Collection Editor**: 
  - **Add** and **Remove** buttons for managing sorting columns.
  - **OK** and **Cancel** for applying or dismissing changes.

**Highlighted columns in the grid**:
- The CompanyName and ContactName columns show ascending sorting indicators, emphasizing the sorted state.

## API Reference

### Classes and Properties
- **SortColumnDescriptor**: Used to define sorting criteria for grid columns.
- **TableDescriptor**: Manages properties related to the grid's data and display.

### Parameters
- **DataMember**: Reference to the data source member.
- **DataSource**: Source of data for the grid.
- **SortMapping**: Property to enable/disable sort mapping feature.
- **AllowSetCur**: Allows setting the current selection.
- **AutoPopulat**: Set to True for automatic population.
- **BackColor**: Background color of the control.
- **BlinkTime**: Duration for any blinking effect.
- **BorderStyle**: Style of the grid’s border.
- **Font**: Specifies the font type and size for the grid.

## Code Examples
```csharp
// Example: Configuring sorting
this.gridGroupingControl1.TableDescriptor.SortedColumns.Add("CompanyName");
this.gridGroupingControl1.TableDescriptor.SortedColumns["CompanyName"].SortDirection = SortDirection.Ascending;
this.gridGroupingControl1.Refresh();
```

## Page-level Navigation/TOC
- SortColumnDescriptor Collection Editor
- TableDescriptor Properties
- Sorted Grid Interaction
- Sorting in gridGroupingControl1*

## Cross References
- See also: gridGroupingControl property documentation, TableDescriptor API reference.

<!-- tags: [grid, sorting, columns, gridGroupingControl, TableDescriptor, SortColumnDescriptor, version: 11.4.0.26] keywords: [Company Name, Contact Name, Sort Direction, DataMapper, TableDescriptor, Columns, sorting, grid, UI controls] -->
```