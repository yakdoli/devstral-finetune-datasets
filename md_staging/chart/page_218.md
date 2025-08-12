```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_218.jpeg
document_name: chart
page_number: 218
page_id: chart#page_218
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:16Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates enabling chart area tooltips in VB.NET.
- Introduces the `ErrorBarsSymbolShape` property and its possible values for customizing error bars.

## Content

### Example Code: Enabling Chart Area Tooltips in VB.NET

```vb
Me.chartControl1.Series(0).EnableAreaToolTip = True
```

#### Chart Example
![Figure: Enable Chart Area Tooltip](https://example.com/enable_chart_area_tooltip.png)  
*Figure 123: EnableAreaToolTip = "True"*

### 4.5.1.21 ErrorBarsSymbolShape

This property determines the shape of the error bar symbol when `DrawErrorBars` is `true`.

#### Details

| Possible Values | Description |
| --- | --- |
| None | No marker will be shown. |
| Line | A Line will be drawn as the marker. |
| Square | A Square will be drawn as the marker. |
| Circle | A Circle will be drawn as the marker. |
| Diamond | A Diamond will be drawn as the marker. |
| Triangle | A Triangle will be drawn as the marker. |

## API Reference

- **Property:** `ErrorBarsSymbolShape`
  - **Namespace:** Syncfusion.Windows.Forms.Chart
  - **Type:** `ErrorBarSymbolShape`
  - **Description:** Used to specify the shape of the error bar symbol.
  - **Possible Values:**
    - None
    - Line
    - Square
    - Circle
    - Diamond
    - Triangle

## Code Examples

```vb
' Setting the error bar symbol shape to a square
Me.chartControl1.Series(0).ErrorBarsSymbolShape = ErrorBarSymbolShape.Square

' Setting the error bar symbol shape to a triangle
Me.chartControl1.Series(1).ErrorBarsSymbolShape = ErrorBarSymbolShape.Triangle
```

## Page-level Navigation/TOC (if applicable)
- [4.5.1.21 ErrorBarsSymbolShape](#4.5.1.21-ErrorBarsSymbolShape)

## Cross References
- Refer to the documentation on `DrawErrorBars` for more information on enabling error bars.

<!-- tags: [winforms, chart, errorbars, toolips] keywords: [error bars, tooltips, errorbarsymbolshape, errorbarssymbolshape, vb.net, enableareatooltip] -->
```