```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: QTP
page_number: 054
page_id: QTP#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:34Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- The section describes interfaces and methods related to managing date-time pickers, docking windows, and group bars in a Syncfusion WinForms application.
- Focus on calendar functionalities, docking features, and navigation panel handling.

## Content

### Date-Time Picker Related Methods

| Method | Description |
| --- | --- |
| `void ShowPopupWindow(object visible, object x, object y);` | Interface to show the calendar popup. |
| `void ShowCalendar(object visible);` | Interface to show the calendar in the popup window. |
| `void SetCalendarValue(object visible, string calValue);` | Interface to set the Calendar value of the `DateTimePickerAdv` control. |
| `void PopupClose(object visible);` | Interface to close the popup window. |
| `void SetTodayValue(string str);` | Interface to set the today value when the today button is clicked. |
| `void SetNoValue(string str);` | Interface to set the null value when the None button is clicked. |
| `System.DateTime GetCalendarValue();` | Returns the current value in the `DateTimePickerAdv` control. |

### DockingManager

| Method | Description |
| --- | --- |
| `DockStateChange(string dock, string prevState, string ctrl, string hostForm, string dockingStyle)` | Changes the docking window according to the specified current and previous state (i.e., Pinned, Unpinned, Tabbed, and MDIChild). |
| `VisibilityChange(string ctrlName, string visibility)` | Changes the visibility of the docked control according to the specified state. |
| `ActivateControl(string ctrlName)` | Activates the specified control. |
| `FloatStateChange(string ctrlName, string x, string y, string width, string height)` | Changes the state of the docking window into a floating state with the specified location and size. |

### GroupBar

| Method | Description |
| --- | --- |
| `SelectGroup(object index, string itemText)` | Selects the GroupBar item. |
| `DropDownButtonClick()` | Simulates click in the Navigation pane drop-down button. |

## API Reference

### Methods

- **ShowPopupWindow**: Displays a calendar popup window.
- **ShowCalendar**: Displays the calendar within the popup window.
- **SetCalendarValue**: Sets the value of the `DateTimePickerAdv` control.
- **PopupClose**: Closes the popup window.
- **SetTodayValue**: Sets the value to the current date when the "Today" button is clicked.
- **SetNoValue**: Sets a null value when the "None" button is clicked.
- **GetCalendarValue**: Retrieves the current value from the `DateTimePickerAdv` control.
- **DockStateChange**: Changes the docking state of a window based on the specified parameters.
- **VisibilityChange**: Adjusts the visibility of a docked control.
- **ActivateControl**: Activates the specified control.
- **FloatStateChange**: Floats a docking window with specified dimensions and position.
- **SelectGroup**: Selects an item in the GroupBar.
- **DropDownButtonClick**: Simulates a click on the drop-down button in the Navigation pane.

## Code Examples

### C# Example for DateTimePickerAdv

```csharp
// Example for setting the calendar value
void SetCalendarValueExample()
{
    // Assuming dateValue is a valid date string
    string dateValue = "2023-08-09";
    Syncfusion.Windows.Forms.Tools.DateTimePickerAdv dateTimePicker = new Syncfusion.Windows.Forms.Tools.DateTimePickerAdv();
    dateTimePicker.SetCalendarValue(true, dateValue);
}
```

### C# Example for DockingManager

```csharp
// Example for changing the docking state
void ChangeDockingStateExample()
{
    string dock = "Docked";
    string prevState = "Unpinned";
    string ctrl = "MyControl";
    string hostForm = "Form1";
    string dockingStyle = "Tabbed";
    DockingManager.DockStateChange(dock, prevState, ctrl, hostForm, dockingStyle);
}
```

### C# Example for GroupBar

```csharp
// Example for selecting a group in the GroupBar
void SelectGroupBarExample()
{
    object index = 0;
    string itemText = "Group 1";
    GroupBar.SelectGroup(index, itemText);
}
```

## Page-level Navigation/TOC (if applicable)

- Date-Time Picker Related Methods
- DockingManager
- GroupBar

## Cross References

- See also: `DateTimePickerAdv`, `DockingManager`, `GroupBar`, `Navigation Pane`, `Popup Window`.

<!-- tags: [Syncfusion, WinForms, DateTimePickerAdv, DockingManager, GroupBar, NavigationPane, PopupWindow] keywords: [calendar, date, time, docking, group, bar, state, visibility, floating, drop-down] -->
```