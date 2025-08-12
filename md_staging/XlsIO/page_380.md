```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_380.jpeg
document_name: XlsIO
page_number: 380
page_id: XlsIO#page_380
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:48Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates the use of template markers in XlsIO to generate customized reports.
- Explains how to replace markers in an Excel template with data from a data table, array, or formula.
- Highlights the benefits of using template markers for end-users to create customized reports without modifying the application's source code.

## Content

### Figure: Template showing Markers replaced by Data using XlsIO
Figure 136 illustrates the use of template markers in an Excel template to bind data dynamically. The template includes a list of company names, contact names, and contact titles, where the markers are replaced with actual data from a data source.

![](image1.png)

#### Figure 136: Template showing Markers replaced by Data using XlsIO

The unique advantage of this approach is that the end-user can have customized reports without modifying the source code of the report generating application.

#### Code Example: Binding Data to a Marker
The following code example demonstrates how to bind the data from a data table, array, and formula to a marker in an Excel template.

```csharp
// Create Template Marker Processor.
// Northwind Customers Table
ITemplateMarkersProcessor marker =
    workbook.CreateTemplateMarkersProcessor();
marker.AddVariable("Customers", northwindDt);
```

### Explanation of Code
- **`ITemplateMarkersProcessor`**: Interface for processing template markers in the Excel document.
- **`workbook.CreateTemplateMarkersProcessor()`**: Creates a new instance of the template marker processor to handle the binding of data to markers.
- **`marker.AddVariable("Customers", northwindDt)`**: Binds the data from the `northwindDt` data table to the marker named "Customers" in the Excel template.

## API Reference
### Methods
- **`CreateTemplateMarkersProcessor()`**: Creates a new instance of the `ITemplateMarkersProcessor` for processing template markers.
- **`AddVariable(string markerName, object data)`**: Replaces a marker with the specified data in the Excel template.

### Parameters
- **`markerName`**: The name of the marker to replace in the Excel template.
- **`data`**: The data to bind to the marker, which can be a data table, array, or formula.

### Returns
- Returns a reference to the `ITemplateMarkersProcessor` instance, allowing for method chaining.

## Code Examples

### C# Example
```csharp
// Example of using the Template Marker Processor to bind data
using (ExcelEngine excelEngine = new ExcelEngine())
{
    IApplication application = excelEngine.Excel;
    application.DefaultVersion = ExcelVersion.Excel2013;
    
    Workbook workbook = application.Workbooks.Open("Template.xlsx");
    ITemplateMarkersProcessor markerProcessor = workbook.CreateTemplateMarkersProcessor();
    
    markerProcessor.AddVariable("Customers", northwindDt);
    
    try
    {
        markerProcessor.Process();
    }
    catch (Exception ex)
    {
        // Handle exception
    }
}
```

## RAG Annotations
<!-- tags: [excel, template, marker, data binding] keywords: [XlsIO, template, marker processor, data table, formula, report generation, end-user customization] -->
```