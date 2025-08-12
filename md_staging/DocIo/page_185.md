```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_185.jpeg
document_name: DocIo
page_number: 185
page_id: DocIo#page_185
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:11Z
fidelity: lossless
-->

# Public Methods

| Name               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Clone              | Creates a new object that is a copy of the current instance.               |
| WCommentFormat     | Initializes a new instance of the WCommentFormat class.                    |
| RemoveCommentedItems | To remove all the items from the comments.                                |
| ReplaceCommentedItems | Replace the commented document content.                                   |

## Public Properties

| Name           | Description                      |
|----------------|-----------------------------------|
| User           | Gets or sets the user.           |
| UserInitials   | Gets or sets the user initials.   |

**Public Methods**

The following example illustrates how to search for a comment in the last section of a document. When it is found, the text and format of the comment is changed.

### Example in C#

```csharp
WSection section = sourceDoc.LastSection;
foreach (IWPParagraph para in section.Paragraphs)
{
    foreach (ParagraphItem item in para.Items)
    {
        if (item is WComment)
        {
            WComment comment = item as WComment;
            comment.TextBody.LastParagraph.Text = "NewText";
            comment.Format.User = "TestUser";
        }
    }
}
```

### Example in VB.NET

```vb
Dim section As WSection = sourceDoc.LastSection
For Each para As IWPParagraph In section.Paragraphs
    For Each item As ParagraphItem In para.Items
        If TypeOf item Is WComment Then
            Dim comment As WComment = DirectCast(item, WComment)
            comment.TextBody.LastParagraph.Text = "NewText"
            comment.Format.User = "TestUser"
        End If
    Next
Next
```

## Code Examples

- **C# Example** demonstrates iterating through paragraphs and comments in a document's last section, replacing the text and updating the user information.

- **VB.NET Example** provides equivalent functionality in VB.NET, showing how to traverse and modify comments in a document.

## Page-level Navigation/TOC

- **Public Methods**: Lists methods for managing WComment functionality, including cloning, initializing, removing, and replacing commented items.
- **Public Properties**: Details properties to get or set user and user initials.
- **Example in C#**: Demonstrates search and modification of comments in a document's last section.
- **Example in VB.NET**: Provides VB.NET alternative for the same functionality as C#.

## Cross References

- Refer to documentation on `WCommentFormat` for more details on initializing and configuring comment formats.
- For additional information on managing document sections, see documentation related to `WSection`.

### Related Components

- `sourceDoc`: The document object being manipulated.
- `WComment`: Represents a comment in the document.

### Notes

- Ensure that the document object (`sourceDoc`) is properly initialized before accessing or modifying comments.
- The code examples assume that the necessary namespaces and imports are included in the application.

<!-- tags: DocIO, public_methods, public_properties, comments, document_management, winforms
keywords: clone, wcommentformat,User,UserInitials,wcomment,textbody,lastparagraph,text,formatuser -->
```