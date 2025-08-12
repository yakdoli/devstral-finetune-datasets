```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: grouping
page_number: 037
page_id: grouping#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:12Z
fidelity: lossless
-->

## Essential Grouping

### VB.NET Code Example

```vb
' Show all records under the TopLevelGroup.
ShowRecordsUnderGroup(groupingEngine.Table.TopLevelGroup)

' Pause
Console.ReadLine()
```

## 4.2.3 Adding a Summary

**Overview**
- Essential Grouping allows summarizing data by adding `SummaryDescriptor` objects to the schema information stored in the `Engine.TableDescriptor.Summaries` collection.
- Multiple summaries can be added by including several `SummaryDescriptors`.

### Content

Essential Grouping lets you summarize your data by adding `SummaryDescriptor` objects to the schema information that is stored in the `Engine.TableDescriptor.Summaries` collection. You can have multiple summaries by adding several `SummaryDescriptors`.

At the bottom of the Main method, add this code to create a summary item for the Engine.

#### C# Example

```csharp
// Create a summary that computes the Int32Aggregate calculations on property B.
SummaryDescriptor sdBInt32Agg = new SummaryDescriptor("BInt32Agg", "B", SummaryType.Int32Aggregate);

// Add this summary to the Summaries collection.
groupingEngine.TableDescriptor.Summaries.Add(sdBInt32Agg);
```

#### VB.NET Example

```vb
' Create a summary that computes the Int32Aggregate calculations on property B.
Dim sdBInt32Agg As New SummaryDescriptor("BInt32Agg", "B", SummaryType.Int32Aggregate)

' Add this summary to the Summaries collection.
groupingEngine.TableDescriptor.Summaries.Add(sdBInt32Agg)
```

### Additional Notes

- There are several overloads of the constructor for `SummaryDescriptor`. Here, we are using the overload that accepts a `SummaryType` enum as the third argument.
- The `SummaryType` enum allows you to pick out some predefined calculations such as the `Int32Aggregate` functions like `Max`, `Min`, `Sum`, and `Average`.
- There are enums that specify double, boolean, and other aggregate types.
- Here, we choose `Int32` as that is the type of value you will see in the `B` property in the data.

---

<!-- tags: [product, module, control, api, version?] keywords: [grouping, summarydescriptor, sum, max, min, average, int32aggregate, Engine.TableDescriptor.Summaries, EssentialGrouping] -->
```