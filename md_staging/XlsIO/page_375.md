```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_375.jpeg
document_name: XlsIO
page_number: 375
page_id: XlsIO#page_375
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:19Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains how to integrate business objects into Excel templates using markers.
- Demonstrates the use of template marker attributes for formatting and inserting data into Excel sheets.

## Content

### Template Integration with Business Objects
The following figure illustrates a sample Excel template that uses markers to represent data fields.

![Sample Excel Template](https://i.imgur.com/rX8QzTg.png)
*Figure 100*

The `%Sales.SalesPerson;insert:copystyles` marker in the template indicates where the salesperson's name data should be inserted, ensuring that styles are preserved. Similarly, the `%Sales.Sold` marker specifies where the sales data should be placed.

---

### Code Implementation
The following C# code snippet demonstrates the definition of a `Sales` class that integrates with the Excel template using the marker argument.

```csharp
[C#]
//Definition of the business objects with the marker argument
class Sales
{
    private string m_salesPerson;
    private int m_sold;

    public string SalesPerson
    {
        get
        {
            return m_salesPerson;
        }
        set
        {
            m_salesPerson = value;
        }
    }

    [TemplateMarkerAttributes("Sold", "$#,###")]
    public int Sold
    {
        get
        {
            return m_sold;
        }
        set
        {
            m_sold = value;
        }
    }

    public Sales()
    {
    }

    public Sales(string name, int sold)
    {
        this.m_salesPerson = name;
        this.m_sold = sold;
    }
}
```

- **Properties**:
  - `SalesPerson`: A public string property that holds the name of the salesperson.
  - `Sold`: A public integer property that represents the sales amount, formatted as `"$#,###"` using the `TemplateMarkerAttributes` attribute.

- **Constructors**:
  - A default constructor is provided for basic initialization.
  - A parameterized constructor `Sales(string name, int sold)` initializes the object with the salesperson's name and sales amount.

## API Reference

### TemplateMarkerAttributes
- **Description**: Specifies how the attribute values of the property bind with the corresponding header. This is particularly useful for formatting data as it is inserted into the Excel template.

## Code Examples

The provided C# code snippet shows how the `Sales` class can be instantiated and used with Excel templates. The class allows for easy data insertion into Excel sheets, leveraging markers for both data placement and styling.

## Cross References

See also:
- [Syncfusion XlsIO Documentation](https://www.syncfusion.com/documentation/xlsio/)
- Template Marker Attributes in Syncfusion XlsIO

<!-- tags: [syncfusion, winforms, xlsio, template markers, sales class, data binding] keywords: [template marker attributes, excel integration, business objects, sales data, formatting] -->
```