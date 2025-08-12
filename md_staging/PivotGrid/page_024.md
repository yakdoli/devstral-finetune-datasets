```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: PivotGrid
page_number: 024
page_id: PivotGrid#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:53Z
fidelity: lossless
-->

## 4.4 Sorting

Sorting enables you to quickly visualize and understand the data in a better way, organize and find the data that you want, and ultimately make more effective decisions. By default, the PivotGrid will populate the data in ascending order. The sorting order can be changed using the Comparer field of PivotItem.

### Overview
- Sorting helps in organizing and visualizing data effectively.
- By default, data is sorted in ascending order.
- Sorting order can be customized using a custom Comparer.

### Content
#### Sorting in PivotGrid
Sorting in the PivotGrid enables users to restructure the data according to their requirements. By default, the data is organized in ascending order. However, this behavior can be adjusted by utilizing a custom Comparer class. Below is an example demonstrating how to achieve this:

```csharp
this.PivotGridControl.PivotRows.Add(new PivotItem
{
    FieldMappingName = "Product",
    TotalHeader = "Total",
    Comparer = new ReverseOrderComparer()
});
```

#### Custom Comparer Example

```csharp
/// <summary>
/// Reverse Order Comparer for sorting data in Descending order
/// </summary>
public class ReverseOrderComparer : IComparer
{
    #region IComparer Members

    public int Compare(object x, object y)
    {
        if (x == null && y == null)
            return 0;
        else if (y == null)
            return 1;
        else if (x == null)
            return -1;
        else
            return -x.ToString().CompareTo(y.ToString());
    }

    #endregion
}
```

This custom Comparer class, `ReverseOrderComparer`, implements the `IComparer` interface and provides a mechanism to sort data in descending order.

---

``` 
``` 
<!-- tags: [pivotgrid, sorting, windowsforms, syncfusion, asc, desc, comparer] keywords: [pivotitem, totals, totalheader, reverseordercomparer, iComparer, sortingorder, ascendingorder, descendingorder] -->
``` 
