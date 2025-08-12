```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: tools
page_number: 116
page_id: tools#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:31:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
Private Sub DoToolBarWrapping(ByVal toolbar As ToolBar, ByVal szmaxwrap As Size, ByVal szminwrap As Size, ByVal arg As Syncfusion.Windows.Forms.Tools.CommandBarWrappingEventArgs)
    Dim szcurrent As Size = arg.ClientSize
    Dim sztemp As Size = ToolBar.Size

    Dim nbtncount As Integer = ToolBar.Buttons.Count
    Dim szbtn As Size = ToolBar.ButtonSize

    If (arg.CommandBarResizeType = Syncfusion.Windows.Forms.Tools.CommandBarResizeType.Right) OrElse (arg.CommandBarResizeType = Syncfusion.Windows.Forms.Tools.CommandBarResizeType.Left) Then
        Dim nfactor As Integer = CInt(Math.Ceiling(CSng(szminwrap.Width) / CSng(szcurrent.Width)))
        Dim ffactor As Single = CSng(szminwrap.Width) / CSng(szcurrent.Width)

        If szcurrent.Width < szmaxwrap.Width Then
            arg.ClientSize = szmaxwrap
        ElseIf (nfactor > 1) AndAlso (nfactor = ffactor) Then
            Dim nnewwidth As Integer = CInt(Math.Ceiling(CSng(nbtncount) / CSng(nfactor)) * szbtn.Width)

            Dim sznew As Size = Size.Empty
            If nnewwidth > szmaxwrap.Width Then
                ' Set this width to be the toolbar's parent panel width and allow the toolbar to
                ' layout itself for this width. We then get the toolbar's height and assign this as
                ' the CommandBar client size.
                sznew.Width = nnewwidth
                ToolBar.Parent.Width = sznew.Width
                sznew.Height = ToolBar.Height
                ToolBar.Parent.Width = sztemp.Width
            Else
                sznew = szmaxwrap
            End If

            ' Set the CommandBar's client size to be equal to this new size.
            arg.ClientSize = sznew
        ElseIf ffactor <= 1 Then
            ' The CommandBar is extended to the maximum width.
            arg.ClientSize = szminwrap
        Else
            arg.ClientSize = ToolBar.Size
        End If
    End If
End Sub
```

## Summary
This section explains how to handle toolbar resizing in Windows Forms applications using the Syncfusion WinForms library. The code snippet demonstrates an event handler that calculates and adjusts the toolbar's size based on constraints like minimum and maximum wrap sizes.

## Overview
- The `DoToolBarWrapping` subroutine is responsible for managing toolbar size adjustments during resizing events.
- It considers resizing directions (`Right` or `Left`) and checks against maximum and minimum wrap widths.
- The logic calculates a new width dynamically based on button counts and toolbar dimensions, ensuring appropriate layout and client size assignments.

## API Reference

### Event: `CommandBarWrappingEventArgs`
#### Parameters
- **toolBar**: `ToolBar` - The toolbar being resized.
- **szmaxwrap**: `Size` - Maximum wrap size for the toolbar.
- **szminwrap**: `Size` - Minimum wrap size for the toolbar.
- **arg**: `CommandBarWrappingEventArgs` - Event arguments containing resizing details.

### Functions Used
- `Math.Ceiling`
- `CInt`, `CSng` for type conversion
- `Size.Empty` for initializing `Size` objects

### Types Used
- `Size`: Represents dimensions of the toolbar and client area.
- `CommandBarResizeType`: Enumerates possible resize directions.
- `CommandBarWrappingEventArgs`: Event argument specific to toolbar resizing events.

## Page-Level Navigation/TOC
- Essential Tools for Windows Forms
  - Toolbar Wrapping Event Handling

<!-- tags: [Syncfusion Winforms, CommandBar, Toolbar, Resize, EventHandling] keywords: [DoToolBarWrapping, CommandBarWrappingEventArgs, ResizeType, ClientSize, MaximumWidth, MinimumWidth] -->
```