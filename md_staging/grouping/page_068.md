```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: grouping
page_number: 068
page_id: grouping#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:36Z
fidelity: lossless
-->

# Essential Grouping

For example, the code below assumes that you have grouped the table on field "C" and are looking for the summary associated with the group whose records have field "C" equal to the value "c1". It also shows the same summary value for the TopLevelGroup.

## C#

```csharp
// To simplify notation, set this using the statement at the top of your code file.
using ISummary = Syncfusion.Collections.BinaryTree.ITreeTableSummary;

// Now get the Summary value for the TopLevelGroup group.
ISummary groupSummary =
groupingEngine.Table.TopLevelGroup.GetSummary("BInt32Agg");
Int32AggregateSummary int32Summary = (Int32AggregateSummary) groupSummary;

Console.WriteLine("whole table {0}, {1}, {2}", int32Summary.Sum,
int32Summary.Average, int32Summary.Maximum);

// Value for "c1" group.
groupSummary =
groupingEngine.Table.TopLevelGroup.Groups["c1"].GetSummary("BInt32Agg");
int32Summary = (Int32AggregateSummary) groupSummary;

Console.WriteLine("c1-group {0}, {1}, {2}", int32Summary.Sum,
int32Summary.Average, int32Summary.Maximum);
```

## VB.NET

```vb.net
' To simplify notation, set this using the statement at the top of your code file.
Imports ISummary = Syncfusion.Collections.BinaryTree.ITreeTableSummary

' Now get the Summary value for the TopLevelGroup group.
Private groupSummary As ISummary =
groupingEngine.Table.TopLevelGroup.GetSummary("BInt32Agg")
Private int32Summary As Int32AggregateSummary = CType(groupSummary,
Int32AggregateSummary)

Console.WriteLine("whole table {0}, {1}, {2}", int32Summary.Sum,
int32Summary.Average, int32Summary.Maximum)

' Value for "c1" group.
Private groupSummary =
groupingEngine.Table.TopLevelGroup.Groups("c1").GetSummary("BInt32Agg")
Private int32Summary = CType(groupSummary, Int32AggregateSummary)
```

<!-- tags: [product, module, control, api, version?] keywords: [grouping, C#, VB.NET, summary, Table, TopLevelGroup, Group, GetSummary, BInt32Agg, Int32AggregateSummary, Syncfusion Winforms, 11.4.0.26] -->
```