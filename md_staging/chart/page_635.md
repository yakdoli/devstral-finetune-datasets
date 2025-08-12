```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_635.jpeg
document_name: chart
page_number: 635
page_id: chart#page_635
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:43Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Search functionality for chart points.
- Finding minimum or maximum values within specified ranges.
- Printing charts across multiple pages.

## Content

### Functionality Summary
The following table describes the functionality of chart search methods:

| Method | Description |
| --- | --- |
| search should start at the specified index. |
| FindMinValue(String, Index, Index) | It should return the first Chart point with a minimum value. The search should start and end at the specified index. |

### Example Code for Finding Maximum Value

#### [C#]
```csharp
String str = txBxString.Text;
staIdx = Int32.Parse(txBxIndex.Text);
endIdx = Int32.Parse(textBox1.Text);
ChartPoint dp4 = this.chartControl1.Series[0].Summary.FindMaxValue(str, ref staIdx, endIdx);
```

#### [VB.NET]
```vbnet
Dim str As String = txBxString.Text
staIdx = Int32.Parse(txBxIndex.Text)
endIdx = Int32.Parse(textBox1.Text)
Dim dp4 As ChartPoint =
Me.chartControl1.Series(0).Summary.FindMaxValue(str, staIdx, endIdx)
```

### Section: 5.17 How to Print a Chart in Multiple Pages

To print a Chart in multiple pages, use the `PrintPage` event to specify the range of X and Y axis. Specify the minimum and maximum value in the `Range` property of the axis you want to divide. Set the `HasMorePages` property to true in the events before specifying the range values and set this to false after chart default maximum value. The following code illustrates this:

#### [C#]
```csharp
this.chartControl1.PrintDocument.PrintPage += new
System.Drawing.Printing.PrintPageEventHandler(PrintDocument_PrintPage);

// PrintPage Event

void PrintDocument_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
{
    if (textBox1.Text == "")
}
```

## API Reference

- **Methods**
  - `FindMaxValue(String, Integer, Integer)`: Returns the Chart point with the maximum value within the specified range.
  - `PrintDocument_PrintPage`: Event handler for customizing the printing process.

## Code Examples

The above sections include multiple code examples demonstrating how to find maximum/minimum values within specified ranges and how to print charts across multiple pages.

<!-- tags: [Windows Forms, Chart Control, PrintPage Event, Multiple Page Printing, Syncfusion Winforms, 11.4.0.26] keywords: [chart, findmaxvalue, findminvalue, printpage, multiple pages, maxvalue, minvalue] -->
```