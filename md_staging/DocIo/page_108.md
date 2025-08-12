```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: DocIo
page_number: 108
page_id: DocIo#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:48Z
fidelity: lossless
-->

### Adding Headers and Footers in VBA

```vb
Dim document As WordDocument = New WordDocument()

' Adding the first section to the document.
Dim section As IWSection = document.AddSection()

' Adding a paragraph to the section.
Dim paragraph As IWParagraph = section.AddParagraph()

' Setting DifferentFirstPage and DifferentOddEvenPages as true for inserting Header and Footer text.
section.PageSetup.DifferentFirstPage = True
section.PageSetup.DifferentOddAndEvenPages = True

' Appending some text to the first page in document.
paragraph.AppendText(Constants.vbCr + Constants.vbCr & "[ First Page ] " & Constants.vbCr + Constants.vbCr & "Text Body_Text Body_Text Body_Text Body_Text Body")
paragraph.ParagraphFormat.PageBreakAfter = True

' Appending some text to the second page in document.
paragraph = section.AddParagraph()
paragraph.AppendText(Constants.vbCr + Constants.vbCr & "[ Second Page ] " & Constants.vbCr + Constants.vbCr & "Text Body_Text Body_Text Body_Text Body_Text Body_Text Body")
paragraph.ParagraphFormat.PageBreakAfter = True

' Appending some text to the third page in document.
paragraph = section.AddParagraph()
paragraph.AppendText(Constants.vbCr + Constants.vbCr & "[ Third Page ] " & Constants.vbCr + Constants.vbCr & "Text Body_Text Body_Text Body_Text Body_Text Body_Text Body")

' Inserting First Page Header
paragraph = New WParagraph(document)
paragraph.AppendText("[ FIRST PAGE Header ]")
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

' Inserting First Page Footer
paragraph = New WParagraph(document)
paragraph.AppendText("[ FIRST PAGE Footer ]")
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)

' Inserting Odd Pages Header
paragraph = New WParagraph(document)
paragraph.AppendText("[ ODD Page Header Text goes here ]")
section.HeadersFooters.OddHeader.Paragraphs.Add(paragraph)
```

<!-- tags: [DocIO, Syncfusion, WinForms, VBA, Headers, Footers, Word Document] keywords: [DocIO, document manipulation, header and footer, first page, odd页, WParagraph, ISection] -->
```
