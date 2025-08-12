```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_318.jpeg
document_name: tools
page_number: 318
page_id: tools#page_318
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Implementing the IEditControlsEmbed interface in a RichTextBox class to enable AutoComplete functionality.
- Integrating the AutoComplete control with the RichTextBox control in a form.

## Content

### Implementing the IEditControlsEmbed Interface in a RichTextBox Class

To enable AutoComplete functionality for the RichTextBox control, implement the IEditControlsEmbed interface in a custom RichTextBox class.

#### C#

```csharp
public class MyRichTextBox : System.Windows.Forms.RichTextBox, IEditControlsEmbed
{
    // Returns the active RichTextBox control.
    public Control GetActiveEditControl(IEditControlsEmbedListener listener)
    {
        return (Control)this;
    }
}
```

#### VB.NET

```vb
Public Class MyRichTextBox Inherits System.Windows.Forms.RichTextBox Implements IEditControlsEmbed

    ' Returns the active RichTextBox control.
    Public Function GetActiveEditControl(ByVal listener As IEditControlsEmbedListener) As Control
        Return CType(Me, Control)
    End Function

End Class
```

### Drag and Drop the RichTextBox Control and AutoComplete Control to a Form

To integrate the RichTextBox control with the AutoComplete functionality, drag and drop both controls to a form and initialize them.

#### C#

```csharp
// Initialization
Syncfusion.Windows.Forms.Tools.AutoComplete autoComplete1 = new Syncfusion.Windows.Forms.Tools.AutoComplete();
MyRichTextBox richTextBox1 = new MyRichTextBox();
```

#### VB.NET

```vb
' Initialization
Dim autoComplete1 As Syncfusion.Windows.Forms.Tools.AutoComplete = New Syncfusion.Windows.Forms.Tools.AutoComplete()
Dim richTextBox1 As MyRichTextBox = New MyRichTextBox()
```

## Page-level Navigation/TOC (if applicable)

- [Introduction](#introduction)
- [Implementing the IEditControlsEmbed Interface](#implementing-the-ieditcontrolsembed-interface)
- [Integrating AutoComplete with RichTextBox](#integrating-autocomplete-with-richtextbox)

## Cross References

- Refer to the [AutoComplete documentation](#autocompletedocumentation) for more details on configuring AutoComplete for RichTextBox controls.

<!-- tags: [Syncfusion, WinForms, AutoComplete, RichTextBox, IEditControlsEmbed] keywords: [AutoComplete, RichTextBox, IEditControlsEmbed, initialization, integration,拖放控件, WinForms, Windows Forms] -->
```