<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_063.jpeg
document_name: grouping
page_number: 063
page_id: grouping#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:19Z
fidelity: lossless
-->

# Essential Grouping

## 5.4 How to Add Summary Items?

Essential Grouping lets you summarize data by adding SummaryDescriptor objects to the schema information stored in the Engine.TableDescriptor.Summaries collection. You can have multiple summaries by adding several SummaryDescriptors.

### Code Examples

```csharp
[C#]

// Create a summary that computes the Int32Aggregate calculations on field B.
SummaryDescriptor sdInt32Agg = new SummaryDescriptor("BInt32Agg", "B", 
    SummaryType.Int32Aggregate);

// Add this summary to the Summaries collection.
groupingEngine.TableDescriptor.Summaries.Add(sdInt32Agg);
```

```vb
[VB.NET]

' Create a summary that computes the Int32Aggregate calculations on property B.
Dim sdInt32Agg As New SummaryDescriptor("BInt32Agg", "B", 
    SummaryType.Int32Aggregate)

' Add this summary to the Summaries collection.
groupingEngine.TableDescriptor.Summaries.Add(sdInt32Agg)
```

### Note

There are several overloads of the constructor for the SummaryDescriptor. We are using the overload that accepts a SummaryType enum as the third argument. This SummaryType will allow you to pick out some predefined calculations such as the Int32Aggregate functions like Max, Min, Sum, and Average. There are enums that specify double, boolean, and other aggregate types. Here we choose Int32 as that is the type of value we see in the B property in the data.

## 5.5 How to Bind a Datasource to the Grouping Engine?

Essential Grouping can use any IList object holding objects and a common System.Type as its datasource. The public properties of the common type can be used to group, sort and summarize the data in the IList.

### Example

The following code shows how to set an IList object to be the data source of a GroupingEngine object. Within Essential Grouping, the items in your IList datasource are referred to as records.

## Page-level Navigation/TOC (if applicable)
- 5.4 How to Add Summary Items?
- 5.5 How to Bind a Datasource to the Grouping Engine?

## Cross References
See also: Grouping Engine, SummaryDescriptor, TableDescriptor, Summaries collection, IList, System.Type.

## RAG Annotations
<!-- tags: [Syncfusion, Windows Forms, Grouping, SummaryDescriptor, TableDescriptor, IList, System.Type] keywords: [grouping engine, summaries, data source, aggregate calculations, summary types, add summary, bind data source, Essential Grouping] -->
