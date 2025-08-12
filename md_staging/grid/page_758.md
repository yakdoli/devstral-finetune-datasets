```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_758.jpeg
document_name: grid
page_number: 758
page_id: grid#page_758
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:26Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Explains how to use the grouping grid feature with caption summaries.
- Illustrates the behavior of the grouping grid when caption summaries are disabled.
- Describes how to sort groups by the values of the summary.

## Content

### Grouping Grid With Caption Summaries
Here is another screenshot that shows the grouping grid with Caption Summaries disabled.

![Figure 303: Grouping Grid With Caption Summaries](#)
- **Group Caption Cells**: Highlighted areas showing the group caption cells.
- **Group Summary**: Displays the summary for each group.
- **Table Summary**: Summary displayed for the entire table.

### Grouping Grid Without Caption Summaries
![Figure 304: Grouping Grid Without Caption Summaries](#)

#### Note: For more details, refer the following browser sample:
```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Calculate Summary\Summary In Caption Demo
```

### Sort By Summary In Caption
This section illustrates how to sort the groups by the values of the summary.

#### 4.3.4.3.3.3 Sort By Summary In Caption
- By default, when grouping is applied, it sorts the records by the values of the grouped column.
- To change the default group order to sort the records by the values of group summaries:
  - Use a custom comparer to define the sort order.
  - Utilize the built-in method `SetGroupSummaryOrder`, specifically designed for this scenario.

## API Reference

### Methods
#### `SetGroupSummaryOrder`
- **Namespace**: Syncfusion.Windows.Forms.Grid.Grouping
- **Description**: Sorts the groups by the values of the summary.
- **Parameters**:
  - Customizable based on the user-defined comparer or built-in functionality.
- **Returns**: Type: void
- **Exceptions**: Not explicitly listed.

## Code Examples

### Example: Sorting Groups by Summary Value

```csharp
// Example code for sorting groups by summary value using SetGroupSummaryOrder
using Syncfusion.Windows.Forms.Grid.Grouping;

// Assuming grid is the instance of GroupingGrid
grid.SetGroupSummaryOrder(Order.Ascending, SummaryColumn);
```

## Cross References
- Refer to the sample location provided for detailed implementation.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Grouping Grid, Caption Summaries] keywords: [GroupingGrid, Summary In Caption, SetGroupSummaryOrder, sort, custom comparer, built-in method] -->
```