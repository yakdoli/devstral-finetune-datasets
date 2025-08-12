```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_305.jpeg
document_name: XlsIO
page_number: 305
page_id: XlsIO#page_305
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:48Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- This section explains how to embed and set the type of an OLE object in an Excel worksheet.
- Demonstrates the use of Adobe Acrobat Document as an OLE object type within an Excel file.
- Describes how to control the page layout in an Excel worksheet using XlsIO.

## Content

### Setting the Type of the OLE Object

The following code samples illustrate the condition when the property is set to **AdobeAcrobatDocument**.

#### Code Examples

```csharp
/* C# */
oleObject1.OleObjectType = OleObjectType.AdobeAcrobatDocument;
```

```vb.net
/* VB.NET */
oleObject1.OleObjectType = OleObjectType.AdobeAcrobatDocument
```

### 4.3 Page Layout

**Excel also provides support to control the layout of a particular page. It provides various customization options to customize the page margin, orientation, size, and so on.**

The following topics explain the various ways your spreadsheet fits onto paper, and how it can be controlled by using XlsIO.

## API Reference

This section provides a reference for the methods and properties related to page layout in XlsIO.

## Code Examples

Examples demonstrating setting up page layout using XlsIO can be found in the [XlsIO API documentation](#xlsio-api-documentation).

## Page-Level Navigation/TOC

- **Setting the Type of the OLE Object**
- **4.3 Page Layout**

## Cross References

See also:
- [OLE Object Handling in XlsIO](#ole-object-handling-in-xlsio)
- [Page Layout Options in Excel](#page-layout-options-in-excel)

## RAG Annotations

<!-- tags: [XlsIO, Excel, OLE Object, Page Layout, Adobe Acrobat Document] keywords: [embedded object, page orientation, page margin, page size] -->
```