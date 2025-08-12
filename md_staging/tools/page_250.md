```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_250.jpeg
document_name: tools
page_number: 250
page_id: tools#page_250
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:41Z
fidelity: lossless
-->

## Overview

- Demonstrates how to retrieve and set the size of docked or floating controls using the `GetControlSize` and `SetControlSize` methods.
- Explains how to check the docking status of a control (e.g., whether it is floating or docked).
- Provides steps to enable and retrieve the docking properties of a control, such as a `listview`, using the `DockHost` and `DockHostController`.

## Essential Tools for Windows Forms

### Code to Get and Set Control Size

```vb
' Get the size of docked or Floating control using the GetControlSize method
Me.dockingManager1.GetControlSize(Me.panel2)
Console.Write("Size" + Me.dockingManager1.GetControlSize(Me.panel2))

' Set the size of docked or Floating control using the GetControlSize method
this.dockingManager1.SetControlSize(this.panel1, new Size(100, 50));
```

### How to Get the Individual Docked Control's Properties?

#### Section 3.4.4.1.8: How to Get the Individual Docked control's Properties?

To check whether a control (in this case, it's a `listbox`) is floating or docked, you could use the following code snippet:

#### C#

```csharp
this.dockingManager1.IsFloating(this.listBox1);
```

#### VB.NET

```vb
Me.dockingManager1.IsFloating(this.listBox1);
```

### To get the Dock location

1. Add a listview and a docking manager in your form.
2.
3. Enable the listview as a docked control.

#### C#

```csharp
this.dockingManager1.SetEnableDocking(this.listView1, true);
```

#### VB.NET

```vb
Me.dockingManager1.SetEnableDocking(Me.listView1, True)
```

4. Now add the below given code in your form's constructor.

```csharp
[//inline code below]
```

```csharp
// listView1 is the dockable control. We could get it's dock properties
// by accessing DockHost and DockHostController.
```

## Page-level Navigation/TOC

- [3.4.4.1.8 How to Get the Individual Docked control's Properties?](#3.4.4.1.8-how-to-get-the-individual-docked-controls-properties)

## Cross References

See also:
- DockManager properties and methods
- DockHost and DockHostController

## RAG Annotations

<!-- tags: [DockManager, DockHost, DockHostController, GetControlSize, SetControlSize, IsFloating, Windows Forms, C#, VB.NET] keywords: [Docked control, Floating control, Control size, Dock location, listView, listbox, form constructor] -->
```