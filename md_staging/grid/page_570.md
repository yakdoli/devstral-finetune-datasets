```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_570.jpeg
document_name: grid
page_number: 570
page_id: grid#page_570
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:25:21Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
DataView dv = cm.List as DataView;
```

```vbnet
Dim cm As CurrencyManager = TryCast(BindingContext(Grid.DataSource, Grid.DataMember), CurrencyManager)
Dim dv As DataView = TryCast(cm.List, DataView)
```

The `DataView` sort is applied to this with the `sortName`.

```csharp
[C#]

if (dv.Sort == sortName)
{
    dv.Sort = sortName + " DESC";
}
else
    dv.Sort = sortName;
```

```vbnet
[VB.NET]

If dv.Sort = sortName Then
    dv.Sort = sortName & " DESC"
Else
    dv.Sort = sortName
End If
```

> ![Note]({{timestamp}}) **Note:** `CurrencyManager` manages a list of binding objects when the data source uses the `IBindingList` interface.

In the `QueryCellInfo` handler, the sorting icon is drawn with respect to sorting.

```csharp
[C#]

if (dv.Sort == sortName)
    e.Style.Tag = ListSortDirection.Ascending;
else if (dv.Sort == sortName + " DESC")
    e.Style.Tag = ListSortDirection.Descending;
```

```vbnet
[VB.NET]

If dv.Sort = sortName Then
    e.Style.Tag = ListSortDirection.Ascending
```

---
© 2013 Syncfusion. All rights reserved. 570 | Page
```