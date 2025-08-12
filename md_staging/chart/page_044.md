```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: chart
page_number: 044
page_id: chart#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:21Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

There is however no DESIGN-TIME support for data binding. This has to be setup in code.

## Content

### Binding a DataSet to the Chart

### Data binding via custom interfaces

There is also a more flexible support for implementing custom data models by implementing specific interfaces. Using this approach you can query and provide data for the chart much more flexibly and from any kind of data store.

#### Note

One important reason you might want to use either of the above two approaches is to greatly enhance performance (speed and memory) especially while dealing with a large set of data points.

### See Also

[Implementing Custom Data Binding Interfaces](Implementing Custom Data Binding Interfaces)

#### 4.2.1 Binding a DataSet to the Chart

The following sample code illustrates how a custom `DataSet` can be bound to a `ChartSeries` to provide data points and to a `ChartAxis` to provide label names. Note that the `DataSet` can easily be replaced with a `DataTable` or `DataView`.

```html
<Demographics...hartData.mdb>
```

| ID | City       | Population |
|----|------------|------------|
| 1  | New York   | 13         |
| 2  | Houston    | 6          |
| 3  | Tokyo      | 17         |
| 4  | London     | 15         |
| 5  | Los Angeles | 11         |

Figure 24: Access Table data that is about to get bound to Chart

### Code Example

```csharp
[C#]
```

## API Reference

- **Namespace**: Not explicitly mentioned in the text.
- **Class**: Not explicitly mentioned in the text.
- **Methods/Properties/Events**: `DataSet`, `ChartSeries`, `ChartAxis`, `DataTable`, `DataView`.

### Code Examples (multi-language supported)

- **Language**: C#
  
```csharp
// Sample code for binding DataSet to Chart
using System.Data;
using Syncfusion.Windows.Forms.Chart; // Assuming the usage of Syncfusion's Chart control

// Assuming the Access database connection is established
// And assuming the query has been executed to populate the dataset
DataSet demoDataSet = new DataSet();
// Populate demoDataSet from the database (procedure not shown here)

// Assuming the chart control is already added to the form as an instance named demoChart

// Binding DataSet to ChartSeries for data points
ChartSeries series = new ChartSeries("Population");
series.Binding.DataMember = "Population";
series.Binding.DataSource = demoDataSet.Tables[0];
demoChart.Series.Add(series);

// Binding DataSet to ChartAxis for label names
ChartAxis axis = new ChartAxis();
axis.Binding.DataMember = "City";
axis.Binding.DataSource = demoDataSet.Tables[0];
demoChart.PrimaryXAxis = axis;
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Chart, DataSet, Data Binding] keywords: [Syncfusion, Winforms, Chart, DataSet, Data Binding, Custom Data Binding, DataTable, DataView, Performance Enhancement] -->
```