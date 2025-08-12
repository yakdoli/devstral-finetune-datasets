```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_160.jpeg
document_name: chart
page_number: 160
page_id: chart#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:53Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Provides details about essential chart properties and methods for Windows Forms.
- Focuses on sparkline properties and their descriptions.
- Lists methods to interact with sparkline data points.

## Content

### Properties

| Property    | Description                                                                 | Type | Data Type | Reference links |
|-------------|-----------------------------------------------------------------------------|------|-----------|----------------|
| Type        | Specifies the types of spark lines. <br> - Line <br> - Column <br> - WinLoss <br> By default, it is set to Line type. | NA    | NA          | NA             |
| Source      | Gets or sets the data source for sparkline data points.                  | NA    | NA          | NA             |
| LineStyle   | Customizes the styles of Line sparkline.                                  | NA    | NA          | NA             |
| ColumnStyle | Customizes the styles of Column and Winloss sparklines.                  | NA    | NA          | NA             |
| Markers     | Enables the markers support to sparkline.                                 | NA    | NA          | NA             |
| BackInterior| Customizes the background color of the control. By default, it is set to White color. | NA    | NA          | NA             |

### Methods

| Method      | Description                                                                 | Parameters | Type  | Return Type | Reference links |
|-------------|-----------------------------------------------------------------------------|------------|-------|-------------|----------------|
| GetHighPoint| Gets the highest point value from the sparkline.                           | NA         | NA    | Void        | NA             |
| GetLowPoint | Gets the lowest point value from the sparkline.                            | NA         | NA    | Void        | NA             |

## API Reference

### Namespace
- Syncfusion.Windows.Forms.Chart

### Members
#### Properties
- **Type**: Specifies the types of spark lines. It allows choices like Line, Column, and WinLoss. Default: Line.
- **Source**: Gets or sets the data source for sparkline data points.
- **LineStyle**: Customizes the styles of Line sparkline.
- **ColumnStyle**: Customizes the styles of Column and Winloss sparklines.
- **Markers**: Enables markers support to sparkline.
- **BackInterior**: Customizes the background color of the control. Default: White color.

#### Methods
- **GetHighPoint()**: 
  - **Parameters**: None.
  - **Returns**: Void.
  - **Description**: Gets the highest point value from the sparkline.

- **GetLowPoint()**: 
  - **Parameters**: None.
  - **Returns**: Void.
  - **Description**: Gets the lowest point value from the sparkline.

## Code Examples

### Example: Configuring Sparkline Properties
```csharp
using Syncfusion.Windows.Forms.Chart;

// Initialize Sparkline
ChartControlLine sparkline = new ChartControlLine();

// Set Data Source
sparkline.Source = new object[] { 10, 20, 30, 40, 50 };

// Customize Line Style
sparkline.LineStyle.DashStyle = DashStyle.Solid;
sparkline.LineStyle.Thickness = 2;

// Enable Markers
sparkline.Markers = true;

// Set Background Color
sparkline.BackInterior = System.Drawing.Color.LightGray;
```

## Page-level Navigation/TOC
- Properties
- Methods

## Cross References
- Refer to the Syncfusion official documentation for more details on Chart Control in Windows Forms.
  
<!-- tags: [Syncfusion Winforms, Chart Control, Windows Forms, Properties, Methods, Sparkline, API Reference] keywords: [sparklines, data points, line charts, column charts, winloss charts, markers, background color, GetHighPoint, GetLowPoint] -->
```