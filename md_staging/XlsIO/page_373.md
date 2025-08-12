<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_373.jpeg
document_name: XlsIO
page_number: 373
page_id: XlsIO#page_373
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:12Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Representing the `NumberFormat` using C# Attributes - the Template Marker can apply the number format based on the property's `NumberFormat` attribute.
- Template Marker with the Class name - The Template Maker can bind all the properties of the business objects dynamically.

### 4.5.4.1.3 Attributes

| Attributes    | Description                        | Type     | Data Type |
|---------------|------------------------------------|----------|-----------|
| **HeaderName** | Header name of the column/row.   | Normal   | String    |
| **NumberFormat** | Number Format for the column/row | Normal   | String    |

### 4.5.4.1.4 Binding Business Objects to Template Markers

The Marker Syntax with business objects is shown below:

![Marker Syntax with business objects](https://i.imgur.com/8i83yFZ.png)

**Figure 99**

The following code sample illustrates the binding of data from a business object to a marker.

```csharp
// Definition of the business objects
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
    }
}
```

## API Reference (if applicable)
- None specified in the current scope.

## Code Examples
- The provided C# code demonstrates the class `Sales` and its properties. Further implementation details for the binding mechanism are not shown in the current context.

## Page-level Navigation/TOC (if applicable)
- None specified in the current scope.

## Cross References
- See also: The detailed implementation of `NumberFormat` and Template Markers in the broader XlsIO documentation.

<!-- tags: [XlsIO, Business Objects, Template Markers, NumberFormat, C# Attributes] keywords: [template syntax, dynamic binding, marker name, number format, header name] -->