```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_105.jpeg
document_name: DocIo
page_number: 105
page_id: DocIo#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:05Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Contains details about managing headers and footers in a document.
- Explains how to utilize the `HeaderFooter` class inherited from `WTextBody`.
- Provides information on adding text to various types of headers and footers.

## Content

### HeaderFooter Properties

| HeaderFooter Property | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Header                | Gets default header.                                                       |
| IsEmpty               | Detects whether all headers/footers are empty.                         |
| OddFooter             | Gets odd footer (This is also the default footer).                     |
| OddHeader             | Gets odd header (This is also the default header).                     |
| LinkToPrevious        | Links to previous section's header and footer.                          |

### Public Methods

| Name             | Description                                    |
|------------------|-----------------------------------------------|
| GetEnumerator    | Returns an enumerator that iterates through a collection. |

### HeaderFooter Class
The `HeaderFooter` class represents the page header or footer. It is inherited from the `WTextBody`, and hence can hold other paragraphs inside.

#### Public Properties

| Name        | Description                      |
|-------------|---------------------------------|
| EntityType   | Gets the type of the entity.    |

#### Example: Adding Text to Headers and Footers

The following example illustrates how to add text to different types of headers and footers.

```csharp
// A new document is created
WordDocument document = new WordDocument();

// Adding the first section to the document.
IWSection section = document.AddSection();

// Adding a paragraph to the section.
IWParagraph paragraph = section.AddParagraph();

// Setting DifferentFirstPage and DifferentOddEvenPages as true for inserting
```

## Page-level Navigation/TOC (if applicable)
- None available on this page.

## Cross References
- See also: [Additional Syncfusion Winforms Documentation](#additional-syncfusion-winforms-documentation)

<!-- tags: [DocIO, headers, footers, HeaderFooter, WTextBody, WordDocument, Word Processing, Syncfusion, Winforms] 
keywords: [DocumentHeaderFooter, documentheaders, documentfooters, WTextBody, Section, Paragraph, Header, Footer, IsEmpty, Enumerator] -->
```