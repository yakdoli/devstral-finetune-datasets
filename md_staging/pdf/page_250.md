```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_250.jpeg
document_name: pdf
page_number: 250
page_id: pdf#page_250
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:16Z
fidelity: lossless
-->

# Essential PDF

```csharp
// To hide the viewer application's Tool bar
doc.ViewerPreferences.HideToolbar = True

// To hide the viewer application's Menu bar
doc.ViewerPreferences.HideMenubar = True

// To hide the user interface elements such as Scroll bar, navigation controls
doc.ViewerPreferences.HideWindowUI = True
```

## Sample Location

A sample which demonstrates the PDF Page Settings is available in the following sample installation location:

```
<Install Location>\Windows\Pdf.Windows\Samples\2.0\Settings\Page Settings
```

## 4.1.7.8 Headers and Footers

Headers and footers can be placed in the pages of your PDF document.

Follow the below procedure to place a header:

1. Create a template object for the header. `PdfPageTemplateElement` class can be used for creating a template object.
2. Assign the created template header to PDF document header.

The same procedure can be followed to create a footer. Page numbers on the footer of a document are set by using automatic fields.

You can dock the header or footer to any position.

The following code example illustrates how to create a Header and Footer.

```csharp
[C#]

// Create a header and draw the image.
RectangleF rect = new RectangleF(0, 0, doc.Pages[0].GetClientSize().Width, 50);
```

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  ```html
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
  ```
- Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., ```<!-- anchor: pdf#page_250#headers-and-footers -->```. Do not add if the heading text is unclear.
```