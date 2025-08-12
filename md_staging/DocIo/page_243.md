```html
<!--source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_243.jpeg
document_name: DocIo
page_number: 243
page_id: DocIo#page_243
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:24Z
fidelity: lossless
-->

# Essential DocIO

```csharp
// Creating a new instance for the Word document
WordDocument document = new WordDocument();
// Setting the base folder path
string basePath=@"C:\InputFolder\";
// Opening the html file along with the base path of the html file
document.Open(Path.Combine(basePath,"Input.html"),
Syncfusion.DocIO.FormatType.Automatic, XHTMLValidationType.None, basePath);
// Saving the document
document.Save("sample.doc");
```

## Insert Formatted Text Snippet

This option enables to insert XHTML formatted text inside Word paragraphs with the following limitations:

- The content will be placed inside a `<p>` tag, to validate against the XHTML schemas as explained before.
- This html snippet cannot contain any block elements like `div`, and so on, and will result in an exception being thrown otherwise. The only exception to this case is a single `<p>` tag.
- Among the supported XHTML tags, only the inline tags can be used for formatting text.

The following code illustrates appending a HTML formatted string into a paragraph.

```csharp
// Adding a new paragraph to the section.
IWParagraph paragraph = section.AddParagraph();
paragraph.AppendXHTML(htmlstring);
```

The following references enable to validate the HTML string for XHTML compliance.

- http://www.w3schools.com/tags/default.asp
- http://validator.w3.org/check

### Appendix 1 – Imported HTML Tags

| HTML Element                  | Style Attributes specific to this element (In addition to standard style attributes) | Non-Style Attributes supported (These attributes are applied directly to the element) | Limitations |
|-------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------|

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

<!-- tags: [DocIO, HTML, Formatted Text, XHTML, WordDocument, Word, Syncfusion Winforms, version] keywords: [XHTMLformattedtext, Wordparagraphs, HTMLformattedstrings, AppendXHTML, HTMLcompliance, XHTMLValidationType, WebReferences, HTMLtags, StyleAttributes, NonStyleAttributes, Limitations] -->
```