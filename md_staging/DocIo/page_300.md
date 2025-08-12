```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_300.jpeg
document_name: DocIo
page_number: 300
page_id: DocIo#page_300
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:47:58Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This page describes the feature in Essential DocIO that enables the conversion of Word documents to reflowable content (EPUB Formatted Book) for distribution and sales.
- It covers how DocIO supports converting MS Word documents to EPUB, including elements like text formatting, lists, images, hyperlinks, tables, and footnotes.
- Provides support for generating a Table of Contents (TOC) based on document headings and allows conversion to EPUB format across multiple platforms.

## Content

### Reflowable Documents
**Note:** A reflowable document is a type of electronic document that can adapt its presentation to the output device. Typical desktop publishing (DTP) output formats like Postscript or PDF are page-oriented, so are not generally reflowable, whereas the world wide web standard, HTML is a reflowable format.

#### Use Case Scenario
This feature helps users to convert Word documents to reflowable content (EPUB Formatted Book) that can be used for distribution and sales.

#### EPUB Conversion Using DocIO
Essential DocIO supports conversion of MS Word documents to EPub v2.0.1. DocIO supports conversion of elements such as Text and Paragraph formatting, Lists, Images, Hyperlinks, Tables and Footnotes to EPub format.

**By default**, Table of Contents (TOC) is enabled in the EPub document. It is generated based on the built-in heading styles or custom styles mentioned in the TOC field.

**Note:** You need to have an EPub reader installed in the machine to view the output EPub document.

#### Support for Conversion to EPub
Support for conversion to EPub is available in the following platforms:
- Windows Forms
- ASP.NET
- WPF
- ASP.NET MVC

#### Code Example: Converting a Word Document to EPub Format
The following code illustrates how to convert a Word document to EPub file format.

##### C#
```csharp
// Load any .doc or .docx file
WordDocument document = new WordDocument(filename);

// Save the EPub file
document.Save("Sample.epub", FormatType.EPub);
```

##### VB
```vb
' Load any .doc or .docx file
Dim document As WordDocument = New WordDocument(filename)

' Save the EPub file
document.Save("Sample.epub", FormatType.EPub)
```

### Additional Notes
Ensure that you have an EPub reader installed to view the converted EPub documents.

<!-- tags: [EssentialDocIO, EPUBConversion, DocumentFormatting, TableOfContents, HTMLReflowable, MSWordConversion] keywords: [DocIO, EPub, Word, Reflowable, Table of Contents] -->
```