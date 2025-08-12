```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_353.jpeg
document_name: tools
page_number: 353
page_id: tools#page_353
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:03Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes how to identify if a ButtonAdv control is in a pressed state.
- Explains the use of the ButtonAdv.PushButton property to maintain the button state.
- Demonstrates the run-time behavior and state tracking of the button.

## How to identify whether a ButtonAdv control is in pressed state or not

When ButtonAdv.PushButton property is enabled, the button will remain in its pressed state when clicked. The state of the button will be present in the property State. So by examining the state property, we can conclude whether the button is in the Pressed state or not. Using the Office2007 visual styles will help better understanding of this feature.

| Property      | Description                                                                                                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PushButton    | Specifies the state of the control. By default it is set to false. Set this to true. Now at run time, when the user clicks this button, the appearance of the button will change to pushed state and will regain its original state only by clicking it again. |

### [C#]

```csharp
private void buttonAdv1_Click(object sender, System.EventArgs e)
{
    if (this.buttonAdv1.State == Syncfusion.Windows.Forms.ButtonAdvState.Pressed)
        MessageBox.Show("Button is pushed");
    else
        MessageBox.Show("Button is in normal state");
}
```

### [VB.NET]

```vb
Private Sub buttonAdv1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles buttonAdv1.Click
    If Me.buttonAdv1.State == Syncfusion.Windows.Forms.ButtonAdvState.Pressed Then
        MessageBox.Show("Button is pushed")
    Else
        MessageBox.Show("Button is in normal state")
    End If
End Sub
```

## API Reference
- **Namespace:** Syncfusion.Windows.Forms
- **Class:** ButtonAdv
- **Property:** PushButton
- **State:** ButtonAdvState

## Code Examples
- Demonstrates how to handle the Click event to determine the state of the button and display a message accordingly.

<!-- tags: [syncfusion, winforms, buttonadv, pushbutton, state, event, csharp, vbnet]
keywords: [buttonadv, pushed state, state property, click event, visual styles, office2007] -->
```