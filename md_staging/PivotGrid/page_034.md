```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: PivotGrid
page_number: 034
page_id: PivotGrid#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:35Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

| SubTotalsRendering | Handles rendering of cells(showing or hiding the cells) by calculating the cell range values in the Pivot Engine based on the ShowSubTotals property value in the control | - | Void | - |
|--------------------|----------------------------------------------------------------------------------------------------|---|-----|---|

## Sample Link

Follow the steps given below to view a sample of this feature:

1. Select Start > Programs > Syncfusion > Essential Studio x.x.x.x -> Dashboard.
2. Click Run Samples under UI edition.
3. Select PivotGrid.
4. Navigate to Selection > Cell Selection Demo.

## 4.8.1 Showing or Hiding Subtotals in PivotGrid

The user can show or hide the PivotGrid subtotals using `ShowSubTotals` property. To show subtotals, set this property to `true`. To hide subtotals, set this property to `false`. By default, the value of the `ShowSubTotals` property is set to `true`.

The following code example illustrates how to set values for the `ShowSubTotals` property to show the subtotals.

### Code Example

```csharp
this.pivotGridControl1.ShowSubTotals = true;
```

```vb
Me.pivotGridControl1.ShowSubTotals = True
```

The following code example illustrates how to set values for the `ShowSubTotals` property to hide the subtotals.

<!-- tags: [PivotGrid, windowsforms, subtotals, showsubtotals, property, rendering, cell selection] keywords: [showsubtotals, pivotgrid, windowsforms, subtotals, property, cell selection, demo, c#, vb] -->
```