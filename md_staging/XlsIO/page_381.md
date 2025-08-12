```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_381.jpeg
document_name: XlsIO
page_number: 381
page_id: XlsIO#page_381
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:14:45Z
fidelity: lossless
-->

## Overview
- Demonstrates how to insert arrays horizontally and apply markers in a template.
- Explains the usage of CreateTemplateMarkerProcessor to manipulate marker data.
- Describes the ApplyMarkers method for processing markers in the template.

## Content

### Example Code: Inserting Arrays Horizontally and Applying Markers

```csharp
// Insert Array Horizontally.
string[] names = new string[] { "Mickey", "Donald", "Tom", "Jerry" };
string[] descriptions = new string[] { "Mouse", "Duck", "Cat", "Mouse" };
marker.AddVariable("Names", names);
marker.AddVariable("Descriptions", descriptions);

// Stretch Formula
marker.AddVariable("NumbersTable", numbersDt);

// Process the markers in the template.
marker.ApplyMarkers();
```

### VB.NET Code: Creating Template Marker Processor

```vb
' Create Template Marker Processor.
' Northwind Customers Table
Dim marker As ITemplateMarkersProcessor = workbook.CreateTemplateMarkersProcessor()
marker.AddVariable("Customers", northwindDt)

' Insert Array Horizontally.
Dim names As String() = New String() {"Mickey", "Donald", "Tom", "Jerry"}
Dim descriptions As String() = New String() {"Mouse", "Duck", "Cat", "Mouse"}
marker.AddVariable("Names", names)
marker.AddVariable("Descriptions", descriptions)

' Stretch Formula
marker.AddVariable("NumbersTable", numbersDt)

' Process the markers in the template.
marker.ApplyMarkers()
```

### Explanation
Here, `CreateTemplateMarkerProcessor` returns the `ITemplateMarkersProcessor` interface, which creates and manipulates the marker data. The `ApplyMarkers` method of `ITemplateMarkersProcessor` is the special method that processes the markers in the template.

### Specifying Markers
You can also specify the marker by using the following code.

## References
- [Sample Code: Applying Template Markers](#sample-code)
- [ITemplateMarkersProcessor Documentation](#itemplatemarkersprocessor)

### Related Topics
- [Marker Variables in Excel Templates](#marker-variables)
- [Processing Markers in Templates](#processing-markers)

## API Reference

### `CreateTemplateMarkerProcessor`
- **Description**: Creates a new instance of the `ITemplateMarkersProcessor` interface.
- **Returns**: An instance of `ITemplateMarkersProcessor`.

### `ApplyMarkers`
- **Description**: Processes the markers in the template.
- **Parameters**: None.
- **Returns**: None.

### `AddVariable`
- **Description**: Adds a variable to the template marker processor.
- **Parameters**:
  - `name`: Name of the variable.
  - `value`: Value of the variable.

## Code Examples
### C#
```csharp
// Example of using ApplyMarkers
marker.ApplyMarkers();
```

### VB.NET
```vb
' Example of using ApplyMarkers
marker.ApplyMarkers()
```

<!-- tags: [xlsio, template, marker, variable, processor, applymarkers] keywords: [template markers, array insertion, horizontal array, stretch formula, marker processing] -->
```