```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_347.jpeg
document_name: DocIo
page_number: 347
page_id: DocIo#page_347
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:17Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to add a watermark to a Word document using C#.

## Content

### Code Example: Adding a Watermark to a Word Document
This code snippet illustrates how to use the Microsoft Office Interop library to create a new Word document, add a watermark to its header, and save the document.

```csharp
[C#]

using word = Microsoft.Office.Interop.Word;
-----------

// Initialize objects
object nullobject = Missing.Value;
object newFilePath = "NewFileWatermark.doc";

// Start the word application
word.Application wordApp = new word.Application();

// Create a new word document
wordApp.Documents.Add(ref nullobject, ref nullobject, ref nullobject, ref nullobject);
word.Document doc = wordApp.ActiveDocument;

// Seek the current page header
wordApp.ActiveWindow.ActivePane.View.SeekView =
    word.WdSeekView.wdSeekCurrentPageHeader;

// Insert watermark
word.Shape watermark =
    wordApp.Selection.HeaderFooter.Shapes.AddTextEffect(
        Microsoft.Office.Core.MsoPresetTextEffect.msoTextEffect1,
        "Watermark",
        "Arial",
        (float)48,
        Microsoft.Office.Core.MsoTriState.msoTrue,
        Microsoft.Office.Core.MsoTriState.msoFalse,
        0,
        0,
        ref nullobject
    );

// Set watermark properties
watermark.Fill.Visible =
    Microsoft.Office.Core.MsoTriState.msoTrue;
watermark.Line.Visible =
    Microsoft.Office.Core.MsoTriState.msoFalse;
watermark.Fill.Solid();
watermark.Fill.ForeColor.RGB = (Int32)word.WdColor.wdColorGray30;

// Set focus back to the document
wordApp.ActiveWindow.ActivePane.View.SeekView =
    word.WdSeekView.wdSeekMainDocument;

// Save the document
doc.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject,
   	ref nullobject, ref nullobject, ref nullobject, ref nullobject,
    ref nullobject, ref nullobject, ref nullobject, ref nullobject);

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

## RAG Annotations
<!-- tags: [DocIO, Word, Watermark, Microsoft Office Interop, C#, DocumentProcessing] keywords: [Word document, watermark, header, Microsoft.Office.Interop.Word, SeekView, AddTextEffect, SaveAs, Close, Quit] -->

```