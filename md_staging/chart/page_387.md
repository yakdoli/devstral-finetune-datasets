```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_387.jpeg
document_name: chart
page_number: 387
page_id: chart#page_387
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:22Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Chart Axes Layouts

[VB.NET]
```vb
Me.ChartControl1.ChartArea.XAxesLayoutMode = ChartAxesLayoutMode.SideBySide;
```

![Multiple Axes with Side by Side Layout](https://example.com/image)

*Figure 252: ChartControl with SideBySide Layout of Multiple Axes*

### ChartAxesLayouts

You can now combine the stacking and side-by-side chart axes layouts when multiple Axes are used, as shown in the below image. Using this feature, it is possible to position the three Y axis, as one on the right side and the second one on the same side and the third one on the opposite side.

### WinForms-specific conventions
- Prefer C# samples when language is ambiguous; if VB is explicitly shown, keep both.
- Treat control names, namespaces, and types exactly (e.g., Syncfusion.Windows.Forms.Tools.TabControlAdv, Syncfusion.Windows.Forms.Grid).
- Distinguish design-time vs runtime features; preserve property grids, designer steps, and menu paths as regular text or ordered lists.
- When API elements are listed (Properties/Methods/Events/Enums), keep their exact order and names, including parentheses for methods and event handler signatures if visible.

### Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

### API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.
```