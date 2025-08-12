<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_334.jpeg
document_name: DocIo
page_number: 334
page_id: DocIo#page_334
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:20Z
fidelity: lossless
-->

# Essential DocIO

```csharp
[C#]

using word = Microsoft.Office.Interop.Word;

// Initialize objects
object nullobject = Missing.Value;
object filepath = "FindAndReplaceTemplate.doc";
object newFilePath = "FindAndReplace.doc";
object item = word.WdGoToItem.wdGoToPage;
object whichItem = word.WdGoToDirection.wdGoToFirst;
object replaceAll = word.WdReplace.wdReplaceAll;
object forward = true;
object matchAllWord = true;
object matchCase = false;
object originalText = "Hello";
object replaceText = "World";
object save = true;

// Start the word application
word.Application wordApp = new word.Application();

// Open the word document
word.Document document = wordApp.Documents.Open(ref filepath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

wordApp.Visible = false;

// Search for text and replace
document.GoTo(ref item, ref whichItem, ref nullobject, ref nullobject);
foreach (word.Range rng in document.StoryRanges)
{
    rng.Find.Execute(ref originalText, ref matchCase, ref matchAllWord, ref nullobject, ref nullobject, ref nullobject, ref forward, ref nullobject, ref nullobject, ref replaceText, ref replaceAll, ref nullobject, ref nullobject, ref nullobject, ref nullobject);
}

// Save the document
document.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

## Overview
- Demonstrates how to use `Microsoft.Office.Interop.Word` to find and replace text in a Word document.
- Includes initializing objects, opening a document, performing a search and replace operation, saving the modified document, closing it, and quitting the application.

## Content

### Step-by-Step Breakdown
1. **Initialize Objects**: 
   - Sets up necessary objects like file paths, document elements, and text settings.
   
2. **Start the Word Application**:
   - Creates a new instance of the Word application.

3. **Open the Document**:
   - Uses `wordApp.Documents.Open` to open an existing document.
   - Sets `wordApp.Visible` to `false` to execute operations without displaying the UI.

4. **Search and Replace**:
   - Navigates to the beginning of the document.
   - Iterates through all text ranges (`StoryRanges`) to replace occurrences of `originalText` with `replaceText`.
   - Configures options for matching cases and whole words.

5. **Save the Document**:
   - Saves the modified document under a new file path.

6. **Close and Exit**:
   - Closes the document and quits the Word application.

## Callouts
- **Note:** Ensure proper handling of resources and error conditions when working with COM interop objects.

## Related Information
- Refer to the official Microsoft documentation for more details on `Microsoft.Office.Interop.Word`.

<!-- tags: [docio, word document, find replace, winforms, interop, text manipulation] keywords: [find, replace, word, document, interop, text, manipulat^^^^ion] -->