```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_294.jpeg
document_name: chart
page_number: 294
page_id: chart#page_294
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:02Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

| 2D / 3D Limitations | No                      |
|----------------------|-------------------------|
| Applies to Chart Element | Any series          |
| Applies to Chart Types   | Polar and Radar Chart |

## Code Snippet Example

Here is code snippet using `RadarType`.

```csharp
[C#]
this.chartControl1.Series[0].ConfigItems.RadarItem.Type = ChartRadarDrawType.Symbol;
this.chartControl1.Series[1].ConfigItems.RadarItem.Type = ChartRadarDrawType.Symbol;
this.chartControl1.Series[0].Style.Symbol.Shape = ChartSymbolShape.Star;
this.chartControl1.Series[1].Style.Symbol.Shape = ChartSymbolShape.Star;
this.chartControl1.Series[0].Style.Symbol.Color = Color.Blue;
this.chartControl1.Series[1].Style.Symbol.Color = Color.Green;
```

```vbnet
[VB.NET]
Private Me.chartControl1.Series(0).ConfigItems.RadarItem.Type = ChartRadarDrawType.Symbol
Private Me.chartControl1.Series(1).ConfigItems.RadarItem.Type = ChartRadarDrawType.Symbol
Private Me.chartControl1.Series(0).Style.Symbol.Shape = ChartSymbolShape.Star
Private Me.chartControl1.Series(1).Style.Symbol.Shape = ChartSymbolShape.Star
Private Me.chartControl1.Series(0).Style.Symbol.Color = Color.Blue
Private Me.chartControl1.Series(1).Style.Symbol.Color = Color.Green
```

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Chart`

### Enumerations

- `ChartRadarDrawType`
  - **Values**:
    - `Symbol`

- `ChartSymbolShape`
  - **Values**:
    - `Star`

### Properties

- `ChartRadarDrawType Type`
  - **Description**: Specifies the type of drawing for the radar items.
  - **Type**: Enum
  - **Default**: `None`

- `ChartSymbolShape Shape`
  - **Description**: Specifies the shape of the symbol.
  - **Type**: Enum
  - **Default**: `None`

- `Color Color`
  - **Description**: Specifies the color of the symbol.
  - **Type**: Color
  - **Default**: `Color.Empty`

<!-- tags: [essential chart, windows forms, radar chart, symbol, shape, color, c#, vb.net] keywords: [RadarType, ChartRadarDrawType, ChartSymbolShape, Shape, Color, Blue, Green] -->
```