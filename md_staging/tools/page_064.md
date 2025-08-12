```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: tools
page_number: 064
page_id: tools#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to manage and configure command bars in Windows Forms using Syncfusion.
- Explains adding a detached command bar both programmatically and through design-time verbs.

## Content

### Programmatically Adding a Detached CommandBar

The following code demonstrates how to programmatically add a detached command bar to a `MainFrameBarManager`.

#### Code Example: C#

```csharp
this.commandBar1.Text = "commandBar1";
```

#### Code Example: VB.NET

```vbnet
' Declare the controls.
Private mainFrameBarManager2 As Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager
Private commandBar2 As Syncfusion.Windows.Forms.Tools.CommandBar

' Initialize the controls.
Me.mainFrameBarManager2 = New Syncfusion.Windows.Forms.Tools.XPMenus.MainFrameBarManager(Me)
Me.commandBar2 = New Syncfusion.Windows.Forms.Tools.CommandBar()

' Set the properties.
Me.mainFrameBarManager2.DetachedCommandBars.Add(Me.commandBar2)
Me.mainFrameBarManager2.Form = Me
Me.commandBar1.Text = "commandBar1"
```

### Adding a Detached CommandBar Through Design-Time Verbs

The following image illustrates the process of adding a detached command bar using design-time verbs.

![Figure 14: Adding Detached CommandBar Through Design Time Verb](https://example.com/image_url)

### Figure 14: Adding Detached CommandBar Through Design Time Verb

This figure shows the context menu for `MainFrameBarManager`, with the option to "Add Detached CommandBar" highlighted.

## See also:
- [Syncfusion WinForms Documentation](https://www.syncfusion.com/products/windowsforms/documentation)
- [MainFrameBarManager](https://www.syncfusion.com/documentation/windowsforms/mainframebarmanager)
- [CommandBar](https://www.syncfusion.com/documentation/windowsforms/commandbar)

<!-- tags: [syncfusion, winforms, mainframebarmanager, commandbar, detachedcommandbar] keywords: [windows forms, command bar, design time, programmatically, mainframebarmanager,_syncfusion windows forms, tools, detached, verb, add, context menu] -->
```
