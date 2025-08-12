```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_255.jpeg
document_name: DocIo
page_number: 255
page_id: DocIo#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:15Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- TextSelection Find(Regex pattern) - finds and returns entry of specified regular expression along with formatting.
- TextSelection[] FindAll(Regex pattern) - finds and returns all entries of specified regular expression along with formatting.
- TextSelection[] FindAll(string given, bool caseSensitive, bool wholeWord) - finds and returns all entries of specified string along with formatting, taking into consideration case-sensitive and whole word options.

The following example illustrates how to use the Find method.

### Example Usage of Find Method

#### C#

```csharp
doc.Open( "sample.doc" );
TextSelection rangesHolder1 = doc.Find( "The Placeholder1", false, false );
```

#### VB.NET

```vb.net
doc.Open("sample.doc")
Dim rangesHolder1 As TextSelection = doc.Find("The Placeholder1", False, False)
```

### FindNext Method

You can find a particular string from a paragraph region or table by using the FindNext method. The following code illustrates this.

#### C#

```csharp
// To find and replace particular table
IWTable table = doc.Sections[0].Tables[0];
TextSelection selc = doc.FindNext(table as TextBodyItem, "textAA", false, false);
WTextRange range = selc.GetAsOneRange();
range.Text = "TextReplaced";

// or To find and replace from particular paragraph
IWTable table1 = doc.Sections[0].Tables[0];
IWParagraph par = table1.Rows[1].Cells[0].Paragraphs[0];
TextSelection sell = doc.FindNext(par as TextBodyItem, "ref AA", false, false);
WTextRange range1 = sell.GetAsOneRange();
range1.Text = "New Text";
```
```