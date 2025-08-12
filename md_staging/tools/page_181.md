```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_181.jpeg
document_name: tools
page_number: 181
page_id: tools#page_181
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:16:22Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the DockToFill property and its usage in WinForms applications.
- Introduces the FreezeResizing property to prevent resize actions on specific controls.

## Content

### DockToFill Property

The DockToFill property allows a control to fill the entire client area of its container. Below is an example in VB.NET:

```vb
[VB.NET]
Me.dockingManager1.DockToFill = True;
```

**Figure 95: DockToFill Enabled**

![DockToFill Enabled](image_url)

A sample demonstrating the DockToFill property is available in the following sample installation path:
```
..My Documents\Syncfusion\EssentialStudio\Version
Number\Windows\Tools.Windows\Samples\2.0\Docking Package\WindowFill
```

### FreezeResizing

#### Overview
The FreezeResizing property has been implemented for each control, allowing users to freeze any particular control. The property value can also be persisted, and a global FreezeResizing property is available to freeze all controls simultaneously.

#### Usage
The controls can be frozen by calling the `SetFreezeResizing` method. This method freezes the specified control, preventing the user from resizing it.

#### Parameter Description

| Parameter          | Description                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|
| SetFreezeResizing | Freezes the specified control. The parameters are:                                           |
|                    | <br>`Ctrl` - The control for which docking is enabled.                                      |
|                    | <br>`freeze` - Represents a boolean value which determines whether the control is frozen. |

## API Reference (if applicable)

- **SetFreezeResizing Method**:
  - **Parameters**:
    - `Ctrl` - The control for which docking is enabled.
    - `freeze` - A boolean value representing whether the control is frozen.

## Code Examples (multi-language supported)

```vb
Me.dockingManager1.DockToFill = True;
```

## Cross References

- See also: Docking Package samples, Control freezing mechanisms.

<!-- tags: [syncfusion-sdk, winforms, docking, freezing, controls] keywords: [DockToFill, FreezeResizing, resizing, control freezing, controls, WinForms, Syncfusion, version, VB.NET] -->
```