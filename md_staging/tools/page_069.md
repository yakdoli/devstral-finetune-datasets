```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: tools
page_number: 069
page_id: tools#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:43Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Code Examples

```csharp
this.commandBar1.DisableDocking = true;
this.commandBar1.ShowDockModeText = false;
this.commandBar1.DockState = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Top;
this.commandBar1.DockModeWrapping = true;

this.commandBarController1.EnabledDockBorders =
    (Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Top) (((Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Bottom |
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Left) |
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Right));
```

```vb
Me.commandBar1.AllowedDockBorders =
    (CType(((Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Top Or
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Bottom) Or
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Left), 
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder))

Me.commandBar1.AlwaysLeadingEdge=True
Me.commandBar1.AlwaysTrailingEdge = True
Me.commandBar1.DisableDocking=True
Me.commandBar1.ShowDockModeText = False
Me.commandBar1.DockState =
    Syncfusion.Windows.Forms.Tools.CommandBarDockState.Top
Me.commandBar1.DockModeWrapping = True

Me.commandBarController1.EnabledDockBorders =
    (CType(((Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Bottom Or
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Left) Or
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder.Right), 
    Syncfusion.Windows.Forms.Tools.CommandBarDockBorder))
```

### Explanation

The following figure illustrates the above settings.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, CommandBar, Docking, StateWrapping, DockBorders] keywords: [DisableDocking, ShowDockModeText, DockState, DockModeWrapping, EnabledDockBorders, commandBar1, commandBarController1] -->
```