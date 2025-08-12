```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_524.jpeg
document_name: chart
page_number: 524
page_id: chart#page_524
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:16Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

The following output is displayed when the Skins value is set to VS2010.

![Chart with Skins](attachment://Figure_345_VS2010.png)

*Figure 345: VS2010*

### Code Example

```csharp
ChartSeries ser1 = new ChartSeries("Series 1");
ser1.Type = ChartSeriesType.StackingColumn;
// specifying group name .
ser1.StackingGroup = "FirstGroup";
ChartSeries ser2 = new ChartSeries("Series 2");
ser2.Type = ChartSeriesType.StackingColumn;
// specifying group name .
ser2.StackingGroup = "SecondGroup";
ChartSeries ser3 = new ChartSeries("Series 3");
```

## Page-level Navigation/TOC
- [Essential Chart for Windows Forms](#Essential-Chart-for-Windows-Forms)

## Cross References
- See also: [Syncfusion Winforms Documentation](https://www.syncfusion.com/products/winforms/documentation)

<!-- tags: [syncfusion, winforms, chart, visual studio 2010, stackingcolumn] keywords: [chartseries, stackinggroup, essential chart, windows forms, vs2010] -->
```