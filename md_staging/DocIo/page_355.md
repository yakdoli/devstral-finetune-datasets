```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_355.jpeg
document_name: DocIo
page_number: 355
page_id: DocIo#page_355
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:45Z
fidelity: lossless
-->

## Overview

- Demonstrates adding headers and footers to a Word document programmatically using the Microsoft Interop library.
- Sample Visual Basic (VB) code snippet to open, modify, and save a Word document with headers and footers.
- Includes initialization of Word Application and document objects.
- Iterates through each section to add predefined header and footer content.

## Content

### Adding Headers and Footers in Word Documents

This example illustrates how to open an existing Word document, add a header and footer to each section, and save the modified document using the `Microsoft.Office.Interop.Word` library.

#### Code Example: Visual Basic

```vb
Imports word = Microsoft.Office.Interop.Word
-----------

' Initialize objects
Dim nullobject As Object = System.Reflection.Missing.Value
Dim filePath As Object = GetPath("original.doc")
Dim newFilePath As Object = GetPath("HeaderFooterOffice.doc")

' Start the application
Dim wordApp As word.Application = New word.Application()

' Open the document
Dim document As word.Document = wordApp.Documents.Open(filePath, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject)

wordApp.Visible = False

' Add header and footer for each section in the document
For Each section As word.Section In document.Sections
    Dim fieldEmpty As Object = word.WdFieldType.wdFieldPage

    ' Footer
    section.Footers(word.WdHeaderFooterIndex.wdHeaderFooterPrimary).Range.Text = "Internal"

    section.Footers(word.WdHeaderFooterIndex.wdHeaderFooterPrimary).Range.ParagraphFormat.Alignment = word.WdParagraphAlignment.wdAlignParagraphLeft

    ' Header
    section.Headers(word.WdHeaderFooterIndex.wdHeaderFooterPrimary).Range.Fields.Add(section.Headers(word.WdHeaderFooterIndex.wdHeaderFooterPrimary).Range, fieldEmpty, nullobject, nullobject)

    section.Headers(word.WdHeaderFooterIndex.wdHeaderFooterPrimary).Range.ParagraphFormat.Alignment = word.WdParagraphAlignment.wdAlignParagraphRight

Next

' Save the document
document.SaveAs(newFilePath, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject)

' Close the document
document.Close(nullobject, nullobject, nullobject)

' Quit the application
wordApp.Quit()
```

### Explanation of Code Steps

1. **Initialization:**  
   - The `Word.Application` object is created to interact with Microsoft Word.
   - Variables for file paths are declared and initialized using the `GetPath` method.

2. **Opening the Document:**  
   - The `Documents.Open` method is used to open the specified document with multiple optional parameters representing various Word document settings.

3. **Setting Visibility:**  
   - `wordApp.Visible = False` ensures that the Word application window is not displayed during the automation process.

4. **Adding Headers and Footers:**  
   - The loop iterates through each `Section` object in the document.
   - For each section, a footer is added with the text "Internal" and aligned to the left.
   - A header is added with a custom field (e.g., page number) and aligned to the right.

5. **Saving the Document:**  
   - The `SaveAs` method is used to save the modified document with a new file path.

6. **Closing and Quitting:**  
   - The document is closed, and the Word application is quit to clean up resources.

### Notes
- Ensure that the `Microsoft.Office.Interop.Word` reference is added to your project if not already included.
- Handle exceptions for file operations, such as file not found or permission issues, in a real-world application.

## API Reference

### `Microsoft.Office.Interop.Word`

- **Namespace:** `Microsoft.Office.Interop.Word`
- **Class:** `Application`
  - **Properties/Members:**
    - `Documents`
    - `Visible`
    - `Quit`

### `Word.Document`

- **Namespace:** `Microsoft.Office.Interop.Word`
- **Class:** `Document`
  - **Properties/Members:**
    - `Open(filepath As String, , , , , , , , , , , , , , , )`
    - `SaveAs(filepath As String, , , , , , , , , , , , , , , )`
    - `Close(SaveChanges As Boolean, OriginalFormat As Boolean, RouteDocument As Boolean)`

### `Word.Section`

- **Namespace:** `Microsoft.Office.Interop.Word`
- **Class:** `Section`
  - **Properties/Members:**
    - `Footers(index As WdHeaderFooterIndex)`
    - `Headers(index As WdHeaderFooterIndex)`

### `Word.Range`

- **Namespace:** `Microsoft.Office.Interop.Word`
- **Class:** `Range`
  - **Properties/Members:**
    - `Text`
    - `ParagraphFormat`

### `Word.Fields`

- **Namespace:** `Microsoft.Office.Interop.Word`
- **Class:** `Fields`
  - **Properties/Members:**
    - `Add(range As Range, Type As Object, FileName As Object, Format As Object)`

## Code Examples

The above VB code demonstrates comprehensive steps to programmatically manipulate Word documents, specifically focusing on adding headers and footers.

### Customization Tips
- Replace the static text "Internal" in the footer with dynamic content or a custom field.
- Adjust alignment properties (`wdAlignParagraphLeft`, `wdAlignParagraphRight`) as needed.

## Cross References
- Refer to the documentation for `Microsoft.Office.Interop.Word` for additional options and methods.
- Consult Syncfusion documentation for integrating `DocIO` with WinForms applications, particularly for more advanced document processing tasks.

<!-- tags: [syncfusion, winforms, docio, microsoft-interop, word, csharp, visual-basic, headers, footers] keywords: [microsoft.office.interop.word, document, headers, footers, wordapp, document, range, fields, saveas, quit] -->
```