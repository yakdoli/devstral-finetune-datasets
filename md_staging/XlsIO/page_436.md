```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_436.jpeg
document_name: XlsIO
page_number: 436
page_id: XlsIO#page_436
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:18:18Z
fidelity: lossless
-->

## Essential XlsIO

- **jump**:[cell reference in R1C1 notation]-This argument binds the data to the cell at the specified reference. Cell reference address can be relative or absolute.
- **copyrange**:[top-left cell reference in R1C1]:[bottom-right cell reference in R1C1]-Copies the specified cells after each cell import.

### Marker Processing and Data Binding

Following code sample illustrates processing and binding the marker with data.

```csharp
// Create marker processor
ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();

// Bind the data from the data table
marker.AddVariable("Customers", northwindDt);

// Process the markers in the template
marker.ApplyMarkers();
```

### Explanation

Here, `CreateTemplateMarkerProcessor` returns `ITemplateMarkersProcessor` interface which creates and manipulates the marker data. The `ApplyMarkers` method of `ITemplateMarkersProcessor` is the special method that processes the markers in the template.

### Result

Here is a screenshot after binding data with marker variable.

## Page-Level Navigation/TOC

- **Overview**
  - Essential XlsIO
    - Marker Processing and Data Binding
    - Explanation
    - Result

## API Reference (if applicable)
- **Namespace**: Unclear from the provided content.
- **Class**: Unclear from the provided content.
- **Members**: Parameters, Methods, Properties (if any)

### Parameters Table
- **Name**: Jump
- **Description**: Binds data to a specified cell reference.
- **Type**: String (R1C1 notation)
- **Default**: None
- **Required**: Yes

### Returns
- **Type**: None (void)

## Code Examples

```csharp
// Example usage of jump marker
marker.AddVariable("Customers", northwindDt);

// Process the markers
marker.ApplyMarkers();
```

## See Also
- Related documentation or examples if available

<!-- 
tags: [xlsio, marker processing, apply markers, data binding, template markers]
keywords: [marker binding, jump, copyrange, northwindDt, ITemplateMarkersProcessor, ApplyMarkers, cell reference, R1C1 notation]
 -->
```