```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_191.jpeg
document_name: diagram
page_number: 191
page_id: diagram#page_191
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:03Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview

- Explains how to configure scrolling behavior in the Diagram control.
- Describes the use of `AllowIncreaseSmallChange` and `HorizontalThumbTrack` / `VerticalThumbTrack` properties for enhanced user interaction.

## Content

### Scroll Behavior Customization

| AllowIncreaseSmallChange | Specifies if the scroll control can increase the ScrollBar.SmallChange property during accelerated scrolling. |
| --- | --- |

Here, setting the `AccelerateScrolling` to `Fast` will increase the scroll speed when the horizontal or vertical thumb is pressed continuously.

```csharp
this.diagram1.AccelerateScrolling =
    Syncfusion.Windows.Forms.AccelerateScrollingBehavior.Fast;
this.diagram1.AllowIncreaseSmallChange = true;
```

```vb
Me.diagram1.AccelerateScrolling =
    Syncfusion.Windows.Forms.AccelerateScrollingBehavior.Fast
Me.diagram1.AllowIncreaseSmallChange = True
```

### ThumbTrack

The `HorizontalThumbTrack` and `VerticalThumbTrack` properties allow you to handle whether the scroll bar thumb should be used for scrolling.

| Property                | Description                                                                 |
| ----------------------- | --------------------------------------------------------------------------- |
| HorizontalThumbTrack    | Specifies if the control should scroll while the user is dragging a horizontal scrollbar thumb. |
| VerticalThumbTrack      | Specifies if the control should scroll while the user is dragging a vertical scrollbar thumb. |

Programmatically, these properties can be set as follows.

```csharp
this.diagram1.HorizontalThumbTrack = true;
this.diagram1.VerticalThumbTrack = true;
```

```vb
Me.diagram1.HorizontalThumbTrack = True
Me.diagram1.VerticalThumbTrack = True
```

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Diagram`
- **Class**: `Diagram`
- **Properties**:
  - `AllowIncreaseSmallChange`: Gets or sets whether the scroll control can increase the ScrollBar.SmallChange property during accelerated scrolling.
  - `AccelerateScrolling`: Gets or sets the behavior for accelerated scrolling.
  - `HorizontalThumbTrack`: Gets or sets whether the control should scroll while the user is dragging a horizontal scrollbar thumb.
  - `VerticalThumbTrack`: Gets or sets whether the control should scroll while the user is dragging a vertical scrollbar thumb.

## Code Examples

Demonstrates how to enable fast scrolling and thumb tracking in the Diagram control.

### C#

```csharp
this.diagram1.AccelerateScrolling =
    Syncfusion.Windows.Forms.AccelerateScrollingBehavior.Fast;
this.diagram1.AllowIncreaseSmallChange = true;
this.diagram1.HorizontalThumbTrack = true;
this.diagram1.VerticalThumbTrack = true;
```

### VB

```vb
Me.diagram1.AccelerateScrolling =
    Syncfusion.Windows.Forms.AccelerateScrollingBehavior.Fast
Me.diagram1.AllowIncreaseSmallChange = True
Me.diagram1.HorizontalThumbTrack = True
Me.diagram1.VerticalThumbTrack = True
```

<!-- tags: [Syncfusion Winforms, Diagram, Scroll, ScrollBar, AccelerateScrolling, AllowIncreaseSmallChange, HorizontalThumbTrack, VerticalThumbTrack, version: 11.4.0.26] keywords: [scrolling behavior, Diagram control, horizontal thumb tracking, vertical thumb tracking, accelerated scrolling, Thumbnails, small change, Fast scrolling] -->
```
