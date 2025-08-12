```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_135.jpeg
document_name: pdf
page_number: 135
page_id: pdf#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:32:50Z
fidelity: lossless
-->

## Content

### PdfLightTableLayoutFormat

**Layouting PdfLightTable** can be done using the `PdfLightTableLayoutFormat` class. Overloads accepting pages can accept standard formats as other laying elements. However, they treat the `PdfLayoutBreakType.FitElement` value of `Format.Break` property as one, for a single row and not for the entire `PdfLightTable`.

#### Properties

| Name               | Description                        | Data Type          |
|--------------------|------------------------------------|--------------------|
| Break              | Gets or sets the break type        | PdfLayoutBreakType |
| EndColumnIndex     | Gets or sets the end column index   | Integer            |
| Layout             | Gets or sets the layout type        | PdfLayoutType      |
| PaginateBounds     | Gets or sets the PdfLightTable bounds for the following page | RectangleF     |
| StartColumnIndex   | Gets or sets the start column index | Integer            |

Also, you may select a range of columns using the `PdfLightTableLayoutFormat` properties, `StartColumnIndex` and `EndColumnIndex`. You should pass an instance of this class to one of the Draw overloads, instead of the `PdfLayoutFormat` class instance.

#### Code Examples

```csharp
[C#]

PdfLightTableLayoutFormat format = new PdfLightTableLayoutFormat();
format.StartColumnIndex = 0;
format.EndColumnIndex = 3;

// Draws the PdfLightTable from the first to the fourth column
pdfLightTable.Draw(page, PointF.Empty, format);
```

```vb
[VB.NET]
```

## API Reference

### Properties of PdfLightTableLayoutFormat

- **Break**: Gets or sets the break type (`PdfLayoutBreakType`).
- **EndColumnIndex**: Gets or sets the end column index (`Integer`).
- **Layout**: Gets or sets the layout type (`PdfLayoutType`).
- **PaginateBounds**: Gets or sets the `PdfLightTable` bounds for the following page (`RectangleF`).
- **StartColumnIndex**: Gets or sets the start column index (`Integer`).

### Methods

- **Draw**: Renders the PdfLightTable using the specified `PdfLightTableLayoutFormat` instance.

#### Parameters

| Name           | Type                           | Description                                 | Default | Required |
|----------------|--------------------------------|---------------------------------------------|---------|----------|
| page           | PdfPage                        | The target page for rendering               | -       | Yes      |
| origin         | PointF                         | The starting position for rendering        | -       | Yes      |
| format         | PdfLightTableLayoutFormat      | The layout format to use                   | -       | Yes      |

### Returns

- Type: `void`
- Description: Renders the PdfLightTable on the specified page.

### Exceptions

- **InvalidOperationException**: If the format is not valid or if any required parameters are missing.

## See also

- [PdfLightTable](#pdflighttable)
- [PdfLayoutBreakType](#pdflayoutbreaktype)
- [PdfLayoutType](#pdflayouttype)

<!-- tags: [Syncfusion Winforms, PdfLightTableLayoutFormat, Table Layout, Breaking Elements, Layout Properties] keywords: [PdfLightTable, LayoutFormat, StartColumnIndex, EndColumnIndex, BreakType, Pagination] -->
```