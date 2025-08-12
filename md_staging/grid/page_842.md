```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_842.jpeg
document_name: grid
page_number: 842
page_id: grid#page_842
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:08Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### WinForms-specific conventions

#### Code Example

```csharp
End If
End Sub
```

## 4.3.4.4 Paging Support in GridGrouping Control

### Overview

- This functionality enhances the performance of the GridGrouping control by providing paging support in Windows Grid.
- It loads data efficiently by storing and retrieving records in pages.
- Each page contains up to 100 records, reducing load time compared to displaying all records on a single page.
- Filters are customized to perform filtering on the current page only.
- Navigation through the retrieved records is facilitated via Arrow buttons in the Record Navigation control.

### Paging Functionality

GridGrouping control supports paging for various data source items using a `Pager` that extracts specific pages from the bound data source and binds them to the control.

#### Example: Using a Pager

```csharp
[C#]
var pager = new Pager { PageSize = 1000 };
pager.Wire(gridGroupingControl, dt); // dt is a DataTable object

[VB]
Dim pager = New Pager With {PageSize = 1000}
pager.Wire(gridGroupingControl, dt) ' dt is a DataTable object
```

### Filtering with Paging

While filtering may be restricted to records on the currently displayed page, this can be addressed by binding the view to a temporary table.

#### Example: Enabling Filtering

```csharp
[C#]
gridGroupingControl.TopLevelGroupOptions.ShowFilterBar = true;
foreach (var col in _gridGroupingControl2.TableDescriptor.Columns)
    col.AllowFilter = true;
```

## References

- **See also:**
  - [Pager Documentation](https://www.syncfusion.com/documentation/windowsforms/pager)

### Notes

- Ensure that the pagination size is set appropriately for optimal performance.
- Customize filters based on user requirements for efficient data retrieval.
- Consider using a temporary table for filtering to overcome any limitations.

<!-- tags: [windowsforms, gridgroupingcontrol, paging, filtering, syncfusion, version:11.4.0.26] keywords: [GridGrouping, Pager, Filtering, Load Time, Temporary Table, Arrow Buttons, DataTable, Performance, Page Size] -->
```