```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_409.jpeg
document_name: grid
page_number: 409
page_id: grid#page_409
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:05Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- **Serialization and De-serialization Support**: Essential Grid control supports serialization and de-serialization of the grid's schema information.
- **Export as Image Support**: Essential Grid provides image export support for the Grid, GridDataBoundGrid, and GridGrouping controls when exporting to Excel.

## Content

### SOAP, Binary and XML Serialization
Essential Grid control has support for serialization and de-serialization of the grid's schema information.

### Export as Image Support
Essential Grid provides image export support for the Grid, GridDataBoundGrid, and GridGrouping controls in the Excel converter. With this support, users can enable or disable image export from a Grid control to Excel. This is a Boolean property and its default value is true. This property will affect the grid-to-Excel converter when the `ExportStyle` property is true.

#### Use Case Scenarios
This feature allows you to control the image export in the grid-to-Excel converter. This property will affect the grid when `ExportStyle` is true.

#### Properties
| Property      | Description                                                                                     | Data Type |
|---------------|-------------------------------------------------------------------------------------------------|-----------|
| ExportImage   | Used to enable or disable the image export in Syncfusion Windows Forms grid.                   | Boolean   |

#### Syntax

##### C#
```csharp
ExcelExport.ExportStyle = true;
// ExportImage works only when ExportStyle is true.
ExcelExport.ExportImage = false;
```

##### VB.NET
```vb
ExcelExport.ExportStyle = True
' ExportImage works only when ExportStyle is true.
ExcelExport.ExportImage = False
```

#### Note
**Serialization is the process of saving the state of an object as a stream of bytes. The reverse of this process is called deserialization.**

Grid control supports three different types of serialization techniques namely:

## API Reference (if applicable)
* **Properties**
  - `ExportImage`: A Boolean property used to enable or disable image export from a Grid control to Excel. Default value: `true`.

## Code Examples (multi-language supported)
The provided code examples demonstrate how to configure the `ExportStyle` and `ExportImage` properties in both C# and VB.NET.

## Cross References
See also:
- Serialization and De-serialization techniques
- Grid control properties and methods related to export functionalities

<!-- tags: [Syncfusion Winforms, Essential Grid, Grid serialization, ExportImage, ExportStyle] keywords: [serialization, de-serialization, Excel export, Windows Forms, Grid control, ExportImage property, ExportStyle property] -->
```