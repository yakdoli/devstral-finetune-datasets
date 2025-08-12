```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_393.jpeg
document_name: XlsIO
page_number: 393
page_id: XlsIO#page_393
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:40Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// Formatting first 4 characters.
IFont redFont = workbook.CreateFont();
redFont.Bold = true;
rtf.SetFont(0, 3, redFont);
```

## Adding Comments in a Cell

### VB.NET

```vb
' Insert Comments.
' Adding comments to a cell.
sheet.Range("A1").AddComment().Text = "Regular Comment"

' Sets author of the comment.
sheet.Range("A1").AddComment().Author = "Syncfusion"

' Add Rich Text Comments.
Dim range As IRange = sheet.Range("A2")
range.AddComment().RichText.Text = "RichText"
Dim rtf As IRichTextString = range.Comment.RichText

' Formatting first 4 characters.
Dim redFont As IFont = workbook.CreateFont()
redFont.Bold = True
rtf.SetFont(0, 3, redFont)
```

### C#

```csharp
// Read plain text comment.
this.txtPlainText.Text = sheet.Range["A1"].Comment.Text;
```

## Displaying Comments in XlsIO

![Figure 142: XlsIO with Comments Inserted](https://i.imgur.com/XY5Z4JU.png)

It is also possible to read the Rich Text string formatting. The following code example illustrates how rich text comments from a cell are read by using XlsIO, and then displayed in a RichTextBox.

### Code Example: Reading Rich Text Comments

```csharp
// Read plain text comment.
this.txtPlainText.Text = sheet.Range["A1"].Comment.Text;
```

<!-- tags: [Syncfusion, Winforms, XlsIO, comments, rich text, formatting, VB.NET, C#] keywords: [添加评论, 设置作者, 富文本, 格式化, 读取评论文本, worksheet, rich text string, XlsIO] -->
```