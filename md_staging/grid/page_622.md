```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_622.jpeg
document_name: grid
page_number: 622
page_id: grid#page_622
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:34Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Create a custom collection class for visualizing large datasets in a grid grouping control.
- Implement interfaces `IList` and `ITypedList` to provide data source functionality.
- Example implementation of a virtualized list class.

## Content

### Creating a VirtualList Class

2. Create another class (`VirtualList`) by implementing `IList` and `ITypedList` interfaces. This class represents your collection that serves as the data source for the grid grouping control. Refer to `CustomCollections` to know how to implement these interfaces.

```csharp
[C#]

public class VirtualList : IList, ITypedList
{
    int virtualCount;
    public VirtualList(int count)
    {
        virtualCount = count;
    }

    // IList Members.
    public bool IsReadOnly
    {
        get
        {
            return true;
        }
    }

    public object this[int index]
    {
        get
        {
            VirtualItem item = new VirtualItem();
            item.Index = index;
            item.Name = "Name" + index.ToString("000000000");
            item.SomeValue = index * 0.873332f;
            item.OtherValue = (293023033 - index) / 8;

            return item;
        }
        set { }
    }

    // Other IList members.
    ...............
    ...............

    // ICollection Members.
    ...............
    ...............
}
```

### Explanation

- The `VirtualList` class implements the necessary interfaces to act as a data source for the grid grouping control.
- The `IsReadOnly` property is set to `true` to indicate that the collection cannot be modified.
- The indexer `[int index]` is implemented to provide virtualized data items on demand.
- Example properties like `SomeValue` and `OtherValue` are dynamically calculated based on the index for demonstration purposes.

## Cross References
- Refer to `CustomCollections` for more details on implementing `IList` and `ITypedList` interfaces.

<!-- tags: [grid, virtualization, data source, Windows Forms, IList, ITypedList] keywords: [VirtualList, large datasets, grid grouping, interfaces, virtualized list, IsReadOnly, indexer, data source implementation] -->
```