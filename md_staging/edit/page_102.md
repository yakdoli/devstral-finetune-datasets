```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: edit
page_number: 102
page_id: edit#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:30Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```xml
[HTML or XML]

<abc>
    <xyz>
        ...
    </xyz>
</abc>
```

- Similarly, when the Edit Control is using C# configuration settings, any text enclosed within '{' and '}' should get automatically indented, just as in the VS.NET editor. Also, the closing brace should be automatically indented with its matching opening brace.
  
- For languages like VB.NET, the End statement should get automatically indented on pressing the ENTER key, after entering the method header for the VB.NET samples.

```vb.net
[VBNET]

Private sub TestMethod() '----> Method header
    '----> Press Enter key

End sub '----> End statement should be automatically aligned with the
function header
```

## 4.4.11.4 Unicode

Unicode is a standard used to encode all the languages of the world in computers. It is an international standard used with the goal to resolve ambiguities that traditionally arise with complex scripts like Japanese, Arabian or Chinese, on computer systems. Besides solving many Internationalization issues, Unicode-enabled programs also run faster under Windows NT, 2000 and XP.

Edit Control fully supports serializing and displaying Unicode characters. All Unicode text is saved in UTF-8 format, by default. Moving Unicode text between Edit Control and other Word Processing software programs is also straightforward through Copy / Paste clipboard functions.

Essential Edit also supports handling of all other text encoding formats specified in the System.Text.Encoding class like ASCII, UTF7, UTF8 and BigEndianUnicode.

The following screenshot illustrates the use of Chinese, Arabic, Hindi, Russian and Greek text in the Edit Control.

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

<!-- tags: [Edit Control, Unicode, Windows Forms, C#, VB.NET, AutoIndentation, Document Samples] keywords: [Unicode, Internationalization, Edit Control, Syncfusion, AutoIndentation, C#, VB.NET] -->
```