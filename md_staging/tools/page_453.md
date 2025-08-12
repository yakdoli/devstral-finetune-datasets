```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_453.jpeg
document_name: tools
page_number: 453
page_id: tools#page_453
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:13:37Z
fidelity: lossless
-->

### 3.5.3.1.6.3 How to identify the current selected date at run time?

**Overview**
- Explains how to identify and display the currently selected date in the MonthCalendarAdv control.
- Demonstrates handling the DateSelected event to access and display the selected date.

## Content

The MonthCalendarAdv control provides an array of selected dates. If you want to retrieve only a single date, you can select the first element from this array. To restrict the user to selecting only one date, set the `AllowMultipleSelection` property to `false`. The `DateSelected` event is triggered after the user completes the selection.

### Code Example

#### C#
```csharp
private void monthCalendarAdv1_DateSelected(object sender, EventArgs e)
{
    // DateSelected event is fired and selected dates will be displayed.
    MessageBox.Show("Selected Date: " + monthCalendarAdv1.SelectedDates[0].ToString());
}
```

#### VB.NET
```vb
Private Sub monthCalendarAdv1_DateSelected(ByVal sender As Object, ByVal e As EventArgs)
    ' DateSelected event is fired and selected dates will be displayed.
    MessageBox.Show("Selected Date: " + monthCalendarAdv1.SelectedDates(0).ToString())
End Sub
```

### Explanation
- The `DateSelected` event is raised once the user has selected a date.
- The `SelectedDates` property of the control contains an array of selected dates.
- If `AllowMultipleSelection` is set to `false`, the user can only select one date, ensuring that `SelectedDates[0]` (or `SelectedDates(0)`) holds the single selected date.
- The `MessageBox.Show` method is used to display the selected date to the user.

## Page-level Navigation/TOC (if applicable)
- This section details the event-handling mechanism for retrieving the currently selected date in the MonthCalendarAdv control.

## Cross References
- Refer to the documentation on configuring the MonthCalendarAdv control for detailed property settings and additional functionalities.

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, MonthCalendarAdv, EventHandling, DateSelection] keywords: [MonthCalendarAdv, DateSelected, AllowMultipleSelection, SelectedDates, C#, VB.NET, DateTime, MessageBox] -->
```