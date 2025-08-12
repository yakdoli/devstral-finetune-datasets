```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_772.jpeg
document_name: grid
page_number: 772
page_id: grid#page_772
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of the `RecordFilterDescriptor Collection Editor` to configure filters for grid data.
- Explains the properties involved in setting up a row filter.

## Content

### Figure 309: RecordFilterDescriptor Collection Editor

The screenshot shows the RecordFilterDescriptor Collection Editor interface, used for configuring filters applied to grid rows. This tool allows users to define complex filtering conditions based on specific field properties.

#### Description of Important Properties Used to Set a Row Filter

| Property       | Description                                                              |
|----------------|--------------------------------------------------------------------------|
| Name           | Specifies the name of the field with which the filter operates.         |

### API Reference

#### Syncfusion Windows Forms Grid Grouping

The gridGroupingControl1, of type `Syncfusion.Windows.Forms.Grid.Grouping.G`, demonstrates the configuration of record filters and primary key columns.

#### WinForms Design-Time Configuration

The **Properties** panel shows various fields such as **Primary Key Columns** and **Record Filters**, with `Count = 1` indicating the number of configured filters.

#### Data Editor Components

1. **RecordFilterDescriptor Collection Editor**
   - **Members**: The `wins` field is highlighted, indicating it is the primary property being filtered.
   - **Conditions Filter**: Defines the logical operator `Or` and the property `wins` for filtering.
   - **Conditions Count**: Displays the total number of filtering conditions applied.

2. **FilterCondition Collection Editor**
   - **Greater Than 20 Properties**:
     - **Name**: `Greaterthan20`
     - **CompareOperator**: Set to `GreaterThan`
     - **CompareText**: Value `20` is used as the threshold for the filter condition.
   - This editor allows users to define complex filter expressions, such as filtering rows where the value of a field exceeds a specified number.

### Code Examples

#### Example C# Code for Configuring Filters

```csharp
using Syncfusion.Windows.Forms.Grid.Grouping;

// Create a new GridGroupingControl instance
GridGroupingControl gridGrouping = new GridGroupingControl();

// Define a filter condition
RecordFilter rd = new RecordFilter();

// Add conditions to the filter
rd.Conditions.Add(new ConditionDescriptor { PropertyName = "wins", CompareOperator = CompareOperator.GreaterThan, CompareText = "20" });

// Apply the filter to the grid
gridGrouping.RecordFilters.Add(rd);
```

## References

- See also: Essential Grid documentation for detailed information on configuring filters and advanced Grid functionalities.

<!-- tags: [product, syncfusion, winforms, grid, filter, configuration, data, demonstration, recordfilterdescriptor, gridgroupingcontrol] keywords: [syncfusion winforms, grid grouping, record filters, conditions filter, configuring filters, filter descriptor, filter condition] -->
```