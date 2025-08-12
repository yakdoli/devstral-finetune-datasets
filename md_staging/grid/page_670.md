```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_670.jpeg
document_name: grid
page_number: 670
page_id: grid#page_670
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:28Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

Grouping a column which has Ilist bound reduces the time taken to refresh the control after grouping. The grouping performance has been improved with huge data loaded.

### Enable Grouping Optimization

Set `OptimizeIListGroupingPerformance` to `true` to enable grouping optimization over the Ilist data source.

The following code illustrates how to enable grouping optimization.

#### C#

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    gridGroupingControl1.OptimizedListGrouping = true;
}
```

#### VB

```vb
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    GridGroupingControl1.OptimizedListGrouping = True
End Sub
```

### Enable Real Time Updates

The `OptimizeIListGroupingPerformance` method has to be called to enable real time updates with the data source from the GridGroupingControl.

The following code illustrates how to enable real time updates.

#### C#

```csharp
void gridGroupingEmployee_SourceListListChanged(object sender, TableListChangedEventArgs e)
{
    this.gridGroupingEmployee.OptimizeIListGroupingPeformance(sender, e);
}
```

#### VB

```vb
Private Sub gridGroupingEmployee_SourceListListChanged(ByVal
```

## API Reference (if applicable)
- This section includes namespace, class, and method references related to the functionality described above.

#### C#
- `GridGroupingControl1`
  - Property: `OptimizedListGrouping`
  - Method: `OptimizeIListGroupingPerformance`

#### VB
- `GridGroupingControl1`
  - Property: `OptimizedListGrouping`
  - Method: `OptimizeIListGroupingPerformance`

### Code Examples

- **C# Example**

```csharp
gridGroupingControl1.OptimizedListGrouping = true;
// This enables optimized grouping performance.
```

- **VB Example**

```vb
GridGroupingControl1.OptimizedListGrouping = True
' This enables optimized grouping performance.
```

<!-- tags: [Essential Grid, Windows Forms, GridGroupingControl, Performance Optimization, Real Time Updates] keywords: [OptimizedListGrouping, OptimizeIListGroupingPerformance, grouping performance improvement, real time updates, huge data, data source, grouping optimization, C#, VB] -->
```