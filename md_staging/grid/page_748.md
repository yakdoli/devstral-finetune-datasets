```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_748.jpeg
document_name: grid
page_number: 748
page_id: grid#page_748
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
srd.SummaryColumns.Add(scd);
srd.Appearance.AnySummaryCell.Interior = new
BrushInfo(Color.FromArgb(255, 231, 162));
```

Finally add the Summary Row into the grouping grid.

## C#

```csharp
this.gridGroupingControl1.TableDescriptor.SummaryRows.Add(srd);
```

## VB.NET

```vb
Me.gridGroupingControl1.TableDescriptor.SummaryRows.Add(srd)
```

4. Run the sample. The grid will look like this.

![Summary created Through Code for "Wins" Column](https://example.com/summary-created-through-code-for-wins-column.png)

**Figure 299: Summary created Through Code for "Wins" Column**

*Note: For more details, refer the following browser sample:*

```html
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Calculate Summary\Summary Tutorial
```

## Page-level Navigation/TOC (if applicable)
- None

## Cross References
- None

<!-- tags: [product, module, control, api, version?] keywords: [wins, summary row, summary column, gridgroupingcontrol, tabledescriptor, essential grid, windows forms, ado.net data control, version 11.4.0.26] -->
```