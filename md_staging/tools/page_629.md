```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_629.jpeg
document_name: tools
page_number: 629
page_id: tools#page_629
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to control the behavior of a `PopupControlContainer`.
- Explains implementing the `IPopupParent` interface for more advanced control over popups.
- Guides on enabling key navigation within a pop-up.

## Content

### Hiding a PopupControlContainer

```csharp
Private Sub button1_Click(sender As Object, e As EventArgs)
    'Hides the PopupControlContainer under a button click.
    If Not txtbox.Text = "" Then
        this.popupControlContainer1.HidePopup(PopupCloseTypes.Done)
    End Sub
```

If you want more control over this behavior, then you will have to implement the `IPopupParent` interface and set the `PopupParent` property in the `PopupControlContainer`.

A sample which illustrates the `IPopupParent` interface is available in the below sample installation location.

```
.\My Documents\Syncfusion\EssentialStudio\<Version Number>\Windows\Tools.Windows\Samples\2.0\Editors Package\Container controls\PopupContainer\PopupsInDepth
```

#### Figure 386: Custom Popup using IPopupParent

![Custom Popup using IPopupParent](image.png)

### Key navigation

When the pop-up is visible, the `PopupControlContainer` will look for Alt, Enter, Tab, Esc, F4, and F2 keys and either cancel or close the pop-up. In order to navigate, the `PopupControlContainer`'s `IgnoreDialogKey` property must be set to `true`.

#### Code Examples

```csharp
this.popupControlContainer1.IgnoreDialogKey = true;
```

```vb
Me.popupControlContainer1.IgnoreDialogKey = True
```

## Cross References

See also: detailed sections on `IPopupParent`, `PopupControlContainer`, and `Key navigation`.

<!-- tags: [tools, windows forms, popupcontrolcontainer, ipopupparent, keynavigation, version 11.4.0.26] keywords: [popup, ipopupparent, ignoredialogkey, windows forms, syncfusion] -->
```
