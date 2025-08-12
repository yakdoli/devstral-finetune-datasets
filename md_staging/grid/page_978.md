```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_978.jpeg
document_name: grid
page_number: 978
page_id: grid#page_978
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:56:12Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the process of adding row filters through the `RecordFilters` property.
- Explains the use of `RecordFilterDescriptor` to define conditions for filtering rows.
- Details the settings within the `FilterCondition Collection Editor` for conditional filtering.

## Content

### Adding Row Filters through RecordFilters Property

The following screenshot illustrates the steps to add filters to a `gridGroupingControl1` to display rows based on specific conditions:

#### Step 1: Configuring the Filter Conditions
- **RecordFilterDescriptor Collection Editor** is opened, allowing the user to define conditions for the `ContactTitle` column.
- The properties for the filter condition include:
  - **Name**: `ContactTitle`
  - **Logical Operator**: `Or`
  - **Conditions**:
    - **Count**: `1`

Within the **FilterCondition Collection Editor**:
- The member `Equals Marketing Manager` is defined.
- **Equals Marketing Manager** properties include:
  - **CompareOperat**: `Equals`
  - **CompareText**: `Marketing Manager`

#### Step 2: Applying the Filter
- The filters are set up to show rows where the `ContactTitle` is `Marketing Manager`.
- After applying the filter, the grid displays only rows where the `ContactTitle` matches the specified condition.
  
#### Visual Representation of Filtered Data
- The grid shows filtered rows with the `ContactTitle` set to `Marketing Manager`.
- The corresponding rows are listed below:
  - **SupplierID**: 4, **Company Name**: Tokyo Traders, **ContactName**: Yoshi Nagase
  - **SupplierID**: 7, **Company Name**: Pavlova, Ltd., **ContactName**: Ian Devling
  - **SupplierID**: 10, **Company Name**: Refrescos Americanas LTDA, **ContactName**: Carlos Diaz
  - **SupplierID**: 15, **Company Name**: Norske Meierier, **ContactName**: Beate Vileid
  - **SupplierID**: 25, **Company Name**: Ma Maison, **ContactName**: Jean-Guy Lauzon

#### UI Details
- The table descriptors include settings such as `AllowEdit`, `AllowNew`, and `AllowRemove`, all set to `True`.
- There are options for `Appearance`, `ChildGroupOptions`, `Columns`, `ColumnSets`, and other grid properties.

#### Example Code Context
- The grid control is initialized with settings for `RecordFilters`.
- Filters are applied to ensure only rows meeting the defined conditions are displayed.

### Figure: Adding Row Filters through RecordFilters Property

#### Figure 371: Adding row filters through RecordFilters Property
The first part of the screenshot shows the configuration process for applying filters. The second part demonstrates the grid after the filter is applied, displaying only rows where the `ContactTitle` is "Marketing Manager."

### Additional Notes
- The `gridGroupingControl1` allows sophisticated filtering through property editors.
- The `RecordFilters` property is crucial for defining conditional rows in a grid.
- The screenshots provide a visual guide to configuring and applying conditional filters.

## API Reference

### Namespaces and Classes
- **Syncfusion.Windows.Forms.Grid.Grouping**
  - **RecordFilterDescriptor**
  - **FilterCondition**

#### Properties
- **RecordFilters**: Manages and defines filters for rows in the grid.

#### Methods
- **AddFilterCondition**: Adds a new condition to the filter descriptor.

#### Events
- **FilterChanged**: Triggered when the filter conditions change.

### Code Examples

#### Example: Setting up RecordFilters in C#
```csharp
RecordFilterDescriptor descriptor = new RecordFilterDescriptor();
descriptor.Name = "ContactTitle";
descriptor.LogicalOperator = FilterLogicalOperator.Or;

FilterCondition condition = new FilterCondition();
condition.Operator = FilterOperator.Eq;
condition.Value = "Marketing Manager";

descriptor.Conditions.Add(condition);

gridGroupingControl1.RecordFilters = new RecordFilterDescriptorCollection(new RecordFilterDescriptor[] { descriptor });
```

## Cross References
- See also: gridGroupingControl documentation for advanced filtering and conditional formatting.
- Additional resources available for complete reference on Syncfusion.Windows.Forms.Grid controls and their associated classes.

<!-- tags: [gridGroupingControl, recordFilter, filterCriteria, filters] keywords: [row filtering, conditional filtering, Syncfusion Grid] -->
```