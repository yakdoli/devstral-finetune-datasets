```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: DocIo
page_number: 110
page_id: DocIo#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:37Z
fidelity: lossless
-->

# Essential DocIO

```plaintext
' Inserting Second Sections's Footer
paragraph = New WParagraph(document)
paragraph.AppendText("SECOND SECTION Footer Text goes here")
section.HeadersFooters.OddFooter.Paragraphs.Add(paragraph)

' Saving the document to disk.
document.Save("Sample.doc", FormatType.Doc)
```

DocIO provides options to link the header or footer of a section to the corresponding header or footer in the previous section by using the `LinkToPrevious` property. This option is available in the Header/Footer toolbar in MS Word. By default this property is set to `True`.

The following code illustrates how to enable this option by using DocIO.

### LinkToPrevious Example

#### C#

```csharp
doc.AddSection().HeadersFooters.LinkToPrevious = true;
```

#### VB.NET

```vb
doc.AddSection().HeadersFooters.LinkToPrevious = True
```

## Page Number Format

You can insert page numbers of different formats such as arabic numbers, roman numbers, and so on, to the pages in the document. It is also possible to restart the page numbers from any section, and change the starting number of the page number for each section. This is equivalent to the `Insert -> Page Numbers -> Format` option of MS Word.

### Page Number Configuration Example

#### C#

```csharp
section.PageSetup.PageStartingNumber = 3;
section.PageSetup.RestartPageNumbering = true;
sections.PageSetup.PageNumberStyle = PageNumberStyle.Arabic;
```

#### VB.NET

```vb
section.PageSetup.PageStartingNumber = 3
section.PageSetup.RestartPageNumbering = True
sections.PageSetup.PageNumberStyle = PageNumberStyle.Arabic
```

<!-- Page-level Navigation/TOC (if applicable) -->
<!-- tags: [DocIO, WordProcessing, HeadersFooters, LinkToPrevious, PageNumberFormat, Syncfusion Winforms, 11.4.0.26] keywords: [DocIO, LinkToPrevious, Page Number Format, Restart Page Numbering, Headers, Footers, Section, Document] -->
```