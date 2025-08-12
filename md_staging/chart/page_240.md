```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_240.jpeg
document_name: chart
page_number: 240
page_id: chart#page_240
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Introduces a method to customize the gap ratio for Funnel and Pyramid chart types.
- Demonstrates how to set the `GapRatio` property for different chart elements programmatically.
- Includes sample code in both C# and VB.NET.

## Content

### Chart Element Customization

| Applies to Chart Element | Applies to Chart Types |
|--------------------------|------------------------|
| All series               | Funnel Chart, Pyramid Chart |

### Sample Code

Here is some sample code.

#### C#

```csharp
// Setting GapRatio for Funnel Chart
this.chartControl1.Series[0].ConfigItems.FunnelItem.GapRatio = 0.1f;

// Setting GapRatio for Pyramid Chart
this.chartControl1.Series[0].ConfigItems.PyramidItem.GapRatio = 0.1f;
```

#### VB.NET

```vb
' Setting GapRatio for Funnel Chart
Me.chartControl1.Series(0).ConfigItems.FunnelItem.GapRatio = 0.1f

' Setting GapRatio for Pyramid Chart
Me.chartControl1.Series(0).ConfigItems.PyramidItem.GapRatio = 0.1f
```

### Visual Representation

The following image illustrates a funnel chart with the project cost breakdown:

**Project Cost Breakdown**
- 25.3
- 45.7
- 97.3
- 20.6
- 125.8
- 216.1

The chart visually represents the project cost breakdown, demonstrating the application of the `GapRatio` property.

## API Reference

### FunnelItem Properties

- **GapRatio**: Determines the gap between sections in a Funnel Chart.

### PyramidItem Properties

- **GapRatio**: Determines the gap between sections in a Pyramid Chart.

## Code Examples

The sample code demonstrates how to programmatically set the `GapRatio` for Funnel and Pyramid chart types using C# and VB.NET.

<!-- tags: [Funnel Chart, Pyramid Chart, GapRatio, chart customization, Syncfusion Winforms, chart control, Windows Forms] keywords: [Funnel Chart, Pyramid Chart, GapRatio, chart customization, FunnelItem, PyramidItem, C#, VB.NET] -->
```