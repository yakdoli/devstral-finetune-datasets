```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_683.jpeg
document_name: tools
page_number: 683
page_id: tools#page_683
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the advanced functionalities related to collapsing panels in a `SplitContainer`.
- Explains the usage of `Panel1Collapsed`, `Panel2Collapsed`, `PanelToBeCollapsed`, and `TogglePanelOn` properties.
- Demonstrates how to specify minimum sizes for panels.

## Content

### SplitContainer Tools

| Column 1 | Column 2 |
| --- | --- |
| Splitter. | |
| Panel2Collapsed | Indicates if the Panel2 is collapsed or not. |
| PanelToBeCollapsed | Sets the panel to be collapsed when a predefined event occurs on it. |
| TogglePanelOn | A predefined event, which leads to collapsing of the panel specified in `PanelToBeCollapsed` property. Using `TogglePanelOn` property, we can decide whether, the panel needs to be collapsed on a single click or a double click. |

#### Code Examples

**[C#]**
```csharp
this.splitContainerAdv1.Panel1Collapsed = true;
this.splitContainerAdv1.Panel2Collapsed = false;
this.splitContainerAdv1.PanelToBeCollapsed = Syncfusion.Windows.Forms.Tools.CollapsedPanel.Panell;
this.splitContainerAdv1.TogglePanelOn = Syncfusion.Windows.Forms.Tools.TogglePanelOn.DoubleClick;
```

**[VB.NET]**
```vb.net
Me.SplitContainerAdv1.Panel1Collapsed = True
Me.SplitContainerAdv1.Panel2Collapsed = False
Me.SplitContainerAdv1.PanelToBeCollapsed = Syncfusion.Windows.Forms.Tools.CollapsedPanel.Panell
Me.splitContainerAdv1.TogglePanelOn = Syncfusion.Windows.Forms.Tools.TogglePanelOn.DoubleClick
```

### Panel Size

#### Setting Minimum Panel Sizes

**Overview**
- We can specify the minimum size for the `Panel1` and `Panel2` in `Panel1MinSize` and `Panel2MinSize` properties.
- Default value for both the properties is 25.

**Code Examples**

**[C#]**
```csharp
this.splitContainerAdv1.Panel1MinSize = 50;
this.splitContainerAdv1.Panel2MinSize = 50;
```

**[VB.NET]**
```vb.net
Me.splitContainerAdv1.Panel1MinSize = 50
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown.
- Fix extract positions of specific sections unless page 683 is the full document.

## Cross References
- Refer to the Synfusion Winforms documentation for other related controls like Toolbars, Grids, and Tooltips.

<!-- tags: [syncfusion-sdk, winforms, splitcontainer, panel, collapse, size, syncfusion-winforms] keywords: [splitcontainer properties, panel collapse, toggle panel, minimum size, double-click, single click] -->
```
