```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_156.jpeg
document_name: edit
page_number: 156
page_id: edit#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:01Z
fidelity: lossless
-->

Essential Edit for Windows Forms

## IntelliPrompt Features

This section covers the following topics:

### Code Snippets

Essential Edit supports an advanced feature of VS 2005 like Code Snippets. It is also used to load/save VS.NET 2005-compatible XML snippets.

**Code Snippets are inserted into the Edit Control by following the procedure given below:**

1. Type the snippet name. For example "do".
2. Pressing the TAB key, or CTRL + ' combination.
3. Select an item from the list as shown in the image below.

---

```csharp
/* Choose any desired Code Snippet from
the Code Snippets Menu. Press Ctrl + ' to
see the Code Snippets. Press Enter to
insert the selected Code Snippet into the
EditControl*/

// Insert snippet:
- Loops
- class
- enum
- struct
- switch
```

**Figure 55: Inserting Code Snippets into the Edit Control**

The code snippets allow you to input data to the highlighted fields.

**Code Snippets can also be inserted into the Edit Control by using the static Extract method of the CodeSnippetsExtractor class. The Extract method takes the following two parameters:**

1. Path of the folder containing the code snippets.
2. Instance of the Edit Control into which the extracted code snippet should be inserted.
```