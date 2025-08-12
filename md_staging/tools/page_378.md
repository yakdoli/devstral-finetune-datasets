```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_378.jpeg
document_name: tools
page_number: 378
page_id: tools#page_378
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:06Z
fidelity: lossless
-->

## Overview
- Demonstrates handling the `Click` event of the `buttonEditChildButton1` control to display a Calendar.
- Explains how to use the `DateSelected` event to update the selected date in the ButtonEdit control.

## Content

### Handle the Click Event for Calendar Display

To handle the `Click` event of `buttonEditChildButton1` to display the Calendar, use the following code:

```csharp
[C#]
private void buttonEditChildButton1_Click(object sender, System.EventArgs e)
{
    this.calendarPop1.Visible = true;
    this.calendarPop1.ShowPopup (new Point(200,200));
}
```

```vb
[VB.NET]
Private Sub buttonEditChildButton1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.calendarPop1.Visible = True
    Me.calendarPop1.ShowPopup(New Point(200, 200))
End Sub
```

### Handle the DateSelected Event

The `DateSelected` event can also be handled to display the selected date in the textbox of the ButtonEdit control. Use the following code:

```csharp
[C#]
this.MonthCal.DateSelected+=new EventHandler(MonthCal_DateSelected);

private void MonthCal_DateSelected(object sender,System.EventArgs e)
{
    this.buttonEdit1.TextBox.Text= this.MonthCal.Value.ToString();
}
```

```vb
[VB.NET]
Private Me.MonthCal.DateSelected+= New EventHandler(MonthCal_DateSelected)

Private Sub MonthCal_DateSelected(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.buttonEdit1.TextBox.Text = Me.MonthCal.Value.ToString()
End Sub
```

## API Reference

### Events
- **DateSelected**: Triggered when a date is selected in the Calendar control.

### Methods
- **ShowPopup(Point location)**: Displays the Calendar control at a specified location.

### Properties
- **Visible**: Determines if the Calendar control is visible.

### Namespace: Syncfusion.Windows.Forms.Tools

This section provides a comprehensive reference to the methods and properties used in the examples.

## Code Examples

### C# Example
```csharp
private void buttonEditChildButton1_Click(object sender, System.EventArgs e)
{
    this.calendarPop1.Visible = true;
    this.calendarPop1.ShowPopup (new Point(200,200));
}

private void MonthCal_DateSelected(object sender, System.EventArgs e)
{
    this.buttonEdit1.TextBox.Text = this.MonthCal.Value.ToString();
}
```

### VB.NET Example
```vb
Private Sub buttonEditChildButton1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.calendarPop1.Visible = True
    Me.calendarPop1.ShowPopup(New Point(200, 200))
End Sub

Private Sub MonthCal_DateSelected(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.buttonEdit1.TextBox.Text = Me.MonthCal.Value.ToString()
End Sub
```

## See also
- [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation/windowsforms/)

<!-- tags: [product, module, control, api, version?] keywords: [Syncfusion, WinForms, Calendar, DateSelected, ButtonEdit, Click Event, ShowPopup, Visible] -->
```