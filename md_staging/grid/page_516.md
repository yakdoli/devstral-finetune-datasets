```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_516.jpeg
document_name: grid
page_number: 516
page_id: grid#page_516
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:20Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Example

Let us consider the Grid Folder Browser sample which is available under the following installation path.

**Install Location:** Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Product Showcase\Grid Folder Browser Demo

This sample operates the grid in virtual mode in order to populate the data dynamically on demand, i.e., when the tree is expanded. The `QueryCellInfo`, `QueryColCount`, and `QueryRowCount` events must be handled in order to implement a virtual grid. These events provide basic information about the number of rows and columns and the values of the data.

The following code examples illustrate how to set the data from the data source.

### Using C#

```csharp
[C#]
void GridQueryCellInfo(object sender, GridQueryCellInfoEventArgs e)
{
    if (e.RowIndex > 0 && e.ColIndex > 0)
    {
        e.Style.CellValue = externalData[e.RowIndex - 1].Items[e.ColIndex - 1];
        if (e.ColIndex == 1)
        {
            e.Style.CellType = "TreeCell";
            e.Style.Tag = externalData[e.RowIndex - 1].IndentLevel;
            e.Style.ImageIndex = (int) externalData[e.RowIndex - 1].ExpandState;
        }
    }
    e.Handled = true;
}
```

### Using VB.NET

```vb.net
[VB.NET]
Private Sub GridQueryCellInfo(ByVal sender As Object, ByVal e As
```

## API Reference (if applicable)
No specific API reference is provided in this example, as it focuses on demonstrating the use of `GridQueryCellInfo` event handling for virtual grid data population.

### Code Examples (multi-language supported)
This page includes examples of handling `GridQueryCellInfo` for setting cell data in virtual mode using both C# and VB.NET. These examples demonstrate how to dynamically populate data for virtual grids by handling events that query cell information.

### Cross References
- This example is related to the Grid Folder Browser demo, showcasing virtual grid operations.

### RAG Annotations
<!-- tags: [Grid, VirtualGrid, QueryCellInfo, C#, VB.NET, DynamicData] keywords: [dynamic data, virtual grid, GridQueryCellInfo, Grid Folder Browser sample, event handling, data population] -->
```