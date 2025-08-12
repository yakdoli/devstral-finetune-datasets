```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_502.jpeg
document_name: tools
page_number: 502
page_id: tools#page_502
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:26Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Event Handling

The following table lists key events and their descriptions specific to the control:

| Event                 | Description                                                                   |
|-----------------------|-------------------------------------------------------------------------------|
| StretchDropDownImageChanged | Handled when the `StretchDropDownImage` property changes.        |
| ValueChanged         | Event is handled when the Value property changes.                           |

#### 3.5.3.2.4.1 `PopupClosed` Event

This event is handled when the popup is closed. Using the `PopupCloseType` member of the `PopupClosedEventArgs`, we can identify the type of closing.

##### [C#]

```csharp
private void dateTimePickerAdv1_PopupClosed(object sender, PopupClosedEventArgs e)
{
    // Canceled - User cancels the updates if any.
    // Deactivated - If the user moves the focus to some other window
    // Done - If the user wants the changes to be applied to the control
    Console.WriteLine(e.PopupCloseType.ToString());
}
```

##### [VB.NET]

```vbnet
Private Sub dateTimePickerAdv1_PopupClosed(ByVal sender As Object, ByVal e As PopupClosedEventArgs)
    ' Canceled - User cancels the updates if any.
    ' Deactivated - If the user moves the focus to some other window
    ' Done - If the user wants the changes to be applied to the control
    Console.WriteLine(e.PopupCloseType.ToString())
End Sub
```

#### 3.5.3.2.5 Frequently Asked Questions

This section illustrates the solutions for various task-based queries about the control.

##### 3.5.3.2.5.1 How to change the date in a `DateTimePickerAdv` control, when it is ReadOnly?

We can make the control read-only by setting `ReadOnly` property to true. `DateTimePickerAdv` control have an option to change the date, even in ReadOnly mode using Arrow keys. Set `ReadOnlyValueChange` property to true to effect this setting.

##### [C#]

```csharp
// Code placeholder - incomplete
```

## API Reference

For more detailed information on the properties, methods, and events of the `DateTimePickerAdv` control, please refer to the Syncfusion WinForms documentation.

## Code Examples

See the examples above for usage in both C# and VB.NET languages.

## Cross References

For additional details and related topics, refer to the following sections within the documentation:

- `DateTimePickerAdv` control documentation
- `PopupCloseType` enumeration details

### Getting Started

See the initial setup instructions in the product's documentation.

### Troubleshooting

Refer to the FAQs for common issues and solutions.

<!-- tags: [syncfusion, winforms, datetimepickeradv, readonly, popupclosed, events] keywords: [syncfusion winforms, datetimepickeradv control, readonly mode, popupclosed event] -->
```