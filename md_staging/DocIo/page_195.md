```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_195.jpeg
document_name: DocIo
page_number: 195
page_id: DocIo#page_195
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:08Z
fidelity: lossless
-->

# Essential DocIO

## Break Class

### Constructor

| Break.Break (IWordDocument, BreakType) | Initializes a new instance of the Break class. |

### Public Properties

| Name       | Description                     |
|------------|----------------------------------|
| BreakType  | Gets the type of the break.     |
| EntityType | Gets the type of the entity.    |

The following example illustrates how to use the Break class.

#### [C#]

```csharp
IWordDocument doc = new WordDocument();
ISection section = doc.AddSection();
IParagraph para = section.AddParagraph();

para.AppendText("Before line break");
para.AppendBreak(BreakType.LineBreak);
para.AppendText("After line break");

IParagraph pageBreakPara = section.AddParagraph();
pageBreakPara.AppendText("Before page break");
pageBreakPara.AppendBreak(BreakType.PageBreak);
pageBreakPara.AppendText("After page break");

doc.Save("Breaks.doc");
```

#### [VB.NET]

```vb
Dim doc As IWordDocument = New WordDocument()
Dim section As ISection = doc.AddSection()
Dim para As IParagraph = section.AddParagraph()

para.AppendText("Before line break")
para.AppendBreak(BreakType.LineBreak)
para.AppendText("After line break")

Dim pageBreakPara As IParagraph = section.AddParagraph()
pageBreakPara.AppendText("Before page break")
pageBreakPara.AppendBreak(BreakType.PageBreak)
pageBreakPara.AppendText("After page break")

doc.Save("Breaks.doc")
```

<!-- tags: [essential docio, break class, c#, vb.net, line break, page break, document manipulation, word document] keywords: [break, line break, page break, csharp, vb.net, essential docio, document manipulation, line break example, page break example] -->
```