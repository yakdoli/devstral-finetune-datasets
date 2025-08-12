```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_377.jpeg
document_name: XlsIO
page_number: 377
page_id: XlsIO#page_377
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:25Z
fidelity: lossless
-->

# Overview

- **Description**: Demonstrates the use of C# classes to define business objects with marker attributes for managing sales data.
- **Key Features**: Includes properties for the salesperson's name and number of units sold, formatted with specific styles.
- **API Reference**: Markdown and C# code examples are provided to illustrate the implementation of the `Sales` class with TemplateMarkerAttributes.

## Content

### Defining Business Objects with Marker Attributes

The following C# code defines a `Sales` class with properties for managing sales data. These properties are marked with attributes to specify formatting and display information.

```csharp
[C#]
//Definition of the business objects with the marker argument
class Sales
{
    private string m_salesPerson;
    private int m_sold;

    [TemplateMarkerAttributes("Sales Person Name")]
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

### Explanation of Code

1. **Properties**:
   - **SalesPerson**: Represents the name of the salesperson, marked with the attribute `"Sales Person Name"`.
   - **Sold**: Represents the number of units sold, marked with the attribute `"Sold", "$#,###"` to format the output as a numeric value with thousands separators.

2. **Constructors**:
   - A default constructor is provided for flexibility.
   - A parameterized constructor is included to initialize the `Sales` class with a salesperson's name and the number of units sold.

3. **TemplateMarkerAttributes**:
   - These attributes are used to specify how the properties will be displayed or formatted in the application.

## API Reference

### Namespace and Class

```csharp
namespace YourNamespace
{
    class Sales
    {
        // Properties and methods as described above
    }
}
```

### Properties

- **SalesPerson**:
  - **Type**: `string`
  - **Attribute**: `[TemplateMarkerAttributes("Sales Person Name")]`
  - **Description**: Holds the name of the salesperson.

- **Sold**:
  - **Type**: `int`
  - **Attribute**: `[TemplateMarkerAttributes("Sold", "$#,###")]`
  - **Description**: Holds the number of units sold, formatted with thousands separators.

### Constructors

- **Sales()**
  - **Description**: Default constructor for the `Sales` class.
  
- **Sales(string name, int sold)**
  - **Parameters**:
    - `name`: The name of the salesperson.
    - `sold`: The number of units sold.
  - **Description**: Parameterized constructor to initialize the `Sales` object with specific values.

## Code Examples

### Example 1: Creating a Sales Object

```csharp
Sales sale = new Sales("John Doe", 5000);
Console.WriteLine($"Salesperson: {sale.SalesPerson}, Sold: {sale.Sold}");
```

### Example 2: Using TemplateMarkerAttributes

```csharp
// Assume a template is configured to use these marker attributes
// The attributes will be used to format and display the sales data in the desired style.
```

## Conclusion

This example illustrates how to define a `Sales` class with marked attributes in C#. These attributes are crucial for integrating the class with templates or other formatting mechanisms, ensuring consistent and well-presented data output.

<!-- tags: [XlsIO, Sales, TemplateMarkerAttributes, C#] keywords: [Sales class, marker attributes, formatting, sales data, C# example] -->
```