```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_033.jpeg
document_name: DocIo
page_number: 033
page_id: DocIo#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:38Z
fidelity: lossless
-->

# Essential DocIO

> Note: The WordDocument class represents the Word documents created in memory. This is the memory representation of the Word document written to disk.

1. Add a section to the newly created Word document by using the following code.

```csharp
// Add a new section to the document.
IWSection section = document.AddSection();
```

```vbnet
' Add a new section to the document.
Dim section As IWSection = document.AddSection()
```

2. Add a paragraph to the newly created section in the Word document by using the following code.

```csharp
// Add a new paragraph to the section.
IWPParagraph paragraph = section.AddParagraph();
```

```vbnet
' Add a new paragraph to the section.
Dim paragraph As IWPParagraph = section.AddParagraph()
```

3. Add a paragraph to the newly created section in the Word document by using the following code.

```csharp
// Insert text into the paragraph.
paragraph.AppendText("Hello World!");
```

```vbnet
' Insert text into the paragraph.
paragraph.AppendText("Hello World!")
```

4. Finally, save the Word document. The following code example illustrates how to do this.

### Summary

© 2013 Syncfusion. All rights reserved.
Page 033

<!-- tags: [DocIO, WordDocument, add section, add paragraph, append text, save document, C#, VB.NET] keywords: [WordDocument, IWSection, IWPParagraph, AddSection, AddParagraph, AppendText] -->
```