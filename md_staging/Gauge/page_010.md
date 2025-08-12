```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_010.jpeg
document_name: Gauge
page_number: 010
page_id: Gauge#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:13:52Z
fidelity: lossless
-->

## Overview
- Focus on configuring and customizing the appearance of the CircularGauge control.
- Detailed instructions on setting up major and minor ticks, labels, and annotations.
- Highlighting the usage of GaugeStyle to enhance aesthetic visualization.

## Content

### Customizing Tick Appearance
The CircularGauge control provides numerous options to customize the appearance of ticks, including major ticks and minor ticks. These ticks can be used to divide the range and enhance the readability of the gauge.

#### Major Ticks
Major ticks are used to mark specific intervals on the gauge scale and are a prominent visual element. You can customize the appearance of major ticks using the following properties:

- **Width**: Specifies the width of the tick.
- **Height**: Specifies the length of the tick.
- **Color**: Specifies the color of the tick.
- **LineStyle**: Changes the line style of the tick (Solid, Dash, Dotted, etc.).
- **Offset**: Controls the distance from the center where the tick is drawn.

**Example:**
```csharp
circularGauge1.MajorTicks.Width = 2;
circularGauge1.MajorTicks.Height = 10;
circularGauge1.MajorTicks.Color = Color.Black;
circularGauge1.MajorTicks.LineStyle = DashStyle.Dash;
circularGauge1.MajorTicks.Offset = 0.8;
```

#### Minor Ticks
Minor ticks provide additional divisions between major ticks and enhance the granularity of the gauge scale. You can customize minor ticks using the following properties:

- **Width**: Specifies the width of the minor tick.
- **Height**: Specifies the length of the minor tick.
- **Color**: Specifies the color of the minor tick.
- **LineStyle**: Changes the line style of the minor tick.
- **Offset**: Controls the distance from the center where the minor tick is drawn.
- **Steps**: Specifies the number of intervals between each major tick.

**Example:**
```csharp
circularGauge1.MinorTicks.Width = 1;
circularGauge1.MinorTicks.Height = 5;
circularGauge1.MinorTicks.Color = Color.Gray;
circularGauge1.MinorTicks.LineStyle = DashStyle.Solid;
circularGauge1.MinorTicks.Offset = 0.85;
circularGauge1.MinorTicks.Steps = 5;
```

### Configuring Labels
Labels are used to assign numerical or textual values to the ticks on the gauge. You can customize labels using the following properties:

- **Font**: Specifies the font style, size, and weight of the label text.
- **Text**: Specifies the content of the label.
- **Color**: Specifies the color of the label text.
- **Format**: Specifies how the value should be formatted (e.g., "##.##" for decimal points).
- **Offset**: Controls the distance from the center where the label is positioned.
- **Position**: Determines whether the label should be placed inside or outside the gauge.

**Example:**
```csharp
circularGauge1.Labels.Font = new Font("Arial", 10, FontStyle.Bold);
circularGauge1.Labels.Color = Color.Black;
circularGauge1.Labels.Format = "##.##";
circularGauge1.Labels.Offset = 1.2;
circularGauge1.Labels.Position = GaugeTextPosition.Outside;
```

### Adding Annotations
Annotations allow you to include additional visual elements, such as text or images, on the gauge to convey important information to the user. These annotations can be positioned at specific coordinates on the gauge.

**Example:**
```csharp
circularGauge1.Annotations.Add(new CircularGaugeAnnotation
{
    RoundShape = true,
    Size = new SizeF(15, 15),
    Offset = new PointF(0, 0),
    FillStyle = new FillStyle
    {
        Color = Color.DarkRed
    },
    Text = "Error!"
});
```

### Setting the Gauge Style
The GaugeStyle property is used to set a pre-defined aesthetic theme for the gauge. Syncfusion provides several predefined styles such as "None", "Classic", "Modern", etc. You can also create a custom style and apply it to your gauge.

**Example:**
```csharp
circularGauge1.Style = CircularGaugeGaugeStyle.Classic;
```

If you need a more customized look, you can create a custom style and override the properties:

**Example:**
```csharp
circularGauge1.Style = new CircularGaugeCustomStyle();
circularGauge1.Style.Background = new FillStyle
{
    GradientStyle = GradientStyle.Linear,
    StartColor = Color.LightBlue,
    EndColor = Color.White,
};
```

By combining these customization options, you can create a visually appealing and functional CircularGauge control tailored to your specific application needs.

## Code Examples

### Major Ticks
```csharp
using Syncfusion.Windows.Forms.CircularGauge;

circularGauge1.MajorTicks.Width = 2;
circularGauge1.MajorTicks.Height = 10;
circularGauge1.MajorTicks.Color = Color.Black;
circularGauge1.MajorTicks.LineStyle = DashStyle.Dash;
circularGauge1.MajorTicks.Offset = 0.8;
```

### Minor Ticks
```csharp
using Syncfusion.Windows.Forms.CircularGauge;

circularGauge1.MinorTicks.Width = 1;
circularGauge1.MinorTicks.Height = 5;
circularGauge1.MinorTicks.Color = Color.Gray;
circularGauge1.MinorTicks.LineStyle = DashStyle.Solid;
circularGauge1.MinorTicks.Offset = 0.85;
circularGauge1.MinorTicks.Steps = 5;
```

### Labels
```csharp
using Syncfusion.Windows.Forms.CircularGauge;

circularGauge1.Labels.Font = new Font("Arial", 10, FontStyle.Bold);
circularGauge1.Labels.Color = Color.Black;
circularGauge1.Labels.Format = "##.##";
circularGauge1.Labels.Offset = 1.2;
circularGauge1.Labels.Position = GaugeTextPosition.Outside;
```

## Cross References
- **Related Documentation:** 
    - [Syncfusion CircularGauge Overview](#overview)
    - [Gauge Customization Techniques](#customization)
    - [Styling and Themes in CircularGauge](#styling)

## RAG Annotations
<!-- tags: circulargauge, winforms, customization, ticks, labels, annotations, style, gauge, syncfusion-sdk keywords: major ticks, minor ticks, labels, annotations, gauge style, customization, winforms controls -->
```