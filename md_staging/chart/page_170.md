```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: chart
page_number: 170
page_id: chart#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:26Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Chart Data Points and Axis Value Types

#### Chart Data Point Examples

[C#]

```csharp
// Option 1: 1 X double value; 2 double Y values in a point
series1.Points.Add(0, 2.5, 3.5);

// Option 2: 1 X double value; 1 DateTime Y value
series2.Points.Add(1, DateTime.Now);

// Option 3: 1 X DateTime value; 1 double Y value
series1.Points.Add(DateTime.Now, 5.3);
```

[VB.NET]

```vbnet
' Option 1: 1 X double value; 2 double Y values in a point
series1.Points.Add(0, 2.5, 3.5)

' Option 2: 1 X double value; 1 DateTime Y value
series2.Points.Add(1, DateTime.Now)

' Option 3: 1 X DateTime value; 1 double Y value
series1.Points.Add(DateTime.Now, 5.3)
```

---

### **ValueType**

**Always use the `ChartAxis.ValueType` property to specify what kind of values you have added in the series data points for the corresponding axis.**

```csharp
// To specify DateTime values in the X axis
this.chartControl1.PrimaryXAxis.ValueType = ChartValueType.DateTime;

// To specify Double values
this.chartControl1.PrimaryXAxis.ValueType = ChartValueType.Double;
```

[VB.NET]

```vbnet
' To specify DateTime values in the X axis
Me.chartControl1.PrimaryXAxis.ValueType = ChartValueType.DateTime

' To specify Double values
Me.chartControl1.PrimaryXAxis.ValueType = ChartValueType.Double
```

---

## API Reference

- **ChartAxis.ValueType**: Specifies the type of values used in the corresponding axis. The possible values are:
  - `ChartValueType.DateTime`
  - `ChartValueType.Double`
  - `ChartValueType.String`
  - `ChartValueType.Int`

- **Points.Add**: Adds a data point to the series. Overloaded methods allow adding data points with different combinations of X and Y values.

---

### Code Examples

#### Adding Data Points

##### C#

```csharp
// Example of adding a DateTime value as X and a Double as Y
series1.Points.Add(DateTime.Now, 5.3);
```

##### VB.NET

```vbnet
' Example of adding a DateTime value as X and a Double as Y
series1.Points.Add(DateTime.Now, 5.3)
```

---

### Notes

- Always ensure that the `ChartAxis.ValueType` property is correctly set to avoid mismatch errors when rendering the chart.
- The `Points.Add` method can handle various data types for X and Y axes based on the specified `ValueType`.

---

<!-- tags: [syncfusion-winforms, chart-winforms, axis-support, data-points, datatype-support] 
     keywords: [chartaxis, valuetype, chartvalue, value type, datetime, double, add points, csharp, vb.net, axis configuration] -->
```