```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_263.jpeg
document_name: pdf
page_number: 263
page_id: pdf#page_263
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:54Z
fidelity: lossless
-->

## Content

### Removing Pages

You can also remove pages from the existing PDF document by using the following methods of the `PdfLoadedPageCollection` class.

- Remove
- RemoveAt

#### Example: Removing an Existing Page

The following code snippet illustrates how to remove an existing page from the PDF document.

#### C#

```csharp
PdfLoadedDocument doc = new PdfLoadedDocument("Sample.pdf");

// Removes the page by passing the PDF page
doc.Pages.Remove(doc.Pages[1]);

// Removes the page by specifying the page index
doc.Pages.RemoveAt(2);
```

#### VB.NET

```vb
Dim doc As PdfLoadedDocument = New PdfLoadedDocument("Sample.pdf")

' Removes the page by passing the PDF page
doc.Pages.Remove(doc.Pages(1))

' Removes the page by specifying the page index
doc.Pages.RemoveAt(2)
```

### Adding an Attachment

#### Overview
- An attachment can be easily added to a PDF document using the `PdfAttachment` class.
- The following code example illustrates this.

### Code Example: Adding an Attachment

```csharp
// Code example to add an attachment (implementation not included)
```

## API Reference

### `PdfAttachment` Class

#### Methods
- `AddAttachment`: Adds an attachment to the PDF document.
- `RemoveAttachment`: Removes an attachment from the PDF document.

## Code Examples

#### C#

```csharp
// Example of adding an attachment using the PdfAttachment class
```

#### VB.NET

```vb
' Example of adding an attachment using the PdfAttachment class
```

## Page-level Navigation/TOC

- **Removing Pages**
  - Example: Removing an Existing Page
- **Adding an Attachment**
  - Overview
  - Code Example: Adding an Attachment

## Cross References

See also:
- [PdfLoadedPageCollection](#)
- [PdfAttachment](#)

## RAG Annotations

<!-- tags: [pdf, document manipulation, page removal, attachment, Syncfusion Winforms, code examples] keywords: [PdfLoadedPageCollection, Remove, RemoveAt, PdfAttachment, adding an attachment, removing pages, document editing] -->
```