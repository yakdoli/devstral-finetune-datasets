```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_448.jpeg
document_name: tools
page_number: 448
page_id: tools#page_448
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Handles events related to property changes, including `StretchScrollImage` and `ThemedBorder`.
- Describes the `DateCellQueryInfo` event and its use for custom formatting in calendar cells.

## Content

### StretchScrollImage Changed

| Event Name            | Description                                   |
|-----------------------|-----------------------------------------------|
| StretchScrollImageChanged | Handled when the `StretchScrollImage` property is changed. |
| ThemedBorderChanged   | Handles when the `ThemedBorder` property is changed. |

#### 3.5.3.1.5.1 DateCellQueryInfo Event

This event is handled to provide custom formatting for calendar cells.

| Members        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| CollIndex      | Specifies the column index of GridCell.                                    |
| DateValue      | Specifies the date value.                                                  |
| RowIndex       | Specifies the row index of GridCell.                                       |
| Style          | Specifies GridStyleInfo object.                                            |
| Handled        | Indicates whether the event has been handled. It is a bool value.         |
| IsCurrentCell  | Returns the current cell at run time.                                      |
| IsOutsideRange | Specifies whether the query is outside the range of a month.               |

### Example

The style parameter can be used to set tooltips for the MonthCalendarAdv control as follows. This example uses `IsCurrentCell`, `IsOutsideRange`, `CollIndex`, and `Handled` members.

#### Implementation in C#

```csharp
private void monthCalendarAdv1_DateCellQueryInfo(object sender, DateCellQueryInfoEventArgs e)
{
    // Identifies current cell and sets the tooltip text for the calendar
    if (e.IsCurrentCell)
    {
        e.Style.CellTipText = "Syncfusion calendar control";
        e.Style.CellAppearance = Syncfusion.Windows.Forms.Grid.GridCellAppearance.Flat;
    }
}
```

## Code Examples

The example demonstrates how to use the `DateCellQueryInfo` event to customize the appearance and tooltip of calendar cells in a `MonthCalendarAdv` control. The `Style` property is used to set the tooltip text and appearance based on specific conditions.

```csharp
// Example usage of DateCellQueryInfo
private void monthCalendarAdv1_DateCellQueryInfo(object sender, DateCellQueryInfoEventArgs e)
{
    if (e.IsCurrentCell)
    {
        e.Style.CellTipText = "Syncfusion calendar control";
        e.Style.CellAppearance = Syncfusion.Windows.Forms.Grid.GridCellAppearance.Flat;
    }
}
```

## RAG Annotations

<!-- tags: [Windows Forms, Event Handling, Calendar Control, Custom Formatting, MonthCalendarAdv, GridCellAppearance] keywords: [StretchScrollImageChanged, ThemedBorderChanged, DateCellQueryInfo, GridCell, GridStyleInfo, IsCurrentCell, IsOutsideRange, CellTipText, Flat] -->
```