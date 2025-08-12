```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_417.jpeg
document_name: grid
page_number: 417
page_id: grid#page_417
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- This subsection explains the use of optional events to extend the read-only virtual grid functionality.
- Focuses on the `SaveCellInfo` and `QueryRowHeight` events for handling data storage and dynamic row height specification.

## Content

### 4.1.4.11.2 Optional Events

Optional events can be used to extend the functionality of the basic Read-only virtual grid that you get by handling these three required events. One event lets you save information back into your external **datasource** while other events let you dynamically specify row heights and column widths. You can also dynamically provide covered cell ranges.

#### 4.1.4.11.2.1 SaveCellInfo Event

This event is used to store data back into your data source when it has been changed by the user. Here is a sample handler.

```csharp
[C#]
void GridSaveCellInfo(object sender, GridSaveCellInfoEventArgs e)
{
    if (e.ColIndex > 0 && e.RowIndex > 0)
    {
        // Store data back to the data source from the grid cell.
        this._extData[e.RowIndex - 1, e.ColIndex - 1] = int.Parse(e.Style.CellValue.ToString());
        e.Handled = true;
    }
}
```

```vbnet
[VB.NET]
Private Sub GridSaveCellInfo(ByVal sender As Object, ByVal e As GridSaveCellInfoEventArgs)
    If ((e.ColIndex > 0) AndAlso (e.RowIndex > 0)) Then
        
        ' Store data back to the data source from the grid cell.
        Me._extData((e.RowIndex - 1), (e.ColIndex - 1)) = System.Int32.Parse(e.Style.CellValue.ToString())
        e.Handled = True
    End If
End Sub
```

#### 4.1.4.11.2.2 QueryRowHeight

### 4.1.4.11.2.2 QueryRowHeight

<!-- tags: [grid, optional events, data source, row height, column width] keywords: [SaveCellInfo, QueryRowHeight, virtual grid, external datasource, dynamic row height, covered cell ranges] -->
```