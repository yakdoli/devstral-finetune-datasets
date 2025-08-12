```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_760.jpeg
document_name: grid
page_number: 760
page_id: grid#page_760
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:38:40Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### 2. Trigger caption summaries by setting appropriate properties.

```csharp
this.gridGroupingControl.TableDescriptor.ChildGroupOptions.ShowCaptionSummaryCells = true;
this.gridGroupingControl.TableDescriptor.ChildGroupOptions.CaptionSummaryRow = "Caption";
this.gridGroupingControl.TableDescriptor.ChildGroupOptions.ShowSummaries = false;
```

```vb.net
Me.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowCaptionSummaryCells = True
Me.gridGroupingControl1.TableDescriptor.ChildGroupOptions.CaptionSummaryRow = "Caption"
Me.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowSummaries = False
```

### 3. Create a SortColumnDescriptor for the field ShipCountry. Change the default group order by using the method SetGroupSummaryOrder with its parameters conveying the summary name and the property in the summary. Then group the grid against this column.

```csharp
// Specify group sort order behavior when adding SortColumnDescriptor to GroupedColumns
this.gridGroupingControl.TableDescriptor.GroupedColumns.Clear();
SortColumnDescriptor gsd = new SortColumnDescriptor("ShipCountry");

// specify a summary name and the property (values will be determined using reflection)
gsd.SetGroupSummarySortOrder(summaryColumn1.GetSummaryDescriptorName(), "Average");

this.gridGroupingControl.TableDescriptor.GroupedColumns.Add(gsd);
```

```vb.net
' Specify group sort order behavior when adding SortColumnDescriptor to GroupedColumns
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()
Dim gsd As New SortColumnDescriptor("ShipCountry")

' specify a summary name and the property (values will be determined using reflection)
```
```