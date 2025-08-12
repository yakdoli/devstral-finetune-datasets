```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_196.jpeg
document_name: chart
page_number: 196
page_id: chart#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:21Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### ChartFinancialColorsMode

- **DarkLight**:
  - **Figure 108:** Renko Chart with "DarkLight" ColorsMode
    ![Renko Chart with "DarkLight" ColorsMode](https://via.placeholder.com/300x200?text=Figure+108)

  - **Figure 109:** Renko Chart with "Mixed" ColorsMode
    ![Renko Chart with "Mixed" ColorsMode](https://via.placeholder.com/300x200?text=Figure+109)

### Visit Also
- [Renko Chart](Renko+Chart)

### DarkLightPower
#### 4.5.1.9 DarkLightPower

- **Description:** Gets or sets the intensity of the dark and light colors used in DarkLight color mode.

## API Reference

### ChartFinancialColorsMode

- **DarkLight**: The mode for setting the intensity of dark and light colors.

### Properties

- **DarkLightPower**: 
  - Type: `float`
  - Description: Represents the intensity of the dark and light colors used in DarkLight color mode.

## Code Examples

### C#

```csharp
ChartFinancialColorsMode mode = ChartFinancialColorsMode.DarkLight;
chart.Series[0].Appearance.FillStyle.ColorMode = mode;
chart.Series[0].DarkLightPower = 0.7f;
```

## Cross References

- **See Also**: Renko Chart

<!-- tags: [Syncfusion Winforms, Chart, ColorMode, DarkLightPower, Renko Chart] keywords: [ChartFinancialColorsMode, DarkLight, Mixed ColorsMode, DarkLightPower, Renko Chart] -->
``` 
```