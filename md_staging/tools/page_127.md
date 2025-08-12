```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: tools
page_number: 127
page_id: tools#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:39:49Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to add necessary namespaces for Syncfusion Windows Forms Tools.
- Demonstrates creating and initializing the Docking Manager and two listbox controls.
- Guides on setting properties of the DockingManager, such as VisualStyle.

## Content

### Step 1: Add the Below Namespace
#### C#
```csharp
// namespaces
using Syncfusion.Windows.Forms.Tools;
using Syncfusion.Windows.Forms;
```

#### VB.NET
```vb
' namespaces
Imports Syncfusion.Windows.Forms
Imports Syncfusion.Windows.Forms.Tools
```

### Step 2: Create and Initialize the Docking Manager and Two Listbox Controls
#### C#
```csharp
// Create the DockingManager instance and add it the component list.
private Syncfusion.Windows.Forms.Tools.DockingManager dockingManager;
private System.Windows.Forms.ListBox listBox1;
private System.Windows.Forms.ListBox listBox2;

this.dockingManager = new
Syncfusion.Windows.Forms.Tools.DockingManager(this.components);
this.listBox1 = new System.Windows.Forms.ListBox();
this.listBox2 = new System.Windows.Forms.CheckedListBox();
```

#### VB.NET
```vb
' Create the DockingManager instance and add it the component list.
Private Syncfusion.Windows.Forms.Tools.DockingManager dockingManager;
Private System.Windows.Forms.ListBox listBox1;
Private System.Windows.Forms.ListBox listBox2;

Me.dockingManager = New
Syncfusion.Windows.Forms.Tools.DockingManager(Me.components)
Me.dockingManager.BeginInit()
Me.listBox1 = New System.Windows.Forms.ListBox()
Me.listBox2 = New System.Windows.Forms.ListBox()
```

### Step 3: Set Some Properties of the DockingManager
Set some properties of the DockingManager. Ex `VisualStyle` to "Office2003".

---

<!-- tags: [syncfusion, windows forms, tools, controls, namespaces, docking manager, listbox] keywords: [DockingManager, ListBox, VisualStyle, Syncfusion.Windows.Forms.Tools, namespace, initialization, Office2003] -->
```