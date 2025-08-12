```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_193.jpeg
document_name: DocIo
page_number: 193
page_id: DocIo#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:52Z
fidelity: lossless
-->

# Essential DocIO

| Method/Property                          | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| WSymbol.WSymbol (IWordDocument)          | Initializes a new instance of the WSymbol class.                        |

## Public Properties

| Name               | Description                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------|
| CharacterCode      | Gets or sets symbol's character code.                                                                |
| CharacterFormat    | Gets character format for the symbol.                                                                |
| EntityType         | Gets the type of the entity.                                                                         |
| FontName           | Gets or sets symbol font name.                                                                       |

---

The following example illustrates how to use the WSymbol class.

### Example 1: Adding a Symbol to a Document (C#)

```csharp
IWordDocument doc = new WordDocument();
IWSection section = doc.AddSection();

IWParagraph paragraph = section.AddParagraph();
paragraph.AppendText("Testing symbols");
WSymbol symbol = paragraph.AppendSymbol(140);
symbol.FontName = "Wingdings";

doc.Save("Symbol.doc");
```

### Example 2: Adding a Symbol to a Document (VB.NET)

```vb
Dim doc As IWordDocument = New WordDocument()
Dim section As IWSection = doc.AddSection()

Dim paragraph As IWParagraph = section.AddParagraph()
paragraph.AppendText("Testing symbols")
Dim symbol As WSymbol = paragraph.AppendSymbol(140)
symbol.FontName = "Wingdings"

doc.Save("Symbol.doc")
```

## 4.4.1.7 Break

---

<!-- tags: [syncfusion, winforms, docio, Watext, symbol, WSymbol, IWordDocument, paragraph, break] keywords: [Essential DocIO, WSymbol, CharacterCode, CharacterFormat, EntityType, FontName, example, C#, VB.NET] -->
```