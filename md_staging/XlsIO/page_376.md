```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_376.jpeg
document_name: XlsIO
page_number: 376
page_id: XlsIO#page_376
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:29Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to create and use template markers in an Excel template.
- Explains the process of adding variables to a template and applying markers to populate data.

## Content

### Creating and Using Template Markers
The following code demonstrates the creation and usage of template markers in an Excel template:

```csharp
// Creating the Template Marker Processor
// Northwind Customers Table
ITemplateMarkersProcessor marker =
    workbook.CreateTemplateMarkersProcessor();
marker.AddVariable("Sales", arrSalesPerson);

// Processing the markers in the template
marker.ApplyMarkers();
```

#### Output

The output of the template marker processing is shown below:

| Sales Person Name              | Sold     |
|---------------------------------|----------|
| Andy Bernard                    | $45,000  |
| Jim Halpert                     | $34,000  |
| Karen Fillipelli               | $75,000  |
| Phyllis Lapin                   | $56,500  |
| Stanley Hudson                  | $46,500  |
| BernardShah                     | $48,000  |
| Patricia McKenna                | $34,000  |
| Antonio Moreno Taquería         | $90,000  |
| Thomas Hardy                    | $56,500  |
| Christina Berglund              | $46,500  |
| Hanna Moos                      | $45,000  |
| Frédérique Citeaux              | $34,000  |
| Martin Sommer                   | $75,000  |
| Laurence Lebihan                | $56,500  |
| Elizabeth Lincoln               | $25,000  |
| Victoria Ashworth               | $45,000  |
| Patricio Simpson                | $34,000  |
| Marketing Manager               | $75,000  |
| Yang Wang                       | $56,500  |
| Pedro Afonso                    | $46,500  |
| Elizabeth Brown                 | $45,000  |

**Figure 101**

### Template Marker with the Class Name
The following is the Marker syntax with the Class Name:

## API Reference
- Namespace: `Syncfusion.XlsIO`
- Class: `ITemplateMarkersProcessor`
- Method: `CreateTemplateMarkersProcessor()`
- Method: `AddVariable(string name, object value)`
- Method: `ApplyMarkers()`

## Code Examples

```csharp
WorkBook workbook = new WorkBook();
// Initialize arrSalesPerson as an array of sales data
// ...
WorkBook.ActiveSheet sheet = workbook.WorkSheets[0];

// Creating the Template Marker Processor
ITemplateMarkersProcessor marker =
    workbook.CreateTemplateMarkersProcessor();
marker.AddVariable("Sales", arrSalesPerson);

// Processing the markers in the template
marker.ApplyMarkers();
```

## Page-level Navigation/TOC
- Creating and Using Template Markers
- Output
- Template Marker with the Class Name

## Cross References
- See also: [XlsIO API Reference](#api-reference)

<!-- tags: XlsIO, template markers, Excel templates, WinForms, SalesPerson, markers, ApplyMarkers, ITemplateMarkersProcessor, Sales data, output, processor keywords: XlsIO, template markers, Excel,_sales_data,markers,processor,sales_person -->
```