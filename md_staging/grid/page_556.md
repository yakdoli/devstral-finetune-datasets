```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_556.jpeg
document_name: grid
page_number: 556
page_id: grid#page_556
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Explains filtering data records using the GridFilterBar feature.
- Demonstrates filtering by both value and display members in a grid.
- Provides an example of enabling the Filter By DisplayMember feature.

## Content

### Filter By DisplayMember

#### Overview

Grid Data Bound Grid filters the data records by the value member of the columns. The default behavior can be customized to accomplish filtering by display member instead. This can be achieved by deriving a custom filter from the `GridFilterBar` class and customizing the `GetFilterFromRow` method to replace the display strings in the filter with the value strings.

#### Feature Description

The Filter By DisplayMember feature allows customization to filter grid data by the display member instead of the value member. This feature is particularly useful when the display member is more relevant for filtering purposes.

#### Example Code

The following code example illustrates how to enable the Filter By DisplayMember feature.

```csharp
GridDataBoundGridFilterBarExt filterBar = new GridDataBoundGridFilterBarExt();
filterBar.WireGrid(gridDataBoundGrid1);
```

### Figure 218: Demonstration of Filtering by DisplayMember

**Figure 218:** *Top Grid is Before Grid Filter Bar; Middle Shows Selecting to Filter on City = Boston; Bottom Grid is Filtered Grid*

This figure illustrates the process of filtering the grid by selecting a specific city ("Boston") from the City column. The grid is initially displayed without any filters applied (top grid). The middle grid shows the selection of "Boston" from the dropdown menu in the City column, and the bottom grid displays only the rows where the City is "Boston."

## API Reference

### Overview

The `GridDataBoundGridFilterBarExt` class is an extension of the `GridFilterBar` class, allowing customization of filtering functionality. The key method to customize is `GetFilterFromRow`.

#### Class: GridDataBoundGridFilterBarExt

- **Purpose:** Customizes the GridFilterBar to filter by display member instead of value member.
- **Example Usage:** See the code example above.

#### Method: GetFilterFromRow

- **Purpose:** Replaces the display strings in the filter with the value strings.
- **Customization:** Requires overriding to implement the desired filtering logic.

## Code Examples

### Enabling Filter By DisplayMember

The example below demonstrates how to use the `GridDataBoundGridFilterBarExt` class to enable filtering by display member.

```csharp
GridDataBoundGridFilterBarExt filterBar = new GridDataBoundGridFilterBarExt();
filterBar.WireGrid(gridDataBoundGrid1);
```

This code creates a custom filter bar and attaches it to the grid, allowing filtering by display member.

## Cross References

- Refer to the documentation on `GridFilterBar` for more information on default filtering behavior.
- See the `GridDataBoundGrid` documentation for grid-specific properties and methods.

<!-- tags: GridFilterBar, Filter By DisplayMember, GridDataBoundGridFilterBarExt, GridDataBoundGrid keywords: filtering, display member, value member, customization, Filter By DisplayMember feature, GridFilterBar class, GridDataBoundGridFilterBarExt, GetFilterFromRow -->
```