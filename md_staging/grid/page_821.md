```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_821.jpeg
document_name: grid
page_number: 821
page_id: grid#page_821
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:41:54Z
fidelity: lossless
-->

## Content

### Code Example

This section contains a code example demonstrating a `Country` class that can be used with Syncfusion's Essential Grid for Windows Forms. The `Country` class is designed to store and manage country information with properties such as `CountryCode` and `Name`.

```csharp
// Country Class.
[Serializable]
public class Country
{
    private string _code;
    private string _name;

    public Country()
    {
    }

    public Country(string strCode, string strName)
    {
        this._code = strCode;
        this._name = strName;
    }

    [System.ComponentModel.Browsable(true)]
    public string CountryCode
    {
        get
        {
            return _code;
        }
        set
        {
            _code = value;
        }
    }

    [System.ComponentModel.Browsable(true)]
    public string Name
    {
        get
        {
            return _name;
        }
        set
        {
            _name = value;
        }
    }
}
```

### Explanation

- **Serializable Attribute**: Indicates that the `Country` class can be serialized.
- **Properties**:
  - `CountryCode`: Represents the country's code.
  - `Name`: Represents the name of the country.
- **Constructors**:
  - A default constructor is provided.
  - A parameterized constructor allows initializing the `Country` object with `CountryCode` and `Name`.
- **Browsable Attribute**: Marks the properties as browsable, making them visible in the Visual Studio Property Grid.

### Purpose

This `Country` class can be utilized to populate the GridControl in Syncfusion's Essential Grid for Windows Forms. It ensures that the country data is properly serialized and can be browsed and edited in the UI.

## API Reference

### Class: `Country`

#### Properties
- **CountryCode**
  - Type: `string`
  - Description: Gets or sets the code of the country.
  - Default: Not specified.
  - Required: Yes

- **Name**
  - Type: `string`
  - Description: Gets or sets the name of the country.
  - Default: Not specified.
  - Required: Yes

#### Constructors
- **`Country()`**
  - Description: Initializes a new instance of the `Country` class.

- **`Country(string strCode, string strName)`**
  - Description: Initializes a new instance of the `Country` class with the specified country code and name.
  - Parameters:
    - `strCode`: The code of the country.
    - `strName`: The name of the country.

---

<!-- tags: [Syncfusion, WinForms, GridControl, Serializable, BrowsableAttribute, country class, properties, constructors, serialization] keywords: [Code Example, Serializable Attribute, Browsable Attribute, Country Code, Country Name, GridControl, Property, Constructor] -->
```