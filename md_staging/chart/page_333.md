```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_333.jpeg
document_name: chart
page_number: 333
page_id: chart#page_333
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:32Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.Series[0].ConfigItems.StepItem.Inverted = true;
```

### [VB.NET]
```vb
Private Me.chartControl1.Series(0).ConfigItems.StepItem.Inverted = True
```

### Figure 211: Inverted = "False"

![](https://chart.googleapis.com/chart?cht=qr&chl=https://syncfusion.com&chs=150x150)

Figure 211: Inverted = "False"

### Overview

1. Demonstrates configuring the StepItem property with `Inverted` set to false.
2. Shows a visualization using a chart control in a Windows Forms application.
3. Focuses on the appearance of the chart when the `Inverted` property is set.

## Content

### StepItem Configuration
The `StepItem` property within the chart control allows for customization of the step plotting style. When `Inverted` is set to false, the steps are displayed in their default orientation.

### Chart Visualization
The provided figure illustrates a 3D bar chart with two distinct series, represented by orange and blue bars. The steps are aligned horizontally, indicating the default behavior when `Inverted` is false.

### API Reference
#### Namespace: Syncfusion.Windows.Forms.Chart
- **Member:** `ConfigItems.StepItem.Inverted`
  - Type: `Boolean`
  - Description: Determines whether the steps are inverted or not.

### Code Examples
- **C#**
  ```csharp
  this.chartControl1.Series[0].ConfigItems.StepItem.Inverted = false;
  ```
- **VB.NET**
  ```vb
  Private Me.chartControl1.Series(0).ConfigItems.StepItem.Inverted = False
  ```

### Cross References
- Related topic: configuring other chart properties.
- See also: step plotting alternatives and customization options.

<!-- tags: [chart, stepitem, inverted, windows forms, syncfusion] keywords: [chartcontrol, series, stepitem, inverted, windows forms, visualization, 3d bar chart, orange and blue bars] -->
``` 
