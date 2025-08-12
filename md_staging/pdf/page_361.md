```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_361.jpeg
document_name: pdf
page_number: 361
page_id: pdf#page_361
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:46:12Z
fidelity: lossless
-->

# Essential PDF

```csharp
' Draw the rectangle for the size of the text.
page.Graphics.DrawRectangle(PdfPens.Red, New RectangleF(rect.Location, textSize))
```

## 5.1.2.7 How to set margins for the PDF pages?

Margins can be set on all sides or on a particular side of the page using the `PageSettings.Margins` property. Following are the options of this property:

- `All`: Sets margins size on all the sides
- `Bottom`: Sets the bottom margin size
- `Left`: Sets the left margin size
- `Top`: Sets the top margin size
- `Right`: Sets the right margin size

```csharp
[C#]

// Adds a section to the document
PdfSection section = doc.Sections.Add();

// Adds a page to the section
PdfPage page = section.Pages.Add();

// Sets Margin to the page
section.PageSettings.Margins.All = 0;
```

```vbnet
[VB.NET]

' Adds a section to the document
Dim section As PdfSection = doc.Sections.Add()

' Adds a page to the section
PdfPage = section.Pages.Add()

' Sets Margin to the page
section.PageSettings.Margins.All = 0
```

<!-- tags: [product, module, control, api, version?] keywords: [margin, pdf, page, setting, essentialpdf, all, bottom, left, top, right, csharp, vb.net, syncfusion, winforms] -->
```