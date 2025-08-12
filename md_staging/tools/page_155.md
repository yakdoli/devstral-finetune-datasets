```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: tools
page_number: 155
page_id: tools#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:58:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
this.dockingManager1.BrowsingKey = 
((System.Windows.Forms.Keys)(System.Windows.Forms.Keys.Control |
System.Windows.Forms.Keys.D0));
this.treeViewAdv1.TabStop = true;
this.treeViewAdv1.TabIndex = 0;
```

### [VB.NET]

```vb
Me.DockingManager1.BrowsingKey = 
CType((System.Windows.Forms.Keys.Control Or 
System.Windows.Forms.Keys.D0), System.Windows.Forms.Keys)
Me.TreeViewAdv1.TabStop = True
Me.TreeViewAdv1.TabIndex = 0
```

## Overview
- Configures browsing key and tab settings for `DockingManager` and `TreeViewAdv` controls.
- Demonstrates setting tab properties for interactive navigation.
- Includes support for tooltips on docked control caption buttons.

## Content

### 3.4.3.4.2 ToolTip
By default, tooltips will be displayed for the caption buttons in a docked control when the mouse is moved over it.

![Default Tooltip for Menu Button](image.png)

**Figure 70: Default Tooltip for Menu Button**

#### Note
The `EnableSuperTooltip` property, which is discussed below, should be set to `false` to effect the above default tooltip.

### SuperTooltip Support

``` 
© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [DockingManager, TreeViewAdv, ToolTip, SuperTooltip] keywords: [DockedControls, CaptionButtons, TooltipBehavior, InteractiveNavigation, TooltipSettings] -->
``` 
