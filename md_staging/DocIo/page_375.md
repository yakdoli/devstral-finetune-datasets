```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_375.jpeg
document_name: DocIo
page_number: 375
page_id: DocIo#page_375
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:02Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Displays how to work with comments in a Word document using DocIO.
- Includes code examples in both C# and VB to remove all comments from a document.

## Content

### C#

```csharp
// Open the word document
WordDocument doc = new WordDocument("Comments.doc");

// Get all comments in the document
CommentsCollection comments = doc.Comments;

// Remove all comments from the document
comments.Clear();

// Save the document
doc.Save("CommentsRemovedDocIO.doc", FormatType.Doc);
```

### VB

```vb
' Open the word document
Dim doc As WordDocument = New WordDocument("Comments.doc")

' Get all comments in the document
Dim Comments As CommentsCollection = doc.Comments

' Remove all comments from the document
Comments.Clear()

' Save the document
doc.Save("CommentsRemovedDocIO.doc", FormatType.Doc)
```

### Note

The following note provides additional documentation for working with comments in DocIO.

> ![external link icon](./icon.png) For more information on working with the comments using DocIO, you can refer the following online documentation link:  
> http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/44143comment.htm

## Cross References
- See also: [DocIO Online Documentation](http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/44143comment.htm)

<!-- tags: DocIO, Word document, comments, C#, VB, Synfusion Winforms, 11.4.0.26 keywords: comments, DocIO, code examples, C#, VB, documentation -->
```