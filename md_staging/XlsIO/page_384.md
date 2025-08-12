```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_384.jpeg
document_name: XlsIO
page_number: 384
page_id: XlsIO#page_384
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:05Z
fidelity: lossless
-->

### Overview
- Documenting the use of `ITemplateMarkersProcessor` class in `XlsIO`.
- Demonstrating how to process template markers with various `VariableTypeAction` enumerations.
- Examples provided in both C# and VB.NET languages.
- Description of enumerations `DetectDataType`, `DetectNumberFormat`, and `None`.
- Highlighting the ability to apply conditional formatting dynamically using `CreateConditionalFormat` method.

### Content

#### Template Marker Processing Example

```csharp
ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();
// Northwind customers table
marker.AddVariable("Customers", northwindDt, VariableTypeAction.DetectNumberFormat);
// Process the markers and detect the number format along with the data type in the template.
marker.ApplyMarkers();
```

---

```vb
' Create Template Marker Processor
Dim marker As ITemplateMarkersProcessor = workbook.CreateTemplateMarkersProcessor()
' Northwind customers table
marker.AddVariable("Customers", northwindDt, VariableTypeAction.DetectNumberFormat)
' Process the markers and detect the number format along with the data type in the template.
marker.ApplyMarkers()
```

#### List of Enumerations

The following table gives the list of enumerations available:

| Enum                | Description                                      |
|---------------------|--------------------------------------------------|
| DetectDataType      | Detects the DataType of the marker variable     |
| DetectNumberFormat  | Detects both the NumberFormat and DataType of the marker variable |
| None                | Represents the ‘None’ action                      |

---

#### Template Marker with Conditional Formatting

XlsIO allows the `CreateConditionalFormat` method in the `ITemplateMarkerProcessor` to dynamically apply the conditional format. It then creates or applies the conditional format to the template marker range dynamically.

### Page-level Navigation/TOC (if applicable)
- [Main Content]()
- [Template Marker Processing Example](#template-marker-processing-example)
- [List of Enumerations](#list-of-enumerations)
- [Template Marker with Conditional Formatting](#template-marker-with-conditional-formatting)

### Cross References
See also:
- `ITemplateMarkersProcessor` documentation
- `CreateConditionalFormat` method reference

### Notes
- Ensure proper handling of enumerations to detect data types and formats dynamically.
- Utilize conditional formatting for advanced template processing.

<!-- tags: [xlsio, template markers, dynamic formatting, enumerations, conditional formatting] keywords: [ITemplateMarkersProcessor, DetectDataType, DetectNumberFormat, CreateConditionalFormat, northwindDt, ApplyMarkers, VariableTypeAction] -->
```