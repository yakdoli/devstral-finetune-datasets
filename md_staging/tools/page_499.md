```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_499.jpeg
document_name: tools
page_number: 499
page_id: tools#page_499
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:21Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
Public Sub FireNullEvent()
    RaiseEvent NullButtonDown(Me, New EventArgs())
End Sub

Private Property Culture() As CultureInfo Implements IDateTimePickerAdvCalendar.Culture
    Get
        Throw New Exception("The method or operation is not implemented.")
    End Get
    Set(ByVal value As CultureInfo)
        Throw New Exception("The method or operation is not implemented.")
    End Set
End Property
End Class
```

### Steps to Configure Custom Calendar

1. **Set the properties**:
   - Set the `Active` property of the MonthCalendar to `True`.
   - Set the `CustomPopupWindow` property of the `DateTimePickerAdv` to the `PopupControlContainer` control.
   - Set the `CustomDrop` property of the `DateTimePickerAdv` to `True`.

#### C# Code Example

```csharp
this.dateTimePickerAdv1.CustomDrop = true;
this.dateTimePickerAdv1.CustomPopupWindow = this.popupControlContainer1;
// Setting the DateTimePickerAdv control to consider the interface events by enabling Active property
this.MonthCalendar.Active = true;
// Adding Calendar to the Popup Control Container
this.popupControlContainer1.Controls.Add(this.MonthCalendar);
```

#### VB.NET Code Example

```vb
Me.dateTimePickerAdv1.CustomDrop = True
Me.dateTimePickerAdv1.CustomPopupWindow = Me.popupControlContainer1
' Setting the DateTimePickerAdv control to consider the interface events by enabling Active property
Me.MonthCalendar.Active = True
' Adding Calendar to the Popup Control Container
Me.popupControlContainer1.Controls.Add(Me.MonthCalendar)
```

### Button Click Event Handling

2. In the button click event, call the `MyCustomCalendar`'s `FireNullEvent` method.

## Summary

This section explains how to configure a custom calendar using `DateTimePickerAdv` in Syncfusion WinForms. It includes setting necessary properties and handling button click events to trigger custom calendar actions. The examples provided demonstrate the implementation in both C# and VB.NET.

## References

For more details on customizing controls and handling events, refer to the Syncfusion documentation.

<!-- tags: [Syncfusion, WinForms, DateTimePickerAdv, CustomCalendar, VB.NET, C#, EventHandling] keywords: [CustomPopupWindow, CustomDrop, MonthCalendar, ActiveProperty, FireNullEvent] -->
```