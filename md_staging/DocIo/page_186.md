```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_186.jpeg
document_name: DocIo
page_number: 186
page_id: DocIo#page_186
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:39Z
fidelity: lossless
-->

# Essential DocIO

```vb
Dim section As WSection = sourceDoc.LastSection
For Each para As IParagraph In section.Paragraphs
    For Each item As ParagraphItem In para.Items
        If TypeOf item Is WComment Then
            Dim comment As WComment = CType(IIf(TypeOf item Is WComment, item, Nothing), WComment)
            comment.TextBody.LastParagraph.Text = "NewText"
            comment.Format.User = "TestUser"
        End If
    Next item
Next para
```

## Comments Collection

You can access comments while browsing through the collection of paragraph items or through the collection of comments by using the `WordDocument.GetComments` method.

### Public Methods

| Name       | Description                                          |
|------------|------------------------------------------------------|
| Clear      | Remove all comments from the document.              |
| RemoveAt   | Remove second comments from the document.           |

The following example illustrates how to get all the comments from the document and remove them.

#### [C#]

```csharp
WordDocument doc = new WordDocument("sample.doc");
commentsCollection comments = doc.GetComments();

// Remove second comments from the document.
comments.RemoveAt(1);

// Remove all comments from the document.
comments.Clear();
```

#### [VB]

```vb
Dim doc As New WordDocument("sample.doc")
Dim comments As CommentsCollection = doc.GetComments()
```

## Page-level Navigation/TOC (if applicable)

- [unclear]

### WinForms-specific conventions

- [unclear]

### API Reference (if applicable)

#### Methods

| Name         | Description                                    |
|--------------|-----------------------------------------------|
| `Clear`      | Remove all comments from the document.        |
| `RemoveAt`   | Remove second comments from the document.     |

#### Parameters

| Name       | Type    | Description                     | Default | Required |
|------------|---------|---------------------------------|---------|----------|
| index      | Integer | Index of the comment to remove. | None    | Yes      |

## Code Examples

- Example in C#:
  ```csharp
  WordDocument doc = new WordDocument("sample.doc");
  commentsCollection comments = doc.GetComments();
  comments.RemoveAt(1);
  comments.Clear();
  ```

- Example in VB:
  ```vb
  Dim doc As New WordDocument("sample.doc")
  Dim comments As CommentsCollection = doc.GetComments()
  comments.RemoveAt(1)
  comments.Clear()
  ```

## Cross References

- Related features: [unclear]
- See also: [WordDocument, commentsCollection, GetComments, RemoveAt, Clear]

<!-- tags: [Syncfusion, Winforms, DocIO, Comments Collection, API Reference, Code Examples, Cross References] keywords: [WordDocument, commentsCollection, GetComments, RemoveAt, Clear] -->
```