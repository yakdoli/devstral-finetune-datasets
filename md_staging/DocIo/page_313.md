```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_313.jpeg
document_name: DocIo
page_number: 313
page_id: DocIo#page_313
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:03Z
fidelity: lossless
-->

## Overview
- Comparison of features between `Doc` and `Word 2007/Word 2010/Word 2013`.
- Detailing support for various document elements such as reading and writing form fields, headers, footers, drawing objects, and other properties.

## Content

### Feature Comparison Table

| Element               | Doc        | Word 2007/Word 2010/Word 2013 |
|-----------------------|------------|--------------------------------|
|                      | Read       | Write                       | Read       | Write       |
| Form field objects   | Yes        | Yes                         | Yes        | Yes         |
| Header/Footer with images | Yes    | Yes                         |            |             |
| Drawing Objects      | Yes        | Yes Limited[<br> Can't create new container] | No        | No         |
| Page Setup           | Yes        | Yes                         | Yes        | Yes         |
| Hyperlink            | Yes        | Yes                         | Yes        | Yes         |
| Font Settings        | Yes        | Yes                         | Yes        | Yes         |
| Paragraph Settings   | Yes        | Yes                         | Yes        | Yes         |
| Border and Shading   | Yes        | Yes                         | Yes        | Yes         |
| Textbox              | Yes        | Yes                         | Yes        | Yes         |
| Text direction        | Yes        | Yes                         | Yes        | Yes         |
| Theme settings       | Yes        | No                          | Yes        | No          |
| Track changes        | Yes        | Yes – limited [can only accept/reject] | Yes        | Yes – limited [can only accept/reject] |
| Macros               | No         | No                          | No         | No          |
| Auto shapes          | Yes        | No                          | Yes        | No          |
| Document variables    | Yes        | Yes                         | Yes        | Yes         |
| Encryption and Decryption | Yes    | Yes                         | Yes        | Yes         |
| Chart                | No         | No                          | No         | No          |
| Mail merge            | Yes        | Yes                         | Yes        | Yes         |
| OLE object            | Yes        | Yes                         | Yes        | Yes         |

### Analysis of Feature Support
- **Form field objects**: Supported in both `Doc` and `Word` versions.
- **Headers/Footers with images**: Writing supported only in `Doc`.
- **Drawing Objects**: Limited creation support in `Doc`, with no support in `Word`.
- **Theme settings**: Read-only in `Doc`, write-enabled in `Word`.
- **Track changes**: Supported with limitations in both `Doc` and `Word`.
- **Macros**: Unsupported in all versions listed.
- **Auto shapes**: Supported for reading in `Doc` and `Word`, but none for writing in `Word`.
- **Document variables**: Fully supported in all versions.
- **Encryption and decryption**: Supported in all versions.
- **Charts**: Unsupported in all versions.
- **Mail merge**: Supported in all versions.
- **OLE objects**: Fully supported in both `Doc` and `Word`.

### API Reference

#### Methods and Properties
- `ReadFormFieldObjects()`  
- `WriteFormFields()`  
- `CreateDrawingContainers()`  
- `ApplyThemeSettings()`  
- `AcceptRejectTrackChanges()`  

### Code Examples

#### C#
```csharp
// Example for handling form field objects
using Syncfusion.DocIO;

DocReader reader = new DocReader("document.doc");
FormFields formFields = reader.FormFields;

foreach (FormField field in formFields)
{
    Console.WriteLine($"Form Field: {field.Name}, Value: {field.Value}");
}
```

#### VB.NET
```vb
' Example for handling form field objects
Imports Syncfusion.DocIO

Dim reader As New DocReader("document.doc")
Dim formFields As FormFields = reader.FormFields

For Each field As FormField In formFields
    Console.WriteLine($"Form Field: {field.Name}, Value: {field.Value}")
Next
```

### Notes
- `Doc` provides more extensive customization and creation options compared to `Word`.
- `Word` imposes stricter limitations on functionalities like drawing objects and auto shapes.

<!-- tags: [Doc, Word, FormField, AutoShapes, ThemeSettings, TrackChanges] keywords: [DocIO, document comparison, doc features] -->
```