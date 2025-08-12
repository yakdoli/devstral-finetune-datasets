```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_634.jpeg
document_name: chart
page_number: 634
page_id: chart#page_634
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:57:18Z
fidelity: lossless
--> 

## Overview

- Describes methods for finding maximum and minimum values in chart point collections within Syncfusion WinForms.
- Explains the use of `FindMaxValue` and `FindMinValue` methods with different parameters to specify search criteria and ranges.
- Includes code examples in C# and VB.NET for implementing these methods.

## Content

### Essential Chart for Windows Forms

The following table describes the various overloads of the `FindMaxValue` method:

| Method | Description |
| --- | --- |
| `FindMaxValue()` | It should return the first chart point in the collection with a maximum first Y-value. The search always should start at the beginning of the collection. |
| `FindMaxValue(String)` | It should return the first chart point in the collection with the maximum specified value. The search always should start at the beginning of the collection. |
| `FindMaxValue(String, index)` | It should return the first chart point with a maximum value. The search should start at the specified index. |
| `FindMaxValue(String, Index, Index)` | It should return the first chart point with a maximum value. The search should start and end at the specified index. |

#### Code Examples

##### C#

```csharp
String str = txBxString.Text;
staIndx = Int32.Parse(txBxIndex.Text);
endIndx = Int32.Parse(textBox1.Text);
ChartPoint dp4 = this.chartControl1.Series[0].Summary.FindMinValue(str, ref staIndx, endIndx);
```

##### VB.NET

```vbnet
Dim str As String = txBxString.Text
staIndx = Int32.Parse(txBxIndex.Text)
endIndx = Int32.Parse(textBox1.Text)
Dim dp4 As ChartPoint =
Me.chartControl1.Series(0).Summary.FindMinValue(str, ref staIndx, endIndx)
```

### FindMinimumvalue

The following table describes the methods for finding the minimum value in chart point collections:

| Method | Description |
| --- | --- |
| `FindMinValue()` | It should return the first chart point in the collection that has a first Y-value that is equal to the series' minimum Y1 value. The search always should start at the beginning of the collection. |
| `FindMinValue(String)` | It should return the first chart point in the collection that has an X or Y-value that is equal to the series' minimum value. The search always should start at the beginning of the collection. |
| `FindMinValue(String, index)` | It should return the first Chart point with a minimum value. The |

## Cross References

- See also: Other charting functionalities, data handling, and WinForms integration in Syncfusion documentation.

<!-- tags: [Syncfusion, WinForms, Chart, Methods, FindMaxValue, FindMinValue] keywords: [ChartPoint, Series, Collection, Maximum, Minimum, Value, Search, Index] -->
```