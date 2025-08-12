```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: DocIo
page_number: 083
page_id: DocIo#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:09Z
fidelity: lossless
-->

## Essential DocIO

### Example Code: Configuring Text Watermark

#### C#

```csharp
textWatermark.Semitransparent = false;
textWatermark.Color = Color.Black;
textWatermark.Text = "TextWatermark";
```

#### VB.NET

```vb
Dim doc As IWordDocument = New WordDocument()
doc.EnsureMinimal()
Dim textWatermark As TextWatermark = New TextWatermark()
doc.Watermark = textWatermark
textWatermark.Size = 96
textWatermark.Layout = WatermarkLayout.Horizontal
textWatermark.Semitransparent = False
textWatermark.Color = Color.Black
textWatermark.Text = "TextWatermark"
```

### 4.2.3 Docx Support

Essential DocIO provides support for creating Microsoft Word 2007, Microsoft Word 2010, and Microsoft Word 2013 format files from scratch by using the DocIO API. Word 2007, Word 2010, and Word 2013 format files are created with the same API as that of `.doc` files; the only difference is the format type in which they are saved and opened.

**Note:** The format type option `"Docx"` specifies the Microsoft Word 2013 format and its usage is deprecated. We recommend using Word 2007, Word 2010, or Word 2013.

#### Example Code: Creating a Word 2007 Format Document

```csharp
[C#]

WordDocument doc = new WordDocument();
//Add a new section to the document.
IWSection section = document.AddSection();
//Adding a new paragraph to the section.
IWParagraph paragraph = section.AddParagraph();
//Insert text into the paragraph.
paragraph.AppendText( "Hello World!" );
//Saves the document in Word 2007 format type.
doc.Save("OutDocument.docx", FormatType.Word2007);
```

<!-- tags: [essential docio, word document, docx support, text watermark] keywords: [docio, text watermark, word 2007, word 2010, word 2013, semitransparent, color, document creation, format type] -->
```