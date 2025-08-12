```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_099.jpeg
document_name: DocIo
page_number: 099
page_id: DocIo#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:10Z
fidelity: lossless
-->

# Essential DocIO

```csharp
// Set Page break
paragraph.ParagraphFormat.PageBreakAfter = true;

paragraph = section.AddParagraph();
paragraph.AppendText("[ After PAGE BREAK ] \rText Body_Text");

section = doc.AddSection();

// Set Section break
section.BreakCode = SectionBreakCode.NewPage;
paragraph = section.AddParagraph();
paragraph.AppendText("[ After SECTION BREAK ( New page ) ] \rText Body_Text");

section = doc.AddSection();

// Set page setup Options
section.PageSetup.Borders.BorderType = BorderStyle.DashLargeGap;
section.PageSetup.Borders.Color = Color.DeepPink;
section.PageSetup.PageBorderOffsetFrom = PageBorderOffsetFrom.PageEdge;
section.PageSetup.Borders.LineWidth = 2;
section.BreakCode = SectionBreakCode.NoBreak;
paragraph = section.AddParagraph();
paragraph.AppendText("[ After SECTION BREAK ( continuous page ) ] \rText Body_Text");
```

### VB.NET

```vb
' Create a new Word document
Dim doc As IWordDocument = New WordDocument()

Dim section As ISection = doc.AddSection()
Dim paragraph As IParagraph = section.AddParagraph()
paragraph.AppendText("Text Body_Text")

' Set Page break
paragraph.ParagraphFormat.PageBreakAfter = True

paragraph = section.AddParagraph()
paragraph.AppendText("[ After PAGE BREAK ] " & Constants.vbCr & "Text Body_Text")

section = doc.AddSection()

' Set Section break
section.BreakCode = SectionBreakCode.NewPage
```

## Cross References
- See also: [DocIO Namespace](#docio-namespace), [Word Document Operations](#word-document-operations)

<!-- tags: [Syncfusion, Winforms, DocIO, Word Documents, Page Break, Section Break] keywords: [DocIO, WordDocument, ISection, IParagraph, PageSetup, SectionBreakCode, PageBreakAfter, BorderStyle, PageBorderOffsetFrom] -->
```