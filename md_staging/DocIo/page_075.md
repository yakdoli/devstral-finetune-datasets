```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: DocIo
page_number: 075
page_id: DocIo#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:36Z
fidelity: lossless
-->

# Essential DocIO

```vb
[VB.NET]

Dim doc1 As IWordDocument = New WordDocument()
doc1.Open("Background.doc")
Dim doc2 As IWordDocument = New WordDocument()
doc2.EnsureMinimal()

Select Case doc1.Background.Type
    Case BackgroundType.Gradient
        doc2.Background.Gradient = doc1.Background.Gradient.Clone()

    Case BackgroundType.Picture, BackgroundType.Texture
        doc2.Background.Picture = doc1.Background.Picture

    Case BackgroundType.Color
        doc2.Background.Color = doc1.Background.Color

    Case Else
End Select

doc2.Background.Type = doc1.Background.Type
doc1.Background.Type = BackgroundType.Color
doc1.Background.Color = Color.Red

doc1.Save("Background.doc")
doc2.Save("BackgroundNew.doc")
```

## Background Gradient

The Background Gradient class represents the background gradient fill effect in the Word document. To set the gradient by using Word menu, open the Format menu, point to Background, Fill Effects, and then click Gradient.

The following screen shot shows the Fill Effects dialog box.
```html

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list of exceptions.

## Code Examples (multi-language supported)
- Extract ALL code examples exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
 - Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: DocIo#page_075#getting-started -->. Do not add if the heading text is unclear.
```
```html
<!-- tags: [product, module, control, api, version?] keywords: [Background Gradient, Fill Effects, DocIO, Word document, Microsoft Word] -->
```