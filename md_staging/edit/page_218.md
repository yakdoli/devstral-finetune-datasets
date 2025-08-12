```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_218.jpeg
document_name: edit
page_number: 218
page_id: edit#page_218
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:24Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

You can set any desired background to a particular line or block of selection, as explained below.

## Setting Background Colors

- **Register a backcolor format** with the Edit Control by using its `RegisterBackcolorFormat` method, with appropriate values for `BackgroundColor`, `ForegroundColor`, and `HatchStyle` parameters.
  
- **Set the background color** to the entire line or just the selected text by using the `SetLineBackColor` and `SetSelectionBackColor` methods respectively.

### Code Examples

#### C#
```csharp
[C#]

// Register a backcolor format with EditControl.
this.editControl.RegisterBackcolorFormat(Color.Aquamarine, Color.Beige, 
System.Drawing.Drawing2D.HatchStyle.Cross, true);

// Set the background for the entire line of text.
this.editControl.SetLineBackColor(editControl.CurrentLine, true, format);

// Set the background for the selected block of text.
this.editControl.SetSelectionBackColor(format);
```

#### VB.NET
```vb
[VB.NET]

' Register a backcolor format with EditControl.
Me.editControl.RegisterBackcolorFormat(Color.Aquamarine, Color.Beige, 
System.Drawing.Drawing2D.HatchStyle.Cross, True)

' Set the background for the entire line of text.
Me.editControl.SetLineBackColor(editControl.CurrentLine, True, format)

' Set the background for the selected block of text.
Me.editControl.SetSelectionBackColor(format)
```

<!-- tags: [Syncfusion, WinForms, EditControl, BackgroundColor, SelectionBackgroundColor, Version11.4.0.26] keywords: [Essential Edit, Windows Forms, Background Color, SetLineBackColor, SetSelectionBackColor, RegisterBackcolorFormat, HatchStyle] -->
```