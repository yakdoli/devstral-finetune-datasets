```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_248.jpeg
document_name: DocIo
page_number: 248
page_id: DocIo#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:12Z
fidelity: lossless
--> 

## Standard Style Attributes and Limitations

### Overview
- Supported style attributes for all XHTML elements.
- No listed limitations for the supported attributes.

### Standard Style Attributes

| Standard Style Attributes (These style attributes are supported by all supported XHTML elements) | Limitations |
| --- | --- |
| padding-right | - |
| padding-bottom | - |
| padding-top | - |
| line-height | - |
| letter-spacing | - |
| text-transform | - |
| white-space | - |
| list-style-image | - |
| list-style-type | - |
| outline | - |
| outline-style | - |
| outline-width | - |
| outline-color | - |

### Notes
- Currently inserting XHTML formatted string in the Word document is not supported in Silverlight application.

## 4.5 Find and Replace

### Overview
- The essential feature to find and replace text in a Word document provided in MS Word.
- Essential for translators' work and efficiency in handling Word documents and reports.

### Description
Find and replace text in a Word document is an essential feature in MS Word. This feature may often prove to be extremely helpful in the translator's work. Essential DocIO provides support to find a string, document element, or a bookmark in a Word document, and replace it with other document elements. This enables you to work more easily and efficiently with Word documents and reports.

## API Reference
- Namespace: Syncfusion.DocIO
- Class: WordDocument

### Methods
- `Find(string searchText)`
- `Replace(string searchText, string replaceText)`
- `Find(string searchText, Range position)`
- `Replace(string searchText, string replaceText, ReplaceFlags flags)`

### Parameters
| Name | Type | Description | Default | Required |
| --- | --- | --- | --- | --- |
| `searchText` | `string` | The text to find. | None | Yes |
| `replaceText` | `string` | The text to replace the found text with. | None | Yes (for Replace methods) |
| `position` | `Range` | The range to find the text within. | None | No |
| `flags` | `ReplaceFlags` | Flags to specify the type of replacement. | None | No |

### Returns
- Returns the found text positions or modified document elements based on the method called.

### Exceptions
- Throws an exception if the search text is not found or replacement fails due to invalid parameters.

## Code Examples

### C# Example

```csharp
using Syncfusion.DocIO;

// Load a Word document.
WordDocument document = new WordDocument();
document.Open("SampleDoc.docx");

// Find and replace text.
document.Find("oldText");
document.Replace("oldText", "newText");

// Save the modified document.
document.Save("ModifiedDoc.docx");
```

### VB.NET Example

```vbnet
Imports Syncfusion.DocIO

' Load a Word document.
Dim document As New WordDocument()
document.Open("SampleDoc.docx")

' Find and replace text.
document.Find("oldText")
document.Replace("oldText", "newText")

' Save the modified document.
document.Save("ModifiedDoc.docx")
```

## RAG Annotations
<!-- tags: DocIO, WordDocument, Find, Replace, Syncfusion Winforms, MS Word, Translator Tools, version: 11.4.0.26 -->
<!-- keywords: Find and Replace, Word documents, text replacement, document elements, bookmarks, MS Word, translators, efficiency, Silverlight limitations -->
```