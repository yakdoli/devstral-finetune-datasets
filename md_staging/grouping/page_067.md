```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: grouping
page_number: 067
page_id: grouping#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:37Z
fidelity: lossless
-->

# Essential Grouping

- "[B] = 5 OR [B] < 0"
- "[D] LIKE 'd1' OR [B] = 2"

### Sample Code

```csharp
[C#]

// Filter on [D] = d1
RecordFilterDescriptor rfd = new RecordFilterDescriptor("[D] LIKE 'd1'");
this.groupingEngine.TableDescriptor.RecordFilters.Add(rfd);
```

```vbnet
[VB.NET]

' Filter on [D] = d1
Dim rfd As New RecordFilterDescriptor("[D] LIKE 'd1'")
Me.groupingEngine.TableDescriptor.RecordFilters.Add(rfd)
```

## 5.10 How to Group a Collection?

To sort your data, add the name of the property you want to sort to the **Engine.TableDescriptor.GroupedColumns** collection.

```csharp
[C#]

// Group column A.
groupingEngine.TableDescriptor.GroupedColumns.Add("A");
```

```vbnet
[VB.NET]

' Group column A.
groupingEngine.TableDescriptor.GroupedColumns.Add("A")
```

## 5.11 How to Retrieve Summary Item Values?

Summaries are calculated on groups of records. The **TopLevelGroup** is the collection of all records in the **IList** data source. If you have added additional grouping through the **groupingEngine.TableDescriptor.GroupedColumns.Add**, then in addition to the top level group, there will be additional groups available to you. Each group will have an associated summary value. So to retrieve a summary value, you need to specify the group associated with the summary.

<!-- tags: [grouping, filtering, sorting, summaries, data source, groups, records, summary values] keywords: [group, filter, sort, summary, record, data, values] -->
```