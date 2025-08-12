```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: DocIo
page_number: 166
page_id: DocIo#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:17Z
fidelity: lossless
-->

# BookmarkEnd Public Constructor

| Name | Description |
| --- | --- |
| WTextField.WTextField (IWordDocument) | Initializes a new instance of the `BookmarkEnd` class. |

## Public Properties

| Name | Description |
| --- | --- |
| EntityType | Gets the type of the entity. |
| Name | Gets or sets bookmark name. |
| OwnerParagraph | Gets owner paragraph. |

DocIO provides support to navigate between bookmarks. For details, see **BookmarkNavigator**.

**Note**: Modification of bookmarks in the Bookmarks Collection causes document corruption.

The following example illustrates how to use bookmarks.

### Usage Example

```csharp
IWordDocument doc = new WordDocument();
IWSection section = doc.AddSection();
IWP‌aragraph paragraph = section.AddParagraph();
paragraph.AppendText("Book with one ");
paragraph.AppendBookmarkStart("one_word");
paragraph.AppendText("word");
paragraph.AppendBookma‌rkEnd("one_word");
paragraph.AppendText(" selected");

section.AddParagraph();
paragraph = section.AddParagraph();
paragraph.AppendBookmarkStart("beginning_paragraph");
paragraph.AppendText("Beginning of the paragraph selected");

section.AddParagraph();
paragraph = section.AddParagraph();
paragraph.AppendBookmarkStart("bigger_bookmark");
paragraph.AppendText("Smaller bookmark ");
paragraph.AppendBookmarkStart("smaller_bookmark");
```
```html
<!-- tags: [DocIo, bookmark, bookmarks, document corruption, navigation, BookmarkEnd, Public Properties, C#' ] -->
```