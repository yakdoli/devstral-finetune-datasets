```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_189.jpeg
document_name: diagram
page_number: 189
page_id: diagram#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:36Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Describes the Scroll Properties of the Diagram control in Windows Forms.
- Covers the management of scrollable areas using the ScrollVirtualBounds property.
- Provides examples in C# and VB to set scrollable bounds.

## Content

### Scrollable Area

Diagram has ScrollVirtualBounds property, which determines the bounds of the scrollable area. This sets the Diagram control's virtual space i.e, gray area around the control. Sometimes, we may need to remove that area and use Diagram control area alone.

#### Code Examples

[C#]

```csharp
this.diagram1.ScrollVirtualBounds = new RectangleF(0, 0, 0, 0);
```

[VB]

```vb
Me.diagram1.ScrollVirtualBounds = New RectangleF(0, 0, 0, 0)
```

## Page-level Navigation/TOC
- **Scrollable Area**
  - Explanation of ScrollVirtualBounds property.
  - Code examples in C# and VB for setting scrollable bounds.

## Cross References
- Related topics and additional resources may be found in the Windows Forms documentation or other sections of this guide.

<!-- tags: [Windows Forms, diagram, scroll properties, ScrollVirtualBounds, C#, VB] keywords: [scrollable area, diagram control, virtual space, bounds, gray area, Set boundaries, control area, Window] -->
```