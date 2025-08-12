```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_132.jpeg
document_name: pdf
page_number: 132
page_id: pdf#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:41Z
fidelity: lossless
-->

# Essential PDF

```csharp
' Drawing the PdfLightTable
pdfLightTable.Draw(page, PointF.Empty)
```

## Overview

- Demonstrates how to use `PdfLightTable` in the Silverlight platform.
- Highlights the use of `IEnumerable` objects as input for `PdfLightTable`.
- Provides examples in both C# and VB.NET.

## Content

### 4.1.2.3.1.2.1.2.1 IEnumerable

**PdfLightTable** in the Silverlight platform can take input from `IEnumerable` objects. The following is the code snippet:

#### C#

```csharp
// Creating PdfLightTable.
PdfLightTable pdfLightTable = new PdfLightTable();

// Creating IEnumerable source.
Dictionary<string, string> dictionary = new Dictionary<string, string>();
dictionary.Add("AAA", "111");
dictionary.Add("BBB", "112");
dictionary.Add("CCC", "113");

pdfLightTable.DataSource = dictionary;

// Draw.
pdfLightTable.Draw(page, PointF.Empty);
```

#### VB.NET

```vb.net
' Creating PdfLightTable.
Dim pdfLightTable As New PdfLightTable()

' Creating IEnumerable source.
Dim dictionary As New Dictionary(Of String, String)()
dictionary.Add("AAA", "111")
dictionary.Add("BBB", "112")
dictionary.Add("CCC", "113")

pdfLightTable.DataSource = dictionary

' Drawing the PdfLightTable
pdfLightTable.Draw(page, PointF.Empty)
```

### 4.1.2.3.1.2.1.3 Event Handlers

## API Reference

### WinForms-specific conventions
- Ensure to prefer C# examples unless VB is explicitly shown.
- Maintain control names, namespaces, and types exactly.
- Differentiate between design-time and runtime features.
- Include property grids, designer steps, and menu paths as needed.

## Code Examples

- Demonstrates the use of `PdfLightTable` with `IEnumerable` objects using both C# and VB.NET code snippets.
- The `DataSource` property is assigned a `Dictionary` to populate the table.
- Drawing the `PdfLightTable` is performed using the `Draw` method.

## Page-level Navigation/TOC

- The section is organized under "4.1.2.3.1.2.1.2.1 IEnumerable" and "4.1.2.3.1.2.1.3 Event Handlers."

<!-- tags: [product, module, control, api, version?] keywords: [PdfLightTable, IEnumerable, Silverlight, DataSource, Draw] -->
```