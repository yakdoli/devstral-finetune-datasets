```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_109.jpeg
document_name: DocIo
page_number: 109
page_id: DocIo#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:35:19Z
fidelity: lossless
-->

### Essential DocIO

```vb
' Inserting Odd Pages Footer
paragraph = New WParagraph(document)
paragraph.AppendText("[ ODD Page Footer Text goes here ]")
section.HeadersFooters.OddFooter.Paragraphs.Add(paragraph)

' Inserting Even Pages Header
paragraph = New WParagraph(document)
paragraph.AppendText("[ EVEN Page Header Text goes here ]")
section.HeadersFooters.EvenHeader.Paragraphs.Add(paragraph)

' Inserting Even Pages Footer
paragraph = New WParagraph(document)
paragraph.AppendText("[ EVEN Page Footer Text goes here ]")
section.HeadersFooters.EvenFooter.Paragraphs.Add(paragraph)

' Adding the second section to the document.
section = document.AddSection()
section.PageSetup.DifferentFirstPage = True

' Appending some text to the Second Sections's first page in the document.
paragraph = section.AddParagraph()
paragraph.AppendText(Constants.vbCr + Constants.vbCr & "[ First Page for SECOND SECTION ]" & Constants.vbCr & "[ ON DIFFERENT FIRST PAGE ]" & Constants.vbCr + Constants.vbCr & "Text Body_Text Body_Text Body_Text Body_Text")
paragraph.ParagraphFormat.PageBreakAfter = True

' Appending some text to the Second Sections's second page in the document.
paragraph = section.AddParagraph()
paragraph.AppendText(Constants.vbCr + Constants.vbCr & "[ Second Page for SECOND SECTION ]" & Constants.vbCr & "Text Body_Text Body_Text Body_Text Body_Text Body_Text")

' Inserting Second Sections's First Header
paragraph = New WParagraph(document)
paragraph.AppendText("[ SECOND SECTION FIRST PAGE Header ]")
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

' Inserting Second Sections's First Footer
paragraph = New WParagraph(document)
paragraph.AppendText("[ SECOND SECTION FIRST PAGE Footer ]")
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)

' Inserting Second Sections's Header
paragraph = New WParagraph(document)
paragraph.AppendText("SECOND SECTION Header Text goes here")
section.HeadersFooters.OddHeader.Paragraphs.Add(paragraph)
```

<!-- tags: [DocIO, HeaderFooter, Section, WinForms] keywords: [Odd Pages Footer, Even Pages Header, Even Pages Footer, First Page Header, First Page Footer, Second Section, Page Break] -->
```