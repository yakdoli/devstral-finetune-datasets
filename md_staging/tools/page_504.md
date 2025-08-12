```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_504.jpeg
document_name: tools
page_number: 504
page_id: tools#page_504
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Handles `DateChanged` events in the `DateTimePickerAdv` control.
- Implements `DateChanged` and `ValueChanged` event handlers.

---

## Content

```csharp
void Calendar_DateChanged(object sender, EventArgs e)
{
    Console.WriteLine("Date Changed");
}
```

```vb
[VB.NET]

Me.dateTimePickerAdv1.Calendar.DateChanged += New
EventHandler(Calendar_DateChanged)

Private Sub Calendar_DateChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("Date Changed")
End Sub
```

### 3.5.3.2.5.4 Which event will raise when the month is changed using arrow button?

When the month in the `DateTimePickerAdv` is changed using the Arrow button, the `ValueChanged` event is raised.

```csharp
[C#]

this.dateTimePickerAdv1.ValueChanged += new
EventHandler(dateTimePickerAdv1_ValueChanged);

private void dateTimePickerAdv1_ValueChanged(object sender, EventArgs e)
{
    if (Control.MouseButtons != MouseButtons.None)
    {
        Console.WriteLine("Month Changed using ArrowButton");
    }
}
```

```vb
[VB.NET]

Me.dateTimePickerAdv1.ValueChanged += New
EventHandler(dateTimePickerAdv1_ValueChanged)

Private Sub dateTimePickerAdv1_ValueChanged(ByVal sender As Object, ByVal e As EventArgs)
    If Control.MouseButtons <> MouseButtons.None Then
        Console.WriteLine("Month Changed using ArrowButton")
    End If
End Sub
```

---

## API Reference

### WinForms-specific

- **Namespaces**: `System.Windows.Forms`, `Syncfusion.Windows.Forms.Tools`
- **Events**: `DateChanged`, `ValueChanged`
- **Control**: `DateTimePickerAdv`

### Parameters

| Name | Type             | Description | Default | Required |
|------|------------------|-------------|---------|----------|
| `sender` | `object` | The source of the event. | `null` | Yes |
| `e` | `EventArgs` | Event arguments. | `null` | Yes |

### Returns

None.

### Exceptions

- `InvalidOperationException`: Thrown if the operation is not valid for the control's current state.

## Code Examples

### C# Example

```csharp
this.dateTimePickerAdv1.ValueChanged += new
EventHandler(dateTimePickerAdv1_ValueChanged);

private void dateTimePickerAdv1_ValueChanged(object sender, EventArgs e)
{
    if (Control.MouseButtons != MouseButtons.None)
    {
        Console.WriteLine("Month Changed using ArrowButton");
    }
}
```

### VB.NET Example

```vb
Me.dateTimePickerAdv1.ValueChanged += New
EventHandler(dateTimePickerAdv1_ValueChanged)

Private Sub dateTimePickerAdv1_ValueChanged(ByVal sender As Object, ByVal e As EventArgs)
    If Control.MouseButtons <> MouseButtons.None Then
        Console.WriteLine("Month Changed using ArrowButton")
    End If
End Sub
```

### See also

- [DateTimePickerAdv](#)
- [Event Handling](#)
- [Control.MouseButtons](#)

<!-- tags: [syncfusion, winforms, datetimepickeradv, datechanged, valuechanged, eventhandling] keywords: [datetimepicker, datechanged event, valuechanged event, arrowbutton, month change] -->
```