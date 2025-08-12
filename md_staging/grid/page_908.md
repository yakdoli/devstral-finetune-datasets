```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_908.jpeg
document_name: grid
page_number: 908
page_id: grid#page_908
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:45Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Illustrates handling the `FieldChooserShowing`, `FieldChooserShown`, and `FieldChooserClosing` events in the Syncfusion Grid control.
- Demonstrates setting and retrieving the caption name of the FieldChooser dialog.
- Includes examples in both C# and VB.NET.

## Content

### Handling the `FieldChooserShowing` Event
The following code example illustrates handling the `FieldChooserShowing` event. It is used to set the caption name of the FieldChooser dialog and cancel showing the dialog box.

```vb
[VB.NET]

' FieldChooserShowing Event
Private Sub GroupingControl_FieldChooserShowing(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Grid.FieldChooserShowingEventArgs)
    e.Caption = "Syncfusion"
    e.Cancel = True
End Sub
```

### Handling the `FieldChooserShown` Event
The following code example illustrates handling the `FieldChooserShown` event. It is used to get the caption name of the FieldChooser dialog after showing the dialog box.

#### C# Example
```csharp
[C#]
// FieldChooserShown Event
void gridGroupingControl1_FieldChooserShown(object sender, FieldChooserShownEventArgs e)
{
	string captionName = e.Caption;
	Console.WriteLine(captionName);
}
```

#### VB.NET Example
```vb
[VB.NET]
' FieldChooserShown Event
Private Sub GroupingControl_FieldChooserShown(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Grid.FieldChooserShownEventArgs)
	Dim captionName As String = e.Caption
	Console.WriteLine(captionName)
End Sub
```

### Handling the `FieldChooserClosing` Event
The following code example illustrates handling the `FieldChooserClosing` event. Here it is used to change the caption name of the FieldChooser dialog and cancel closing it.

#### C# Example
```csharp
[C#]
// FieldChooserClosing Event
void gridGroupingControl1_FieldChooserClosing(object sender,
```

## API Reference

This section details the events and their parameters for the FieldChooser control in the Syncfusion Grid:

- **FieldChooserShowing Event**
  - Parameters:
    - `sender`: The object that raised the event.
    - `e`: The event arguments containing:
      - `Caption`: The caption of the FieldChooser dialog.
      - `Cancel`: A boolean to cancel the showing of the dialog.

- **FieldChooserShown Event**
  - Parameters:
    - `sender`: The object that raised the event.
    - `e`: The event arguments containing:
      - `Caption`: The caption of the FieldChooser dialog.

- **FieldChooserClosing Event**
  - Parameters:
    - `sender`: The object that raised the event.
    - `e`: The event arguments containing:
      - `Caption`: The caption of the FieldChooser dialog.
      - `Cancel`: A boolean to cancel the closing of the dialog.

## Code Examples

The provided examples demonstrate how to:
1. Customize the caption of the FieldChooser dialog.
2. Retrieve and display the caption of the FieldChooser dialog after it is shown.
3. Change the caption and cancel the closing of the FieldChooser dialog.

<!-- tags: [Syncfusion Winforms, Grid, FieldChooser, Events] keywords: [FieldChooserShowing, FieldChooserShown, FieldChooserClosing, Caption, C#, VB.NET] -->
```