```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_414.jpeg
document_name: grid
page_number: 414
page_id: grid#page_414
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the separation between the datasource and grid in a virtual grid.
- Explains how virtual grids display large amounts of data quickly without pre-populating cells.
- Highlights the events that need to be handled to implement a virtual grid.

## Content

### Overview of Virtual Grid
Essential Grid supports complete separation between the **datasource** and the grid. In a virtual grid, no cell data is stored in the **GridStyleInfo** objects or any other internal grid storage. All information is provided on demand through handled events. For example, whenever Essential Grid needs a row count for a grid, it fires a **QueryRowCount** event. In your handler, you must provide the row count from your datasource. Virtual grids can display large amounts of data extremely fast. There is no need to perform the time-consuming task of populating the grid.

### Implementing a Read-Only Virtual Grid
To implement a Read-only virtual grid, you'll need to handle three events. To remove the Read-only limitation, you will have to handle a fourth event. In addition to these four events, there are other events that you may want to handle depending upon the behavior you are trying to implement. We will first discuss the required events and then discuss the optional events that you can handle to affect virtual grid behavior. You can also work through the virtual grid tutorial to see an implementation of a simple virtual grid.

#### The Events
The events are discussed under the below sections:

#### Required Events
These are the three events that you should handle in order to implement a virtual grid. They provide the basic information about the number of rows, columns and the values for your data.

##### QueryRowCount Event
This event is used to return the row count on demand. Here is a sample handler.

```csharp
private void GridQueryRowCount(object sender, GridRowColCountEventArgs e)
{
    // Determine number of rows.
    e.Count = this.numArrayRows;
    e.Handled = true;
}
```

```vb
Private Sub GridQueryRowCount(ByVal sender As Object, ByVal e As GridRowColCountEventArgs)
End Sub
```

## API Reference

### Events
- **QueryRowCount**: Triggered to retrieve the row count on demand.

## Code Examples

### C#
```csharp
private void GridQueryRowCount(object sender, GridRowColCountEventArgs e)
{
    // Determine number of rows.
    e.Count = this.numArrayRows;
    e.Handled = true;
}
```

### VB.NET
```vb
Private Sub GridQueryRowCount(ByVal sender As Object, ByVal e As GridRowColCountEventArgs)
End Sub
```

<!-- tags: [syncfusion, winforms, virtual grid, event handling, queryrowcount] keywords: [datasource, virtual grid, gridstyleinfo, read-only limitation, queryrowcount event, tutorial] -->
```