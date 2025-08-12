```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_047.jpeg
document_name: chart
page_number: 047
page_id: chart#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:03Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### 4.2.2 Implementing Custom Data Binding Interfaces

**Overview**

- Explains how to implement custom data binding interfaces for the chart in Windows Forms applications.
- Highlights the use of the `IChartSeriesModel` interface for custom data binding.
- Demonstrates how to create a custom implementation of `IChartSeriesModel`, such as `ArrayModel`, which adheres to the interface requirements.

**Content**

Note that the `ChartDataBindModel` type in the previous topic implements a simple interface called `IChartSeriesModel`. This interface requires the implementation of one property, two methods, and one optional event. So, you can easily provide a custom implementation of this interface instead of using the `ChartDataBindModel`.

Shown below is some sample code that implements `IChartSeriesModel` interface for use with the chart.

```csharp
[C#]

// Custom Model
public class ArrayModel : IChartSeriesModel
{
    private double[] data;

    public ArrayModel(double[] data)
    {
        this.data = data;
    }

    // Returns the number of points in this series.
    public int Count
    {
        get
        {
            return this.data.GetLength(0);
        }
    }

    // Returns the Y value of the series at the specified point index.
    public double[] GetY(int xIndex)
    {
        return new double[] { data[xIndex] };
    }

    // Returns the X value of the series at the specified point index.
    public double GetX(int xIndex)
    {
```

## API Reference (if applicable)
- Samples demonstrate the implementation of `IChartSeriesModel` interface methods and properties.
- Classes demonstrated include:
  - `ArrayModel` as a concrete implementation example.

## Code Examples (multi-language supported)
- Example provided implements `IChartSeriesModel` using a custom class `ArrayModel`.

## Cross References
- For more on data binding with the chart, refer to the relevant sections of the user guide.
- Refer to the `IChartSeriesModel` interface documentation for specific requirements.

<!-- tags: [Syncfusion, Winforms, chart, data binding, IChartSeriesModel, custom implementation] keywords: [ChartDataBindModel, Interface Implementation, Custom Model, Data points, X value, Y value] -->
```