```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_879.jpeg
document_name: grid
page_number: 879
page_id: grid#page_879
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:44Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Once a display element is retrieved, the style information of the corresponding cell can be obtained using the `Table.GetTableCellStyleInfo` method.
- The `PointToNestedDisplayElement` method returns the nested display element at a given mouse position.
- An example demonstrates how to use these methods to retrieve and display cell style information.

## Content

### Retriving Cell Style Information
Once the display element is retrieved, the style information of the corresponding cell can be obtained by using the `Table.GetTableCellStyleInfo` method, which returns a cell style information given its row and column indices.

#### PointToNestedDisplayElement Method
This method returns the nested display element that is displayed at the given mouse position. The details are as follows:

| **Method Name**              | **Parameter**                                                                 | **Return Value**                                                                                           |
|------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| PointToNestedDisplayElement  | ptClient: A type of System.Drawing Point object that represents the mouse position in client coordinates. | An Element object that represents the underlying display element. |

### Example

Below is an example that demonstrates how to use `PointToTableCellStyle` to retrieve the cell style information. This example handles a `MouseMove` event of the Grid Table Control, retrieves the cell content using the above method, and writes the content to a listbox control.

1. **Setup a Grouping Grid and bind it to a dataset.**
   Handle `TableControl.MouseMove` event to let the user get the cell style information printed while hovering the mouse over the grid cells. Once you have the style, you can check `Style.TableCellIdentity` for information about the cell such as its column, underlying record, parent table, and so on.

#### Code Example

```csharp
private void TableControl_MouseMove(object sender, MouseEventArgs e)
{
    Point ptClient = new Point(e.X, e.Y);
    GridTableControl tableControl = this.groupingGrid1.TableControl;

    GridTableCellStyleInfo style = tableControl.PointToTableCellStyle(ptClient);
    Element displayElement = style.TableCellIdentity.DisplayElement;
    string info = "";

    if (style != null)
    {
        if (style.TableCellIdentity.Column != null)
            info = "Field Name - " + style.TableCellIdentity.Column.Name
                + ", Field Value - \"" + style.CellValue.ToString() + "\", Field Type -";
    }
}
```

## Page-level Navigation/TOC (if applicable)
- Getting Cell Style Information
- PointToNestedDisplayElement Method
- Example

## RAG Annotations
The section discusses methods to retrieve and handle cell style information in a Grid Table Control, using specific methods like `PointToTableCellStyle`. Code examples illustrate handling mouse events to display cell content and style details.

<!-- tags: [Syncfusion Grid, Windows Forms, cell style information, Table.GetTableCellStyleInfo, PointToNestedDisplayElement, GroupingGrid, MouseMove event] keywords: [cell, display element, client coordinates, Element object, mouse position, GridTableControl, TableCellStyleInfo, GroupingGrid, mouse event, TableControl_MouseMove] -->
```