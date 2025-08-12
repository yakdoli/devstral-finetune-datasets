```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_129.jpeg
document_name: DocIo
page_number: 129
page_id: DocIo#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:28Z
fidelity: lossless
-->

# Essential DocIO

## Table of Operations

| Operation       | Description                                          |
|-----------------|------------------------------------------------------|
| AppendTOC      | Appends the TOC.                                     |
| ApplyStyle     | Applies style to the paragraph.                      |
| Find           | Finds text inside the paragraph.                     |
| GetStyle       | Gets related style.                                 |
| Replace        | Replaced text inside the paragraph.                  |
| InsertSectionBreak | Inserts a section break.                        |

## Example of Adding Formats to Paragraphs

The following example illustrates how to add various formats to paragraphs.

### C#

```csharp
// Add paragraph and apply formatting.
paragraph = section.AddParagraph(); 
paragraph.ParagraphFormat.Borders.Bottom.BorderType = 
    BorderStyle.ThinThickSmallGap;
paragraph.ParagraphFormat.HorizontalAlignment = 
    HorizontalAlignment.Center; 
paragraph.ParagraphFormat.BeforeSpacing = 18; 
textRange = paragraph.AppendText("Windows Forms. ");

paragraph = section.AddParagraph(); 
paragraph.ParagraphFormat.PageBreakBefore = true; 
paragraph.ParagraphFormat.BackColor = Color.FromArgb(102, 102, 153); 
paragraph.ParagraphFormat.BeforeSpacing = 18; 
paragraph.ParagraphFormat.AfterSpacing = 6; 
paragraph.ParagraphFormat.FirstLineIndent = 45; 
```

### VB.NET
```vbnet
' Add paragraph and apply formatting.
paragraph = section.AddParagraph()
paragraph.ParagraphFormat.Borders.Bottom.BorderType = 
    BorderStyle.ThinThickSmallGap
paragraph.ParagraphFormat.HorizontalAlignment = 
    HorizontalAlignment.Center
paragraph.ParagraphFormat.BeforeSpacing = 18
textRange = paragraph.AppendText("Windows Forms. ")

paragraph = section.AddParagraph()
paragraph.ParagraphFormat.PageBreakBefore = True
paragraph.ParagraphFormat.BackColor = Color.FromArgb(102, 102, 153)
paragraph.ParagraphFormat.BeforeSpacing = 18
paragraph.ParagraphFormat.AfterSpacing = 6
paragraph.ParagraphFormat.FirstLineIndent = 45
```

<!-- tags: [DocIO, paragraph formatting, style application, text operations, version 11.4.0.26] keywords: [AppendTOC, ApplyStyle, Find, GetStyle, Replace, InsertSectionBreak, C#, VB.NET, paragraph, textRange, BorderStyle, HorizontalAlignment, BeforeSpacing, AfterSpacing, FirstLineIndent] -->
```