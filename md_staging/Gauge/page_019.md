```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: Gauge
page_number: 019
page_id: Gauge#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:14:22Z
fidelity: lossless
-->

# Essential Gauge for Windows Forms

## Content

### Scale inside the arc

- **Figure 11:** Scale inside the arc

This image illustrates the placement of labels inside the arc of a RadialGauge.

### Placing Labels in the RadialGauge Control

The following code sample demonstrates how to place labels in the RadialGauge control:

#### C# Code Sample

```csharp
this.radialGauge1.LabelPlacement = 
    Syncfusion.Windows.Forms.Gauge.LabelPlacement.Outside;

this.radialGauge1.TextOrientation = 
    Syncfusion.Windows.Forms.Gauge.TextOrientation.SlideOver;
```

#### VB Code Sample

```vb
Me.radialGauge1.LabelPlacement = 
    Syncfusion.Windows.Forms.Gauge.LabelPlacement.Outside

Me.radialGauge1.TextOrientation = 
    Syncfusion.Windows.Forms.Gauge.TextOrientation.SlideOver
```

### 3.2.2.3 Ticks

This section discusses the configuration and properties of ticks in a gauge control.

## Code Examples

Example code snippets are provided in both C# and VB to demonstrate the configuration of ticks and labels within a RadialGauge.

## API Reference

This section covers the various properties, methods, and events associated with the RadialGauge control, focusing on label placement and tick configurations.

#### Properties

- **LabelPlacement**: Determines the placement of labels in the RadialGauge (inside or outside the arc).
- **TextOrientation**: Defines how the text orientation is applied to labels; options include `SlideOver`.

### Cross References

For more information on configuring other aspects of the RadialGauge, refer to the [Syncfusion WinForms documentation](https://www.syncfusion.com/documentation/windowsforms).

<!-- tags: [Syncfusion Windows Forms, RadialGauge, LabelPlacement, TextOrientation, Ticks, C#, VB, Windows Forms User Guide] 
keywords: [Syncfusion, Windows Forms, RadialGauge, Label Placement, Text Orientation, Ticks, CSharp, VB.NET, User Guide, SDK, Documentation, Gauge Control, Configuration, Placement, Orientation, Examples] -->
``` 
