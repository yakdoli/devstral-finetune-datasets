```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_822.jpeg
document_name: grid
page_number: 822
page_id: grid#page_822
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:46Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Code Example: C#
```csharp
public override string ToString()
{
    return this._name + "(" + this._code + ")";
}
```

### Code Example: VB.NET
```vb
'[Countries Collection
<Serializable()> _
Public Class CountriesCollection
Inherits ArrayList

    Default Public Shadows Property Item(index As Integer) As Country
        Get
            Return CType(MyBase.Item(index), Country)
        End Get
        Set
            MyBase.Item(index) = Value
        End Set
    End Property

    Public Shared Function CreateDefaultCollection() As CountriesCollection
        Dim countries As New CountriesCollection()
        countries.Add(New Country("US", "United States"))
        countries.Add(New Country("CA", "Canada"))
        countries.Add(New Country("AU", "Australia"))
        countries.Add(New Country("BR", "Brazil"))
        countries.Add(New Country("IO", "British Indian Ocean Territory"))
        countries.Add(New Country("CN", "China"))
        countries.Add(New Country("FI", "Finland"))
        countries.Add(New Country("FR", "France"))
        countries.Add(New Country("DE", "Germany"))
        countries.Add(New Country("HK", "Hong Kong"))
        countries.Add(New Country("HU", "Hungary"))
        countries.Add(New Country("IS", "Iceland"))
        countries.Add(New Country("IN", "India"))
        countries.Add(New Country("JP", "Japan"))
        countries.Add(New Country("MY", "Malaysia"))
        countries.Add(New Country("SG", "Singapore"))
        countries.Add(New Country("CH", "Switzerland"))
    End Function
End Class
```

## Cross References

See also: [Countries Collection Documentation](#)

## RAG Annotations
<!-- tags: grid, windows forms, countries collection, essential grid, winforms, version: 11.4.0.26 keywords: grid, windows forms, countries collection, oops, string, return, this, name, code, override, countriescollection, inherits, arraylist, default, property, item, shared, createdefaultcollection, country, add, new, us, ca, au, br, io, cn, fi, fr, de, hk, hu, is, in, jp, my, sg, ch -->
``` 
