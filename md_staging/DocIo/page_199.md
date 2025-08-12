```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: DocIo
page_number: 199
page_id: DocIo#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:20Z
fidelity: lossless
-->

# Essential DocIO

```csharp
WSection section = doc.LastSection;
WParagraph newPara = section.AddParagraph() as WParagraph;
WTextRange text = newPara.AppendText("My Style1") as WTextRange;
newPara.ApplyStyle("MyStyle1");

// Updates the table of contents.
doc.UpdateTableOfContents();
```

### [VB.NET]

```vb
Dim doc As New WordDocument()
doc.EnsureMinimal()

Dim para As WParagraph = doc.LastParagraph
Dim toc As TableOfContent = para.AppendTOC(1, 1)

toc.UseHeadingStyles = false

' Set the TOC level style based on which the TOC should be created.
toc.SetTOCLevelStyle(1, "MyStyle1")

Dim section As WSection = doc.LastSection
Dim newPara As WParagraph = TryCast(section.AddParagraph(), WParagraph)
Dim text As WTextRange = TryCast(newPara.AppendText("My Style1"), WTextRange)
newPara.ApplyStyle("MyStyle1")

' Updates the table of contents.
doc.UpdateTableOfContents()
```

## 4.4.1.9 OLE Object

OLE object is used to make the content that is created in one program available in another program. To know what types of content you can insert, click **Insert** tab and select **Object** in the Text group.

**Note:** Only installed programs that support OLE objects appear in the Object dialog box.

Essential DocIO supports insertion and extraction of these OLE objects with small piece of code in both .doc and doc formats. **WOleObject** class is responsible for manipulating OLE objects.

<!-- tags: [DocIo, OLE, Object, OLE insertion, extraction, WOleObject, WinForms, WordDocument, TableOfContent, OLE object support, OLE object manipulation] keywords: [OLE, object, OLE insertion, OLE extraction, WOleObject, WordDocument, TableOfContent, OLE manipulation] -->
```