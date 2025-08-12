```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: tools
page_number: 166
page_id: tools#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:06:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The Docking Manager provides an event for customizing the rendering of the docking window caption area.
- Provides the ability to handle custom rendering through the `ProvideGraphicsItems` event.
- Explains how to customize styling for Metro VisualStyle in DockingManager.
- Describes properties for setting caption and button colors in Metro style DockingManager.

## Content

### DockingManager Custom Styling with Metro VisualStyle
In the DockingManager, the Metro visual style has a default caption color and button color. The menu color and button color can be customized by using the properties `MetroCaptionColor` and `MetroButtonColor`, which are present in the caption bar of the docking manager.

#### Properties and Descriptions

| Property       | Description                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| `MetroCaptionColor` | Gets or sets the color value of a caption in metro style DockingManager. |
| `MetroButtonColor` | Gets or sets the color value of a metro button in metro style DockingManager. |

#### Code Examples

##### Setting the MetroCaptionColor

**[C#]**
```csharp
// Gets or sets the color value of caption in metro style DockingManager.
this.dockingMgr.MetroCaptionColor = Color.Red;
```

**[VB.NET]**
```vbnet
// Gets or sets the color value of caption in metro style DockingManager.
Me.dockingMgr.MetroCaptionColor = Color.Red
```

##### Setting the MetroButtonColor

**[C#]**
```csharp
// Gets or sets the color value of button in metro style DockingManager.
this.dockingMgr.MetroButtonColor = Color.Red;
```

**[VB.NET]**
```vbnet
// Gets or sets the color value of button in metro style DockingManager.
Me.dockingMgr.MetroButtonColor = Color.Red
```

### See Also
- [Visual Styles](#Visual-Styles)
- [3.4.3.5.2 Background Settings](#3.4.3.5.2-Background-Settings)

---

<!-- tags: [syncfusion, windows forms, controls, docking manager, visual styles, metro style, caption color, button color, code examples, customization] keywords: [DockingManager, MetroVisualStyle, MetroCaptionColor, MetroButtonColor, custom styling, color customization] -->
```