```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_456.jpeg
document_name: grid
page_number: 456
page_id: grid#page_456
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:57Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Setting the behavior of the vertical scroll bar.
- Configuring scroll behavior using HorizontalThumbTrack properties in C# and VB.NET.
- Illustrating the transformation of the Grid when HorizontalThumbTrack is enabled.

## Content

### Scroll Bar Behavior

#### C#

Set the behavior of the vertical scroll bar:

```csharp
this.gridControl1.VScrollBehavior = GridScrollbarMode.Shared;
```

#### VB.NET

Set the behavior of the vertical scroll bar:

```vb
Me.gridControl1.VScrollBehavior = GridScrollbarMode.Shared
```

### HorizontalThumbTrack

- **Specification**: Specifies whether the control should scroll while the user is dragging the horizontal scroll bar thumb. Default value is set to `false`.
- **Code Examples**:

#### C#

Specify whether the control should scroll while dragging the horizontal scroll bar thumb:

```csharp
this.gridControl1.HorizontalThumbTrack = true;
```

#### VB.NET

Specify whether the control should scroll while dragging the horizontal scroll bar thumb:

```vb
Me.gridControl1.HorizontalThumbTrack = True
```

#### Illustration

The following illustration shows how the Grid in "Figure 1" is transformed when the HorizontalThumbTrack property is set to `true`.

![Illustration Description](#)
<!-- Placeholder for the illustration if it exists -->

## API Reference

### Properties

- **VerticalScrollBehavior**
  - Type: `GridScrollbarMode`
  - Description: Determines the behavior of the vertical scroll bar.
  - Default: `GridScrollbarMode.Auto`

- **HorizontalThumbTrack**
  - Type: `bool`
  - Description: Indicates whether the control should scroll while the horizontal scroll bar thumb is being dragged.
  - Default: `false`

## Code Examples

### C#

```csharp
// Setting the scroll behavior properties
this.gridControl1.VScrollBehavior = GridScrollbarMode.Shared;
this.gridControl1.HorizontalThumbTrack = true;
```

### VB.NET

```vb
' Setting the scroll behavior properties
Me.gridControl1.VScrollBehavior = GridScrollbarMode.Shared
Me.gridControl1.HorizontalThumbTrack = True
```

## Cross References

- For more information on scroll bar modes, see the GridScrollbarMode documentation.
- Refer to the Grid control's feature guide for additional scroll-related properties.

<!-- tags: [syncfusion, winforms, grid, scrollbar, horizontalthumbtrack, vscroll] keywords: [scrollbar behavior, horizontal scroll, scroll bar, grid control, horizontalthumbtrack, vscroll] -->
```