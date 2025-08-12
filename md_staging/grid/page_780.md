```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_780.jpeg
document_name: grid
page_number: 780
page_id: grid#page_780
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:06Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
This page discusses the usage of the Grid Grouping Control in Windows Forms. It focuses on setting properties, specifically enabling the `AllowFilter` property using the `GridColumnDescriptor Collection Editor`. The figure illustrates configuring filter options for columns such as `CompanyName`.

## Content

### Setting AllowFilter property for the column CompanyName

Figure 312 shows how the `AllowFilter` property can be enabled for the `CompanyName` column using the `GridColumnDescriptor Collection Editor`.

#### Figure 312: AllowFilter property enabled by using the GridColumnDescriptor Collection Editor
- The figure displays both the `Properties` window and the `GridColumnDescriptor Collection Editor`.
- The `Properties` window shows the `gridGroupingControl1` with properties such as `AllowEdit`, `AllowNew`, and `AllowRemove` set to `True`.
- The `GridColumnDescriptor Collection Editor` allows users to configure specific column properties, such as:
  - **Layout**:
    - `Width` is set to `100`.
  - **Misc**:
    - `MappingName` is set to `CompanyName`.
    - `HeaderText` is displayed as `CompanyName`.
    - `ReadOnly` is set to `False`.
    - `TrackWidthOfParentColumn` is set to `True`.
    - `AllowDropDownCell` is set to `True`.
    - `AllowFilter` is explicitly set to `True`.
    - `AllowGroupByColumn` is set to `True`.
    - `AllowBlink` is set to `False`.
    - GroupBy options are configured.

#### Explanation of functionality:
- A sample screenshot shows the filter bar with filters enabled for the columns `CompanyName` and `ContactTitle`. The records are filtered based on the condition `ContactTitle = 'Sales Representative'`.
- The image also illustrates the filter options for the `CompanyName` column.

### API Reference

#### Grid Grouping Control Properties
- **AllowFilter**: A property that allows users to enable or disable filtering for specific columns in the grid.

### Code Examples

#### Example: Setting AllowFilter property programmatically
```csharp
// Enabling AllowFilter for the CompanyName column
gridGroupingControl1.Columns["CompanyName"].AllowFilter = true;
```

### Page-level Navigation/TOC (if applicable)
- Setting `AllowFilter` property for the column `CompanyName`
- API Reference for Grid Grouping Control Properties

### Cross References
See also:
- [`gridGroupingControl`](#gridGroupingControl) documentation
- [`GridColumnDescriptor`](#GridColumnDescriptor) properties

<!-- tags: [product, module, control, api, version?] keywords: [Grid Grouping Control, Windows Forms, AllowFilter, GridColumnDescriptor, filter options, CompanyName] -->
```