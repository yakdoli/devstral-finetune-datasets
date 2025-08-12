```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_639.jpeg
document_name: tools
page_number: 639
page_id: tools#page_639
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Provides methods to control and display `PopupControlContainer` in a Windows Forms application.
- Instructions on how to set properties and handle events related to `PopupControlContainer`.

## Content

### Setting Opacity for the Popup

The code snippet below demonstrates how to set the opacity of the `PopupControlContainer`.

```csharp
' and set the opacity.
Me.popupControlContainer1.PopupHost.Opacity = 0.75
End Sub
```

### 3.5.6.1.5.2 How to identify whether the popup is currently dropped down

The `PopupControlContainer.IsShowing()` method can be used to determine if the popup is currently displayed.

#### C#

```csharp
this.popupControlContainer1.IsShowing();
```

#### VB.NET

```vb
Me.popupControlContainer1.IsShowing()
```

### 3.5.6.1.5.3 How to show PopupControlContainer as the popup for a RichTextBox control

Displaying the `PopupControlContainer` as the popup for a `RichTextBox` control involves associating the `RichTextBox` control with the `ParentControl` property of `PopupControlContainer`.

1. **Add a RichTextBox control onto the form.**
2. **Associate it with the `ParentControl` property of `PopupControlContainer` as follows.**

#### C#

```csharp
this.popupControlContainer1.ParentControl = this.richTextBox1;
```

#### VB.NET

```vb
Me.popupControlContainer1.ParentControl = Me.richTextBox1
```

3. **To display the Popup at a desired location, handle `RichTextBox.MouseUp` event and call `ShowPopup()` method of `PopupControlContainer` as follows.**

The following code displays the popup just below the `RichTextBox` control when the user clicks.

#### C#

```csharp
this.richTextBox1.MouseUp += new MouseEventHandler(richTextBox1_MouseUp);
private void richTextBox1_MouseUp(object sender, System.Windows.Forms.MouseEventArgs e)
{
    this.popupControlContainer1.ShowPopup(Point.Empty);
}
```

## API Reference

- **Methods**:
  - `IsShowing()`: Returns a boolean indicating whether the popup is currently displayed.
  - `ShowPopup(Point location)`: Displays the popup at the specified location.

## Code Examples

The examples demonstrate how to integrate `PopupControlContainer` with a `RichTextBox` control to dynamically show or hide a popup based on user interaction.

- **Setting up the `ParentControl` property:** Assign the `RichTextBox` control as the `ParentControl` for `PopupControlContainer`.
- **Handling the `MouseUp` event:** Display the popup below the `RichTextBox` when the user clicks.

## Cross References

See also: `PopupControlContainer`, `RichTextBox`, `MouseEventHandler`.

<!-- tags: [WinForms, PopupControlContainer, RichTextBox, MouseUp, IsShowing, ShowPopup] keywords: [opacity, dropped down, parent control, location, event handler] -->
```