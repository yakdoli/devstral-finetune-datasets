```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_377.jpeg
document_name: DocIo
page_number: 377
page_id: DocIo#page_377
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:53:06Z
fidelity: lossless
-->

### 1. Protecting a Word Document Using C#

#### Overview
- 1-2 sentences summarizing the page scope using only visible text.
- This code snippet demonstrates how to protect a Microsoft Word document using the Microsoft Office Interop library in C#. It includes the process of opening a document, applying a protection type (`wdAllowOnlyComments`), and saving the changes.

#### Content
##### WinForms-specific conventions
This section explains how to interact with Microsoft Word documents programmatically using the Microsoft Office Interop library in C#. The code snippet covers the following steps:
1. **Initialization**: Setting up necessary objects and references.
2. **Opening the Document**: Loading an existing Word document.
3. **Applying Protection**: Restricting document editing to allow only comments.
4. **Saving Changes**: Saving the updated document with protection enabled.
5. **Closing the Application**: Properly closing the Word application after operations.

Here is the complete code example:

```csharp
using word = Microsoft.Office.Interop.Word;

// Initialize objects
object nullobject = System.Reflection.Missing.Value;
object filePath = "Document.doc";
object newFilePath = "FileProtectionOffice.doc";
object noReset = false;
object password = System.String.Empty;
object useIRM = false;
object enforceStyleLock = false;

// Start the word application
word.Application wordApp = new word.Application();

// Open the word document that is to be protected
word.Document doc = wordApp.Documents.Open(ref filePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

wordApp.Visible = false;

// Set "Allow only Comments" protection to word document
doc.Protect(word.WdProtectionType.wdAllowOnlyComments, ref noReset, ref password, ref useIRM, ref enforceStyleLock);

// Save the document
doc.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

// Close the document
doc.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

### API References
The code utilizes the following namespaces and classes:
- **Microsoft.Office.Interop.Word**: Provides the required classes and interfaces to interact with Microsoft Word.
- **System.Reflection.Missing.Value**: Represents a missing value for optional parameters in the COM interop.
- **word.WdProtectionType.wdAllowOnlyComments**: Specifies the protection type to allow only comments on the document.

### Code Examples
The above snippet demonstrates a complete workflow for protecting a Word document using C#. The `doc.Protect()` method is used to apply protection with the specified parameters. The `doc.SaveAs()` method is utilized to save the changes under a new file name.

### Cross References
For more information on using the Microsoft Office Interop Library, refer to the official documentation:
- [Microsoft Office Interop Documentation](https://docs.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word?view=word-pia)

### RAG Annotations
<!-- tags: [Microsoft.Office.Interop.Word, DocumentProtection, C#, Winforms, InteropLibrary] keywords: [script, document, protection, Microsoft Word, Authentication] -->
```