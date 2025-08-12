```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_156.jpeg
document_name: DocIo
page_number: 156
page_id: DocIo#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:37Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Discusses the use of the Hyperlink class in Essential DocIO.
- Explains how to insert, edit, and replace hyperlinks as fields.
- Highlights the HyperlinkType enumerator specifying the type of link in use.

## Content

### Insert Hyperlink Dialog Box in MS Word

The following image depicts the Insert Hyperlink Dialog Box in MS Word:

![Figure 54: Insert Hyperlink Dialog Box in MS Word](https://example.com/image-link)

**Description:**
Essential DocIO allows you to insert, edit, and replace hyperlinks as fields using the Hyperlink class. The HyperlinkType enumerator specifies the type of the link in use.

### Public Constructor

| Name                     | Description                                               |
|--------------------------|-----------------------------------------------------------|
| Hyperlink( WField hyperlink ) | Initializes a new instance of the Hyperlink class. |

### Public Properties

#### Name | Description

| Name           | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| FilePath       | Gets / sets file path.                                                    |
| Uri            | Gets / sets url link.                                                     |
| BookmarkName   | Gets / sets Bookmark.                                                     |
| HyperlinkType  | Gets / sets a HyperlinkType object that indicates the link type. Below are the Hyperlink types supported by DocIO: <br><br> WebLink - Sets the URI |

## API Reference

### Hyperlink Class

#### Constructor

- **Hyperlink( WField hyperlink )**  
  Initializes a new instance of the Hyperlink class.

#### Properties

- **FilePath**  
  Gets / sets file path.

- **Uri**  
  Gets / sets url link.

- **BookmarkName**  
  Gets / sets Bookmark.

- **HyperlinkType**  
  Gets / sets a HyperlinkType object that indicates the link type. Supported Hyperlink types include:
  - **WebLink**: Sets the URI.

## Code Examples

The following is an example of how to use the Hyperlink class in C# to insert a hyperlink in a document:

```csharp
// Create a new instance of the Hyperlink class
Hyperlink hyperlink = new Hyperlink("https://www.example.com");

// Set the hyperlink type
hyperlink.HyperlinkType = HyperlinkType.WebLink;

// Add the hyperlink to the document
document.InsertHyperlink(hyperlink);
```

## Page-level Navigation/TOC (if applicable)
- [Link to Related Topic] (if applicable)

## Cross References
See also:
- Related topics in the documentation

## RAG Annotations
<!-- tags: [Essential DocIO, Hyperlink, HyperlinkType, MS Word, WinForms] keywords: [hyperlink insertion, hyperlink editing, hyperlink replacement, hyperlink type, MS Word integration, DocIO] -->
```