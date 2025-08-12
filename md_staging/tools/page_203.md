```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_203.jpeg
document_name: tools
page_number: 203
page_id: tools#page_203
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:31:50Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Adds the `DockingManager` to the `Target Providers List`.
- Removes the `DockingManager` from the Target Manager List.
- Demonstrates the `Linked Managers` concept with code examples in C# and VB.NET.
- Handles events during the transfer of `Docking Manager`.

## Content

### Methods

| Method                         | Description                                                                                                                                                                                                 |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AddToTargetManagersList**    | Adds the `DockingManager` to the `Target Providers List`, belonging to the current manager. The parameter is: <br> `dockingmgr` - docking manager to be added to the target list. |
| **RemoveFromTargetManagersList** | Removes the `DockingManager` from the `Target Providers List`, belonging to the current manager. The parameter is: <br> `dockingmgr` - docking manager to be removed from the target list. |

### Example Usage

#### C#

```csharp
// Control from form2 to be transferred to form1 
// dockingManager1 an instance of Form1 and dockingManager2 an instance of Form2
this.dockingManager1.AddToTargetManagersList(dockingManager2);
```

#### VB.NET

```vb
' Control from form2 to be transferred to form1 
' dockingManager1 an instance of Form1 and dockingManager2 an instance of Form2
Me.dockingManager1.AddToTargetManagersList(dockingManager2)
```

### Events during the Transfer of Docking Manager

- If any control comes from other docking manager, **TransferredToManager event** will be handled.
- If a control is transferred out to other docking managers, **TransferredFromManager event** will be handled.

### Sample

A sample which demonstrates the `Linked Managers` concept is available in the below sample installation path.

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Docking Package\LinkedManagers
```

### Page-level Navigation/TOC

- Essential Tools for Windows Forms
  - Methods
  - Example Usage
    - C#
    - VB.NET
  - Events during the Transfer of Docking Manager
  - Sample

## RAG Annotations

<!-- tags: [DockingManager, Target Providers List, Events, TransferredToManager, TransferredFromManager, Linked Managers, C#, VB.NET, sample installation, Tools.Windows] keywords: [DockingManager, Target Providers List, Events, TransferredToManager, TransferredFromManager, Linked Managers, C#, VB.NET, sample installation] -->
```