```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_490.jpeg
document_name: chart
page_number: 490
page_id: chart#page_490
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Describes properties for configuring tooltip appearance and behavior in Syncfusion charts for Windows Forms.
- Includes settings for alignment, color, font, style, and other visual elements.
- Provides C# and VB.NET code examples for enabling fancy tooltips.

## Content

### Tooltip Configuration Properties

| **Property**      | **Description**                                                                 |
|-------------------|---------------------------------------------------------------------------------|
| **Angle**         | Specifies the angle at which to render the balloon in the alignment specified. |
| **BackColor**     | Specifies the back color.                                                      |
| **Border**        | Lets you customize the border look of the tooltip.                            |
| **CheckLocation** | Specifies whether the tooltip should auto-align when shown for data points close to the chart border. |
| **Font**          | Specifies the font for the tooltip text.                                      |
| **ForeColor**     | Specifies the color for the tooltip text.                                     |
| **Spacing**       | The space between the tooltip text and the border.                           |
| **Style**         | Specifies the tooltip style. Possible values: <br>- Ellipse <br>- Rectangle <br>- SmoothRectangle - Default value |
| **Symbol**        | Specifies the symbol shape to use.                                            |
| **SymbolColor**   | Specifies the inner color of the symbol.                                      |
| **SymbolSize**    | Specifies the size of the symbol.                                             |
| **ToTarget**      | Specifies the distance between the balloon and the target.                   |
| **Visible**       | Turns on/off fancy tooltips.                                                  |

### Code Examples

#### C#

```csharp
series1.FancyToolTip.Visible = true;
series1.FancyToolTip.Alignment = TabAlignment.Top;
```

#### VB.NET

```vb
series1.FancyToolTip.Visible = True
series1.FancyToolTip.Alignment = TabAlignment.Top
```

## Page-level Navigation/TOC (if applicable)

- No local Table of Contents present on this page.

## Cross References

- For more information on tooltip customization, refer to the chart documentation on tooltips.

## RAG Annotations

<!-- tags: [syncfusion, winforms, chart, tooltip, fancytooltip, windowsforms, version: 11.4.0.26] keywords: [tooltip alignment, tooltip style, tooltip font, tooltip color, tooltip spacing, symbol style, tooltip visibility, series fancy tooltip] -->
```