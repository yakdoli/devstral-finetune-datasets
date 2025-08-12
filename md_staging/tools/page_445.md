```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_445.jpeg
document_name: tools
page_number: 445
page_id: tools#page_445
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:53Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Custom Context Menu for MonthCalendarAdv

The following code snippet demonstrates how to customize the context menu for a `MonthCalendarAdv` control, allowing users to navigate to tomorrow's date when a specific menu item is clicked.

```vb
Private Sub Form1_Load_1(ByVal sender As Object, ByVal e As EventArgs)
    Me.monthCalendarAdv1.GetInternalGridControl().ContextMenu = Me.contextMenuStrip1
End Sub

' Focus moves to tomorrow's date, when menu item is clicked.
Private Sub menuItem1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.monthCalendarAdv1.Value = DateTime.Today.AddDays(1)
End Sub
```

### Custom MonthCalendarAdv Class

To extend the functionality of the `MonthCalendarAdv` control, a custom class can be created by inheriting from the `Syncfusion.Windows.Forms.Tools.MonthCalendarAdv` class.

```vb
' Defining CustomMonthCalendarAdv class
Public Class CustomMonthCalendarAdv
    Inherits Syncfusion.Windows.Forms.Tools.MonthCalendarAdv
    Private internalGrid As Syncfusion.Windows.Forms.Tools.CalendarGrid

    ' Overrides the InitializeGrid.
    Protected Overloads Overrides Sub InitializeGrid(ByRef grid As Syncfusion.Windows.Forms.Tools.CalendarGrid)
        MyBase.InitializeGrid(grid)
        internalGrid = grid
    End Sub

    ' Returns the internal grid.
    Public Function GetInternalGridControl() As Syncfusion.Windows.Forms.Tools.CalendarGrid
        Return internalGrid
    End Function
End Class
```

### Example: MonthCalendarAdv with Custom Context Menu

The following example shows the implementation of a `MonthCalendarAdv` control with a custom context menu that includes an option to navigate to tomorrow's date.

#### Figure: MonthCalendarAdv with Custom Context Menu
![MonthCalendarAdv with Custom Context Menu](https://i.imgur.com/11.png)

### ToolTips

Tooltips can be set using the `DateCellQueryInfo` event. This allows dynamic generation of tooltips based on specific date cells or other custom logic.

```vb
' Tooltips can be set using DateCellQueryInfo event.
```

### Summary

This section covers the customization of the `MonthCalendarAdv` control in Windows Forms, demonstrating how to implement a custom context menu and tooltips. By extending the functionality of the control, you can create more user-friendly and dynamic applications.

### API Reference

- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Class:** MonthCalendarAdv
- **Events:**
  - `DateCellQueryInfo`: Used to set tooltips dynamically for date cells.
- **Methods:**
  - `GetInternalGridControl()`: Returns the internal grid control for customization.
- **Properties:**
  - `ContextMenu`: Sets the custom context menu for the calendar control.

### Code Examples

#### Example 1: Custom Context Menu Implementation

```vb
Private Sub Form1_Load_1(ByVal sender As Object, ByVal e As EventArgs)
    Me.monthCalendarAdv1.GetInternalGridControl().ContextMenu = Me.contextMenuStrip1
End Sub

Private Sub menuItem1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.monthCalendarAdv1.Value = DateTime.Today.AddDays(1)
End Sub
```

#### Example 2: Custom MonthCalendarAdv Class

```vb
Public Class CustomMonthCalendarAdv
    Inherits Syncfusion.Windows.Forms.Tools.MonthCalendarAdv
    Private internalGrid As Syncfusion.Windows.Forms.Tools.CalendarGrid

    Protected Overloads Overrides Sub InitializeGrid(ByRef grid As Syncfusion.Windows.Forms.Tools.CalendarGrid)
        MyBase.InitializeGrid(grid)
        internalGrid = grid
    End Sub

    Public Function GetInternalGridControl() As Syncfusion.Windows.Forms.Tools.CalendarGrid
        Return internalGrid
    End Function
End Class
```

### See Also

- `Syncfusion.Windows.Forms.Tools.MonthCalendarAdv`
- `Syncfusion.Windows.Forms.Tools.CalendarGrid`
- `ContextMenuStrip`

### References

For more information on customizing controls and handling events in Windows Forms, refer to the official documentation:

- [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms)

<!-- tags: [winforms, monthcalendar, calendar, contextmenu, tooltips, datecellqueryinfo, event, customcontrols, controls, windowsforms] keywords: [monthcalendaradv, contextmenu, customcontrols, tooltips, datelinequeryinfo, contextmenustrip, windowsforms, datetime, navigation, userinterface, userinput, dynamic, customization, customizationcontrols, form1] -->
```