```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_252.jpeg
document_name: DocIo
page_number: 252
page_id: DocIo#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:31Z
fidelity: lossless
-->

# Essential DocIO

```csharp
Dim bn As BookmarksNavigator = New BookmarksNavigator(doc)
bn.MoveToBookmark("bookmark1")
Dim bodyPart As TextBodyPart = bn.GetBookmarkContent()
```

## TextBodySelection

`TextBodySelection` gives you an opportunity to select items in the `TextBodyPart`.

For example, you have the following text:

**Text NEED COPY**

THIS TEXT Other text

You may want to copy the "NEED COPY" table and "THIS TEXT", and paste in another location.

### Objects Tree is as follows.

**TextBody**
- **[0]Paragraph**
  - [0]TextRange – "Text"
  - [1]TextRange – "NEED"
  - [2]TextRange – "COPY"
- **[1]Table**
- **[2]Paragraph**
  - [0]TextRange – "THIS"
  - [1]TextRange – "TEXT"
  - [2]TextRange – "Other Text"

The following code is used for this purpose.

```csharp
TextBodySelection bodySelection = new TextBodySelection(body, 0, 2, 1, 1);
```
```