```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_689.jpeg
document_name: grid
page_number: 689
page_id: grid#page_689
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:49Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Code Example

```vb
Inherits CollectionBase

' Using Default Property Indexer.
Default Public Property Item(ByVal Index As Integer) As Product
    Get
        Return CType(List.Item(Index), Product)
    End Get
    Set(ByVal Value As Product)
        List.Item(Index) = Value
    End Set
End Property

Public Function Add(ByVal Item As Product) As Integer
    Return List.Add(Item)
End Function
End Class
```

### Steps

1. **Create a Products Collection**
   - Instantiate the `Products` class and add a few records to it.

#### [C#]

```csharp
Products MyProducts = new Products();
MyProducts.Add(new Product("Chai", "10 boxes x 20 bags"));
MyProducts.Add(new Product("Aniseed Syrup", "12 - 550 ml bottles"));
MyProducts.Add(new Product("Sir Rodney's Marmalade", "30 gift boxes"));
```

#### [VB.NET]

```vb
Dim MyProducts As Products = New Products()
MyProducts.Add(New Product("Chai", "10 boxes x 20 bags"))
MyProducts.Add(New Product("Aniseed Syrup", "12 - 550 ml bottles"))
MyProducts.Add(New Product("Sir Rodney's Marmalade", "30 gift boxes"))
```

2. **Assign the Collection to the Grouping Grid's DataSource**

#### [C#]

```csharp
this.gridGroupingControl1.DataSource = MyProducts;
```

#### [VB.NET]

```vb
Me.GridGroupingControl1.DataSource = MyProducts
```

3. **Run the Sample**
   - Here is a sample screenshot.

```html
<p>Unclear: Screenshot content not present in OCR.</p>
```

## Footer
© 2013 Syncfusion. All rights reserved. 689 | Page
```