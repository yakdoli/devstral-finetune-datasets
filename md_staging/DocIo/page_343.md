```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_343.jpeg
document_name: DocIo
page_number: 343
page_id: DocIo#page_343
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:59Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This page demonstrates how to apply formatting to footers in a Word document using Syncfusion's DocIO library.
- It includes steps to align the footer paragraph, set the font and size, add page numbers, save the document, close it, and quit the application.

## Content

### Formatting and Adding Page Numbers to the Footer
Below is the code snippet that demonstrates how to apply formatting for the footer and add page numbers.

```csharp
// Apply formatting for the footer
wordApp.Selection.Paragraphs.Alignment = word.WdParagraphAlignment.wdAlignParagraphCenter;
wordApp.ActiveWindow.Selection.Font.Name = "Arial";
wordApp.ActiveWindow.Selection.Font.Size = 8;

// Add page numbers in footer
Object CurrentPage = word.WdFieldType.wdFieldPage;

wordApp.ActiveWindow.Selection.Fields.Add(wordApp.Selection.Range, ref CurrentPage, ref nullobject, ref nullobject);

// Save the document
document.Save();

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

### Explanation of Code
1. **Footer Formatting**:
   - `wordApp.Selection.Paragraphs.Alignment`: Aligns the footer paragraph to the center using `wdAlignParagraphCenter`.
   - `wordApp.ActiveWindow.Selection.Font.Name`: Sets the font to "Arial".
   - `wordApp.ActiveWindow.Selection.Font.Size`: Sets the font size to 8.

2. **Adding Page Numbers**:
   - `word.WdFieldType.wdFieldPage`: Creates a field type for page numbers.
   - `wordApp.ActiveWindow.Selection.Fields.Add`: Adds the page number field to the footer.

3. **Saving and Closing the Document**:
   - `document.Save()`: Saves the document with the applied changes.
   - `document.Close()`: Closes the document programmatically.

4. **Quitting the Application**:
   - `wordApp.Quit()`: Quits the Word application.

## API Reference
### Methods and Properties Used
- `Selection.Paragraphs.Alignment`: Sets the alignment of the paragraph.
- `Selection.Font.Name`: Sets the font type.
- `Selection.Font.Size`: Sets the font size.
- `Fields.Add`: Adds fields to the document.
- `Document.Save()`: Saves the document.
- `Document.Close()`: Closes the document.
- `Application.Quit()`: Quits the Word application.

## Code Examples
The provided code snippet demonstrates the complete process of formatting the footer and adding page numbers to a Word document using Syncfusion's DocIO library.

## Cross References
- For more information on DocIO and its features, refer to the [Syncfusion Winforms Documentation](https://help.syncfusion.com/windowsforms).
- Additional resources can be found in the [Syncfusion Product Documentation](https://help.syncfusion.com/documentation).

<!-- tags: DocIO, Syncfusion Windows Forms, Word document, footer formatting, page numbers, API reference, document manipulation keywords: DocIO, footer, page numbers, formatting, Word document, Syncfusion, Windows Forms, documentation -->
```