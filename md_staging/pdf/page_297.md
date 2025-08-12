```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_297.jpeg
document_name: pdf
page_number: 297
page_id: pdf#page_297
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:52Z
fidelity: lossless
-->

# Essential PDF

```csharp
// Load the Document.
PdfLoadedDocument ldoc1 = new PdfLoadedDocument("Form_Action.pdf");

// Create a PdfLodedForm.
PdfLoadedForm form = ldoc1.Form;

PdfJavaScriptAction javaAction1 = new PdfJavaScriptAction("app.alert(\"You are looking at Java script action of PDF (PdfLoadedCheckBoxField)\\\")");

(form.Fields[".NET"] as PdfLoadedCheckBoxField).LostFocus = javaAction1;
```

### [VB.NET]

```vb
' Load the Document.
Dim ldoc1 As New PdfLoadedDocument("Form_Action.pdf")

' Create a PdfLodedForm.
Dim form As PdfLoadedForm = ldoc1.Form

Dim javaAction1 As New PdfJavaScriptAction("app.alert(""You are looking at Java script action of PDF (PdfLoadedCheckBoxField)"")")
```

```vb
TryCast(form.Fields(".NET"), PdfLoadedCheckBoxField).LostFocus = javaAction1
```

## 4.3.2 Form Fields

An interactive form is a collection of fields for gathering information interactively from the user. A PDF document may contain any number of fields appearing on any combination of pages, all of which makes up a single global interactive form spanning the entire document. Arbitrary subsets of these fields can be imported or exported from the document.

You can change the form's properties, add new fields or remove existing fields. Also, you can flatten the loaded field by using the Flatten property.

This section covers the following:

- Form Fields Creation
- Editing Form Fields

### Form Fields Creation
```markdown
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
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
 - Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: pdf#page_297#getting-started -->. Do not add if the heading text is unclear.
```

<!-- tags: [syncfusion, pdf, form fields, document, loaded, interactive, creation,编辑] keywords: [form fields, PDF, document, Syncfusion Winforms, version 11.4.0.26, interactive forms, loaded document, creation, editing] -->
```