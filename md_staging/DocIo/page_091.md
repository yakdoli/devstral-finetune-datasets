```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: DocIo
page_number: 091
page_id: DocIo#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:40Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Revision Tracking is a feature designed to track changes in a document, useful in shared environments or for individual users.
- Provides options to accept or reject changes made to a document via `AcceptChanges` and `RejectChanges` properties.
- Supports tracking of insertions and deletions via `IsInsertRevision` and `IsDeleteRevision`.
- Useful for maintaining document history and ensuring document integrity.

## Content

### Revision Tracking

Revision Tracking is typically used in a shared environment to track changes made by others to a document. However, it can also be valuable for individual users, allowing them to review their own changes.

### Accessing Revisions

You can choose to accept or reject changes made to a document in Microsoft Word. `ParagraphItem` and `TextBodyItem` (WParagraph and WTable are `TextBodyItems`) objects have `WordDocument.AcceptChanges` and `WordDocument.RejectChanges` properties, which detect whether an object was inserted or deleted in Microsoft Word when revision tracking is enabled.

#### Properties

- **WordDocument.HasChanges**: Specifies whether the document has any revisions. Returns `True` if the document has at least one revision.
- **WordDocument.TrackChanges**: This property is used to enable revision tracking in Microsoft Word. Note that changes made using DocIO are never tracked as revisions.

### Example Code

```csharp
Syncfusion.DocIO.DLS.WordDocument doc = new WordDocument(@"../../Essential DocIO.doc", FormatType.Doc);
foreach (WSection section in doc.Sections)
{
    for (int i = 0; i <= section.Paragraphs.Count - 1; i++)
    {
        var para = section.Paragraphs[i];

        // Check each paragraph items revisions.
        foreach (ParagraphItem item in para.Items)
        {
            Console.WriteLine(item.EntityType.ToString() + " Inserted: " + item.IsInsertRevision.ToString());
            Console.WriteLine(item.EntityType.ToString() + " Deleted: " + item.IsDeleteRevision.ToString());
        }
    }
}

// Accept tracking changes of the document.
doc.AcceptChanges();
doc.Save("sample.doc");
```

## API Reference

### WordDocument Class
- **Properties**
  - `HasChanges`: Boolean indicating if the document has any revisions.
  - `TrackChanges`: Boolean to enable or disable revision tracking.
- **Methods**
  - `AcceptChanges()`: Accepts all tracked changes in the document.
  - `RejectChanges()`: Rejects all tracked changes in the document.

### ParagraphItem Class
- **Properties**
  - `EntityType`: Indicates the type of entity (e.g., Run, Hyperlink).
  - `IsInsertRevision`: Boolean indicating if the entity was inserted.
  - `IsDeleteRevision`: Boolean indicating if the entity was deleted.

## Code Examples

The example demonstrates how to:
1. Iterate through sections and paragraphs in a Word document.
2. Check each paragraph item for revisions.
3. Accept all changes in the document and save it.

```csharp
// Iterate through sections and paragraphs
foreach (WSection section in doc.Sections)
{
    for (int i = 0; i <= section.Paragraphs.Count - 1; i++)
    {
        // Access paragraph items and check for revisions
        foreach (ParagraphItem item in para.Items)
        {
            Console.WriteLine($"Entity Type: {item.EntityType}, Inserted: {item.IsInsertRevision}, Deleted: {item.IsDeleteRevision}");
        }
    }
}

// Accept all tracked changes
doc.AcceptChanges();
doc.Save("sample.doc");
```

## RAG Annotations
<!-- tags: [DocIO, revision tracking, WordDocument, ParagraphItem, accept changes, reject changes, track changes] -->
```