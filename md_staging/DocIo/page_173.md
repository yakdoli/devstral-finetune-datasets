```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_173.jpeg
document_name: DocIo
page_number: 173
page_id: DocIo#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:18Z
fidelity: lossless
-->

## Overview

- This page explains how to work with bookmarks in a Word document using the Essential_DocIO component.
- It covers the process of moving to a specific bookmark, deleting its content, and inserting new text.
- The page also discusses shapes in Word documents and their representation using DocIO, specifically focusing on shape objects, inline shape objects, and how to manipulate shapes like pictures and text boxes.

## Content

### [VB.NET]

```vb
' Move to the Essential_DocIO bookmark.
bk.MoveToBookmark("Essential_DocIO")

' Delete bookmark content without deleting the format in the target document.
bk.DeleteBookmarkContent(False)

' Insert text.
bk.InsertText("Essential XlsIO is a Non UI component that can be used in both ASP.NET and windows forms applications. The usage is common for both environments except for the part where the created spreadsheet is saved to disk or stream in the case of a windows forms application and streamed to the client browser in the case of asp.net applications.")
```

### 4.4.1.4 Shapes

Shape is a subdocument of the Word document. Shape is a general name for a group of elements. Shapes can be added to the document with the help of Microsoft Word. The AutoShapes combo box lists the group of shapes. Picture and TextBox are shapes too.

Every shape is represented in Word Document with a special shape marker (among text block) and a block of information about the shape, which is situated in the other part of the document.

DocIO has four classes which represent shapes:
- ShapeObject
- InlineShapeObject
- WPicture
- WTextBox

You have full access to the WPicture and WTextBox classes, i.e., you can read, modify, and create pictures and text boxes. Other shapes are only preserved by DocIO (user cannot create or modify them).

#### ShapeObject and InlineShapeObject

The ShapeObject class represents all types of Word document shapes except pictures and text boxes.

## API Reference

### ShapeObject
- Represents all types of Word document shapes except pictures and text boxes.
- Provides methods to manipulate and preserve shape properties.

### InlineShapeObject
- Represents inline shapes within the Word document.
- Allows for the manipulation of inline shapes, including their position and formatting.

### WPicture
- Represents picture shapes in a Word document.
- Provides methods to handle picture insertion, modification, and properties.

### WTextBox
- Represents text box shapes in a Word document.
- Facilitates operations such as inserting, modifying, and querying text box properties.

## Code Examples

### Example: Working with Shapes in a Word Document

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.Dls;

// Open the Word document
WordDocument document = new WordDocument("template.docx");

// Access the shapes collection
ShapeCollection shapes = document.LastSection.Shapes;

// Create a new picture shape
WPicture picture = shapes.AddPicture("image.jpg");

// Create a new text box shape
WTextBox textBox = shapes.AddTextBox("This is a text box content");

// Save the modified document
document.Save("output.docx", SaveFormat.Docx);
```

## Cross References

- See also: [Working with Bookmarks in Word Documents](#working-with-bookmarks-in-word-documents)
- See also: [Manipulating Text in Word Documents](#manipulating-text-in-word-documents)

<!-- tags: [DocIO, WordDocument, Shapes, WPicture, WTextBox, ShapeObject, InlineShapeObject] keywords: [Word document shapes, shape manipulation, WPicture, WTextBox, ShapeObject, InlineShapeObject, document modification, text boxes, pictures] -->
```