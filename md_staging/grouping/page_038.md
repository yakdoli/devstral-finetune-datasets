```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_038.jpeg
document_name: grouping
page_number: 038
page_id: grouping#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:56Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Retrieves Summary Values for a particular group.
- Maintains summary items by group basis in the GroupingEngine.
- Demonstrates obtaining summary values for specified groups using the GetSummary method.

## Content

### Getting Summary Values for a Particular Group

**4.2.4 Retrieving Summary Values for a Particular Group**

After adding the `SummaryDescriptor`, the `GroupingEngine` will maintain these summary items in a group by group basis. You can access these summary values for any group. Here we will get the values for the `TopLevelGroup` and for our `c1` group to illustrate how this is done.

To obtain a particular group's summary values, you need to get the group and access the summary through its `GetSummary` method. Once you have the summary, you can cast it to its `Int32AggregateSummary` type.

The following code snippet illustrates this.

#### Code Example in C#

```csharp
[C#]

// To simplify notation, add this statement at the top of the file.
using ISummary = Syncfusion.Collections.BinaryTree.ITreeTableSummary;

// At the bottom of the Main method, add these lines.

// Now go through the group to get the Summary value for the group.
ISummary groupSummary =
groupingEngine.Table.TopLevelGroup.GetSummary("BInt32Agg");
Int32AggregateSummary int32Summary = (Int32AggregateSummary) groupSummary;

Console.WriteLine("whole table {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum);

// Value for "cl" group.
groupSummary =
groupingEngine.Table.TopLevelGroup.Groups["c1"].GetSummary("BInt32Agg");
int32Summary = (Int32AggregateSummary) groupSummary;

Console.WriteLine("c1-group {0}, {1}, {2}", int32Summary.Sum, int32Summary.Average,int32Summary. Maximum);

// Pause
Console.ReadLine();
```

#### Code Example in VB.NET

```vb.net
[VB.NET]

' At the bottom of the Main method, add these lines.

' Now go through the group to get the Summary value for the group.
```

## Page-Level Navigation/TOC (if applicable)
- 4.2.4 Retrieving Summary Values for a Particular Group

## Cross References
- See also: Section 4.2 for more details on using `SummaryDescriptor`.
- For additional functionality, refer to the `GroupingEngine` documentation.

<!-- tags: [Syncfusion Winforms, Grouping, SummaryValues, Retrieval, TopLevelGroup, SummaryDescriptor, GroupingEngine, Int32AggregateSummary] keywords: [GroupingEngine, SummaryDescriptor, Int32AggregateSummary, GetSummary, TopLevelGroup, c1 group] -->
```