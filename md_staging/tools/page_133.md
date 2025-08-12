```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_133.jpeg
document_name: tools
page_number: 133
page_id: tools#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:43:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to dock controls with a tabbed style.
- Provides a runtime example using C# and VB.NET code snippets.
- Highlights the use of the docking manager to tab two docked controls (Panel1 and Panel2).

## Content

### Docking Controls with Tabbed Style

#### Figure 52: Docking a Control with Tabbed Style into Another Control

![Docking controls with tabbed style into another Control](https://i.imgur.com/actual_image_url.png)

### Runtime Example

The below code lets you tab two docked controls (Panel1 and Panel2).

#### Code Example

[C#]

```csharp
this.dockingManager.DockControl(this.Panel1, this.Panel2,
    Syncfusion.Windows.Forms.Tools.DockingStyle.Tabbed, 200, true);
```

[VB.NET]

```vb
Me.dockingManager.DockControl(Me.Panel1, Me.Panel2,
    Syncfusion.Windows.Forms.Tools.DockingStyle.Tabbed, 200, True)
```

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: DockManager
- **Method**: DockControl(Control, Control, DockingStyle, Int32, Boolean)
  - **Parameters**:
    - **Control**: The control to be docked.
    - **Control**: The dock target control.
    - **DockingStyle**: The docking style to use (e.g., Tabbed).
    - **Int32**: The minimum width for the docked control (default is 200).
    - **Boolean**: Indicates whether to show the docking tab (default is true).

### See also:
- For more details on docking styles and controls, refer to the Syncfusion WinForms documentation at:
  [Syncfusion WinForms Documentation](https://www.syncfusion.com/products/windowsforms/documentation)

<!-- tags: [Syncfusion Winforms, DockManager, DockingControls, C#, VB.NET, version] keywords: [dockcontrol, tabbed style, runtime example, documentation, panel1, panel2, Syncfusion.Windows.Forms.Tools.DockingStyle, DockingStyle.Tabbed, minimum width] -->
```