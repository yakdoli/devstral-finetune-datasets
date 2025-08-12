```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_279.jpeg
document_name: DocIo
page_number: 279
page_id: DocIo#page_279
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:54Z
fidelity: lossless
-->

## Essential DocIO

The following example illustrates how to get the names of all the merge fields in a document.

### Getting Merge Field Names

```csharp
string[] fieldNames = doc.MailMerge.GetMergeFieldNames();
```

```vb
Dim fieldNames As String() = doc.MailMerge.GetMergeFieldNames()
```

### Obtaining Merge Field Group Names

You can get the collection of the Merge Field Group names available in the document by using the `MailMerge.GetMergeGroupNames` method. This returns an array of string that contains the names.

```csharp
string[] groupNames = doc.MailMerge.GetMergeGroupNames()
```

```vb
Dim filenames As String() = doc.MailMerge.GetMergeFieldNames(groupName)
```

### Obtaining Merge Fields for a Specific Group

You can get the collection of the Merge Fields for a specific group in the document by using the `doc.MailMerge.GetMergeFieldNames(String groupName)` method. This returns an array of string that contains the field names.

```csharp
string[] filenames = doc.MailMerge.GetMergeFieldNames(groupName);
```

```vb
Dim filenames As String() = doc.MailMerge.GetMergeFieldNames(groupName)
```

### Removing Empty Paragraphs

### Removing Empty Paragraphs

```csharp

```

```vb

```
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```