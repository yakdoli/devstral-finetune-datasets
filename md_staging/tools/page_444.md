```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_444.jpeg
document_name: tools
page_number: 444
page_id: tools#page_444
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to override the internal grid context menu using a custom context menu in Windows Forms applications.
- Focus moves to tomorrow's date when a menu item is clicked, showcasing event handling.
- Implementation with Syncfusion.Windows.Forms.Tools.MonthCalendarAdv control.

## Content

### Customizing MonthCalendar Context Menu

In this section, we override the internal grid context menu of the `MonthCalendarAdv` control and define custom menu items.

```csharp
{
    this.monthCalendarAdv1.GetInternalGridControl().ContextMenu = this.contextMenuStrip1;
}
```

```csharp
// Focus moves to tomorrow's date, when menu item is clicked
private void menuItem1_Click(object sender, System.EventArgs e)
{
    this.monthCalendarAdv1.Value = DateTime.Today.AddDays(1);
}
```

#### Custom MonthCalendar Class

We create a custom class `CustomMonthCalendarAdv` that inherits from `Syncfusion.Windows.Forms.Tools.MonthCalendarAdv`. This class overrides the `InitializeGrid` method to access the internal grid and provides a method to retrieve it.

```csharp
// Defining CustomMonthCalendarAdv class
public class CustomMonthCalendarAdv : Syncfusion.Windows.Forms.Tools.MonthCalendarAdv
{
    private Syncfusion.Windows.Forms.Tools.CalendarGrid internalGrid;
    // Overrides the InitializeGrid.
    protected override void InitializeGrid(ref Syncfusion.Windows.Forms.Tools.CalendarGrid grid)
    {
        base.InitializeGrid(ref grid);
        internalGrid = grid;
    }
    // Returns the internal grid.
    public Syncfusion.Windows.Forms.Tools.CalendarGrid GetInternalGridControl()
    {
        return internalGrid;
    }
}
```

### VB.NET Example

The following example shows how to declare, initialize, and override the internal grid context menu using the custom context menu in VB.NET.

```vb
' Declaring and Initializing the calendar, Context menu and menu item
Private monthCalendarAdv1 As CustomMonthCalendarAdv
Private menuItem1 As System.Windows.Forms.MenuItem
Private contextMenuStrip1 As System.Windows.Forms.ContextMenu
Me.contextMenuStrip1 = New System.Windows.Forms.ContextMenu()
Me.menuItem1 = New System.Windows.Forms.MenuItem()
Me.monthCalendarAdv1 = New MonthCalendar.Form1.CustomMonthCalendarAdv()
Me.contextMenuStrip1.MenuItems.AddRange(New System.Windows.Forms.MenuItem() {Me.menuItem1})
Me.menuItem1.Text = "Go To Tomorrow"
AddHandler Me.menuItem1.Click, AddressOf Me.menuItem1_Click

' Override the internal grid context menu using the custom context menu
```

## API Reference

### Namespace
- **Syncfusion.Windows.Forms.Tools.MonthCalendarAdv**

### Methods
- **InitializeGrid**:  
  - **Signature**: `protected override void InitializeGrid(ref CalendarGrid grid)`
  - **Description**: Overrides the base `InitializeGrid` method to access the internal grid for customization.

### Properties
- **GetInternalGridControl**:  
  - **Signature**: `public CalendarGrid GetInternalGridControl()`
  - **Description**: Returns the internal grid for accessing and customizing properties.

## Code Examples

The code examples above demonstrate how to:
1. Override the internal grid context menu of a `MonthCalendarAdv` control.
2. Handle menu item events to perform actions, such as moving focus to tomorrow's date.

## Cross References

- **Related Controls**:  
  - `Syncfusion.Windows.Forms.Tools.MonthCalendarAdv`
  - `System.Windows.Forms.ContextMenu`
  - `System.Windows.Forms.MenuItem`

<!-- tags: [windows-forms, month-calendar, context-menu, custom-calendars, event-handling] keywords: [monthcalendaradv, contextmenustrip, menuitem, datetime, tomorrow] -->
```