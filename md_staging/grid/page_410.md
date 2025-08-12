```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_410.jpeg
document_name: grid
page_number: 410
page_id: grid#page_410
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:14:51Z
fidelity: lossless
-->

## Overview

- **SOAP**: Helps convert the grid schema information to SOAP format.
- **Binary**: Helps convert the grid schema information to binary format.
- **XML**: Helps convert the grid schema information to XML format.

## Content

### SOAP

#### Serialization Example

##### Using C#

```csharp
this.gridControl1.Model.SaveSoap(dlg.FileName);
```

##### Using VB.NET

```vb
Me.gridControl1.Model.SaveSoap(dlg.FileName)
```

#### Deserialization Example

##### Using C#

```csharp
this.gridControl1.Model = GridModel.LoadSoap(dlg.FileName);
this.gridControl1.Refresh();
```

##### Using VB.NET

```vb
Me.gridControl1.Model = GridModel.LoadSoap(dlg.FileName)
Me.gridControl1.Refresh()
```

### Binary

## API Reference (if applicable)

Not specified in the provided content.

## Code Examples (multi-language supported)

Not additional code examples provided.

## Page-level Navigation/TOC (if applicable)

Not applicable for this page.

## Cross References

Not specified in the provided content.

## RAG Annotations

<!-- tags: [Syncfusion, Winforms, Grid, SOAP, Binary, XML, Serialization, Deserialization, C#, VB.NET] keywords: [grid schema, SOAP format, binary format, XML format, serialization, deserialization, C#, VB.NET, gridControl1, dlg.FileName, GridModel, Model] -->
```