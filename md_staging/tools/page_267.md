```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_267.jpeg
document_name: tools
page_number: 267
page_id: tools#page_267
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to auto hide controls when an application loads.
- Demonstrates finding whether a particular docked control is hidden.
- Provides methods and code examples for managing hidden controls.

## Content

### 3.4.4.7.1 How to auto hide a control when an application loads

A control can be autohidden on loading, by enabling the **AutoHideOnLoad** property through designer or by calling **SetAutoHideOnLoad** method programmatically.

| Method              | Description                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|
| SetAutoHideOnLoad   | AutoHides the docked control when the application loads. The parameters are:                    |
|                     | - **Ctrl** - Indicates the docked control.                                                    |
|                     | - **bautohide** - Value indicating true or false.                                             |

#### Example Code

**[C#]**
```csharp
this.dockingManager1.SetAutoHideOnLoad(this.listBox1, true);
```

**[VB.NET]**
```vb
Me.DockingManager1.SetAutoHideOnLoad(Me.ListBox1, True)
```

### 3.4.4.7.2 How to find whether a particular docked control is hidden or not?

This can be achieved using the **GetHiddenOnLoad** method.

**GetHiddenOnLoad** - This method returns a value which indicates whether the specified control is hidden or not. The docked control should be passed as a parameter.

| Parameter | Description                          |
|-----------|--------------------------------------|
| Ctrl      | Indicates the docked control.       |

#### Example Code

**[C#]**
```csharp
this.dockingManager1.GetHiddenOnLoad(this.listBox1);
Console.Write("Hidden on Load" + this.dockingManager1.GetHiddenOnLoad(this.listBox1));
```

**[VB.NET]**
<!-- No code provided for VB.NET in the input. -->

---

### API Reference

#### SetAutoHideOnLoad
- **Parameters**:
  - **Ctrl** - Indicates the docked control.
  - **bautohide** - Indicates whether the control should be hidden on load.
- **Returns**: None

#### GetHiddenOnLoad
- **Parameters**: **Ctrl** - Indicates the docked control.
- **Returns**: Boolean indicating whether the control is hidden on load.

## Code Examples

### C#
```csharp
this.dockingManager1.SetAutoHideOnLoad(this.listBox1, true);
Console.Write("Hidden on Load: " + this.dockingManager1.GetHiddenOnLoad(this.listBox1));
```

### VB.NET
```vb
Me.DockingManager1.SetAutoHideOnLoad(Me.ListBox1, True)
Console.WriteLine("Hidden on Load: " & Me.DockingManager1.GetHiddenOnLoad(Me.ListBox1))
```

---

### Conclusion
This section provides a straightforward guide on managing the visibility of docked controls in a Windows Forms application, including setting up autohide functionality and checking the hidden status of controls.

## Related Topics

For more information on docked controls and additional functionalities, refer to the related sections in the Syncfusion WinForms documentation.

<!-- tags: [syncfusion, winforms, autohide, control, visibility, docked control, tutorial] keywords: [dockmanager, gethiddenonload, setautohideonload, boolean, hidden, load, application] -->
```