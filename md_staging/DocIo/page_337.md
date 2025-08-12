```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_337.jpeg
document_name: DocIo
page_number: 337
page_id: DocIo#page_337
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:35Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to perform a simple "find and replace" operation using DocIO.
- Includes code examples in C# and VB for interacting with Word documents.

## Using DocIO

### Overview
The following code example shows how to perform a simple find and replace operation using DocIO.

#### Example: C#

```csharp
// Open the word document
WordDocument doc = new WordDocument("FindAndReplaceTemplate.doc", FormatType.Doc);

// Define replacement text
string replaceText = "World";

// Perform replace
doc.Replace(new Regex("Hello"), replaceText);

// Save the document
doc.Save("Find And Replace.doc");

// Close the document
doc.Close();
```

#### Example: VB

```vb
' Open the word document
Dim doc As WordDocument = New WordDocument("FindAndReplaceTemplate.doc")

' Define text to be replaced
Dim replaceText As String = "World"

' Perform replace
doc.Replace(New Regex("Hello"), replaceText)

' Save the document
doc.Save("Find And Replace.doc")

' Close the document
doc.Close()
```

## API Reference

### WinForms-specific conventions
- The `WordDocument` class is used to manipulate Word documents.
- The `Replace` method utilizes a regular expression to search for and replace text within the document.

### Methods
- `Replace`: Replaces all occurrences of a specified string or regular expression pattern with a replacement string.
  - Parameters:
    - `Regex`: The search pattern.
    - `String`: The replacement text.
  - Returns: The modified `WordDocument` object.

### Examples
Both examples demonstrate:
1. Opening a Word document.
2. Defining the text to replace.
3. Performing the replace operation using a regular expression.
4. Saving the modified document.
5. Closing the document to free resources.

## Code Examples

#### C# Code
```csharp
// Open the word document
WordDocument doc = new WordDocument("FindAndReplaceTemplate.doc", FormatType.Doc);

// Define replacement text
string replaceText = "World";

// Perform replace
doc.Replace(new Regex("Hello"), replaceText);

// Save the document
doc.Save("Find And Replace.doc");

// Close the document
doc.Close();
```

#### VB Code
```vb
' Open the word document
Dim doc As WordDocument = New WordDocument("FindAndReplaceTemplate.doc")

' Define text to be replaced
Dim replaceText As String = "World"

' Perform replace
doc.Replace(New Regex("Hello"), replaceText)

' Save the document
doc.Save("Find And Replace.doc")

' Close the document
doc.Close()
```

## See also
- [DocIO Documentation](https://www.syncfusion.com/documentation/docio/)
- [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation/windows-forms/)

<!-- tags: [product, DocIO, WinForms, WordDocument, Replace, Regex, Syncfusion.Windows.Forms] keywords: [DocIO, WordDocument, replace, regex, find, replace operation] -->
```