<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_864.jpeg
document_name: tools
page_number: 864
page_id: tools#page_864
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
{
    Console.WriteLine(" CharacterCasingChanged event is raised ");
}
```

### [VB.NET]

```vb
Private Sub maskedEditBox1_CharacterCasingChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" CharacterCasingChanged event is raised ")
End Sub
```

### 3.5.8.8.4.6 HideSelectionChanged

This event occurs when the HideSelection property is changed. The HideSelection property indicates that the selection should be hidden when the edit control loses focus.

The event handler receives an argument of type EventArgs containing data related to this event.

### [C#]

```csharp
private void maskedEditBox1_HideSelectionChanged(object sender, EventArgs e)
{
    Console.WriteLine(" HideSelectionChanged event is raised ");
}
```

### [VB.NET]

```vb
Private Sub maskedEditBox1_HideSelectionChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" HideSelectionChanged event is raised ")
End Sub
```

### 3.5.8.8.4.7 MaskCustomValidate

This event is handled to provide custom behavior to any mask characters.

The event handler receives an argument of type MaskCustomValidateArgs containing data related to this event. The following MaskCustomValidateArgs members provide information specific to this event.

| Members | Description |
|---------|-------------|
|         |             |

## API Reference (if applicable)
- Namespace, Class, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

### Code Examples (multi-language supported)

Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
```csharp
Imports Syncfusion.Windows.Forms
```

### Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page.

### RAG Annotations
- Add an HTML comment with tags and keywords derived ONLY from visible content:
  <!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
