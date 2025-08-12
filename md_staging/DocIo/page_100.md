```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: DocIo
page_number: 100
page_id: DocIo#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:23Z
fidelity: lossless
-->

## Essential DocIO

```csharp
paragraph = section.AddParagraph()
paragraph.AppendText("[ After SECTION BREAK ( New page ) ]" & Constants.vbCr & "Text Body_Text")

section = doc.AddSection()

'Set page setup Options
section.PageSetup.Borders.BorderStyle = BorderStyle.DashLargeGap
section.PageSetup.Borders.Color = Color.DeepPink
section.PageSetup.PageBorderOffsetFrom = PageBorderOffsetFrom.PageEdge
section.PageSetup.Borders.LineWidth = 2
section.BreakCode = SectionBreakCode.NoBreak
paragraph = section.AddParagraph()
paragraph.AppendText("[ After SECTION BREAK ( continuous page ) ]" & Constants.vbCr & "Text Body_Text")
```

### Cloning and Merging

#### 4.3.1 Cloning and Merging

DocIO has an ability to clone the whole Word document or a part of it.

Use the `Clone` method for "deep" document cloning. This method returns the new object of the WordDocument class along with the content of the cloned document which invoked the `Clone` method. You can use the `Clone` method to clone any document entity.

> **Note:** If source and destination documents have styles with the same names, then the styles of the imported document will be renamed after importing.

The following example illustrates how to merge two documents by using the `Clone` method.

```csharp
[C#]

// Create the first document.
IWordDocument doc = new WordDocument();
IWSection section = doc.AddSection();
IWRange text1 = section.AddParagraph().AppendText("First document section...");
text1.CharacterFormat.TextColor = Color.Red;
section.AddParagraph().AppendText("Some Text...");
```
```Income: 2023 | Page 100
```