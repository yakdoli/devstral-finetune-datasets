```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_101.jpeg
document_name: DocIo
page_number: 101
page_id: DocIo#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:52Z
fidelity: lossless
-->

# Essential DocIO

```csharp
section.AddParagraph().AppendText("New Paragraph");
section.AddParagraph().AppendText("Third Paragraph");

// Create the second document.
IWordDocument doc2 = new WordDocument();
IWSection section2 = doc2.AddSection();
IWTextRange text2 = section2.AddParagraph().AppendText("Second document section...");
text2.CharacterFormat.TextColor = Color.Blue;
section2.AddParagraph().AppendText("Some Text...");
section2.AddParagraph().AppendText("New Paragraph More Text");
section2.AddParagraph().AppendText("Third Paragraph More Text");

// Merge the second document with the first.
doc.Sections.Add(section2.Clone());
```

### [VB.NET]

```vb.net
' Create the first document.
Dim doc As IWordDocument = New WordDocument()
Dim section As IWSection = doc.AddSection()
Dim text1 As IWTextRange = section.AddParagraph().AppendText("First document section...")
text1.CharacterFormat.TextColor = Color.Red
section.AddParagraph().AppendText("Some Text...")
section.AddParagraph().AppendText("New Paragraph")
section.AddParagraph().AppendText("Third Paragraph")

' Create the second document.
Dim doc2 As IWordDocument = New WordDocument()
Dim section2 As IWSection = doc2.AddSection()
Dim text2 As IWTextRange = section2.AddParagraph().AppendText("Second document section...")
text2.CharacterFormat.TextColor = Color.Blue
section2.AddParagraph().AppendText("Some Text...")
section2.AddParagraph().AppendText("New Paragraph More Text")
section2.AddParagraph().AppendText("Third Paragraph More Text")

' Merge the second document with the first.
doc.Sections.Add(section2.Clone())
```

## Import Contents

Import content functionality is used to copy/hmerge the contents from one document to another. Compatibility options of the source document will not be imported to the destination document.

<!-- tags: [DocIO, Syncfusion Winforms, Import Content, Merge Documents, OLE Support] keywords: [Import, Copy, Merge, Documents, WordDocument, Section, Paragraph, TextRange, CharacterFormat, Compatibility, OLE, Page Merge] -->
```