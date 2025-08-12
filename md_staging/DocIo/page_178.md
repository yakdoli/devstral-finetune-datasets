```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_178.jpeg
document_name: DocIo
page_number: 178
page_id: DocIo#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:03Z
fidelity: lossless
-->

# Essential DocIO

The following code illustrates how to use the WPicture class.

## Using WPicture Class

### Code Example

#### [C#]

```csharp
IWordDocument doc = new WordDocument();
IWSection section = doc.AddSection();
IWParagraph paragraph = section.AddParagraph();
paragraph.AppendText("First image");
WPicture picture = paragraph.AppendPicture(new Bitmap(ImagesPath + DEF_IMAGE1_NAME));
picture.HeightScale = 50f;
picture.WidthScale = 50f;

paragraph = section.AddParagraph();
paragraph.AppendText("Second image");
picture = paragraph.AppendPicture(new Bitmap(ImagesPath + DEF_IMAGE2_NAME));
picture.HeightScale = 50f;
picture.WidthScale = 50f;

section.HeadersFooters.OddHeader.Paragraphs.Add(paragraph);
```

#### [VB.NET]

```vbnet
Dim doc As IWordDocument = New WordDocument()
Dim section As IWSection = doc.AddSection()
Dim paragraph As IWParagraph = section.AddParagraph()
paragraph.AppendText("First image")
Dim picture As WPicture = paragraph.AppendPicture(New Bitmap(ImagesPath + DEF_IMAGE1_NAME))
picture.HeightScale = 50f
picture.WidthScale = 50f

paragraph = section.AddParagraph()
paragraph.AppendText("Second image")
picture = paragraph.AppendPicture(New Bitmap(ImagesPath + DEF_IMAGE2_NAME))
picture.HeightScale = 50f
picture.WidthScale = 50f

section.HeadersFooters.OddHeader.Paragraphs.Add(paragraph)
```

### 4.4.1.4.2 TextBox

#### Overview
- The WTextBox class represents a text box in the Word document.

#### Content

The WTextBox class is used to insert and manage text boxes within a Word document.
