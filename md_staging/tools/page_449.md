```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_449.jpeg
document_name: tools
page_number: 449
page_id: tools#page_449
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates setting tooltip text and appearance for specific cells in a Windows Forms grid.
- Uses `Syncfusion` controls for advanced grid functionality.
- Includes code examples in C# and VB.NET for handling different cell conditions.

## Content

### Handling Cell Appearance and Tooltip in Windows Forms Grid

#### C# Example
```csharp
e.Style.BackColor = Color.LightSteelBlue;
}
//Sets Tooltip text for the cells outside range
else if (e.IsOutsideRange)
    e.Style.CellTipText = "Outside range";
//Sets Cell Appearance to "Raised" for fourth Column
else if (e.ColIndex == 4)
    e.Style.CellAppearance =
Syncfusion.Windows.Forms.Grid.GridCellAppearance.Raised;
else
    //event is stopped
    e.Handled = false;
}
```

#### VB.NET Example
```vb
Private Sub monthCalendarAdv1_DateCellQueryInfo(ByVal sender As Object, ByVal e As DateCellQueryInfoEventArgs)
    'Identifies current cell and sets the tooltip text for the calendar
    If e.IsCurrentCell Then
        e.Style.CellTipText = "Syncfusion calendar control"
        e.Style.CellAppearance =
Syncfusion.Windows.Forms.Grid.GridCellAppearance.Flat
        e.Style.BackColor = Color.LightSteelBlue
        'Sets Tooltip text for the cells outside range
        ElseIf e.IsOutsideRange Then
            e.Style.CellTipText = "Outside range"
        'Sets Cell Appearance to "Raised" for fourth Column
        ElseIf e.ColIndex = 4 Then
            e.Style.CellAppearance =
Syncfusion.Windows.Forms.Grid.GridCellAppearance.Raised
        Else
            e.Handled = False
            'event is stopped
        End If
End Sub
```

### Note:
1. **In Fig 1**, 18th is identified as the current cell, and the tooltip is displayed. Additionally, the background of the current cell is painted with LightSteelBlue.
2. **Edges of the 4th column cells** (`ColIndex=4`), other than the current cell are set to "Raised" and hence show a raised appearance.
3. **In Fig 2**, user tries to query the cells outside the range, i.e., inactive month dates, and the respective tooltip is displayed.

## Page-level Navigation/TOC (if applicable)
- Essential Tools for Windows Forms

## Cross References
- See also: Syncfusion Grid Control documentation for more advanced cell styling and interaction handling.

<!-- tags: [Syncfusion Winforms, GridControl, Appearance, Tooltip, CellInteraction, WindowsForms] keywords: [LightSteelBlue, Raised, CellAppearance, CellTipText, IsCurrentCell, IsOutsideRange, ColIndex, GridCellAppearance, monthCalendarAdv1, eventHandled] -->
```