```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_638.jpeg
document_name: tools
page_number: 638
page_id: tools#page_638
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:42Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of the `popupControlContainer1` to display a Popup when the user right-clicks on a `RichTextBox`.
- Explains how to assign text to the `RichTextBox` after closing the Popup.
- Provides a code snippet for creating a transparent Popup.
- Includes a visual representation of data being assigned to the textbox through the Popup.

## Content

### Displaying the Popup and Text Assignment

```csharp
Me.popupControlContainer1.HidePopup(Syncfusion.Windows.Forms.PopupCloseType.Done)
```

At runtime, the Popup will be shown when the user right-clicks on the `RichTextBox`. Type any text and close the Popup by clicking the 'OK' button. You would then see the text being assigned to the `RichTextBox`.

![Figure 389: Pop-up Data Assigned to the textbox through Popup](image.png)

### Figure 389: Data Assigned to the textbox through Popup

#### Frequently Asked Questions

This section discusses the following topics.

##### Creating a Transparent Popup

**3.5.6.1.5.1 How to create a transparent popup?**

This can be done using the below code snippet.

#### Code Examples

```csharp
[C#]
private void popupControlContainer1_BeforePopup(object sender, System.ComponentModel.CancelEventArgs e)
{
    // Get the popupHost which is used to host the popupControlContainer
    // and set the opacity.
    this.popupControlContainer1.PopupHost.Opacity = 0.75;
}
```

```vb
[VB.NET]
Private Sub popupControlContainer1_BeforePopup(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs)
    'Get the popupHost which is used to host the popupControlContainer
End Sub
```

## API Reference

- `popupControlContainer1.HidePopup(Syncfusion.Windows.Forms.PopupCloseType.Done)` - Hides the Popup with the specified close reason.
- `popupControlContainer1.PopupHost.Opacity` - Sets the opacity of the PopupHost.

## Code Examples

### C#

```csharp
private void popupControlContainer1_BeforePopup(object sender, System.ComponentModel.CancelEventArgs e)
{
    this.popupControlContainer1.PopupHost.Opacity = 0.75;
}
```

### VB.NET

```vb
Private Sub popupControlContainer1_BeforePopup(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs)
    popupControlContainer1.PopupHost.Opacity = 0.75
End Sub
```

<!-- tags: [Syncfusion Winforms, EssentialTools, popupControlContainer, RichTextBox, transparentPopup] keywords: [popupControlContainer, RichTextBox, opacity, text assignment, transparent popup] -->
```