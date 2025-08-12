```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_633.jpeg
document_name: chart
page_number: 633
page_id: chart#page_633
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:54:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## 5.16 How to find value, maximum value and minimum value of the data points

Essential Chart has `FindValue`, `FindMaximumValue` and `FindMinimumValue` methods that can return the corresponding chart data point values depending upon the parameter(s) passed to these methods.

All these methods are overloaded.

### Find Value

| Method                      | Description                                                                                                                      |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `FindValue(Double)`         | It should return the first chart point in the collection that has a specified first Y-value. The search always should start at the beginning of the collection. |
| `FindValue(Double, String)` | It should return the first chart point in the collection with the specified X or Y-value.                                        |
| `FindValue(Double, String, index)` | It should return the first chart point with the specified X or Y-value, and should start the search at the specified index. |
| `FindValue(Double, String, Index, Index)` | It should return the first chart point with the specified X or Y-value, and should start and end the search at the specified index. |

**C#**

```csharp
dbl = Int64.Parse(txBxValue.Text);
ChartPoint dp1 = this.chartControl1.Series[0].Summary.FindValue(db1);
```

**VB.NET**

```vb
dbl = Int64.Parse(txBxValue.Text)
Dim dp1 As ChartPoint = 
Me.chartControl1.Series(0).Summary.FindValue(db1)
```

### FindMaximumValue

| Method | Description |
|--------|-------------|

### FindMinimumValue

| Method | Description |
|--------|-------------|

## API Reference (if applicable)

### WinForms-specific conventions

- `Namespace.Class`: EssentialChart.Chart
- Methods:
  - `FindValue(Double)`
  - `FindValue(Double, String)`
  - `FindValue(Double, String, index)`
  - `FindValue(Double, String, Index, Index)`
  - `FindMaximumValue`
  - `FindMinimumValue`

## Code Examples (multi-language supported)

- **C#**

```csharp
// Example of finding a data point with a specific Y-value
var dp1 = this.chartControl1.Series[0].Summary.FindValue(10.5);
```

- **VB.NET**

```vb
' Example of finding a data point with a specific Y-value
Dim dp1 As ChartPoint = 
Me.chartControl1.Series(0).Summary.FindValue(10.5)
```

## Cross References

- `FindMinimumValue` method
- `FindMaximumValue` method

### Useful Links

- [Syncfusion Documentation: Charts](https://help.syncfusion.com/windowsforms/chart)
- [Syncfusion WinForms NuGet Package](https://www.nuget.org/packages/Syncfusion.EssentialStudio.Windows)

### RAG Annotations

- **Keywords**: `FindValue`, `FindMaximumValue`, `FindMinimumValue`, `chart data point`, `value search`, `maximum value`, `minimum value`
- **Tags**: `Syncfusion`, `WindowsForms`, `Chart`, `DataPoint`, `API`, `version 11.4.0.26`

```html
```