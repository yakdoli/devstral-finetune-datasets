```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_398.jpeg
document_name: chart
page_number: 398
page_id: chart#page_398
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- 1. Describes the `LabelRotateAngle` property in detail.
- 2. Explains how axis labels can be customized in a Windows Forms chart.
- 3. Provides a code example to achieve specific label customization features.

## Content

### Label Rotate Angle

| LabelRotateAngle | If `LabelRotate` is true, this property specifies the angle of rotation. |
|-------------------|--------------------------------------------------------------------------|
|                   |                                                                      |

### Axis Label Customization

#### Figure 257: Axis Label Customization

![Figure 257: Axis Label Customization](attachment:chart_label_customization_image)
*Figure 257: Axis Label Customization*

**Description of the Chart:**
- The chart displayed illustrates a bar graph with monthly data (Jan to Jun).
- The Y-axis is labeled with dollar amounts (e.g., $0.00, $200.00, etc.).
- The X-axis uses a custom label format (`MMM`), showing three-letter month abbreviations.
- The legend highlights various settings applied to the axes, such as font, color, and rotation.

### Code Example

```csharp
//Settings datetime format to Xaxis
this.chartControl1.PrimaryXAxis.DateTimeFormat = "MMM";

//Settings format to Yaxis
this.chartControl1.PrimaryYAxis.ValueType = ChartValueType.Double;
this.chartControl1.PrimaryYAxis.Format = "C";

//setting ForeColor and Font to axes labels
this.chartControl1.PrimaryXAxis.ForeColor = System.Drawing.Color.Navy;
this.chartControl1.PrimaryXAxis.Font = new System.Drawing.Font("Arial", 9F, System.Drawing.FontStyle.Bold);
this.chartControl1.PrimaryYAxis.ForeColor = System.Drawing.Color.Navy;
```

## API Reference

### Properties

- **PrimaryXAxis.DateTimeFormat**:  
  - **Type**: String  
  - **Description**: Specifies the date-time format for the X-axis labels. In the example, `"MMM"` is used to display three-letter month abbreviations.

- **PrimaryYAxis.ValueType**:  
  - **Type**: ChartValueType  
  - **Description**: Specifies the type of values displayed on the Y-axis. In the example, `ChartValueType.Double` is used to display monetary values.

- **PrimaryYAxis.Format**:  
  - **Type**: String  
  - **Description**: Specifies the format for the Y-axis labels. In the example, `"C"` is used to display values in currency format.

- **PrimaryXAxis.ForeColor**:  
  - **Type**: Color  
  - **Description**: Specifies the foreground color of the X-axis labels. In the example, `System.Drawing.Color.Navy` is used to set the color to navy.

- **PrimaryXAxis.Font**:  
  - **Type**: Font  
  - **Description**: Specifies the font for the X-axis labels. In the example, a bold Arial font with 9 points is used.

- **PrimaryYAxis.ForeColor**:  
  - **Type**: Color  
  - **Description**: Specifies the foreground color of the Y-axis labels. In the example, `System.Drawing.Color.Navy` is used to set the color to navy.

## Code Examples

The following code demonstrates how to customize axis labels in a chart control:

```csharp
// Setup secondary X-axis label settings
this.chartControl1.PrimaryXAxis.DateTimeFormat = "MMM";

// Setup secondary Y-axis label settings
this.chartControl1.PrimaryYAxis.ValueType = ChartValueType.Double;
this.chartControl1.PrimaryYAxis.Format = "C";

// Customize font and colors for axis labels
this.chartControl1.PrimaryXAxis.ForeColor = System.Drawing.Color.Navy;
this.chartControl1.PrimaryXAxis.Font = new System.Drawing.Font("Arial", 9F, System.Drawing.FontStyle.Bold);
this.chartControl1.PrimaryYAxis.ForeColor = System.Drawing.Color.Navy;
```

### Explanation

The above code snippet configures the axis labels in a Windows Forms chart control:
- The X-axis is set to display abbreviated month names (`MMM`).
- The Y-axis is set to display monetary values in currency format (`C`).
- Both axes use a navy color for their labels.
- The X-axis labels use a bold Arial font with a size of 9 points.

## Cross References

- See also:  
  - **Syncfusion Chart Documentation**: For more detailed information on axis customization and related features.
  - **Syncfusion WinForms Controls**: For comprehensive guidance on using Syncfusion controls in Windows Forms applications.

<!-- tags: [syncfusion, chart, axis, customization, windows forms, controls, sincfusion windows forms, chart control] keywords: [LabelRotateAngle, DateTimeFormat, ValueType, Format, ForeColor, Font, Month Abbreviation, Currency Format, Navy Color, Bold Font, Axis Labels, Chart Customization] -->
```