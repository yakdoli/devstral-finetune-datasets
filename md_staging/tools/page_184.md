```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_184.jpeg
document_name: tools
page_number: 184
page_id: tools#page_184
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:16:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the declaration, initialization, and properties configuration of a `DockingClientPanel` control in C# and VB.NET.
- Includes steps to add the control to the form and handle layout management.

## Content

### C#

```csharp
// Declaration and initialization
private Syncfusion.Windows.Forms.Tools.DockingClientPanel dockingClientPanel1;
this.dockingClientPanel1 = new Syncfusion.Windows.Forms.Tools.DockingClientPanel();
this.dockingClientPanel1.SuspendLayout();

// Add a control to dockingclientpanel
this.dockingClientPanel1.Controls.Add(this.tabControlAdv1);

// Set the properties
this.dockingClientPanel1.Location = new System.Drawing.Point(0, 133);
this.dockingClientPanel1.Name = "dockingClientPanel1";
this.dockingClientPanel1.Size = new System.Drawing.Size(600, 369);
this.dockingClientPanel1.SizeType = true;
this.dockingClientPanel1.TabIndex = 0;
this.dockingClientPanel1.Paint += new System.Windows.Forms.PaintEventHandler(this.DockingClientPanel1_Paint);
this.DockingClientPanel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;

// Add the control to the form
this.Controls.Add(this.dockingClientPanel1);
this.dockingClientPanel1.ResumeLayout(false);
```

### VB.NET

```vb
' Declaration and initialization
Private dockingClientPanel1 As Syncfusion.Windows.Forms.Tools.DockingClientPanel
Me.dockingClientPanel1 = New Syncfusion.Windows.Forms.Tools.DockingClientPanel()
Me.dockingClientPanel1.SuspendLayout()

' Add a control to dockingclientpanel
Me.dockingClientPanel1.Controls.AddRange(New System.Windows.Forms.Control() {Me.tabControlAdv1})

' Set the properties
Me.dockingClientPanel1.AutoScroll = True
Me.dockingClientPanel1.Location = New System.Drawing.Point(106, 0)
Me.dockingClientPanel1.Name = "dockingClientPanel1"
Me.dockingClientPanel1.Size = New System.Drawing.Size(452, 417)
Me.dockingClientPanel1.SizeType = True
Me.DockingClientPanel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D

' Add the control to the form
Me.Controls.AddRange(New System.Windows.Forms.Control() {Me.dockingClientPanel1})
Me.dockingClientPanel1.ResumeLayout(False)
```

## Page-level Navigation/TOC (if applicable)
- This content details the configuration of the `DockingClientPanel` control for use in Syncfusion WinForms.

## Cross References
- See also: Properties of `DockingClientPanel`, Layout management in Windows Forms.

<!-- tags: [WinForms, DockingClientPanel, Control Initialization, Layout Management] keywords: [DockingClientPanel, SuspendLayout, ResumeLayout, Control.Add, Properties] -->
```