```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_318.jpeg
document_name: DocIo
page_number: 318
page_id: DocIo#page_318
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:11Z
fidelity: lossless
-->

# Essential DocIO

## 5.4 How to format a Hyperlink by using DocIO?

### Overview
- Explains the structure of fields in DocIO.
- Details how to format the text of a hyperlink using WTextRange(s).
- Provides examples in both C# and VB to demonstrate formatting hyperlink text.

### Content
Some details about the fields. Each field consists of the following:

- **Field**, which defines field properties (not formatting)
- **FieldMark (FieldSeparator mark)**
- **Text of the Field (WTextTange)**
- **FieldMark (FieldEnd mark)**

If you want to set formatting for the field text, you have to find **WTextRange(s)** between the field separator and field text to set the CharacterFormat for them.

The following code illustrates how to format the hyperlink text.

#### Code Examples

##### C#
```csharp
doc.LastParagraph.AppendHyperlink("www.google.com", "google", HyperlinkType.WebLink);
for (int i = 0, cnt = doc.LastParagraph.Items.Count; i < cnt; i++)
{
    if (doc.LastParagraph.Items[i] is WTextRange)
    {
        WTextRange text = doc.LastParagraph.Items[i] as WTextRange;
        text.CharacterFormat.FontSize = 33f;
    }
}
```

##### VB
```vb
doc.LastParagraph.AppendHyperlink("www.google.com", "google", HyperlinkType.WebLink)
Dim i As Integer = 0, cnt As Integer = doc.LastParagraph.Items.Count
While i < cnt
    If TypeOf doc.LastParagraph.Items(i) Is WTextRange Then
        Dim text As WTextRange = TryCast(doc.LastParagraph.Items(i), WTextRange)
        text.CharacterFormat.FontSize = 33.0F
    End If
    i += 1
End While
```

## Cross References
- See also: details on field properties and formatting of document elements in DocIO.

<!-- tags: [DocIO, Hyperlink, Formatting, FieldProperties, WTextRange, C#, VB] keywords: [DocIO, Hyperlink, CharacterFormat, WTextRange, AppendHyperlink, FontSize, FieldMark, FieldEnd, FieldSeparator] -->
```