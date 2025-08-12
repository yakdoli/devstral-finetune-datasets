```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_067.jpeg
document_name: tools
page_number: 067
page_id: tools#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:14Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the docking functionality of the CommandBar control in Syncfusion WinForms.
- Explains how to control docking using CommandBar and CommandBarController properties.
- Provides examples of setting docking options for different edges of the form.

## Content

### 3.3.3.1.2 Docking CommandBar

CommandBar can be docked to all the edges of the form such as Top, Bottom, Right, and Left. Docking can be controlled by the `CommandBar` and `CommandBarController` properties.

#### Table 6: Docking CommandBar

| CommandBar Property         | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `AllowedDockBorders`        | Gets / sets the edges of the form along which the CommandBar may be docked. The options included are given below.<br><br>- Bottom,<br>- Left,<br>- Right,<br>- Top and<br>- None.<br><br>When set to 'None', the CommandBar cannot be docked to the form. |
| `AlwaysLeadingEdge`         | Indicates whether the CommandBar is always docked to the leading edge. |
| `AlwaysTrailingEdge`        | Indicates whether the CommandBar is always docked to the trailing edge. |
| `DisableDocking`            | Indicates whether the CommandBar is allowed to dock. |
| `DockModeWrapping`         | Wraps the CommandBar when the bounds are less than the maximum length. |

### See Also
- [Docking CommandBar](#docking-commandbar)

## API Reference

### Properties
- **AllowedDockBorders**:
  - **Description**: Gets / sets the edges of the form along which the CommandBar may be docked.
  - **Options**: Bottom, Left, Right, Top, None.
  - **Default**: None
  - **Required**: No
- **AlwaysLeadingEdge**:
  - **Description**: Indicates whether the CommandBar is always docked to the leading edge.
- **AlwaysTrailingEdge**:
  - **Description**: Indicates whether the CommandBar is always docked to the trailing edge.
- **DisableDocking**:
  - **Description**: Indicates whether the CommandBar is allowed to dock.
- **DockModeWrapping**:
  - **Description**: Wraps the CommandBar when the bounds are less than the maximum length.

## Code Examples

### Example: Setting Docking Options in C#
```csharp
// Set Allowed Dock Borders to Top, Bottom, Left, and Right
commandBar.AllowedDockBorders = DockingEdges.Top | DockingEdges.Bottom | DockingEdges.Left | DockingEdges.Right;

// Disable Docking
commandBar.DisableDocking = false;
```

### Example: Enabling Wrapping of Docked CommandBar
```csharp
// Enable wrapping when docked
commandBar.DockModeWrapping = true;
```

<!-- tags: [Syncfusion Winforms, CommandBar, Docking, Event, Version] -->
<!-- keywords: [CommandBar, AllowedDockBorders, AlwaysLeadingEdge, AlwaysTrailingEdge, DisableDocking, DockModeWrapping] -->
```