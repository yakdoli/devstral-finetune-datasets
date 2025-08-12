```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: schedule
page_number: 033
page_id: schedule#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:09:33Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- Demonstrates using the `ContextMenu` to change the `ScheduleViewType`.
- Highlights the `Day` view after executing the `ContextMenu` selection.
- Shows a clear view of the scheduling interface with interactive options for managing items.

## Content

### Schedule and Date Navigation
The image displays a graphical user interface for scheduling, specifically a calendar for November 2006, along with adjacent months for reference.

#### Calendar Layout
- The calendar is structured in a grid format with days of the week labeled as **Monday** through **Sat/Sun**.
- It shows a detailed view of dates, including dates from the previous month (October) and the subsequent month (December) to provide contextual navigation around the current month.
- The selected date is highlighted for interaction, emphasizing its importance in the workflow.

#### ContextMenu Options
The `ContextMenu` provides various options for managing the schedule:
- **New Item**
- **New AllDay item**
- **Edit Item**
- **Delete Item**
- **Day**
- **WorkWeek**
- **Week**
- **Month**

The context menu is active, indicating that a specific date has been clicked, and the user is interacting with it, demonstrating how to switch between different views of the schedule using the context menu.

## API Reference

### ScheduleControl Properties
The `ScheduleControl` includes the following properties, which are relevant to this interface:
- **ScheduleViewType**: Determines the current view type (e.g., Day, WorkWeek, etc.).

### ScheduleViewType Enumeration
- **Day**: Displays a detailed day view of the schedule.
- **WorkWeek**: Shows the focus on working days of the week.
- **Week**: Provides a full-week perspective.
- **Month**: Offers a monthly view of the schedule.

## Code Examples

```csharp
// Example: Changing the ScheduleViewType using the context menu
private void ScheduleControl_ContextMenuOpening(object sender, Syncfusion.Windows.Forms.ContextMenuEventArgs e)
{
    ScheduleControl selectedControl = sender as ScheduleControl;
    if (selectedControl != null)
    {
        // Determine the current ContextMenu item selection
        if (e.ContextMenuItem.Text == "Day")
        {
            selectedControl.ScheduleViewType = ScheduleViewType.Day;
        }
        // Additional cases for other view types...
    }
}
```

## Page-level Navigation/TOC (if applicable)

This section provides a walkthrough of the key features shown in the image:
1. **Date Navigation**: Navigating between months and selecting specific dates.
2. **ContextMenu Interaction**: Using the context menu to change the `ScheduleViewType`.
3. **Day View**: Detailed view after selecting the "Day" option from the context menu.

## Cross References

- See also: Documentation on `ScheduleViewType` and other schedule control features.
- Related topics: Handling context menus, interacting with scheduling controls, and customizing views.

## RAG Annotations
<!-- tags: [schedule, windows forms, contextmenu, scheduleviewtype, dayview] keywords: [contextmenu, Months, Days, Navigation, item management, day view] -->
```