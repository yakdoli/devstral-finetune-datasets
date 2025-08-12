```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_791.jpeg
document_name: tools
page_number: 791
page_id: tools#page_791
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

| Event Name                | Description                                                                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ReadOnlyChanged           | This event occurs when the ReadOnly property is changed.                                                                                 |
| RightToLeftChanged        | This event occurs when the RightToLeft property is changed.                                                                              |
| SetNull                   | This event occurs when the NULL state is to be set based on a value.                                                                     |
| TextAlignChanged          | This event occurs when the TextAlign property is changed.                                                                                |
| ThemesEnabledChanged      | This event occurs when the ThemesEnabled property is changed.                                                                           |
| ValidationError           | This event occurs when the input text is invalid for the current state of the control.                                                   |

## Overview

### WinForms-specific overview

This section provides an overview of a specific event in the Syncfusion WinForms SDK. The event described is `BindablePercentValueChanged`, which is an important property for handling percentage values in a control. The overview includes a description of the event, its usage, and a sample implementation in C# and VB.NET.

---

## Documentation for BindablePercentValueChanged Event

### Overview

This event, `BindablePercentValueChanged`, occurs when the `BindablePercentValue` property is changed. The `BindablePercentValue` property is a wrapper property that indicates the percentage value. This property can be used to set the value of the control to 'Null'.

#### Event Handler

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### C# Code Example

```csharp
[C#]

private void percentTextBox1_BindablePercentValueChanged(object sender, EventArgs e)
{
    Console.WriteLine(" BindablePercentValueChanged event is raised ");
}
```

#### VB.NET Code Example

```vb
[VB.NET]

Private Sub percentTextBox1_BindablePercentValueChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" BindablePercentValueChanged event is raised ")
End Sub
```

### Summary

- **Event Name**: `BindablePercentValueChanged`
- **Trigger**: This event is triggered when the `BindablePercentValue` property is changed.
- **Usage**: Used to handle changes in the percentage value of a control.
- **Argument**: The event handler receives an `EventArgs` object, which provides data related to the event.

---

## Page-level Navigation/TOC

1. **Overview**
   - Specialized overviews of the event and its properties.
2. **Documentation for BindablePercentValueChanged Event**
   - Detailed description, usage, and code examples in C# and VB.NET.

---

<!-- tags: [syncfusion, winforms, event, bindablepercentvaluechanged, percentage, control, sdk, 11.4.0.26] keywords: [events, property, handler, percentage, cSharp, VB.NET, code examples] -->
```