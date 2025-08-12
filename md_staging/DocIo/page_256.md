```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_256.jpeg
document_name: DocIo
page_number: 256
page_id: DocIo#page_256
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:41Z
fidelity: lossless
-->

## Content

To find and replace specific content in a document, the following VB.NET code examples demonstrate how to interact with tables and paragraphs:

```vb
' To find and replace particular table
Dim table As IWTable = doc.Sections(0).Tables(0)
Dim selc As TextSelection = doc.FindNext(TryCast(table, TextBodyItem), "textAA", False, False)
Dim range As WTextRange = selc.GetAsOneRange()
range.Text = "TextReplaced"

' or To find and replace from particular paragraph
Dim table1 As IWTable = doc.Sections(0).Tables(0)
Dim par As IWParagraph = table1.Rows(1).Cells(0).Paragraphs(0)
Dim sell As TextSelection = doc.FindNext(TryCast(par, TextBodyItem), "refAA", False, False)
Dim rang1 As WTextRange = sell.GetAsOneRange()
rang1.Text = "New Text"
```

### Find with SingleLine mode

The `FindSingleLine` method is used to find an entry in a document with a specified text of regular expression, including newline or carriage return. This works in the same way as the SingleLine mode of .NET Regex. Note that the `Find` method will find the text only in a single paragraph without any newlines or carriage return considerations.

#### Methods for SingleLine mode

| Name | Description |
|------|-------------|
| `FindSingleLine(Regex)` | Finds the first entry of specified pattern in single-line mode. |
| `FindSingleLine(String, Boolean, Boolean)` | Finds the first entry of given text in single-line mode. |

#### Using FindNextSingleLine

It is also possible to find the string with SingleLine mode from a particular region by using the `FindNextSingleLine` method of the WordDocument class.

##### Methods for `FindNextSingleLine`

| Name | Description |
|------|-------------|
| `FindNextSingleLine(TextBodyItem, Regex)` | Finds the next text which fits the specified pattern starting from the specified `TextBodyItem` using single-line mode. |
| `FindNextSingleLine(TextBodyItem, String, Boolean, Boolean)` | Finds the next given text starting from the specified `TextBodyItem` using single-line mode. |

## API Reference

### Methods

#### `FindSingleLine`
- **Description**: Finds the first entry of a specified pattern in single-line mode.
- **Parameters**:
  - `Regex`: The regular expression pattern to search for.

#### `FindSingleLine`
- **Description**: Finds the first entry of a given text in single-line mode.
- **Parameters**:
  - `String`: The text to search for.
  - `Boolean`: Case sensitivity flag.
  - `Boolean`: Whole word match flag.

#### `FindNextSingleLine`
- **Description**: Finds the next text which fits the specified pattern starting from the specified `TextBodyItem` using single-line mode.
- **Parameters**:
  - `TextBodyItem`: The starting point for the search.
  - `Regex`: The regular expression pattern to search for.

#### `FindNextSingleLine`
- **Description**: Finds the next given text starting from the specified `TextBodyItem` using single-line mode.
- **Parameters**:
  - `TextBodyItem`: The starting point for the search.
  - `String`: The text to search for.
  - `Boolean`: Case sensitivity flag.
  - `Boolean`: Whole word match flag.

## Code Examples

The provided VB.NET code examples demonstrate how to use the `FindNext` method to interact with tables and paragraphs, and the `FindSingleLine` and `FindNextSingleLine` methods to search for specific patterns in a single-line mode.

### Cross References

- Refer to the documentation on `WordDocument` for more methods and properties related to document manipulation.

<!-- tags: DocIo, VB.NET, SingleLine mode, pattern matching, text replacement, WordDocument, tables, paragraphs, regular expressions keywords: find next, replace text, single-line mode, text manipulation, pattern matching -->
```