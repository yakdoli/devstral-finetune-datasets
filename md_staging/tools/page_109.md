```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_109.jpeg
document_name: tools
page_number: 109
page_id: tools#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:27:06Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```csharp
this.fontComboBox.Visible = true;
this.fontSizeComboBox.Visible = true;
}
}
```

### [VB.NET]

```vbnet
' Handler for the CommandBar.CommandBarStateChanging event.
Private Sub cbFonts_CommandBarStateChanging(ByVal obj As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.CommandBarStateChangingEventArgs)
' If the fonts CommandBar is being docked to a vertical dock position, ie., left or right,
' then hide the two combo boxes and set the commandbar max length to be equal to
' the length of the fonts toolbar.
' NOTE - The CommandBar's dockstate will be set to CommandBarDockState.None when the CommandBar
' is in an indeterminate state. This happens only during loading and deserialization.
Dim currentborder As Syncfusion.Windows.Forms.Tools.CommandBarDockState = Me.commandBarFonts.DockState
Dim newborder As Syncfusion.Windows.Forms.Tools.CommandBarDockState = arg.NewDockState
If ((currentborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Top) OrElse 
(currentborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Bottom) OrElse 
(currentborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Float) OrElse 
(currentborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.None)) AndAlso 
((newborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Left) OrElse 
(newborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Right)) Then
Me.fontComboBox.Visible = False
Me.fontSizeComboBox.Visible = False
Me.commandBarFonts.MaxLength = Me.commandBarFonts.CalcCommandBarMaxLength(Me.szFontToolBarPanel.Width)
' Move the panel containing the fonts toolbar to the (0,0) position of the commandbar panel.
Me.pnlFontsTB.Location = New Point(0, 0)
End If
' If the Fonts CommandBar is being redocked / floated from the left or right borders, then
' increase the max length and restore combo box visibility.
If ((currentborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Left) OrElse 
(currentborder = Syncfusion.Windows.Forms.Tools.CommandBarDockState.Right)) AndAlso 
```

## Footer Information
© 2013 Syncfusion. All rights reserved. 109 | Page
``` 

<!-- tags: [windows-forms, commandbar, essential-tools, dockstate, visibility] keywords: [fonts, fontsize, combo-box, commandbarredocking, max-length, positioning, indeterminate-state] -->
```