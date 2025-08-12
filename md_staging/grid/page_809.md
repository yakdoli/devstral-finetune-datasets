```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_809.jpeg
document_name: grid
page_number: 809
page_id: grid#page_809
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:08Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

```vb
Inherits ArrayList

Default Public Shadows Property Item(index As Integer) As USState
Get
    Return CType(MyBase.Item(index), USState)
End Get
Set
    MyBase.Item(index) = Value
End Set
End Property

Public Shared Function CreateDefaultCollection() As USStatesCollection
    Dim states As New USStatesCollection()
    states.Add(New USState("AL", "Alabama"))
    states.Add(New USState("AK", "Alaska"))
    states.Add(New USState("CA", "California"))
    states.Add(New USState("FL", "Florida"))
    states.Add(New USState("GA", "Georgia"))
    states.Add(New USState("IN", "Indiana"))
    states.Add(New USState("MS", "Mississippi"))
    states.Add(New USState("NJ", "New Jersey"))
    states.Add(New USState("NM", "New Mexico"))
    states.Add(New USState("NY", "New York"))
    states.Add(New USState("TX", "Texas"))
    states.Add(New USState("WA", "Washington"))
    states.Add(New USState("PE", "Prince Edward Island"))
    states.Add(New USState("YT", "Yukon Territories"))
    Return states
End Function

Public Overrides ReadOnly Property IsReadOnly() As Boolean
Get
    Return True
End Get
End Property

Public Overrides ReadOnly Property IsFixedSize() As Boolean
Get
    Return True
End Get
End Property
End Class

' US State Class.
<Serializable()>
_
```

### WinForms-specific conventions
- **Inherits ArrayList**: Inherits from the .NET `ArrayList` class, which is a dynamic array class in the .NET framework.
- **Shadows Property Item**: Provides an override for the `Item` property of the `ArrayList` class, allowing specific typing for `USState`.
- **CreateDefaultCollection**: A shared function that returns a `USStatesCollection` populated with predefined USStates objects.
- **IsReadOnly and IsFixedSize**: Both properties are overridden to specify that this collection is both read-only and fixed in size, ensuring immutability.

### Namespace and Class Structure
- The code demonstrates the structure and functionality of a custom collection class designed specifically for US States. It inherits from `ArrayList` and customizes the behavior through shadowed properties and overridden methods.

### Usage Example
This class can be used in Windows Forms applications where a fixed, read-only collection of US states is needed, such as in dropdown lists or comboboxes.

```markdown
## RAG Annotations
The provided code exemplifies how to create a typed collection in VB.NET, ensuring type safety and immutability.

### Page-level Navigation/TOC (if applicable)
This section details the implementation of a specialized collection class tailored for US states, showing how to override and customize inherited behavior.

### Cross References
- Refer to the documentation on `ArrayList` and `USState` classes for more details.
- Explore collections and immutability patterns in the Syncfusion WinForms documentation for additional insights.

### API Reference
- **Namespace**: Presumably resides in a `Syncfusion.Windows.Forms` or a similar custom namespace.
- **Class**: USStatesCollection
- **Members**: Detailed in the provided code.

## Code Examples
- The code demonstrates how to create and use a typed collection within a Windows Forms application.
```

<!-- tags: [Windows Forms, Essential Grid, US States, Collection, Type Safety, Immutability, ReadOnly, FCollection] keywords: [ArrayList, USStatesCollection, USState, CreateDefaultCollection, IsReadOnly, IsFixedSize, Shadows Property, Inheritance, Typed Collection] -->
```