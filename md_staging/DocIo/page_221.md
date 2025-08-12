```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_221.jpeg
document_name: DocIo
page_number: 221
page_id: DocIo#page_221
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:37Z
fidelity: lossless
-->

# Essential DocIO

| RemoveByTabPosition(float position) | Removes tab at specified tab position from the tab collection. |
| --- | --- |

## Content

The following code examples illustrate how to add the tab to the paragraph and delete the tab from the paragraph.

### Code Examples

#### C#

```csharp
// Create a new instance for the word document
WordDocument document = new WordDocument();
// Add one section to the document
IWSection section = document.AddSection();
// Add one paragraph to the section
IWParagraph paragraph = section.AddParagraph();

// Add tab stop at the position 36 with tab justification [left] and tab leader [dotted]
paragraph.ParagraphFormat.Tabs.AddTab(36, TabJustification.Left, Syncfusion.DocIO.DLS.TabLeader.Dotted);
// Add tab stop at the position 80 with tab justification [Right] and tab leader [Hyphenated]
paragraph.ParagraphFormat.Tabs.AddTab(80, TabJustification.Right, Syncfusion.DocIO.DLS.TabLeader.Hyphenated);
// Add tab stop at the position 144 with tab justification [Center] and with no tab leader
paragraph.ParagraphFormat.Tabs.AddTab(144, TabJustification.Centered, Syncfusion.DocIO.DLS.TabLeader.NoLeader);

// Remove tab at index 1 from the tab collection
paragraph.ParagraphFormat.Tabs.RemoveAt(1);
// Remove tab at the position 144
paragraph.ParagraphFormat.Tabs.RemoveByTabPosition(144);
// Append tab character
paragraph.AppendText("\t");
// Append Text to the paragraph
paragraph.AppendText("Tabs are added and removed");
// Save the word document
document.Save("Sample.doc", FormatType.Doc);
```

#### VB

```vb
' Create a new instance for the word document
Dim document As New WordDocument()
' Add one section to the document
Dim section As IWSection = document.AddSection()
' Add one paragraph to the section
Dim paragraph As IParagraph = section.AddParagraph()
```

## Page-level Navigation/TOC (if applicable)

- Essential DocIO
  - Content
    - Code Examples

### Cross References

- See also: [DocIO Overview](#docio-overview)

### RAG Annotations

<!-- tags: [DocIO, WordDocument, TabularFormatting, ParagraphHandling, WinForms] keywords: [RemoveByTabPosition, TabJustification, TabLeader, RemoveAt, AppendText, Save] -->
```