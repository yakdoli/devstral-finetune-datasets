```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_454.jpeg
document_name: tools
page_number: 454
page_id: tools#page_454
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:14:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to display a selected date using a `MessageBox` in a `MonthCalendarAdv` control.
- Explains how to restrict date selections to specific days of the week using the `DateCellQueryInfo` event handler.

## Content

### Figure 251: MessageBox displaying the selected date at Run Time

![Figure 251](./images/VisualRepresentationOfSelectedDate.png)
**Figure 251:** MessageBox displaying the selected date at Run Time

#### Restricting Date Selections

**3.5.3.1.6.4** **Is it possible to restrict the dates that are selected?**

Yes, we can restrict the dates that are selected. If you want to allow the user to select only Mondays on the calendar, you can set the `Clickable` property to `false` for other days except Monday using the `DateCellQueryInfo` event handler.

The following code snippet can be used for this.

```csharp
[C#]

void monthCalendarAdv1_DateCellQueryInfo(object sender,
    DateCellQueryInfoEventArgs e)
{
    // if not Monday
    if (e.ColIndex != 2)
    {
        e.Style.Clickable = false;
        e.Style.Enabled = false;
    }
}
```

```vb.net
[VB.NET]

Private Sub monthCalendarAdv1_DateCellQueryInfo(ByVal sender As Object, _
    ByVal e As DateCellQueryInfoEventArgs)
End Sub
```

### Summary

This section explains how to display a selected date using a `MessageBox` and restrict date selections to specific days of the week in a `MonthCalendarAdv` control.

## API Reference

### Events

#### DateCellQueryInfo

Triggered when querying each date cell in the `MonthCalendarAdv` control.

### Parameters

- `sender`: The object that triggered the event.
- `e`: An instance of `DateCellQueryInfoEventArgs` containing event data such as the date cell's column index (`ColIndex`), and styling options (`Clickable`, `Enabled`).

---

<!-- tags: [Syncfusion Winforms, MonthCalendarAdv, DateCellQueryInfo] keywords: [MonthCalendarAdv, DateCellQueryInfo, restrict dates, selectable dates, C#, VB.NET] -->
```