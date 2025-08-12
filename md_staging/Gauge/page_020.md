```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_020.jpeg
document_name: Gauge
page_number: 020
page_id: Gauge#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:12Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

Two types of ticks can be added to the RadialGauge control scale. Major tick marks are the primary scale indicators. Minor tick marks and Inter tick marks are the secondary scale indicators that fall between the major ticks. The ticks can be placed by setting the TickPlacement property. Ticks can be placed inside or outside the arc.

The following table lists the important properties that can be used to customize the radial tick marks. This is done to represent the scale with meaningful markers and labels.

## Property Table

| Property                    | Type         | Description                                                                 |
|-----------------------------|--------------|-----------------------------------------------------------------------------|
| TickPlacement               | Enum         | Gets or sets whether to place the tickmarks inside or outside the arc. |
| MajorTickMarkColor         | Color        | Gets or sets the color of the major tickmarks.                        |
| MajorTickMarkHeight        | Integer      | Gets or sets the height of the major tickmarks.                        |
| MinorTickMarkColor         | Color        | Gets or sets the color of the minor tickmarks.                        |
| MinorTickMarkHeight        | Integer      | Gets or sets the height of the minor tickmarks.                        |
| InterLinesColor            | Color        | Gets or sets the color of the InterLines of the gauge.               |
| MinorInnerLinesHeight      | Integer      | Gets or sets the line height of the minor inner lines.               |

The following code example illustrates how to add major and minor ticks to the radial scale.

```csharp
this.radialGauge1.TickPlacement = Synctfusion.Windows.Forms.Gauge.TickPlacement.Outside;
this.radialGauge1.MajorTickMarkColor = System.Drawing.Color.White;
this.radialGauge1.MinorTickMarkColor = System.Drawing.Color.White;
this.radialGauge1.InterLinesColor = System.Drawing.Color.White;
```

<!-- tags: [product, RadialGauge, TickMark, TickPlacement, MajorTickMark, MinorTickMark, InterLines] keywords: [RadialGauge, tick marks, customizing, scale indicators, placement, tick color, line height] -->
```