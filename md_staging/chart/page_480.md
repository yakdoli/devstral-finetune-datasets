```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_480.jpeg
document_name: chart
page_number: 480
page_id: chart#page_480
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:47Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- A guide on adding and customizing Interactive Cursor in a Chart Application
- Focuses on setting orientation and color for the cursor
- Includes a code snippet for implementing an interactive cursor in C#.NET

## Content

### Interactive Cursor Settings

| Color                     | Interactive Cursor is drawn                                         | Color |
|---------------------------|-------------------------------------------------------------|-------|
| Color                     | Specifies the base color, which is to be used other than the<br>default color. This acts as a<br>parent color.                      | Color |


### Drawing Interactive Cursor in a Chart Application

To add Interactive Cursor to the Chart control:

1. Add a Interactive cursor to the Chart control.
2. Set the orientation to horizontal or vertical or both.
3. Choose the color.

Refer to the following code snippets to draw the interactive cursor separately.

### Code Example

```csharp
[C#.NET]
cursor1 = new ChartInteractiveCursor(this.chartControl1.Series[0]);
this.chartControl1.ChartArea.InteractiveCursors.Add(cursor1);
cursor1.CursorOrientation = InteractiveCursorOrientation.Horizontal;
cursor1.HorizontalCursorColor = Color.Red;
```

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list of explicit links/texts present on the page.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## RAG Annotations
- <!-- tags: [chart, interactive cursor, windows forms, orientation, color, c#.net, programming, api] keywords: [interactive cursor, chart control, orientation, color, c#.net, windows forms, essential chart] -->
- Add per-section anchors as HTML comments using IDs derived from the heading (kebab-case), e.g., <!-- anchor: chart#page_480#interactive-cursor -->
```