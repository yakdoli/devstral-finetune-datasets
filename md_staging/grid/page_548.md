```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_548.jpeg
document_name: grid
page_number: 548
page_id: grid#page_548
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:23:18Z
fidelity: lossless
-->

## Overview
- Demonstrates how to bind an ArrayList to a Grid control.
- Explains the use of the ArrayList class with IBindingList support.
- Highlights the ability to add new items and sort list items.
- Includes a code example to populate the grid with sample data.

## Content

### ArrayList with IBindingList Support

#### 4.2.2.1.1 ArrayList Class with IBindingList Support

Any changes that you make to the grid will be posted back to the ArrayList. Keep in mind that you cannot add new items to the ArrayList through the grid. Instead, make sure that your data source supports the IBindingList interface and that it implements an appropriate `AddNew` method. The IBindingList support determines whether you can add new items and sort items as well as do searching for other basic aspects of list behavior.

```vb
al.Add(New Person("John", "Smith"))
al.Add(New Person("Mary", "Tucker"))
al.Add(New Person("Sue", "Gaskins"))
al.Add(New Person("John", "Jacobs"))
al.Add(New Person("Sam", "Garfunkel"))
al.Add(New Person("George", "Shepherd"))
al.Add(New Person("Becky", "Dunsford"))
Me.GridDataBoundGrid1.DataSource = al
End Sub
```

**Figure 216: Grid Data Bound Grid Bound to a Simple ArrayList**

![](./image.png)

Here is a minimal implementation of an ArrayList-derived class that also supports IBindingList. If you add this class to the above code and in the Form-Load change the ArrayList to PersonList, then you will be able to add new entries to your underlying PersonList data source by using the AppendRow at the bottom of the grid. Notice that the implementation of `IBindingList.AddNew` as well as the `IBindingList.AllowNew` property will indicate that new rows are allowed.

## See Also
- **4.2.2.1.1 ArrayList Class with IBindingList Support**
- Detailed information on IBindingList interface and its methods.
- Examples of implementing `AddNew` in a derived class.

<!-- tags: [syncfusion, winforms, ArrayList, IBindingList, data binding] keywords: [ArrayList, IBindingList, data binding, Grid, add new rows, sorting, PersonList] -->
```