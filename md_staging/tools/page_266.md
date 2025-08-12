```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_266.jpeg
document_name: tools
page_number: 266
page_id: tools#page_266
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:03:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- 1-3 bullets summarizing the page scope using only visible text.

## Content

### 3.4.4.7 Hiding Controls

This section discusses how to enable a control to be a float-only control in the context of Windows Forms. The key points are as follows:

#### SetFloatOnly

Make the docked control a float-only control.

- **Ctrl**: The control for which docking is enabled.
- **bFloating**: Represents a boolean value, TRUE, to disable docking.

#### Code Examples

##### C#

```csharp
this.dockingManager1.SetFloatOnly(this.listBox2, true);
```

##### VB.NET

```vb
Me.dockingManager1.SetFloatOnly(Me.listBox2, True)
```

#### Visual Representation

**Figure 110: Float Only Enabled**

![](https://i.imgur.com/cartoon.png)

Figure 110 depicts a scenario where floating controls have been enabled, demonstrating the effect of the `SetFloatOnly` method on the `listBox2` control.

### Hiding Controls

This section covers the following topics:

#### API Reference

##### Parameters

- Ctrl: The program control for which docking features are enabled.
- bFloating: A boolean that determines if the control should float or be docked (TRUE for float, FALSE for dock).

#### Notes

This section introduces the concept of controlling floating and docking behavior for controls in a Windows Forms application, focusing on enabling "float-only" functionality.

## Code Examples (Multi-Language)

The section includes code examples in both C# and VB.NET for configuring the `SetFloatOnly` method applied to a control.

## Page-level Navigation/TOC (if applicable)

Other sections on this page or relevant information may precede or follow this content, but the summary above provides an overview and details of the section focusing on hiding and docking controls.

## RAG Annotations

- **Tags**: Windows Forms, Syncfusion, Docking Manager, Controls, Float Only, Hiding Controls
- **Keywords**: SetFloatOnly, Docking, Floating, WindowsForms, C#, VB.NET, listBox2

<!-- This section provides information on configuring controls to be float-only using the `SetFloatOnly` method in the context of Windows Forms. -->
```