```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_259.jpeg
document_name: tools
page_number: 259
page_id: tools#page_259
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Demonstrates how to interact with DockTabController and DockTabControl in Syncfusion Windows Forms.
- Explains how to retrieve siblings of a control within the same tab.
- Provides code examples in both C# and VB.NET for implementation.

## Code Examples

### C#

```csharp
// If ParentController is DockTabController the control will be in a tab.
if (dhc.ParentController is Syncfusion.Windows.Forms.Tools.DockTabController)
{
    // Getting the DockTabControl from the DockTabController.
    Syncfusion.Windows.Forms.Tools.DockTabControl docktab = 
        (dhc.ParentController as Syncfusion.Windows.Forms.Tools.DockTabController).TabControl;

    // Iterating through the tabpages to get other controls in that tab.
    foreach (DockTabPage tabpage in docktab.TabPages)
    {
        Control siblingcontrol = tabpage.dhcClient.HostControl.Controls[0];
        MessageBox.Show(siblingcontrol.Name);
    }
}
```

### VB.NET

```vb
[VB.NET]

Dim dhost As Syncfusion.Windows.Forms.Tools.DockHost = CType(IIf(TypeOf Me.listBox1.Parent Is Syncfusion.Windows.Forms.Tools.DockHost, Me.listBox1.Parent, Nothing), Syncfusion.Windows.Forms.Tools.DockHost)
Dim dhc As Syncfusion.Windows.Forms.Tools.DockHostController = CType(IIf(TypeOf dhost.InternalController Is Syncfusion.Windows.Forms.Tools.DockHostController, dhost.InternalController, Nothing), Syncfusion.Windows.Forms.Tools.DockHostController)

' If Parentcontroller is DockTabController the control will be in a tab.
If TypeOf dhc.ParentController Is Syncfusion.Windows.Forms.Tools.DockTabController Then

    'Getting the DockTabControl from the DockTabController
    Dim docktab As Syncfusion.Windows.Forms.Tools.DockTabControl = (CType(IIf(TypeOf dhc.ParentController Is Syncfusion.Windows.Forms.Tools.DockTabController, dhc.ParentController, Nothing), Syncfusion.Windows.Forms.Tools.DockTabController)).TabControl

    'Iterating through the tabpages to get other controls in that tab.
    For Each tabpage As DockTabPage In docktab.TabPages
        Dim siblingcontrol As Control = tabpage.dhcClient.HostControl.Controls(0)
    Next

End If
```

## RAG Annotations

<!-- tags: [windowsforms, docktabcontroller, docktabcontrol, controlinteraction, syncfusionwindowsforms, API, 11.4.0.26] keywords: [DockTabController, DockTabControl, ParentController, HostControl, tabpages, MessageBox, ControlName, C#, VB.NET] -->
```