```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: DocIo
page_number: 096
page_id: DocIo#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:07Z
fidelity: lossless
-->

## Essential DocIO

![Figure 34: Page Setup Dialog Box](https://i.imgur.com/8wLXVHr.png)

### Overview
- Describes the configuration of page setup properties for documents.
- Focuses on the `Page Setup` dialog box and its various settings.

### Content

#### Page Setup Properties

PageSetup properties are listed in the following table.

| Name                | Description                                                                                              |
|---------------------|----------------------------------------------------------------------------------------------------------|
| Bidi               | Gets or sets whether section contains right-to-left text.                                                |
| Borders            | Gets page borders collection.                                                                            |
| ClientWidth        | Gets width of client area.                                                                               |
| DefaultTabWidth    | Gets or sets the length of the auto tab.                                                                 |
| DifferentFirstPage | Setting to specify that the current section has a different header / footer for first page.              |

---

## API Reference (if applicable)
- **Namespace**: Not explicitly mentioned in this snippet.
- **Class**: Assuming from the context, `PageSetup` or related.

### Properties

| Name                | Description                                                                                              |
|---------------------|----------------------------------------------------------------------------------------------------------|
| Bidi               | `bool` - Indicates whether the section contains right-to-left text.                                     |
| Borders            | `IPageBorders` - Collection representing the page borders.                                              |
| ClientWidth        | `double` - Retrieves the width of the client area.                                                       |
| DefaultTabWidth    | `double` - Gets or sets the length of the auto tab.                                                     |
| DifferentFirstPage | `bool` - Indicates whether the current section has a different header/footer for the first page.          |

## Code Examples (multi-language supported)

This section would include example code demonstrating how to use the `PageSetup` properties. Since the snippet doesn't provide specific code, the following is a general illustration:

```csharp
// Example: Setting Page Setup Properties
using Syncfusion.DocIO;

// Load a Word document
WordDocument document = new WordDocument();
document.Open("sample.docx", WordDocumentType.OpenXML);

// Get the section
WSection section = document.LastSection;

// Access Page Setup
WPageSetup pageSetup = section.PageSetup;

// Modify settings
pageSetup.Bidi = true;
pageSetup.DifferentFirstPage = true;

// Save the modified document
document.Save("modified.docx", WordDocumentType.OpenXML);
```

## RAG Annotations
<!-- tags: [page-setup, page-properties, docio, winforms, essential-doci, syncfusion-sdk] keywords: [margin, orientation, bidi, borders, clientWidth, tabWidth, first-page, header-footer] -->
```