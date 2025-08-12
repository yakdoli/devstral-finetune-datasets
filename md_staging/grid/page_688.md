<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_688.jpeg
document_name: grid
page_number: 688
page_id: grid#page_688
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Documentation on extending the `Products` class derived from `CollectionBase`.
- Focus on creating a strongly typed collection with default property access and an `Add` method.

## Content

### Code Example: Part of the `Products` Class Implementation

```vb
End Get
    Set(ByVal Value As String)
        ProdName = Value
    End Set
End Property
Public Property QuantityPerUnit() As String
    Get
        Return QtyPerUnit
    End Get
    Set(ByVal Value As String)
        QtyPerUnit = Value
    End Set
End Property
End Class
```

### Creating the `Products` Class Derived from `CollectionBase`

2. Create another class `Products` that derives the `CollectionBase` class. To make it Strongly Typed, add a default property that will return a typed object. Also, implement an `ADD` method.

#### C#

```csharp
using System;
using System.Collections;

class Products : CollectionBase
{
    // Default Property.
    public Product this[int index]
    {
        get { return (Product)List[index]; }
        set { List[index] = (Product)value; }
    }

    public int Add(Product item)
    {
        return List.Add(item);
    }
}
```

#### VB.NET

```vb
Imports System
Imports System.Collections

Public Class Products
```

## API Reference

### CollectionBase Class

- **Default Property**: Provides index-based access to the typed objects in the collection.
- **Add Method**: Adds a new item to the collection.

### Product Object

- **Properties**:
  - `ProdName`: Name of the product.
  - `QuantityPerUnit`: Quantity per unit of the product.

## Code Examples

### C# Example

```csharp
using System;
using System.Collections;

class Products : CollectionBase
{
    // Default Property.
    public Product this[int index]
    {
        get { return (Product)List[index]; }
        set { List[index] = (Product)value; }
    }

    public int Add(Product item)
    {
        return List.Add(item);
    }
}
```

### VB.NET Example

```vb
Imports System
Imports System.Collections

Public Class Products
    ' Default Property.
    Default Public ReadOnly Property Item(index As Integer) As Product
        Get
            Return DirectCast(List(index), Product)
        End Get
    End Property

    Public Function Add(item As Product) As Integer
        Return List.Add(item)
    End Function
End Class
```

## Cross References

- Refer to Syncfusion documentation on `CollectionBase` for more details on implementing strongly typed collections.
- For further information on property and method implementations, see related WinForms SDK documentation.

<!-- tags: [Syncfusion Winforms, CollectionBase, Strongly Typed Collection, Products Class, Property Implementation, Add Method] keywords: [Grid, Collection, Property, Method, Strongly Typed, Product, C#, VB.NET, Implementation] -->