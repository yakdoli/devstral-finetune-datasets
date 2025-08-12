```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_279.jpeg
document_name: pdf
page_number: 279
page_id: pdf#page_279
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:50Z
fidelity: lossless
-->

# Essential PDF

## Overview
- This section provides examples of accessing document information and creating booklet layouts using Essential PDF.

## Content

### Accessing Document Information

```vb
Dim doc As PdfLoadedDocument = New PdfLoadedDocument(filename)

' Accessing document information
authorBox.Text = doc.DocumentInformation.Author
titleBox.Text = doc.DocumentInformation.Title
subjectBox.Text = doc.DocumentInformation.Subject
kwBox.Text = doc.DocumentInformation.Keywords
creatorBox.Text = doc.DocumentInformation.Creator
prodBox.Text = doc.DocumentInformation.Producer
```

**Note:** You can write the document information with the newly created document, but you cannot overwrite the existing meta data information.

### 4.2.8 Booklet

**Overview:** Booklets are documents with multiple pages arranged on sheets of paper. When folded, the paper will represent the correct page order. Essential PDF provides support for creating booklets, which produces the resulting PDF document that can be printed and stapled in the center to form a booklet.

#### Explanation of Booklet Creation

For example, assume that you have a 13 page document. Creating a booklet of the document will result in a PDF file with 7 pages: 
(page 1, null), (page2, page13), (page3, page12), ...((page7, page8).

#### Visualization

- **Original Pages Arranged in PDF**
  ![Figure 60: Pages Arranged in PDF](#)
  *Figure 60: Pages Arranged in PDF*

- **Pages Arranged in Booklet Layout**
  ![Figure 61: Pages Arranged in Booklet Layout](#)
  *Figure 61: Pages Arranged in Booklet Layout*

<!-- tags: [Essential PDF, Document Information, Booklet Creation, Syncfusion Winforms] keywords: [document information, creator, producer, author, title, subject, keywords, booklet, pdf loaded document, page arrangement, staple] -->
```