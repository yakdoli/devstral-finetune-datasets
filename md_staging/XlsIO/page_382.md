```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_382.jpeg
document_name: XlsIO
page_number: 382
page_id: XlsIO#page_382
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:12:03Z
fidelity: lossless
-->

## Overview
- Demonstrates how to insert and process markers in an Excel template using XlsIO.
- Explains inserting different types of markers, including simple markers, markers that retrieve values, and markers that include cell addresses.
- Provides code examples in both C# and VB.NET languages for creating and applying markers.

## Content

### Marker Usage in XlsIO

This section showcases how to utilize markers within an Excel template using the XlsIO library. Markers allow dynamic content insertion into the template based on variables and cell ranges.

#### Code Example: C#

```csharp
// Insert Simple marker.
sheet.Range["B2"].Text = "%Marker";

// Insert marker which gets value of Author name.
sheet.Range["C2"].Text = "%Marker2.Worksheet.Workbook.Author";

// Insert marker which gets cell address.
sheet.Range["H2"].Text = "%ArrayProperty.Cells.Address";

ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();
marker.AddVariable("Marker", "First test of markers");
marker.AddVariable("Marker2", sheet.Range["B2"]);
marker.AddVariable("ArrayProperty", sheet.Range["B2:G2"]);

// Process the markers in the template.
marker.ApplyMarkers();
```

#### Code Example: VB.NET

```vb
' Insert Simple marker.
sheet.Range("B2").Text = "%Marker"

' Insert marker which gets value of Author name.
sheet.Range("C2").Text = "%Marker2.Worksheet.Workbook.Author"

' Insert marker which gets cell address.
sheet.Range("H2").Text = "%ArrayProperty.Cells.Address"

Dim marker As ITemplateMarkersProcessor = workbook.CreateTemplateMarkersProcessor()
marker.AddVariable("Marker", "First test of markers")
marker.AddVariable("Marker2", sheet.Range("B2"))
marker.AddVariable("ArrayProperty", sheet.Range("B2:G2"))

' Process the markers in the template.
marker.ApplyMarkers()
```

### Explanation of Code

1. **Inserting Simple Markers**:
   - The simplest marker (`"%Marker"`) is inserted into cell B2. This marker will be replaced by a predefined value during the marker processing phase.

2. **Markers Retrieving Values**:
   - The marker (`"%Marker2.Worksheet.Workbook.Author"`) in cell C2 retrieves the value of the author from the workbook's properties and replaces the marker with this value.

3. **Markers with Cell Addresses**:
   - The marker (`"%ArrayProperty.Cells.Address"`) in cell H2 inserts the address of the range `sheet.Range["B2:G2"]`. This demonstrates how markers can reference cell addresses from a specified range.

4. **Creating and Applying Markers**:
   - The `ITemplateMarkersProcessor` is created and used to define the variables that will replace the markers in the template. The `AddVariable` method associates each marker with its respective value or range.
   - The markers are processed using the `ApplyMarkers` method, which replaces all the markers in the template with their corresponding values or references.

## API Reference

### Methods

- **`CreateTemplateMarkersProcessor()`**: Creates a new `ITemplateMarkersProcessor` to handle the processing of markers.
- **`AddVariable(String Name, Object Value)`**: Associates a variable name with its corresponding value or range.
- **`ApplyMarkers()`**: Processes all the markers in the template, replacing them with their defined values.

### Usage

This functionality is particularly useful for creating dynamic reports or templates where content needs to be generated based on predefined variables or cell ranges.

## Code Examples

### C#

The above C# example demonstrates creating and applying markers that retrieve values from different sources, including fixed text, workbook properties, and cell addresses.

### VB.NET

The VB.NET example is equivalent to the C# example, performing the same tasks of inserting and processing markers within an Excel template.

## See also

- [XlsIO Documentation](https://documentation.syncfusion.com/windowsforms/XlsIO/Introduction.html)
- [Template Markers in Excel](https://help.syncfusion.com/xlsio/features#template-markers)

<!-- tags: [xlsio, excel, template markers, c#, vb.net, winforms, dynamic content, syncfusion] keywords: [template markers, excel, dynamic content, c#, vb.net, xlsx] -->
```