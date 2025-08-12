```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_761.jpeg
document_name: grid
page_number: 761
page_id: grid#page_761
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:11Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Code Example

```csharp
gsd.SetGroupSummarySortOrder(summaryColumn1.GetSummaryDescriptorName(), "Average")

Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Add(gsd)
```

### Sorting Groups by Summary Values

4. When you run the sample, you will see the groups are sorted against the summary values of Freight. Here is a sample screen shot.

![Figure 305: Sorting Groups by Summary Values](https://i.imgur.com/screenshot.jpg)

**Figure 305: Sorting Groups by Summary Values**

**Note:** For more details, refer the following browser sample:

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Calculate Summary\Sort by Summary Demo
```

### 4.3.4.3 Filters and Expressions

Grouping Grid supports record filters and expression fields. Record Filters let you display a subset of records that meets a given filter criteria. Expression Fields are unbound fields added to the grouping grid that can be used to display any calculation results based on other fields in the same record.

## Footer
© 2013 Syncfusion. All rights reserved.

<!--tags: [product, grid, windows forms, syncfusion-sdk, 11.4.0.26] keywords: [essential grid, record filters, expression fields, group summary sorting, freight summary, windows forms, syncfusion, user guide] -->
```