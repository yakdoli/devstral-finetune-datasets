```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_115.jpeg
document_name: tools
page_number: 115
page_id: tools#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:31:16Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Determines the new width of the toolbar and applies wrapping algorithms based on the CommandBar's state.
- Handles resizing of the CommandBar and its parent panels dynamically.
- Ensures consistent layout and behavior when the CommandBar is floating or docked.

## Content

### Toolbar Wrapping Implementation

```csharp
if (nnewwidth > szmaxwrap.Width)
{
    // Assign the new width to the toolbar parent panel and get the corresponding
    // toolbar height.
    sznew.Width = nnewwidth;
    toolbar.Parent.Width = sznew.Width;
    sznew.Height = toolbar.Height;
    toolbar.Parent.Width = sztemp.Width;
}
else
{
    sznew = szmaxwrap;
}

// Set the CommandBar's client size to be equal to this new size.
arg.ClientSize = sznew;
}
else if (ffactor <= 1)
{
    arg.ClientSize = szminwrap;
}
else
{
    arg.ClientSize = toolbar.Size;
}
}
}
```

### VB.NET Implementation

```vb
Private Sub commandBarAlign_CommandBarWrapping(ByVal obj As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.CommandBarWrappingEventArgs)
    ' Apply the wrapping algorithm only when the CommandBar is floating.
    If Me.commandBarAlign.DockState = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Float Then
        Dim szmaxwrap As New Size(40, 67)
        Dim szminwrap As New Size(72, 23)
        Me.DoToolBarWrapping(Me.tbAlign, szmaxwrap, szminwrap, arg)
    ElseIf (Me.commandBarAlign.DockState = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Left) OrElse (Me.commandBarAlign.DockState = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Right) Then
        Dim szmaxwrap As New Size(24, 67)
        arg.ClientSize = szmaxwrap
    End If
End Sub
```

<!-- tags: [syncfusion, winforms, commandbar, toolswrapping, alignment, toolbar] keywords: [CommandBarWrapping, DockState, ClientSize, DoToolBarWrapping, szmaxwrap, szminwrap, toolbar alignment, floating toolbar, docked toolbar] -->
```