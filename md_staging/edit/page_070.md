```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: edit
page_number: 070
page_id: edit#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:14Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
Me.editControl1.StrikeThrough(Me.editControl1.CurrentLine, Color.IndianRed)

' Strikeout the selected text.
Me.editControl1.StrikeThrough(Me.editControl1.Selection.Top, 
                             Me.editControl1.Selection.Bottom, Color.Navy)

' Strikeout the text in the specified text range.
Me.editControl1.StrikeThrough(startCoordinatePoint, endCoordinatePoint, 
                             Color.Aqua)
```

To remove the strikethrough line, just call one of the above mentioned methods and specify the `Color` parameter as `Color.Empty`.

```csharp
using Syncfusion.Windows.Forms;
using Syncfusion.Windows.Forms.Edit;
using Syncfusion.Windows.Forms.Edit.Implementation;
using Syncfusion.Windows.Forms.Edit.Implementation.IO;
using Syncfusion.Windows.Forms.Edit.Implementation.Parser;
```

Figure 19: Striking Through Range of Text

A sample which demonstrates the StrikeThrough feature is available in the following sample installation path.

```
..\My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Edit.Windows\Samples\2.0\Advanced Editor Functions\StrikeThroughDemo
```

## See Also

- Text Border
- Text Selection

## 4.4.5 Text Handling

Edit control offers support for text manipulation operations like append, delete and insertion of multiple lines of text, which is elaborated in the below topic:

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required.
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
- Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: edit#page_070#getting-started -->.
```