```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: chart
page_number: 052
page_id: chart#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:56Z
fidelity: lossless
-->

### ChartDataBindModel Example

#### Overview
- This example illustrates how to bind a non-indexed data source (an `ArrayList` of class instances) to a `Chart` using `ChartDataBindModel`.
- Demonstrates assigning the x-axis values through the `ChartDataBindAxisLabelModel` class.

#### Content

In this section, we explore how to bind a collection of class instances to a chart using `ChartDataBindModel`.

##### Code Example

```csharp
Private m_population As Double

Public Property Population() As Double
    Get
        Return m_population
    End Get
    Set(ByVal value As Double)
        m_population = value
    End Set
End Property
```

##### Explanation

If you have a class like the one above, you will typically have a collection of instances of this class, stored in an `ArrayList`. To bind this data to a chart, you need to create an instance of `ChartDataBindModel`, supplying the `ArrayList` as the data source.

In this specific example, we are binding non-indexed data, where the x-axis values will not be derived from the data source. Instead, the `x`-axis values will be assigned through the `ChartDataBindAxisLabelModel` class. This class provides functionality to bind axis labels directly from the data source.

##### Implementation

Below is the implementation demonstrating how to use `ChartDataBindModel` to bind data to a chart:

```csharp
[C#]

ArrayList populations = new ArrayList();
populations.Add(new PopulationData("New York", 13));
populations.Add(new PopulationData("Houston", 6));
populations.Add(new PopulationData("Tokyo", 17));
populations.Add(new PopulationData("London", 15));
populations.Add(new PopulationData("Los Angeles", 11));

ChartSeries series = new ChartSeries("Populations");
ChartDataBindModel dataSeriesModel = new ChartDataBindModel(populations);

// If ChartDataBindModel.XName is empty or null, X value is index of point.
// Here I have assigned the property name Population as Y axis name and ChartDataBindModel automatically detects the Population property and will bind the data from it.
dataSeriesModel.YNames = new string[] { "Population" };
```

This code creates an `ArrayList` of `PopulationData` objects, each representing a city and its corresponding population. The `ChartDataBindModel` is then used to bind this data to a `ChartSeries`. The `YNames` property is set to the name of the property (`Population`) that contains the y-axis data.

##### Key Points
- The `ChartDataBindModel` automatically detects the property specified in `YNames` and binds the data from it.
- If the `XName` is not specified, the x-axis values are automatically assigned based on the index of the points in the data source.

## Page-level Navigation/TOC (if applicable)

- **Overview**
- **Content**
  - Explanation of `ChartDataBindModel`
  - Code Example

## Cross References

- **Related Topics**
  - Data Binding in Charts
  - Chart Series

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, Chart, DataBinding, ChartSeries, ChartDataBindModel] keywords: [ChartDataBindModel, PopulationData, YNames, Population, ChartSeries, x-axis, Non-indexed data] -->
```