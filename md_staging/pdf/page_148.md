```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: pdf
page_number: 148
page_id: pdf#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:42Z
fidelity: lossless
-->

# Essential PDF

## Content

### Event Descriptions

| Name           | Description                                                                                 |
|----------------|---------------------------------------------------------------------------------------------|
| BeginPageLayout| This event is raised before the element should is printed on the page. (Inherited from PdfLayoutElement.) |
| EndPageLayout  | This event is raised after the element is printed on the page. (Inherited from PdfLayoutElement.) |

### 4.1.2.3.2.2 PdfGrid Creation

**Note:** You must add Syncfusion.Pdf.Grid namespace to work with PdfGrid.

You can create a PdfGrid by simply specifying the new operator with a proper constructor. After assigning data source it can be drawn using one of the overloads of Draw method.

#### [C#]

```csharp
// Create a PdfGrid.
PdfGrid pdfGrid = new PdfGrid();

// Assign data source.
pdfGrid.DataSource = dataSource;

// Draw PdfGrid.
pdfGrid.Draw(graphics);
```

#### [VB.NET]

```vbnet
' Create a PdfGrid.
Dim pdfGrid As New PdfGrid()

' Assign data source.
pdfGrid.DataSource = dataSource

' Draw PdfGrid.
pdfGrid.Draw(graphics)
```

Data to PdfGrid can be entered manually or taken from an external data source. Also, the draw method helps to control the layout of the PdfGrid and returns information to user after drawing completes. The following topics discuss them.

- Data
- Layout

## Page-level Navigation/TOC

- Creating a PdfGrid
- Assigning a Data Source to PdfGrid
- Drawing a PdfGrid

<!-- tags: [pdfgrid, syncfusionpdfsdk, pdf, grid layout] keywords: [pdfgrid, data source, draw method, grid layout] -->
```