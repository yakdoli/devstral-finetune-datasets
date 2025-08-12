```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_142.jpeg
document_name: tools
page_number: 142
page_id: tools#page_142
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:49:52Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the configuration and behavior of auto-hidden tabs in Syncfusion Winforms.
- Explains the use of animation settings and context menus with auto-hidden tabs.
- Details the property `EnableDragAutoHiddenTabs` for enabling tab dragging.
- Introduces the concept of the caption bar for docked controls.

## Content

### AutoHidden Tabs

#### Animation in AutoHide Mode
- **Animation Step Value**: 
  - The `AnimationStep` property determines the animation speed for auto-hidden controls.
  - It should be **more than the width of the hidden control** to ensure proper animation.

  ```vb
  ' arg.Bounds give the bounds of the autohidden control as a rectangle object.
  DockingManager.AnimationStep = 1000;  ' (arg.Bounds.Width)
  ```

  **Note**: For a control to show animation in autohide mode, the animation step value should be more than the width of the particular hidden control.

#### Context Menu for AutoHidden Tabs
- Discussed in the **Context Menu** topic.

#### Dragging AutoHidden Tabs
- Docked controls that are auto-hidden can be dragged with their tabs.
- Set the `EnableDragAutoHiddenTabs` property to `true` to enable this functionality.

```csharp
this.dockingManager1.EnableDragAutoHiddenTabs = true;
```

```vb
Me.dockingManager1.EnableDragAutoHiddenTabs = True
```

### Caption Bar

#### Enabling Caption Bar
- The caption bar for docked controls can be enabled using the `ShowCaption` property.
- By default, this property is set to `true`.

**Figure**: Caption Bar Illustration  
![Caption Bar Illustration](https://example.com/caption_bar_image)

## API Reference

### Properties
- `EnableDragAutoHiddenTabs`: Boolean property to enable drag-and-drop functionality for auto-hidden tabs.
- `ShowCaption`: Boolean property to enable or disable the caption bar for docked controls.

### Methods
- `SetAnimationStep(int step)`: Method to set the animation step value for auto-hidden controls.

## Code Examples

### Enabling Dragging for AutoHidden Tabs

#### C#
```csharp
this.dockingManager1.EnableDragAutoHiddenTabs = true;
```

#### VB.NET
```vb
Me.dockingManager1.EnableDragAutoHiddenTabs = True
```

### Enabling Caption Bar

#### C#
```csharp
this.dockingManager1.ShowCaption = true;
```

#### VB.NET
```vb
Me.dockingManager1.ShowCaption = True
```

## Cross References
- See also: **Context Menu** topic for further details on auto-hidden tabs.

<!-- tags: [Syncfusion Winforms, AutoHidden Tabs, Animation, Context Menu, Caption Bar] keywords: [autohide, animation step, enable drag, show caption, docked controls] -->
```