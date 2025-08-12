```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_687.jpeg
document_name: grid
page_number: 687
page_id: grid#page_687
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:33:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Example of a product class definition in C# and VB.NET.
- Includes properties for `ProductName` and `QuantityPerUnit`.
- Demonstrates the use of encapsulation and getters/setters.

## Content

### WinForms-specific conventions
The following code snippets illustrate the definition of a `Product` class in both C# and VB.NET, showcasing properties for product name and quantity per unit.

#### C# Code

```csharp
string productName, qtyPerUnit;

public Product(string name, string qty)
{
    this.productName = name;
    this.qtyPerUnit = qty;
}

public string ProductName
{
    get
    {
        return productName;
    }
    set
    {
        productName = value;
    }
}

public string QuantityPerUnit
{
    get
    {
        return qtyPerUnit;
    }
    set
    {
        qtyPerUnit = value;
    }
}
```

#### VB.NET Code

```vb
Class Product
    Private ProdName As String
    Private QtyPerUnit As String

    Public Sub New(ByVal name As String, ByVal qty As String)
        ProdName = name
        QtyPerUnit = qty
    End Sub
    Public Property ProductName() As String
        Get
            Return ProdName
        End Get
    End Property
End Class
```

## Tags and Keywords
<!-- tags: [WinForms, C#, VB.NET, class, property, getter, setter] keywords: [product class, quantity per unit, encapsulation, getters, setters] -->
``` 
