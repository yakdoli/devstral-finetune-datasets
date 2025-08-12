```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_279.jpeg
document_name: edit
page_number: 279
page_id: edit#page_279
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:34Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb.NET
' Handle the WordWrapChanged event.
AddHandler Me.editControl.WordWrapChanged, AddressOf editControl_WordWrapChanged

' Specify the mode of word wrapping.
Me.editControl.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin

Private Sub editControl_WordWrapChanged(ByVal sender As Object, ByVal e As EventArgs)
	' The below line will be displayed in the output window at runtime.
	Console.WriteLine("WordWrapChanged event is raised")
End Sub
```

## API Reference

### WordWrapMode Property

- Type: Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode
- Description: Specifies how to wrap words according to the following ListView properties:
  - WordWrapMargin
  - WordWrapIndent
- Enum Values:
  - WordWrapMode.WordWrapMargin
  - WordWrapMode.WordWrapIndent

### WordWrapChanged Event

- Signature: `Public Event WordWrapChanged As EventHandler`
- Description: Triggered when the word wrapping property of the edit control changes.

## Code Examples

### VB.NET Example

```vb
' Handle the WordWrapChanged event.
AddHandler Me.editControl.WordWrapChanged, AddressOf editControl_WordWrapChanged

' Specify the mode of word wrapping.
Me.editControl.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin

Private Sub editControl_WordWrapChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("WordWrapChanged event is raised")
End Sub
```

### C# Example

```csharp
// Handle the WordWrapChanged event.
editControl.WordWrapChanged += (sender, e) =>
{
    Console.WriteLine("WordWrapChanged event is raised");
};

// Specify the mode of word wrapping.
editControl.WordWrapMode = Syncfusion.Windows.Forms.Edit.Enums.WordWrapMode.WordWrapMargin;
```

## See also

- [EditControl Class](#editcontrol-class)
- [WordWrapMode Enum](#wordwrapmode-enum)
- [Default Properties](#default-properties)

<!-- tags: [product, Windows Forms, WordWrapMode, WordWrapChanged, Syncfusion, control, api, version] keywords: [editcontrol, wordwrapmode, wordwrapchanged, wordwrapmargin, event handler, VB.NET, C#, EditControl, properties, methods, events, api] -->
```