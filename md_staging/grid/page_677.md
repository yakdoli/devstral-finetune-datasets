```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_677.jpeg
document_name: grid
page_number: 677
page_id: grid#page_677
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:31:56Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

The `IBindingList` interface is the most important data-binding interface that provides rich data binding support. Implementing this interface lets you control over changes to the list, sorting and searching the list. One important benefit is the support for providing change notifications to the collection subscribing to this interface.

The `IBindingList` interface overcomes the shortcomings of the other interfaces by declaring a `ListChanged` event. The data sources that referencing this interface will hook onto this event and so, it will be aware of any items that are added or removed from the list, which makes the bound grid to update itself automatically.

The chapters in this section will demonstrate how to create such collections by implementing the collection interfaces and how to bind the grouping grid to these collections.

## 4.3.4.2.3.1 `IList`

This section demonstrates the implementation of a collection using `ArrayList` and shows how to bind this collection to a grouping grid. `ArrayList` is an implementation of `IList` that could be best defined as a hybrid of a normal array and a collection. It holds the items in the order they were added. The items can be retrieved in any order via their index. As elements are added, the capacity of the `ArrayList` increases automatically. It allows null references and allows duplicate elements. Objects implementing the `IList` interface should have at least one record for the data rows to be created. The data rows correspond to the data objects in the collection and the data columns represent the properties of the data.

### Implementation

Follow these steps to bind an array of custom objects to a grouping grid.

1. Create a class (`Data`) whose instances represent the records. Its properties represent the record fields.

```csharp
public class Data
{
    public Data() : this("", "", "")
    {
    }
    public Data(string cat_Id, string cat_Name, string desc)
    {
    }
}
```

<!-- tags: [Syncfusion, Winforms, Grid, IBindingList, IList, ArrayList, Data Binding, ListChanged, Events, Collection Interfaces, Grouping Grid] keywords: [IBindingList, IList, ArrayList, Data Binding, ListChanged, Collection Interfaces, Grouping Grid] -->
```