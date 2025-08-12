```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_261.jpeg
document_name: DocIo
page_number: 261
page_id: DocIo#page_261
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:38Z
fidelity: lossless
-->

# Essential DocIO

The following code snippet illustrates the SingleLine mode replacement.

## Content

### ReplaceSingleLine Methods

The following table describes the `ReplaceSingleLine` methods:

| Method Signature | Description |
|-------------------|-------------|
| ReplaceSingleLine(Regex, String) | Replaces all entries with specified pattern with replace text in single-line mode. |
| ReplaceSingleLine(String, TextBodyPart, Boolean, Boolean) | Replaces the given text with specified replacement in single-line mode. |
| ReplaceSingleLine(String, TextSelection, Boolean, Boolean) | Replaces the given text with replacement in single-line mode. |
| ReplaceSingleLine(String, String, Boolean, Boolean) | Replaces all entries of given text with replace text in single-line mode. |

#### Code Snippet: SingleLine Mode Replacement

**[C#]**

```csharp
WordDocument doc = new WordDocument("sample.doc");
string search = "\\|(.\r\n\r\n)*?\\|";
// The singleline option should cause \r\n to be included in .*
Regex expr = new Regex(search, RegexOptions.Singleline);
doc.ReplaceSingleLine(expr, "test");
```

**[VB.NET]**

```vb
Dim doc As New WordDocument("sample.doc")
Dim search As String = "\|." & vbCr & vbLf & "| " & vbCr & "" & vbLf & ")*)?"
' The singleline option should cause \r\n to be included in .*
Dim expr As New Regex(search, RegexOptions.Singleline)
doc.ReplaceSingleLine(expr, "test")
```

### 4.6 Mail Merge

#### Overview

The mail merge function allows you to fill a template document with data from the data source. It is represented by the `MailMerge` class. The following data source types are used in mail merge: String Arrays, DataTable, SqlDataReader or DataView class objects. The template of the document is created by using the MergeFields of MS Word.

#### Summary of Features
- Utilizes the `MailMerge` class for data population.
- Supports various data sources: String Arrays, DataTable, SqlDataReader, and DataView.
- Requires MergeFields in the document template for integration with MS Word.

#### References

See also:
- [MailMerge Class Documentation](https://docs.syncfusion.com/windowsforms/mail-merge/)
- MS Word Merge Fields Documentation

<!-- tags: Syncfusion Winforms, Mail Merge, Document Processing, Word, String Arrays, DataTable, SqlDataReader, DataView, MergeFields, version: 11.4.0.26 -->
```