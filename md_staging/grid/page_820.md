```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_820.jpeg
document_name: grid
page_number: 820
page_id: grid#page_820
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:42:37Z
fidelity: lossless
-->

```csharp
get
{
    return (Country) base[index];
}
set
{
    base[index] = value;
}

public static CountriesCollection CreateDefaultCollection()
{
    CountriesCollection countries = new CountriesCollection();
    countries.Add(new Country("US", "United States"));
    countries.Add(new Country("CA", "Canada"));
    countries.Add(new Country("AU", "Australia"));
    countries.Add(new Country("BR", "Brazil"));
    countries.Add(new Country("IO", "British Indian Ocean Territory"));
    countries.Add(new Country("CN", "China"));
    countries.Add(new Country("FI", "Finland"));
    countries.Add(new Country("FR", "France"));
    countries.Add(new Country("DE", "Germany"));
    countries.Add(new Country("HK", "Hong Kong"));
    countries.Add(new Country("HU", "Hungary"));
    countries.Add(new Country("IS", "Iceland"));
    countries.Add(new Country("IN", "India"));
    countries.Add(new Country("JP", "Japan"));
    countries.Add(new Country("MY", "Malaysia"));
    countries.Add(new Country("SG", "Singapore"));
    countries.Add(new Country("CH", "Switzerland"));
    return countries;
}

public override bool IsReadOnly
{
    get
    {
        return true;
    }
}

public override bool IsFixedSize
{
    get
```
