```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: PivotGrid
page_number: 018
page_id: PivotGrid#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:44Z
fidelity: lossless
-->

## Content

### Adding PivotItems to the PivotGrid

#### C#

```csharp
// Defining PivotItem
PivotItem m_PivotItem = new PivotItem() { FieldHeader="Product", 
   FieldMappingName ="Product", TotalHeader ="Total" };
// Adding PivotItem to PivotRows
this.PivotGridControl1.PivotRows.Add(m_PivotItem);
```

#### VB

```vb
' Defining PivotItem
Dim m_PivotItem As PivotItem = New PivotItem() With
{.FieldHeader="Product", .FieldMappingName ="Product", .TotalHeader ="Total"}
' Adding PivotItem to PivotRows
Me.PivotGridControl1.PivotRows.Add(m_PivotItem)
```

### 4.1.2 Sorting Using PivotItem

By default, the PivotGrid will sort data in ascending order. The sorting order can be changed using the `Comparer` field of `PivotItem`.

```csharp
// Adding Pivot Rows to Grid with FieldMappingName, TotalHeader and Comparer
this.PivotGridControl1.PivotRows.Add(new PivotItem { FieldMappingName = "Product", TotalHeader = "Total", Comparer = new ReverseOrderComparer() });

/// <summary>
/// Reverse Order Comparer for sorting data in Descending order
/// </summary>
public class ReverseOrderComparer : IComparer
{
```

## Page-level Navigation/TOC (if applicable)
- [4.1.2 Sorting Using PivotItem](#4.1.2-sorting-using-pivotitem)

## Cross References
See also:  
- [Defining PivotItem](#defining-pivotitem)
- [Adding PivotItem to PivotRows](#adding-pivotitem-to-pivotrows)

<!-- tags: [pivotgrid, winform, sort, pivotitem, comparer, reverseordercomparer] keywords: [pivotgrid, wiforms, pivotitem, data sorting, reverse order comparer, total header, field mapping name] -->
``` 
