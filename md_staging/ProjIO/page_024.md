```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_024.jpeg
document_name: ProjIO
page_number: 024
page_id: ProjIO#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:58:35Z
fidelity: lossless
-->

# Essential ProjIO

```csharp
[C#]

// Creating a new instance of the Project object
Project project = new Project();

// Setting Project Default information
project.DefaultStartTime = new TimeSpan(8, 0, 0);
project.DefaultFinishTime = new TimeSpan(17, 0, 0);
project.DefaultStandardRate = 0f;
project.DefaultOvertimeRate = 0f;
project.DefaultTaskEVMethod = EarnedValueMethod.PercentComplete;
project.DefaultFixedCostAccrual = DefaultFixedCostAccrual.Prorated;

// Saving the Project
project.Save("DefaultProjectProperties.xml");
```

```vb
[VB]

' Creating an instance of a Project
Dim project As Project = New Project()

' Setting Project information
project.DefaultStartTime = New TimeSpan(8, 0, 0)
project.DefaultFinishTime = New TimeSpan(17, 0, 0)
project.DefaultStandardRate = 0.0F
project.DefaultOvertimeRate = 0.0F
project.DefaultTaskEVMethod = EarnedValueMethod.PercentComplete
project.DefaultFixedCostAccrual = DefaultFixedCostAccrual.Prorated

' Saving the Project
project.Save("DefaultProjectProperties.xml")
```

## API Reference (if applicable)
### WinForms-specific conventions
- Prefer C# samples when language is ambiguous; if VB is explicitly shown, keep both.
- Treat control names, namespaces, and types exactly (e.g., Syncfusion.Windows.Forms.Tools.TabControlAdv, Syncfusion.Windows.Forms.Grid).
- Distinguish design-time vs runtime features; preserve property grids, designer steps, and menu paths as regular text or ordered lists.
- When API elements are listed (Properties/Methods/Events/Enums) in subsections.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

### RAG Annotations
- At the end, add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
- Add optional per-section anchors as HTML comments before each H2/H3 to aid chunking, using IDs derived from the heading (kebab-case), e.g., <!-- anchor: ProjIO#page_024#getting-started -->. Do not add if the heading text is unclear.
```