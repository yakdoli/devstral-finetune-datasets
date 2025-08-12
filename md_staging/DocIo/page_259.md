```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_259.jpeg
document_name: DocIo
page_number: 259
page_id: DocIo#page_259
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:28Z
fidelity: lossless
-->

## Essential DocIO

```csharp
WordDocument docSource1 = new WordDocument();
docSource1.Open(DocumentPath + FINDSOURCE1);

WordDocument docSource2 = new WordDocument();
docSource2.Open(DocumentPath + FINDSOURCE2);

WordDocument docTemplate = new WordDocument();
docTemplate.Open(DocumentPath + FINDTEMPLATE);

// Finds and returns entry of specified regular expression along with formatting
TextSelection rangesHolder1 = docSource1.Find("The Placeholder1 was replaced by this sample Text.", false, false);

// Create new TextSelection object, with text and its formatting specified by character range. In the current sample, the character range is a paragraph's range of symbols from 1 to 4 position.
TextSelection rangesHolder2 = new TextSelection(docSource2.LastParagraph, 1, 4);

docTemplate.Replace(new Regex("Placeholder1"), rangesHolder1);
docTemplate.Replace(new Regex("Placeholder2"), rangesHolder2);
```

### [VB.NET]

#### Example 1:

```vb
'This sample replaces specified regular expression with Picture
Dim textBodyPart As TextBodyPart = New TextBodyPart(doc)
Dim image As Image = Image.FromFile(ImagesPath & "Image.gif")
Dim pict As WPicture = New WPicture(doc)
pict.LoadImage(image)

Dim para As WParagraph = New WParagraph(doc)
para.Items.Add(pict)
textBodyPart.BodyItems.Insert(0, para)
doc.Replace(New Regex("A"), textBodyPart)
```

#### Example 2:

```vb
Dim docSource1 As WordDocument = New WordDocument()
docSource1.Open(DocumentPath + FINDSOURCE1)

Dim docSource2 As WordDocument = New WordDocument()
docSource2.Open(DocumentPath + FINDSOURCE2)

Dim docTemplate As WordDocument = New WordDocument()
docTemplate.Open(DocumentPath + FINDTEMPLATE)
```

<!-- tags: [DocIO, WordDocument, RegularExpressions, TextSelection] keywords: [DocIO, Word Processing, Regular Expressions, TextSelection, VB.NET, C#, Placeholder Replacement] -->
```