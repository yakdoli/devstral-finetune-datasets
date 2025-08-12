```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_224.jpeg
document_name: chart
page_number: 224
page_id: chart#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:54Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- 1. Overview of essential charting features in Windows Forms.
- 2. Explanation of Doughnut Chart and Pie Chart functionalities.
- 3. Introduction to customizing tooltips in chart controls.

## Content

### 4.5.1.25 FancyToolTip

**Purpose:**
Defines the styles for a fancy tooltip. These styles include font, marker style, symbol shape, back color, and other related styles.

#### Table: Details

| **Possible Values** | **Specifies symbol, symbol styles for the ToolTip.** |
|---------------------|-------------------------------------------------------|
| Default Value       | -   Visible - False                                  <br> -   Angle - 15                                <br> -   Alignment - Left                             <br> -   ForeColor - Color.Black                     <br> -   BackColor - Color.Info                       <br> -   SymbolColor - Color.Red                     <br> -   Font - Arial, 8 pt                           <br> -   Symbol Size - (10,10)                         <br> -   Symbol - Circle                              <br> -   Style - SmoothRectangle                      |
| 2D / 3D Limitations | No                                                   |
| Applies to Chart Element | All series                                        |
| Applies to Chart Types | All Chart Types                                    |

#### Sample Code

Here is some sample code.

```csharp
this.chartControl1.Series[0].FancyToolTip.Angle = 180;
this.chartControl1.Series[0].FancyToolTip.Style = MarkerStyle.SmoothRectangle;
this.chartControl1.Series[0].FancyToolTip.Symbol = ChartSymbolShape.Hexagon;
this.chartControl1.Series[0].FancyToolTip.Visible = true;
```

## API Reference (if applicable)
- Namespace: `Syncfusion.Windows.Forms.Chart`
- Class: `ToolTip`
- Properties:
  - `Angle`
  - `Alignment`
  - `ForeColor`
  - `BackColor`
  - `SymbolColor`
  - `Font`
  - `SymbolSize`
  - `Symbol`
  - `Style`
  - `Visible`

## Code Examples (multi-language supported)
The provided code example demonstrates how to customize the FancyToolTip properties for a specific series in a chart control.

## Page-level Navigation/TOC (if applicable)
- Overview
- Content
  - 4.5.1.25 FancyToolTip
    - Table: Details
    - Sample Code

## Cross References
- See also: Doughnut Chart, Pie Chart.

## RAG Annotations
<!-- tags: [Syncfusion, chart, Windows Forms, FancyToolTip] keywords: [fancytooltip, style, font, markerstyle, symbolshape, backcolor, symbolsize, alignment, angle, visibility] -->
```