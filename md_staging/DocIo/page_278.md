```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_278.jpeg
document_name: DocIo
page_number: 278
page_id: DocIo#page_278
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:42Z
fidelity: lossless
-->

## Content

### Overview
- This section explains how to use the `MailMerge` class to map between names of fields in your data source and names of mail merge fields in the document.

### Additional Mail Merge Features

#### Using Mapped Fields
The `MailMerge` class allows to automatically map between names of fields in your data source and names of mail merge fields in the document. To perform this, use the `MailMerge.MappedDataFields` property that returns a `MappedDataFields` object. `MappedDataFields` is a collection of string keys into string values. The keys are the names of mail merge fields in the document and the values are the names of fields in your data source. The class provides all properties and methods typical for a regular .NET collection such as `Add`, `Clear`, `Remove`, and so on.

The following example illustrates how to add a mapping when a merge field in a document and a data field in a data source have different names.

```csharp
[C#]

doc.MailMerge.MappedDataFields.Add("FieldName_InDocument", "FieldName_InDataSource");
```

```vb
[VB]

doc.MailMerge.MappedDataFields.Add("FieldName_InDocument", "FieldName_InDataSource")
```

#### Obtaining Merge Field Names
You can get the collection of the merge field names available in the document by using the `MailMerge.GetFieldNames` method. This returns an array of string that contains the names.

## API Reference

### Methods
- **GetFieldNames**: Retrieves the collection of the merge field names available in the document.

### Fields
- **MappedDataFields**: A collection of string keys into string values representing the mapping between mail merge fields and data source fields.

## Code Examples

### Example: Adding a Mapping
The following code demonstrates how to add a mapping between a mail merge field and a data source field.

#### C#

```csharp
doc.MailMerge.MappedDataFields.Add("FieldName_InDocument", "FieldName_InDataSource");
```

#### VB

```vb
doc.MailMerge.MappedDataFields.Add("FieldName_InDocument", "FieldName_InDataSource")
```

## Additional Notes
- Ensure that the field names are correctly mapped to avoid merge errors.
- The `MappedDataFields` property can be used to handle cases where the field names in the document and data source do not match.

<!-- tags: [mailmerge, fieldmapping, syncfusion, winforms, dataintegration] keywords: [mappeddatafields, getfieldnames, mailmerge, fieldnames, document, datasource, mapping, mergefields] -->
```