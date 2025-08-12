```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_739.jpeg
document_name: grid
page_number: 739
page_id: grid#page_739
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:09Z
fidelity: lossless
-->

```html
Essential Grid for Windows Forms
```

## Overview
- Demonstrates multi-column sorting in the Essential Grid for Windows Forms.
- Explains how to sort grid data using display members of foreign-key combo boxes.
- Includes a code example for implementing foreign key relations.

## Content

### Multi Column Sorting

![Figure 295: Multi Column Sorting](# "Figure 295: Multi Column Sorting")

**Note:** For more details, refer the following browser sample:

```text
<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Grouping.Windows\Samples\2.0\Sort\Multi Column Sort Demo
```

#### Sorting By Display Member

Grid Grouping control sorts the grid based on the Value member of the grid data, by default. The user can also sort the grid data by Display members of the foreign-key combo boxes by setting up a foreign-key reference relation between the related tables.

**Note:** A foreign-key reference relation allows the user to look up values in a related table using an id column in the main table.

The following code example illustrates the usage of foreign key relation:

1. Save the location of the `mainTable.Customer` column, so that it can be swapped after the foreign table reference has been set.

```csharp
[C#]

GridTableDescriptor td = this.gridGroupingControl1.TableDescriptor;
td.VisibleColumns.LoadDefault();
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Grid.Grouping

#### Class: GridTableDescriptor
##### Properties
- **TableDescriptor**
  - Represents the table descriptor of the grid.

##### Methods
- **LoadDefault()**
  - Loads the default visible columns for the grid.

## Code Examples

### C#

```csharp
GridTableDescriptor td = this.gridGroupingControl1.TableDescriptor;
td.VisibleColumns.LoadDefault();
```

## Page-level Navigation/TOC (if applicable)
- Multi Column Sorting
- Sorting By Display Member

## Cross References
See also:
- `<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Grouping.Windows\Samples\2.0\Sort\Multi Column Sort Demo`

<!-- tags: [syncfusion, windows forms, essential grid, multi-column sorting, foreign key, display member, grid grouping, api reference] keywords: [multi column sorting, foreign key, display member, grid grouping, load default columns, code example] -->
```