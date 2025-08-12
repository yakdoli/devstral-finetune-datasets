```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_106.jpeg
document_name: DocIo
page_number: 106
page_id: DocIo#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:18Z
fidelity: lossless
-->

## Header and Footer

In this section, we demonstrate how to configure headers and footers in a document, specifically setting up different designs for the first page and odd/even pages. Here’s a breakdown of the code:

### Code Example

```csharp
section.PageSetup.DifferentFirstPage = true;
section.PageSetup.DifferentOddAndEvenPages = true;

// Appending some text to the first page in document.
paragraph.AppendText( "\r\r[ First Page ] \r\rText Body_Text Body_Text Body_Text Body_Text Body" );
paragraph.ParagraphFormat.PageBreakAfter = true;

// Appending some text to the second page in document.
paragraph = section.AddParagraph();
paragraph.AppendText( "\r\r[ Second Page ] \r\rText Body_Text Body_Text Body_Text Body_Text Body" );
paragraph.ParagraphFormat.PageBreakAfter = true;

// Appending some text to the third page in document.
paragraph = section.AddParagraph();
paragraph.AppendText( "\r\r[ Third Page ] \r\rText Body_Text Body_Text Body_Text Body_Text Body" );

// Inserting First Page Header
paragraph = new WParagraph( document );
paragraph.AppendText( "[ FIRST PAGE Header ]" );
section.HeadersFooters.FirstPageHeader.Paragraphs.Add( paragraph );

// Inserting First Page Footer
paragraph = new WParagraph( document );
paragraph.AppendText( "[ FIRST PAGE Footer ]" );
section.HeadersFooters.FirstPageFooter.Paragraphs.Add( paragraph );

// Inserting Odd Pages Header
paragraph = new WParagraph( document );
paragraph.AppendText( "[ ODD Page Header Text goes here ]" );
section.HeadersFooters.OddHeader.Paragraphs.Add( paragraph );

// Inserting Odd Pages Footer
paragraph = new WParagraph( document );
paragraph.AppendText( "[ ODD Page Footer Text goes here ]" );
section.HeadersFooters.OddFooter.Paragraphs.Add( paragraph );

// Inserting Even Pages Header
paragraph = new WParagraph( document );
paragraph.AppendText( "[ EVEN Page Header Text goes here ]" );
section.HeadersFooters.EvenHeader.Paragraphs.Add( paragraph );
```

### Explanation

- **DifferentFirstPage**: Ensures that the first page has a distinct header and footer.
- **DifferentOddAndEvenPages**: Configures separate designs for odd and even pages.
- **Appending Text**: Demonstrates how to add content to specific pages using `PageBreakAfter`.
- **Headers and Footers**: Shows how to insert custom text into each type of header and footer using `WParagraph`.

This approach allows for flexible page design with varying headers and footers, suitable for professional documents or reports.

<!-- tags: [docio, headerfooter, document formatting, winforms] keywords: [differentfirstpage, differentoddandevenpages, wparagraph, firstpageheader, oddpageheader, oddpagefooter, evenpagefooter] -->
```