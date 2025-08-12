```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_370.jpeg
document_name: chart
page_number: 370
page_id: chart#page_370
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:03Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## CustomPoints Collection Editor during Design Time

![Figure 238: CustomPoints Collection Editor during Design Time](ChartCustomPoint_Collection_Editor_During_Design_Time.png)

## ChartControl with a Custom Point

![Figure 239: ChartControl with a Custom Point](ChartControl_with_Custom_Point.png)

## Programmatically

### Personalized Appearance Settings

The `ChartCustomPoint` allows for the customization of individual data points within a chart series. Below are the key appearance settings for custom points:

- **Alignment**: Sets the direction of the label or marker relative to the custom point. 
- **Border**: Specifies the style and appearance of the border around the custom point.
- **Color**: Defines the color of the custom point itself.
- **Font**: Determines the font style of any labels or text associated with the custom point.
- **Interior**: Describes whether the custom point is filled, and if so, with what color or transparency.
- **ShowMarker**: Indicates whether a marker should be displayed at the custom point.
- **Symbol**: Specifies the shape of the custom point, such as a diamond in the example.

### Customization Example

The following example demonstrates how to programmatically add and customize a `ChartCustomPoint`:

```csharp
// Create a new ChartCustomPoint
ChartCustomPoint customPoint = new ChartCustomPoint() {
    Shape = CustomPointShape.Diamond,
    Color = Color.Khaki,
    ShowMarker = true,
    Size = new Size(10, 10)
};

// Assign the custom point to a specific data point
chart.Series[0].Points[1].CustomPoints.Add(customPoint);
```

### Key Properties and Methods

#### ChartCustomPoint

| Property             | Description                                                                                                                                               |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Shape**           | Specifies the shape of the custom point. Options include Circle, Diamond, Rect, etc.                                                                     |
| **Color**           | Defines the color of the custom point.                                                                                                                   |
| **ShowMarker**      | Indicates whether the custom point should be displayed on the chart.                                                                                   |
| **Size**            | Specifies the size of the custom point.                                                                                                                   |

---

#### Chart Series Point

| Method               | Description                                                                                                                                                |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Add_customPoint** | Adds the custom point to the data point in the series.                                                                                                   |

### Conclusion

The `ChartCustomPoint` provides a powerful mechanism for enhancing data visualization by allowing detailed customization of individual data points. This feature can be particularly useful for highlighting important data points or adding visual cues directly on the chart.

### See also:
- Syncfusion.Windows.Forms.Chart.ChartCustomPoint
- Syncfusion.Windows.Forms.Chart.ChartSeries.Points

<!-- tags: [chart, windows forms, custom point, appearance, Syncfusion Winforms, design time] keywords: [customization, ChartCustomPoint, alignment, border, color, font, size, marker, shape] -->
```
