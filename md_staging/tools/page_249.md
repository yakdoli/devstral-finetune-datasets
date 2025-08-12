```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_249.jpeg
document_name: tools
page_number: 249
page_id: tools#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:00:53Z
fidelity: lossless
-->

## Overview
- Explains how to get or set the dock ability of controls in Windows Forms.
- Demonstrates methods to get or set the size of docked controls.
- Includes C# code examples for getting and setting control sizes.

## Content

### Getting the Dock Ability
```vb
'Getting the Dock Ability
Me.dockingManager1.GetDockAbility(Me.panel2)
```

### Setting the Dock Ability
```vb
'Setting the Dock Ability
Me.dockingManager1.SetDockAbility(Me.panel2, "Bottom, Horizontal")
```

### How to get or set the size of the docked control?

The below methods let you get or set the size of the control.

| **Methods**       | **Description**                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| GetControlSize    | Gets the size of the docked or the floating control, by passing the control as a parameter to this method. The parameters are,<br>`Ctrl` - Indicates the docking window. |
| SetControlSize    | Sets the new size (width, Height) for the docked or the floating control, by passing the control as a parameter to this method. The default value of size is Empty. The parameters are,<br>`Ctrl` - Indicates the docking window.<br>`Size` - Specifies the new size for the control. |

### C# Examples

```csharp
//Get the size of docked or Floating control using the GetControlSize method
this.dockingManager1.GetControlSize(this.panel2);
Console.Write("Size" +
this.dockingManager1.GetControlSize(this.panel2));

//Set the size of docked or Floating control using the GetControlSize method
this.dockingManager1.SetControlSize(this.panel1, new Size(100, 50));
```

## API Reference

### Methods
| **Name**           | **Description**                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| GetControlSize    | Gets the size of the docked or the floating control, by passing the control as a parameter to this method. |
| SetControlSize    | Sets the size of the docked or the floating control, by passing the control as a parameter to this method.  |

## Code Examples

### Getting the Size of a Docked or Floating Control
```csharp
this.dockingManager1.GetControlSize(this.panel2);
Console.Write("Size" +
this.dockingManager1.GetControlSize(this.panel2));
```

### Setting the Size of a Docked or Floating Control
```csharp
this.dockingManager1.SetControlSize(this.panel1, new Size(100, 50));
```

<!-- tags: [product, module, control, api, version?] keywords: [Dock Ability, Control Size, Windows Forms, C#, GetControlSize, SetControlSize] -->
```