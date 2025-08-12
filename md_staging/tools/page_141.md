```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: tools
page_number: 141
page_id: tools#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:48:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section discusses AutoHidden Tabs with a full caption display and动画效果 in AutoHiding.
- Explains how to adjust the animation speed for DockingPanel using AnimationSpeed and AnimationStep properties.
- Provides links to related topics and examples.

## Content

### AutoHidden Tabs with Full Caption Display

![Figure 58: AutoHidden Tabs with full Caption Display](https://via.placeholder.com/300)

**Figure 58: AutoHidden Tabs with full Caption Display**

AutoHide Animation Speed topic and Dragging Autohidden tabs topic discuss how to drag the autohidden tabs.

#### See Also
- Context Menu
- Animation Events
- AutoHide TabContextMenu Event
- How to autohide a control when an application loads

### 3.4.3.1.4.1 Auto Hide Animation Speed

DockingPanel allows you to change the speed at which your docking panes are displayed or auto hidden. You can easily change the delay of the auto hide windows as fast or as slow as you want, so that your window will hide / show at the perfect speed.

#### Animation Speed Control

The speed of animation can be controlled by `AnimationSpeed` and `AnimationStep` property.

- **AnimationSpeed** property of the DockingManager indicates the speed of animation during auto hide or the timer interval in milli seconds.
- **AnimationStep** indicates the step value for the animation. It is common to all the docked control.

#### Implementation Example

AnimationStep property can be implemented using the code below.

```csharp
//arg.Bounds give the bounds of the autohidden control as a rectangle object.
DockingManager.AnimationStep = 1000; // (arg.Bounds.Width)
```

### Summary

This section provides detailed information on managing autohide animations in DockingPanel, including how to control the speed of these animations through programming.

## Code Examples

- **Example of Setting AnimationStep**

Use the following C# code to set the step value for the animation:

```csharp
DockingManager.AnimationStep = 1000; // (arg.Bounds.Width)
```

## Cross References
- Context Menu
- Animation Events
- AutoHide TabContextMenu Event
- How to autohide a control when an application loads

### Related Topics
- [AutoHide Animation Speed](#3.4.3.1.4.1)
- [Dragging Autohidden Tabs](#Dragging Autohidden tabs)

<!-- tags: [DockingPanel, AutoHide, AnimationSpeed, AnimationStep, Windows Forms, SyncfusionWinforms] keywords: [Auto Hidden Tabs, Animation, Docking Panes, Auto Hide Animation, AnimationStep, AnimationSpeed, Windows Forms, Syncfusion] -->
```