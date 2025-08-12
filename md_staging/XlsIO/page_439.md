```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_439.jpeg
document_name: XlsIO
page_number: 439
page_id: XlsIO#page_439
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:07Z
fidelity: lossless
-->

## Essential XlsIO

### Example Code

```csharp
// Get the first series from the Series collection
IChartSerie serieOne = chart.Series[0];

// Set the Series name to the Data Labels through Data Points
serieOne.DataPoints[0].DataLabels.IsSeriesName = true;

// Set the Value to the Data Labels through Data Points
serieOne.DataPoints[0].DataLabels.IsValue = true;
```

```vb
' Get the chart from the charts collection
Dim chart As IChart = sheet.Charts(0)

' Get the first series from the Series collection
Dim serieOne As IChartSerie = chart.Series(0)

' Set the Series name to the Data Labels through Data Points
serieOne.DataPoints(0).DataLabels.IsSeriesName = True

' Set the Value to the Data Labels through Data Points
serieOne.DataPoints(0).DataLabels.IsValue = True
```

### 5.2 Advanced

This section contains various questions and answers for the Advanced-level users.

#### 5.2.1 How to create a Chart with a discontinuous range?

The following code example illustrates creating a chart with discontiguous data ranges.

```csharp
[C#]
```

---

```markdown
### WinForms-specific conventions

- Treat control names, namespaces, and types exactly (e.g., Syncfusion.Windows.Forms.Tools.TabControlAdv, Syncfusion.Windows.Forms.Grid).

```markdown
### API Reference (if applicable)

- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required.
- Returns: Type + description.
- Exceptions: bullet list.

```markdown
### Code Examples (multi-language supported)

- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

### Page-level Navigation/TOC (if applicable)

- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

### Cross References

- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

### RAG Annotations

- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
- Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: XlsIO#page_439#getting-started -->. Do not add if the heading text is unclear.

---
```