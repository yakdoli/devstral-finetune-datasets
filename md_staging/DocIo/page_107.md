```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_107.jpeg
document_name: DocIo
page_number: 107
page_id: DocIo#page_107
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:34Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to add sections, headers, footers, and manage pagination in a Word document using Syncfusion's DocIO library.

## Content

### Creating and Managing Sections with Headers and Footers

The following C# code snippet illustrates how to add a second section to a document, configure different first-page headers and footers, and append text to different pages:

```csharp
paragraph = new WParagraph( document );
paragraph.AppendText( "[ EVEN Page Footer Text goes here ]" );
section.HeadersFooters.EvenFooter.Paragraphs.Add( paragraph );

// Adding the second section to the document.
section = document.AddSection();
section.PageSetup.DifferentFirstPage = true;

// Appending some text to the Second Sections's first page in the document.
paragraph = section.AddParagraph();
paragraph.AppendText( "\r\r[ First Page for SECOND SECTION ]\r[ ON DIFFERENT FIRST PAGE ]\r\rText Body_Text Body_Text Body_Text Body_Text Body_Text Body" );
paragraph.ParagraphFormat.PageBreakAfter = true;

// Appending some text to the Second Sections's second page in the document.
paragraph = section.AddParagraph();
paragraph.AppendText( "\r\r[ Second Page for SECOND SECTION ]\rText Body_Text Body_Text Body_Text Body_Text Body" );

// Inserting Second Sections's First Header
paragraph = new WParagraph( document );
paragraph.AppendText( "[ SECOND SECTION FIRST PAGE Header ]" );
section.HeadersFooters.FirstPageHeader.Paragraphs.Add( paragraph );

// Inserting Second Sections's First Footer
paragraph = new WParagraph( document );
paragraph.AppendText( "[ SECOND SECTION FIRST PAGE Footer ]" );
section.HeadersFooters.FirstPageFooter.Paragraphs.Add( paragraph );

// Inserting Second Sections's Header
paragraph = new WParagraph( document );
paragraph.AppendText( "SECOND SECTION Header Text goes here" );
section.HeadersFooters.OddHeader.Paragraphs.Add( paragraph );

// Inserting Second Sections's Footer
paragraph = new WParagraph( document );
paragraph.AppendText( "SECOND SECTION Footer Text goes here" );
section.HeadersFooters.OddFooter.Paragraphs.Add( paragraph );

// Saving the document to disk.
document.Save( "Sample.doc", FormatType.Doc );
```

### VB.NET Implementation

The VB.NET equivalent for creating a new document is shown below:

```vb
' A new document is created.
```

## Page-level Navigation/TOC (if applicable)

### See also:

- **DocIO API Reference**: [` אלקמ.עמים.םידעה.WSection`]
- **Related Documentation**: [Managing Sections and Headers/Footers in Word Documents]

<!-- tags: [DocIO, Word Processing, Sections, Headers, Footers, Pagination, C#, VB.NET] keywords: [Section, Header, Footer, DifferentFirstPage, PageBreakAfter, WParagraph, WSection, Document, Word, Text, Syncfusion, DocIO Library] -->
```