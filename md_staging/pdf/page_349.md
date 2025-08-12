```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_349.jpeg
document_name: pdf
page_number: 349
page_id: pdf#page_349
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:45:23Z
fidelity: lossless
-->

# Essential PDF

## Content

### [C#]

```csharp
Font fnt = new Font("c:\\Arial.ttf", 12f);
PdfFont font = new PdfTrueTypeFont(fnt, true);
page.Graphics.DrawString("Embedded font", font, brush, 0, 100);
```

### [VB.NET]

```vb
Dim fnt As PdfFont = New Font("c:\\Arial.ttf", 12f)
Dim font As PdfFont = New PdfTrueTypeFont(fnt, True)
page.Graphics.DrawString("Embedded font", font, brush, 0, 100)
```

### 5.1.1.8 How To Find the End Position Of a Table?

There is often a need to determine the end position of a published table since the next table needs to be positioned after the first one. This position is determined by using the `PdfLightTableLayoutResult` object of the table returned by the `PdfLightTable.Draw` method. This finds the exact position of the table, even if it spans for multiple pages. `PdfLightTableLayoutResult` has several methods to work with the bounds and page where the table ends.

### [C#]

```csharp
// Draw a large table that can span for multiple pages and get the result.
PdfLightTableLayoutResult result = table.Draw(page, PointF.Empty);

// Get the location where the table ends
PointF location = new PointF(bounds.Left, bounds.Bottom);

// Draw another table just below the previous table
table.Draw(result.Page, location);
```

### [VB.NET]

```vb
' Draw a large table that can span for multiple pages and get the result.
Dim result As PdfLightTableLayoutResult = table.Draw(page, PointF.Empty)

' Get the location where the table ends
Dim location As PointF = New PointF(bounds.Left, bounds.Bottom)

' Draw another table just below the previous table
table.Draw(result.Page, location)
```

## API Reference

### Methods

- **`PdfLightTableLayoutResult Draw(PdfPage, PointF)`**
  - **Parameters:**
    - `PdfPage`: The page on which the table is drawn.
    - `PointF`: Starting position for the table.
  - **Returns:** The layout result of the table drawing operation, including bounds and page information.

### Other Classes

- **`PdfLightTableLayoutResult`**
  - This class provides information about the table's layout, such as bounds and the page where the table ends.

## Code Examples

### Embedding a Font in a PDF Document

```csharp
Font fnt = new Font("c:\\Arial.ttf", 12f);
PdfFont font = new PdfTrueTypeFont(fnt, true);
page.Graphics.DrawString("Embedded font", font, brush, 0, 100);
```

### Dynamically Positioning Tables in a PDF Document

```csharp
PdfLightTableLayoutResult result = table.Draw(page, PointF.Empty);
PointF location = new PointF(result.Bounds.Left, result.Bounds.Bottom);
table.Draw(result.Page, location);
```

### VB.NET Example for Positioning Tables

```vb
Dim result As PdfLightTableLayoutResult = table.Draw(page, PointF.Empty)
Dim location As PointF = New PointF(result.Bounds.Left, result.Bounds.Bottom)
table.Draw(result.Page, location)
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Essential PDF, PdfLightTable, PdfLightTableLayoutResult, TablePositioning, FontEmbedding] keywords: [PdfLightTable, PdfLightTableLayoutResult, Draw, Table, Positioning, Font, Embedding, MultiplePages] -->
```