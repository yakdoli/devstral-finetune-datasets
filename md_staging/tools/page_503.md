```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_503.jpeg
document_name: tools
page_number: 503
page_id: tools#page_503
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:35Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
this.dateTimePickerAdv1.ReadOnly = true;
this.dateTimePickerAdv1.ReadOnlyValueChange = true;
```

```vb
Me.dateTimePickerAdv1.ReadOnly = True
Me.dateTimePickerAdv1.ReadOnlyValueChange = True
```

![](https://example.com/image.png "Figure 291: DateTimePickerAdv in ReadOnly Mode")
*Figure 291: DateTimePickerAdv in ReadOnly Mode*

### 3.5.3.2.5.2 How to display DateTimePickerAdv control programmatically?

We can display the Calendar programmatically on a button click. The `DisplayCalendar` method should be called from the click event handler in order to show the control.

#### [C#]

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    // Shows the calendar.
    this.dateTimePickerAdv1.DisplayCalendar();
}
```

#### [VB.NET]

```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs)

    ' Shows the calendar.
    Me.dateTimePickerAdv1.DisplayCalendar()
End Sub
```

### 3.5.3.2.5.3 Which event will raise when the date in the DateTimePickerAdv is changed?

#### CalendarDateChanged event

The `CalendarDateChanged` event is raised when a date in the `DateTimePickerAdv` is changed using the keys, or using the mouse.

#### [C#]

```csharp
this.dateTimePickerAdv1.Calendar.DateChanged += new EventHandler(Calendar_DateChanged);
```

---

<!-- tags: [syncfusion, windowsforms, datetimepickeradv, readonly, displaycalendar, calendardatechanged] keywords: [datetimepickeradv, readonly, readonlyvaluechange, displaycalendar, calendardatechanged, control, events, methods, programmatic, userinteraction] -->
```