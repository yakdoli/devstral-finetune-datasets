```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_374.jpeg
document_name: XlsIO
page_number: 374
page_id: XlsIO#page_374
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:30Z
fidelity: lossless
-->

## Template Marker representing the HeaderName and NumberFormat

### Overview
- Illustrates the binding of data from a business object to a marker.
- Focuses on using the `NumberFormat` and `HeaderName` arguments.

### Content

#### Code Example
The following code demonstrates the creation and usage of a `TemplateMarkerProcessor` to process markers in a template, specifically within the context of a business object (`Customer`). The code also includes examples of binding business object data to markers with specified formats and headers.

```csharp
set
{
    m_salesPerson = value;
}

}

public int Sold
{
    get
    {
        return m_sold ;
    }
    set
    {
        m_sold = value;
    }
}

}

public Customer(string name, int sold)
{
    this.m_salesPerson = name;
    this.m_sold = sold;
}

}

// Creating Template Marker Processor
// Northwind Customers Table
ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();
marker.AddVariable("Sales", arrSalesPerson);

// Processing the markers in the template
marker.ApplyMarkers();
```

#### Key Points
- The `Customer` class contains properties like `SalesPerson` and `Sold`, which are used to store sales-related information.
- The `Customer` constructor initializes these properties with the provided arguments.
- The `TemplateMarkerProcessor` is created to handle template markers, where variables like `Sales` are dynamically replaced with the actual sales data.
- The `ApplyMarkers()` method processes the template, replacing markers with the corresponding data.

### Template Marker Discussion
The template markers are used to insert formatted data directly into the Excel template:
- `NumberFormat` ensures that the data is displayed in the specified numerical format.
- `HeaderName` allows setting a custom header for the column or cell where the data is displayed.

### API Reference

#### Class: `Customer`
- **Properties:**
  - `SalesPerson`: Stores the salesperson's name as a `string`.
  - `Sold`: Stores the quantity sold as an `int`.

- **Constructor:**
  - `public Customer(string name, int sold)`: Initializes the `SalesPerson` and `Sold` properties.

#### Interface: `ITemplateMarkersProcessor`
- **Methods:**
  - `CreateTemplateMarkersProcessor()`: Creates a new instance of the `TemplateMarkerProcessor`.
  - `AddVariable(string name, object value)`: Adds a variable to the template with the specified name and value.
  - `ApplyMarkers()`: Processes all markers in the template, replacing them with the corresponding data.

### Code Examples

#### Example Usage
```csharp
// Assume arrSalesPerson is an array of Customer objects
ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();
marker.AddVariable("Sales", arrSalesPerson);
marker.ApplyMarkers();
```

### Cross References
- See also: [Template Processing in XlsIO] for more details on working with template markers in Excel documents.

<!-- tags: [Syncfusion, XlsIO, TemplateMarkerProcessor, HeaderName, NumberFormat, Customer] keywords: [template markers, dynamic data binding, salesperson, sales data, numerical format, header name, Excel processing] -->
```