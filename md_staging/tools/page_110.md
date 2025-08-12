```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: tools
page_number: 110
page_id: tools#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:28:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
(newborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Top) 
    OrElse (newborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Bottom) 
        OrElse (newborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Float) 
            OrElse (newborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.None))  Then
    Me.commandBarFonts.MaxLength = Me.commandBarFonts.CalcCommandBarMaxLength(Me.szFontCommandBarPanelSize.Width)
    ' Move the fonts toolbar panel to its original position ie., after the two combo boxes.
    Me.pnlFontsTB.Location = New Point(Me.fontSizeComboBox.Right + 6, 0)
    Me.fontComboBox.Visible = True
    Me.fontSizeComboBox.Visible = True
End If
End Sub
```

## 3.3.3.10.3 CommandBarStateChanged Event

This event is raised after a CommandBar's dock / float state changes.  

The event handler receives an argument of type `EventArgs` containing data related to this event.

```csharp
[C#]

// Handler for the CommandBar.CommandBarStateChanged event.
private void cbFonts_CommandBarStateChanged(object sender, System.EventArgs e)
{
    // The Fonts CommandBar client dimensions may have been changed by the redocking.
    // Size the panel containing the Fonts toolbar to fit the new CommandBar panel dimensions.
    if (((this.commandBarFonts.DockState == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Left) || 
         (this.commandBarFonts.DockState == Syncfusion.Windows.Forms.Tools.CommandBarDockState.Right)) &&
         (this.pnlFontsTB.Width > this.commandBarFonts.Width))
    {
        this.pnlFontsTB.Size = this.pnlFonts.Size;
    }
    else
    {
        // The CommandBar has been moved out of a left / right dock position.
        if (this.pnlFontsTB.Height > this.commandBarFonts.Height)
        {
            this.pnlFontsTB.Size = this.szFontToolBarPanel;
        }
    }
}
```

## API Reference  

None in this section.

## Code Examples  
See the code snippets above for handling the `CommandBarStateChanged` event.

<!-- tags: [syncfusion, windows forms, commandbar, eventHandling, version-11.4.0.26] keywords: [commandbar, commandbarstatechanged, docking, floating state, toolbar, FontsCommandBar, Syncfusion Windows Forms] -->
```