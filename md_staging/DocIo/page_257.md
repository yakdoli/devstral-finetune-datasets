```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_257.jpeg
document_name: DocIo
page_number: 257
page_id: DocIo#page_257
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:15Z
fidelity: lossless
-->

# Essential DocIO

## Content

### Finding a String in SingleLine Mode

The following example illustrates how to find a string in the SingleLine mode.

#### C# Code Example

```csharp
WordDocument doc = new WordDocument("Sample.doc");
string search = "\\[start\\](.*)\\[end\\]";

// The singleline option should cause \r\n to be included in .*
Regex expr = new Regex(search, RegexOptions.Singleline);

WTable table = doc.Sections[0].Tables[0] as WTable;
TextSelection[] sel = doc.FindNextSingleLine(table as TextBodyItem, expr);
```

#### VB.NET Code Example

```vb.net
Dim doc As New WordDocument("Sample.doc")
Dim search As String = "\[start\](.*)\[end\]"

' The singleline option should cause \r\n to be included in .*
Dim expr As New Regex(search, RegexOptions.Singleline)

Dim tab As WTable = TryCast(doc.Sections(0).Tables(0), WTable)
Dim sel As TextSelection() = doc.FindNextSingleLine(TryCast(tab, TextBodyItem), expr)
```

### 4.5.5 Replace

#### Overview of the Replace Method

The `Replace` method provides support to replace text in the Word document. The following are the possible input parameters of the `Replace` method.

- **Pattern**: character pattern (object of Regex class)
- **Replace**: replace string
- **Given**: string to be replaced
- **CaseSensitive**: defines if replace is case-sensitive.

**Example**: If case sensitive is set to false and you want to replace the "AA" string, then in such case strings like "aA" and "Aa" also will be replaced.

- **WholeWord**: if set to true, string given must be the whole word (not the part of the word)
- **SaveFormatting**: if set to true, it will preserve the existing placeholder formatting

## API Reference

### Parameters

| Name         | Type      | Description                                           | Default | Required |
|--------------|-----------|-------------------------------------------------------|---------|----------|
| Pattern      | Regex     | The character pattern to search for.                | -       | Yes      |
| Replace      | string    | The string to replace the matched pattern with.     | -       | Yes      |
| Given        | string    | The string to be replaced.                          | -       | Yes      |
| CaseSensitive| bool      | Determines if the replacement is case-sensitive.   | false   | No       |
| WholeWord    | bool      | Determines if the replacement must be the whole word. | false   | No       |
| SaveFormatting | bool    | Determines if the formatting should be preserved.  | false   | No       |

#### Returns

- Type: void
- Description: Replaces the text in the Word document based on the provided parameters.

#### Exceptions

- ArgumentNullException: If the Pattern or Replace parameters are null.
- InvalidOperationException: If the document is not in edit mode.

## Code Examples

### Example 1: Replacing Case-Insensitive Text

```csharp
doc.Replace("hello", "world", false, true, false, false);
```

### Example 2: Replacing Whole Words Only

```vb.net
doc.Replace("apple", "banana", true, true, true, false)
```

## Page-level Navigation/TOC (if applicable)

#### Cross References

- See also: 
  - **Regular Expressions in Document Processing**
  - **Advanced String Manipulation Techniques**

<!-- tags: [DocIO, RegularExpressions, TextReplacement, WordProcessing, SingleLineMode] keywords: [replace, regex, case-sensitive, whole word, formatting, text manipulation] -->
```
