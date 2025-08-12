```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: diagram
page_number: 192
page_id: diagram#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:12Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- ScrollTips functionality can be enabled or disabled for horizontal and vertical scroll bars using specific properties.
- The format of ScrollTips can be customized programmatically using the ScrollTipFormat property.

## Content

### ScrollTips
ScrollTips can be enabled or disabled for horizontal and vertical scroll bars individually by setting the `HorizontalScrollTips` and `VerticalScrollTips` properties.

The format in which the scrolltip should be displayed can be specified using the `ScrollTipFormat` property. The default format is `'Position{0}'`.

| Properties            | Description                                                                 |
|-----------------------|------------------------------------------------------------------------------|
| `HorizontalScrollTips` | Specifies whether to display the horizontal scroll bar.                   |
| `VerticalScrollTips`   | Specifies whether to display the vertical scroll bar.                     |
| `ScrollTipFormat`      | Specifies the format for the scrolltip to be displayed.                    |

Programmatically, these properties can be set as follows.

#### C#
```csharp
this.diagram1.HorizontalScrollTips = true;
this.diagram1.VerticalScrollTips = true;
this.diagram1.ScrollTipFormat = "Offset{0}";
```

#### VB
```vb
Me.diagram1.HorizontalScrollTips = True
Me.diagram1.VerticalScrollTips = True
Me.diagram1.ScrollTipFormat = "Offset{0}"
```

### Using Splitter Control

When a Splitter control is used and one or more diagram controls are added, setting the `FillSplitterPane` property docks the diagram control inside the Splitter control and fills the entire space.

| Property          | Description                                            |
|-------------------|--------------------------------------------------------|
| `FillSplitterPane` | Specifies whether to fill the Splitter control with diagram. |

Programmatically, these properties can be set as follows.

---

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Control**: Diagram
- **Properties**:
  - `HorizontalScrollTips`: Boolean
  - `VerticalScrollTips`: Boolean
  - `ScrollTipFormat`: String
  - `FillSplitterPane`: Boolean

## Code Examples

### C#
```csharp
this.diagram1.FillSplitterPane = true;
```

### VB
```vb
Me.diagram1.FillSplitterPane = True
```

## Page-level Navigation/TOC (if applicable)
- Section 1: ScrollTips
- Section 2: Using Splitter Control

## Cross References
- Refer to the documentation for detailed information on properties and methods related to the Diagram control.

<!-- tags: [syncfusion, winforms, diagram, scrolltips, splitter control, windows forms] keywords: [scrolltips, horizontal scroll bar, vertical scroll bar, scrolltipformat, fillsplitterpane, diagram control] -->
```