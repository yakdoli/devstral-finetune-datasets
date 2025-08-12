```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_488.jpeg
document_name: grid
page_number: 488
page_id: grid#page_488
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:44Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to handle printing operations in a Windows Forms GridControl.
- Provides C# and VB.NET code examples for managing the grid's PrintingMode and determining visible rows during printing.

## Content

### Printing in the GridControl

The following code snippets show how to set up printing in a GridControl by adjusting the PrintingMode property and determining which rows are visible during the printing process.

#### C#
```csharp
_grid.PrintingMode = true;

// Get Top Row Index.
int topRow = _grid.TopRowIndex;
_grid.ViewLayout.Reset();

// Get Bottom Row Index.
int botRow = this._grid.ViewLayout.LastVisibleRow
    - (this._grid.ViewLayout.HasPartialVisibleRows ? 1 : 0);

_grid.PrintingMode = false;

// Print
Console.WriteLine("OnPrintPage " + topRow.ToString() + " " + botRow.ToString());
}
}
```

#### VB.NET
```vb
[VB.NET]

Public Class MyPrintDocument
    Inherits GridPrintDocument
    Private _grid As GridControlBase
    Public Sub New(grid As GridControlBase, printPreview As Boolean)
        MyBase.New(grid, printPreview)
        _grid = grid
    End Sub

    Protected Overrides Sub OnPrintPage(ByVal ev As System.Drawing.Printing.PrintPageEventArgs)
        MyBase.OnPrintPage(ev)
        _grid.PrintingMode = True

        ' Get Top Row Index.
        Dim topRow As Integer = _grid.TopRowIndex
        _grid.ViewLayout.Reset()

        ' Get Bottom Row Index.
        Dim botRow As Integer = Me._grid.ViewLayout.LastVisibleRow
        If Me._grid.ViewLayout.HasPartialVisibleRows Then
            botRow = botRow - 1
        End If
        _grid.PrintingMode = False

        // Print
    End Sub
End Class
```

### Explanation
- **PrintingMode**: Enables or disables the grid's printing mode. When set to true, the grid prepares for printing.
- **Top Row Index**: Determines the topmost visible row in the grid.
- **Bottom Row Index**: Determines the bottommost visible row, adjusting for partial visible rows.
- **Reset**: Ensures the grid's view layout is set correctly before calculating visible rows.

## Cross References
- See also: GridControlBase, GridPrintDocument, ViewLayout, TopRowIndex, LastVisibleRow

<!-- tags: [syncfusion, windows forms, grid, printing, gridcontrol] keywords: [printingmode, toprowindex, lastvisiblerow, haspartialvisiblerows] -->
```