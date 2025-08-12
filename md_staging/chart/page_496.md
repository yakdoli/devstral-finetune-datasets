```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_496.jpeg
document_name: chart
page_number: 496
page_id: chart#page_496
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:50Z
fidelity: lossless
-->

## Chart Control Properties and Background Image Settings

### ChartAreaBackImage

#### Chart control Property

- **ChartAreaBackImage**
- Specifies the image to be used as the background in the chart area.

#### Code Examples

- **C#**
  ```csharp
  this.chartControl1.ChartAreaBackImage = myCustomImage;
  ```

- **VB.NET**
  ```vb
  Me.ChartControl1.ChartAreaBackImage = myCustomImage
  ```

#### Figure: Background Image set for the Chart Area

![ChartArea BackgroundImage Settings](image.png)

*Figure 320: Background Image set for the Chart Area*

### Chart Interior Background Image

Chart Interior can be rendered with a custom background image using the **ChartInteriorBackImage** property.

## API Reference

- **ChartInteriorBackImage**
  - Specifies the custom background image for the chart interior.
  - Type: `Image`
  - Usage: Assign a custom Image object to this property to apply a background image to the chart interior.

## Code Examples

- **C#**
  ```csharp
  this.chartControl1.ChartInteriorBackImage = myCustomImage;
  ```

- **VB.NET**
  ```vb
  Me.ChartControl1.ChartInteriorBackImage = myCustomImage
  ```

## Page-level Navigation/TOC (if applicable)

- **ChartAreaBackImage**
- **ChartInteriorBackImage**

## Cross References

- See also: ChartAreas, ChartAppearance, BackgroundSettings

<!-- tags: [chart, backgroundimage, chartcontrol, chartarea, chartinterior, winforms, syncfusion, version:11.4.0.26] keywords: [chartarea, chartinterior, backgroundimage, customimage, winforms, chart, syncfusion] -->
```