```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_623.jpeg
document_name: grid
page_number: 623
page_id: grid#page_623
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:07Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Implementation of IEnumerable and ITypeList Interfaces

#### C# Example

```csharp
// IEnumerable Members.
............
............

// ITypeList Members.
public PropertyDescriptorCollection
GetItemProperties(PropertyDescriptor[] listAccessors)
{
    PropertyDescriptorCollection pds =
        TypeDescriptor.GetProperties(typeof(VirtualItem));
    string[] atts = new string[] {"Index", "Name", "SomeValue", "OtherValue"};
    return pds.Sort(atts);
}

public string GetListName(PropertyDescriptor[] listAccessors)
{
    return "VirtualList";
}
```

#### VB Example

```vb
[VB]
Public Class VirtualList : Implements IList, ITypeList
    Private virtualCount As Integer

    Public Sub New(ByVal count_Renamed As Integer)
        virtualCount = count_Renamed
    End Sub

    ' IList Members.
    Public ReadOnly Property IsReadOnly() As Boolean Implements IList.IsReadOnly
        Get
            Return True
        End Get
    End Property

    Public Default Property Item(ByVal index As Integer) As Object
        Get
            Dim item As VirtualItem = New VirtualItem()
            item.Index = index
            item.Name = "Name" & index.ToString("000000000")
            item.SomeValue = index * 0.873332f
            item.OtherValue = (293023033 - index) / 8
            Return item
        End Get
    End Property
End Class
```

## API Reference

### Methods

- **GetItemProperties**:  
  ```csharp
  public PropertyDescriptorCollection GetItemProperties(PropertyDescriptor[] listAccessors)
  ```
  - **Parameters**: 
    - `listAccessors`: An array of `PropertyDescriptor` objects.
  - **Returns**: A `PropertyDescriptorCollection` sorted using the specified attributes.

- **GetListName**:  
  ```csharp
  public string GetListName(PropertyDescriptor[] listAccessors)
  ```
  - **Parameters**: 
    - `listAccessors`: An array of `PropertyDescriptor` objects.
  - **Returns**: A `string` representing the list name.

## Code Examples

### C# Example

```csharp
public PropertyDescriptorCollection
GetItemProperties(PropertyDescriptor[] listAccessors)
{
    PropertyDescriptorCollection pds =
        TypeDescriptor.GetProperties(typeof(VirtualItem));
    string[] atts = new string[] {"Index", "Name", "SomeValue", "OtherValue"};
    return pds.Sort(atts);
}
```

### VB Example

```vb
Public ReadOnly Property IsReadOnly() As Boolean Implements IList.IsReadOnly
    Get
        Return True
    End Get
End Property

Public Default Property Item(ByVal index As Integer) As Object
    Get
        Dim item As VirtualItem = New VirtualItem()
        item.Index = index
        item.Name = "Name" & index.ToString("000000000")
        item.SomeValue = index * 0.873332f
        item.OtherValue = (293023033 - index) / 8
        Return item
    End Get
End Property
```

## Cross References

- Refer to the documentation on `IEnumerable` and `ITypeList` interfaces for more detailed information.

<!-- tags: [syncfusion, winforms, grid, ienumerable, itypedlist, vb, csharp, version: 11.4.0.26] keywords: [propertydescriptorcollection, listaccessors, virtualitem, isreadonly, itemproperty, grid implementation] -->
```