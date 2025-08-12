```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_195.jpeg
document_name: chart
page_number: 195
page_id: chart#page_195
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:45Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview
- Introduces the `ColorsMode` property for financial chart types in Windows Forms.
- Explains how to set the `ColorsMode` for boxes in financial chart types.
- Lists possible values and default settings for the `ColorsMode` property.
- Provides sample code in C# and VB.NET.

## Content

### 4.5.1.8 ColorsMode

**Gets / sets ColorsMode of the boxes in the financial chart types.**

#### Details

| Possible Values                                                                                                 | Default Value | 2D / 3D Limitations | Applies to Chart Element | Applies to Chart Types                        |
|---------------------------------------------------------------------------------------------------------------|---------------|----------------------|--------------------------|-----------------------------------------------|
| - **DarkLight** - Draws series data points as a darklight colorsmode.<br>- **Fixed** - Draws series data points as a Fixed colorsmode.<br>- **Mixed** - Draws series data points as a Mixed colorsmode. | Fixed            | None                   | All series                                    | Renko Chart (Financial Chart) |

### Sample Code

#### C#
```csharp
// Setting ColorsMode for series
this.chartControl1.Series[0].ConfigItems.FinancialItem.ColorsMode = ChartFinancialColorMode.DarkLight;
```

#### VB.NET
```vb
' Setting ColorsMode for series
Me.chartControl1.Series(0).ConfigItems.FinancialItem.ColorsMode =
```

## API Reference

### Namespace
- `Syncfusion.Windows.Forms.Chart`

### Class
- `ChartFinancialItem`

### Property
- `ColorsMode`

- **Possible Values:**
  - **DarkLight**: Draws series data points as a darklight colorsmode.
  - **Fixed**: Draws series data points as a Fixed colorsmode.
  - **Mixed**: Draws series data points as a Mixed colorsmode.

- **Default Value**: Fixed
- **Limitations**: None
- **Applies to Chart Element**: All series
- **Applies to Chart Types**: Renko Chart (Financial Chart)

## Code Examples

#### C#
Setting the `ColorsMode` for a series in C#:
```csharp
this.chartControl1.Series[0].ConfigItems.FinancialItem.ColorsMode = ChartFinancialColorMode.DarkLight;
```

#### VB.NET
Setting the `ColorsMode` for a series in VB.NET:
```vb
Me.chartControl1.Series(0).ConfigItems.FinancialItem.ColorsMode =
```

## RAG Annotations

<!-- tags: windows forms, chart, financial chart, renko chart, colorsmode, darklight, fixed, mixed keywords: [colorsmode, financial chart, renko chart, series, c#, vb.net, darklight, fixed, mixed, windows forms, syncfusion] -->
```