```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_784.jpeg
document_name: grid
page_number: 784
page_id: grid#page_784
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:22Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of dynamic filters in the Essential Grid for Windows Forms.
- Highlights how to wire and unwire the grid to enable or disable dynamic filtering.
- Includes both C# and VB.NET code examples to show implementation details.

## Content

### Dynamic Filter Example

#### C# Example
```csharp
else
    f.UnWireGrid(gridGroupingControl);
```

#### VB.NET Example
```vb
Dim f As GridDynamicFilter = New GridDynamicFilter()
If showDynamicFilter Then
    f.WireGrid(gridGroupingControl)
Else
    f.UnWireGrid(gridGroupingControl)
End If
```

### Sample Output

#### Description
The following image illustrates a sample output of the dynamic filter functionality.

#### Image Caption
Figure 315: Dynamic Filter

![Dynamic Filter](https://imgur.com/ebf3eظروف)

#### Note
For more details, refer to the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Filters and Expressions\Dynamic Filter Demo
```

## API Reference

### Methods Used
- `GridDynamicFilter.WireGrid(Control control)`
  - **Purpose**: Connects the grid to the dynamic filter.
  - **Parameters**:
    - `control`: The grid to be wired.
  - **Returns**: None.
  - **Description**: Enables dynamic filtering on the specified grid.

- `GridDynamicFilter.UnWireGrid(Control control)`
  - **Purpose**: Disconnects the grid from the dynamic filter.
  - **Parameters**:
    - `control`: The grid to be unwired.
  - **Returns**: None.
  - **Description**: Disables dynamic filtering on the specified grid.

## Code Examples

#### Dynamic Filter Implementation
```csharp
// C# Example
GridDynamicFilter f = new GridDynamicFilter();
if (showDynamicFilter)
    f.WireGrid(gridGroupingControl);
else
    f.UnWireGrid(gridGroupingControl);
```

```vb
' VB.NET Example
Dim f As GridDynamicFilter = New GridDynamicFilter()
If showDynamicFilter Then
    f.WireGrid(gridGroupingControl)
Else
    f.UnWireGrid(gridGroupingControl)
End If
```

## RAG Annotations
<!-- tags: [grid, windows forms, dynamic filter, essential grid, control, api, version 11.4.0.26] keywords: [dynamic filter, gridGroupingControl, GridDynamicFilter, WireGrid, UnWireGrid, showDynamicFilter] -->
```