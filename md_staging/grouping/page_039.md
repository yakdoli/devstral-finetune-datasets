```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_039.jpeg
document_name: grouping
page_number: 039
page_id: grouping#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:03Z
fidelity: lossless
-->

# Essential Grouping

```vbnet
Dim groupSummary As Syncfusion.Collections.BinaryTree.ITreeTable = ...
```

```vbnet
Dim int32Summary as Int32AggregateSummary = CType(groupSummary, Int32AggregateSummary)
Console.WriteLine("whole table {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum)

' Value for "c1" group.
groupSummary = groupingEngine.Table.TopLevelGroup.Groups("c1").GetSummary("BInt32Agg")
int32Summary = CType(groupSummary, Int32AggregateSummary)

Console.WriteLine("cl-group {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum)

' Pause
Console.ReadLine()
```

![Screenshot of the summary statistics displayed for the whole table and Group c1](https://i.imgur.com/image.png)

Figure 16: Summary Statistics Shown for the Whole Table and for Group c1

## 4.3 Data Manipulation

<!-- tags: [essential grouping, data manipulation, summary statistics, whole table, group, syncfusion winforms, version 11.4.0.26] keywords: [essential grouping, data manipulation, summary statistics, whole table, group, syncfusion winforms, version, csharp, vb net, api, code examples, grouping engine, table, top level group, groups, getsummary, cte, int32aggregatesummary, console.writeline, pause, read line, table manipulation, group manipulation, statistics calculation, example, code, summary, aggregate summary, table, group, whole, c1, cl group, average, maximum, sum,停顿,阅读行,整张表, ] -->
```