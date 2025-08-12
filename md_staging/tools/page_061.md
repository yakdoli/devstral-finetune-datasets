```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: tools
page_number: 061
page_id: tools#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Implements a basic configuration of the CommandBar Controller using Syncfusion's CommandBar tool in both C# and VB.NET.
- Covers creating and initializing the CommandBar and its controller along with setting the host form for the CommandBar.

## Content

### Creating and Initializing CommandBar Components

#### C#
```csharp
commandBarController1;
private Syncfusion.Windows.Forms.Tools.CommandBar commandBar1;
private System.Windows.Forms.Panel panel1;

this.commandBarController1 = new Syncfusion.Windows.Forms.Tools.CommandBarController();
((System.ComponentModel.ISupportInitialize)(this.commandBarController1)).BeginInit();
this.commandBar1 = new Syncfusion.Windows.Forms.Tools.CommandBar();
this.panel1 = new System.Windows.Forms.Panel();
```

#### VB.NET
```vbnet
[VB.NET]

Private commandBarController1 As Syncfusion.Windows.Forms.Tools.CommandBarController
Private commandBar1 As Syncfusion.Windows.Forms.Tools.CommandBar
Private panel1 As System.Windows.Forms.Panel

Me.commandBarController1 = New Syncfusion.Windows.Forms.Tools.CommandBarController()
CType(Me.commandBarController1, System.ComponentModel.ISupportInitialize).BeginInit()
Me.commandBar1 = New Syncfusion.Windows.Forms.Tools.CommandBar()
Me.panel1 = New System.Windows.Forms.Panel()
```

### Setting the Host Form for the CommandBar

#### Step 4: Set the form as the host for all CommandBars using the CommandBarController's `HostForm` property.

#### C#
```csharp
// Set the CommandBarController.HostForm property.
this.commandBarController1.HostForm = this;
```

#### VB.NET
```vbnet
' Set the CommandBarController.HostForm property.
Me.commandBarController1.HostForm = Me
```

### Adding a Client Control to the CommandBar

#### Step 5: Assign a client control to the CommandBar by adding it to the CommandBar's `Controls` collection property.

#### C#
```csharp
// Add the panel control containing the toolbar to the CommandBar.
this.commandBar1.Controls.AddRange(new System.Windows.Forms.Control[] {this.panel1});
```

## API Reference

### Namespaces and Types
- **Syncfusion.Windows.Forms.Tools.CommandBarController**
- **Syncfusion.Windows.Forms.Tools.CommandBar**
- **System.Windows.Forms.Panel**
- **System.ComponentModel.ISupportInitialize**

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.Tools;
using System;

public class Form1 : Form
{
    private CommandBarController commandBarController1;
    private CommandBar commandBar1;
    private Panel panel1;

    public Form1()
    {
        commandBarController1 = new CommandBarController();
        ((ISupportInitialize)(commandBarController1)).BeginInit();
        commandBar1 = new CommandBar();
        panel1 = new Panel();
        commandBarController1.HostForm = this;
        commandBar1.Controls.AddRange(new Control[] { panel1 });
    }
}
```

### VB.NET Example

```vbnet
Imports Syncfusion.Windows.Forms.Tools
Imports System

Public Class Form1 : Inherits Form
    Private commandBarController1 As CommandBarController
    Private commandBar1 As CommandBar
    Private panel1 As Panel

    Public Sub New()
        commandBarController1 = New CommandBarController()
        CType(commandBarController1, ISupportInitialize).BeginInit()
        commandBar1 = New CommandBar()
        panel1 = New Panel()
        commandBarController1.HostForm = Me
        commandBar1.Controls.AddRange(New Control() { panel1 })
    End Sub
End Class
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, CommandBar, CommandBarController, HostForm, Controls, C#, VB.NET] keywords: [CommandBar, CommandBarController, HostForm, Controls, C# example, VB.NET example, initialize, assign, client control, add range, Panel, Form] -->
```