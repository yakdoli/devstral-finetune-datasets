```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: tools
page_number: 170
page_id: tools#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:08:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Introduces the **DockManager** feature in Syncfusion WinForms, focusing on the **HostFormClientBorder** and **SplitterWidth** properties.
- Demonstrates customization of docking windows, including removing borders and adjusting splitter width.

## Content

### HostFormClientBorder

| DockingManager Property | Description |
|--------------------------|-------------|
| HostFormClientBorder     | Gets or sets a value indicating whether a border is drawn around the host form's client rectangle. |

#### Code Examples
##### C#
```csharp
this.DockingManager1.HostFormClientBorder = false;
```

##### VB.NET
```vb
Me.DockingManager1.HostFormClientBorder = False
```

#### Visual Representation

![Docking Window without Border](https://i.imgur.com/2c.png)
*Figure 83: Docking Window without Border*

### 3.4.3.5.2.3 Splitter Width

#### Description
The width of the splitter between the docking windows can be set by using the **SplitterWidth** property.

| DockingManager Property | Description |
|--------------------------|-------------|
| SplitterWidth           | Gets or sets the value indicating the width of splitters between the docking window. |

## API Reference

### Properties
- **HostFormClientBorder** *(Boolean)*: Indicates whether a border is drawn around the host form's client rectangle.
- **SplitterWidth** *(Integer)*: Specifies the width of the splitters between docking windows.

## Code Examples (if not already included above)

#### Setting Splitter Width
##### C#
```csharp
this.DockingManager1.SplitterWidth = 5;
```

##### VB.NET
```vb
Me.DockingManager1.SplitterWidth = 5
```

## RAG Annotations
<!-- tags: [winforms, dockmanager, hostformclientborder, splitterwidth, customization, properties] keywords: [DockingManager, HostFormClientBorder, SplitterWidth, C#, VB.NET, docking windows, border, width] -->
```