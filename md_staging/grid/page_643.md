```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_643.jpeg
document_name: grid
page_number: 643
page_id: grid#page_643
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:30:45Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

```csharp
GridListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate
Me.gridGroupingControl1.SortPositionChangedBehavior = 
GridListChangedInsertRemoveBehavior.ScrollWithImmediateUpdate

Me.gridGroupingControl1.BindToCurrencyManager = False

' Enable Caption Summaries.
gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowCaptionSummaryCells = True
gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowSummaries = True
gridGroupingControl1.TableDescriptor.ChildGroupOptions.CaptionSummaryRow = "Caption"
```

### Setting Up ManualTotalSummary

- **Setup ManualTotalSummary for the columns Freight and EmployeeID.**  
  The `ManualTotalSummary.Total` value will be retrieved and displayed in a summary or caption cell in the `QueryCellStyleInfo` event handler. It tracks the changes in the sort positions of the columns `Freight` and `EmployeeID` by handling the `PropertyChanges` event.

### Code Implementation

[C#]

```csharp
ManualTotalSummaryTable tb = 
    (ManualTotalSummaryTable)this.gridGroupingControl1.Table;
tb.TotalSummaries.Add("Freight");
tb.TotalSummaries.Add("EmployeeID");
tb.TableDirty = true;

this.gridGroupingControl1.QueryCellStyleInfo += 
    new GridTableCellStyleInfoEventHandler(gridGroupingControl1_QueryCellStyleInfo);

private void gridGroupingControl1_QueryCellStyleInfo(object sender, 
    GridTableCellStyleInfoEventArgs e)
{
    Element el = e.TableCellIdentity.DisplayElement;
    ManualTotalSummaryTable table = el.ParentTable as
        ManualTotalSummaryTable;

    if (table == null)
        return;

    if (Element.IsCaption(el))
    {
        if (e.Style.TableCellIdentity.ColIndex > 3)
        {
            // You need to provide manually, the code to look up the
            // summaries you want to display here.
            // e.TableCellIdentity.Column and
        }
    }
}
```

## API Reference

- **ManualTotalSummaryTable**:  
  - `TotalSummaries`: Collection where you can add summary columns like `Freight` and `EmployeeID`.
  - `TableDirty`: Indicates if the table structure needs to be invalidated for updates.

## Code Examples

The example above demonstrates how to enable and configure manual total summaries for specific columns in a Grid Grouping Control, ensuring that the summary values are displayed correctly after sorting changes.

## Cross References

- See also:  
  - [Grid Grouping Control Overview](#overview-grid-grouping-control)
  - [Handling Event Handlers in Grid Controls](#handling-event-handlers)

<!-- tags: [essential grid, grid grouping control, windows forms, manual total summary, event handling] keywords: [freight, employeeid, caption summary, property changes, manual summary, grid control, windows forms, syncfusion] -->
```