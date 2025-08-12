```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: edit
page_number: 024
page_id: edit#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:12Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```xml
<extensions />
<lexems />
<splits />
</ConfigLanguage>
<ConfigLanguage name="C#">
 <formats>
  <format name="Text" Font="Courier New, 10pt" FontColor="Black" />
  <format name="SelectedText" Font="Courier New, 10pt" BackColor="Highlight" FontColor="HighlightText" />
  <format name="Whitespace" Font="Courier New, 10pt" FontColor="Black" />
  <format name="KeyWord" Font="Courier New, 10pt" FontColor="Blue" />
 </formats>
 <extensions>
  <extension>cs</extension>
 </extensions>
 <lexems>
  <lexem BeginBlock="public" Type="KeyWord" />
 </lexems>
 <splits>
  <split>+,</split>
 </splits>
</ConfigLanguage>
</ArrayOfConfigLanguage>
```

From the code given above, the configuration file contains a set of language configurations. Every configuration file must have configuration for the language named **default_language**, which is used as a default configuration.

## Language Configuration (ConfigLanguage) Definition

### Name of the language
The **name** of the language must be set using the `name` attribute of the `ConfigLanguage` tag. If the language is case insensitive, you should set the `Caselnsensitive` attribute to 'True'.

### Language Configuration Sections

Language configuration is divided into the following four sections:

- **Extensions**
- **Splits**
- **Formats**
- **Lexems**

### Extensions
- **Extensions**-Contains a list of extensions that are associated with this language. Every extension can be specified like the following:

```xml
<extension>cs</extension>
```

## API Reference

### WinForms-specific conventions

- Prefer C# samples when language is ambiguous; if VB is explicitly shown, keep both.
- Treat control names, namespaces, and types exactly (e.g., `Syncfusion.Windows.Forms.Tools.TabControlAdv`, `Syncfusion.Windows.Forms.Grid`).
- Distinguish design-time vs runtime features; preserve property grids, designer steps, and menu paths as regular text or ordered lists.
- When API elements are listed (Properties/Methods/Events/Enums), keep their exact order and names, including parentheses for methods and event handler signatures if visible.

## Code Examples

- Extract ALL code exactly. Use fenced blocks with language: ````csharp`, ````vb`, ````xml`, ````xaml`, ````js`, ````css`, ````ts`, ````python`.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

### Cross References

See also: explicit links/texts present on this page.

### RAG Annotations

<!-- tags: Essential Edit for Windows Forms, ConfigLanguage, Lexems, Splits, Formats, C# SDK keywords: edit, windows forms, configlanguage, lexems, splits, formats, programming language configuration, font settings, extension handling -->

```html
```