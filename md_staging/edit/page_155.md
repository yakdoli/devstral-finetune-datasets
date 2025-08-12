```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: edit
page_number: 155
page_id: edit#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:23Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
Me.editControl1.ContextMenuManager.ContextMenuProvider
End Sub 'cm_FillMenu
```

Calling the in-built dialogs.
```vb
Sub ShowFindDialog(ByVal sender As Object, ByVal e As EventArgs)
    Me.editControl1.FindDialog()
End Sub

Sub ShowReplaceDialog(ByVal sender As Object, ByVal e As EventArgs)
    Me.editControl1.ReplaceDialog()
End Sub

Sub ShowGoToDialog(ByVal sender As Object, ByVal e As EventArgs)
    Me.editControl1.GoToDialog()
End Sub
```

![Customized Find, Replace and Goto Menu Items in Context Menu](https://example.com/path/to/image.png)
*Figure 54: Customized Find, Replace and Goto Menu Items in Context Menu*  

## Assembly Dependency

If the Syncfusion.Tools.Windows assembly is loaded before the instantiation of the context menu, then an XPMenus.PopupMenu is displayed as the context menu. Otherwise, a standard .NET context menu is shown.

**Note:** You must have reference to the `Syncfusion.Tools.Windows` assembly in your project.

A sample demonstrating the Context Menu feature is available in the following sample installation path.

```
.. \ My Documents \ Syncfusion \ EssentialStudio \ Version Number \ Windows \ Edit.Windows \ Samples \ 2.0 \ Advanced Editor Functions \ ContextMenuDemo
```

## API Reference
<!-- tags: [Essential Edit, Windows Forms, ContextMenuDemo, Syncfusion.Tools.Windows] keywords: [Syncfusion, Windows Forms, Context Menu, Sample Installation, Advanced Editor, Find, Replace, Goto ] -->
``` 
```