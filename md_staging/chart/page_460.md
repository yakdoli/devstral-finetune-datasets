```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_460.jpeg
document_name: chart
page_number: 460
page_id: chart#page_460
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:16Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview
- Explains how to manage zoom levels in charts using scrollbars and programmatic methods.
- Details how to adjust scroll precision, zoom out functionality, and programmatically set zoom factors and scroll positions.

## Content

### Resultant Zoomed-In Chart

#### Zooming and Scrollbar Behavior
- The scrollbar will shift by the amount specified in the **ScrollPrecision** property, which is set to **20** by default.
- Users can zoom out by clicking the "Zoom Out" button in the scrollbar.

#### Zoom Out Button
**Figure 293:** Resultant Zoomed-In Chart  
![](image.png)  
**Figure 294:** Zoom Out button beside the Scrollbar  

##### ZoomOutIncrement
- The **ZoomOutIncrement** property specifies the increment by which to zoom out. The default value is **0.2**.

### Programmatic Zooming

#### Zoom Factor
- Programmatic zooming can be achieved using the **ZoomFactorX** and **ZoomFactorY** properties. The zoom factor is usually between **0** and **1**:
  - When set to **1**, the chart isn't zoomed.
  - When set to **0.5**, the chart is double its usual size.
  - Scrollbars will automatically appear to allow any section of the hidden range to be viewed.
  - The default value is **1**.

#### Scrollbar Position
- You can programmatically specify the scrollbar position of the zoomed-in axes using the **ZoomPositionX** and **ZoomPositionY** properties.

## API Reference

- **ScrollPrecision**: Specifies the amount the scrollbar shifts during zoom operations (default: **20**).
- **ZoomOutIncrement**: Specifies the increment for zooming out (default: **0.2**).
- **ZoomFactorX/ZoomFactorY**: Controls the zoom level in the X and Y axes (range: **0-1**, default: **1**).
- **ZoomPositionX/ZoomPositionY**: Specifies the scrollbar position for the zoomed-in axes.

## Code Examples

#### C# Example for Programmatic Zooming
```csharp
// Set Zoom Factor
chart1.Model.ZoomFactorX = 0.5;
chart1.Model.ZoomFactorY = 0.5;

// Set Zoom Position
chart1.Model.ZoomPositionX = 0;
chart1.Model.ZoomPositionY = 100;
```

## Page-level Navigation/TOC (if applicable)

- Zooming and Scrollbar Behavior
  - ScrollPrecision
  - Zoom Out Button
  - ZoomOutIncrement
- Programmatic Zooming
  - Zoom Factor
  - Scrollbar Position

## Cross References

- Refer to the Essential Chart documentation for more details on scrollbars and zooming functionalities.

<!-- tags: Essential Chart, Windows Forms, Zooming, Scrollbars, ZoomFactor, ZoomOutIncrement, programmatic zooming, chart, scroll precision, Windows Forms User Guide version 11.4.0.26 -->
```