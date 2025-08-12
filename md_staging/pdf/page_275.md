```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_275.jpeg
document_name: pdf
page_number: 275
page_id: pdf#page_275
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:35Z
fidelity: lossless
-->

## Overview
- Essential PDF provides features for merging and splitting PDF documents.
- The Merge feature appends all documents to the target document, copying bookmarks and attachments.
- Various parameters and methods are available for merging PDF documents.
- Splitting operation is used to generate single-page PDF documents, each saved with a unique name.

## Content

### 4.2.4 Merge PDF

The merging feature in the Essential PDF allows appending all documents to the target document. While merging, all bookmarks and attachments will be copied, additionally to `ImportPageRange` behavior.

There are various overloads of the `Merge` method that allow specifying different parameters. Some important parameters are:

- Array of strings
- Array of `PdfDocumentBase` instances

If the target document is null (in overload that accepts `PdfDocumentBase` class as a target), a new instance will be created.

You can also merge the documents in the following ways:

- Append all the documents one after the other by using the `Append` method.
- Import the pages from different documents by using the `ImportPageRange` or `ImportPage` method.
- Use `Insert` method to insert the pages one by one.

For more details, see [Merge PDF](#merged-pdf).

**Note:** To merge or append the document asynchronously for Windows Store apps, refer to the [Asynchronous Support](#asynchronous-support) section.

### 4.2.5 Split PDF

Splitting operation is used to generate a set of PDF documents, each of which is made of one page from the base document. Each new document is saved with a unique name which is generated from the pattern specified.

The pattern should be in .NET format (for example: "myfile{0:000}.pdf") or just a pdf name. In the latter case, the unique name will have the number before ".pdf".

## Page-level Navigation/TOC (if applicable)
- [Merge PDF](#merge-pdf)
- [Split PDF](#split-pdf)

## Cross References
See also:
- `ImportPageRange`
- `ImportPage`
- `Insert`
- `Append`
- `PdfDocumentBase`
- `Asynchronous Support`

<!-- tags: [pdf, merge, split, bookmarks, attachments, append, async, windows-store] keywords: [merging, splitting, pdf, targets, documents, append, bookmarks, attachments, import, pages, unique names, asynchronous support] -->
```