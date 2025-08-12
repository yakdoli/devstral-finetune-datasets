```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_392.jpeg
document_name: XlsIO
page_number: 392
page_id: XlsIO#page_392
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:36Z
fidelity: lossless
-->

## Formatting Comments

### Overview
- Describes the options available in the Format Comment dialog box for customizing comment formatting.
- Highlights APIs for inserting Regular and Rich Text comments using the `ICommentShape` interface.
- Illustrates how to insert comments with code examples.

### Content

#### Figure: Format Comment Dialog Box
The Format Comment Dialog Box (Figure 141) allows users to customize the appearance of comments in an Excel document. It includes various tabs such as Protection, Properties, Alignment, Colors and Lines, Size, and Font. The Font tab is shown below, which allows users to modify font style, size, color, and effects.

![Figure 141: Format Comment Dialog Box](https://i.imgur.com/your_image_url.png)

The Figure 141 display showcases options for:
- **Font**: Choose from various font types such as Tahoma, Sylfaen, Symbol, System, or Tahoma.
- **Font Style**: Options include Regular, Italic, Bold, and Bold Italic.
- **Size**: Select the font size from a dropdown menu (e.g., 8, 9, 10, 11).
- **Color**: Choose the color for the font, including an "Automatic" option.
- **Underline**: Options for underlining include None, Single, Double, and Dash.
- **Effects**: Options for strikethrough, superscript, and subscript effects can be checked.

#### Inserting Comments
XlsIO provides APIs for inserting both Regular and Rich Text comments via the `ICommentShape` interface. The interface includes properties for formatting comments, as demonstrated in the following code example:

#### Code Example: Inserting Comments
```csharp
// Insert Comments.
// Adding comments to a cell.
sheet.Range["A1"].AddComment().Text = "Regular Comment";

// Sets author of the comment.
sheet.Range["A1"].AddComment().Author = "Syncfusion";

// Add Rich Text Comments.
IRange range = sheet.Range["A2"];
range.AddComment().RichText.Text = "RichText";
IRichTextString rtf = range.Comment.RichText;
```

This example demonstrates how to insert both regular and rich text comments into Excel cells using C#.

### See also
- [Unclear: More details on API usage or related topics]
- [Unclear: Additional examples or advanced scenarios]

<!-- tags: XlsIO, comment formatting, Font dialog, Regular comments, Rich text comments, ICommentShape, C# example, Syncfusion Winforms, Excel, formatting, dialog box -->
```