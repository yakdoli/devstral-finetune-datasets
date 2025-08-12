```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_280.jpeg
document_name: DocIo
page_number: 280
page_id: DocIo#page_280
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:44Z
fidelity: lossless
-->

## Removing Empty Mail Merge Fields

To remove paragraphs that contain empty mail merge fields from the document, set the `doc.MailMerge.RemoveEmptyParagraphs` to `True`.

The following example illustrates how to remove paragraphs that contain empty mail merge fields.

### Removing Empty Paragraphs Using C#

```csharp
doc.MailMerge.RemoveEmptyParagraphs = true;
```

### Removing Empty Paragraphs Using VB

```vb
doc.MailMerge.RemoveEmptyParagraphs = True
```

## Removing Empty Groups

To remove empty groups from the document during mail merge, set the `document.MailMerge.RemoveEmptyGroup` to `True`. The default value of `RemoveEmptyGroup` is false.

The following example illustrates how to remove empty groups from the document.

### Removing Empty Groups Using C#

```csharp
document.MailMerge.RemoveEmptyGroup = true;
```

### Removing Empty Groups Using VB

```vb
document.MailMerge.RemoveEmptyGroup = True
```

## Clear Fields

To remove empty mail merge fields from the document, set the `MailMerge.ClearField` property to `True`.

### Clearing Fields Using C#

```csharp
WordDocument doc = new WordDocument("Sample.doc");
string[] fieldname = { "FirstName", "LastName" };
string[] fieldvalues = { "John", "David", };
doc.MailMerge.ClearFields = false;
doc.MailMerge.Execute(fieldname, fieldvalues);
```

## API Reference

- **Methods**
  - `MailMerge.ClearFields`: Clears the mail merge fields.
  - `MailMerge.Execute`: Executes the mail merge operation.

### Code Examples

#### C#

```csharp
WordDocument doc = new WordDocument("Sample.doc");
string[] fieldname = { "FirstName", "LastName" };
string[] fieldvalues = { "John", "David", };
doc.MailMerge.ClearFields = false;
doc.MailMerge.Execute(fieldname, fieldvalues);
```

#### VB

```vb
Dim doc As New WordDocument("Sample.doc")
Dim fieldname As String() = { "FirstName", "LastName" }
Dim fieldvalues As String() = { "John", "David", }
doc.MailMerge.ClearFields = False
doc.MailMerge.Execute(fieldname, fieldvalues)
```

<!-- tags: [Syncfusion, MailMerge, RemoveEmptyParagraphs, RemoveEmptyGroup, ClearFields, WordDocument, MailMerge.Execute, MailMerge.ClearFields, C#, VB] keywords: [Empty Paragraphs, Empty Groups, Clear Fields, MailMerge, WordDocument, Execute, ClearFields, C#, VB] -->
```