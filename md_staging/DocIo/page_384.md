```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_384.jpeg
document_name: DocIo
page_number: 384
page_id: DocIo#page_384
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:53:18Z
fidelity: lossless
-->

# Essential DocIO

Refer the following online documentation link for more information about adding the table of contents to the word document using DocIO:

http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/4418tableofcontents.htm

## 5.13 How to Attach a Template to a Word Document?

You can use the `AttachedTemplate` property to attach a template to a Word document using DocIO. The following code example illustrates this.

```csharp
//Set the location of the template
document.AttachedTemplate.Path = @"D:\Test.dot";

//Set the UpdateStylesOnOpen to 'true' to automatically update the styles from the attached template each time the document is opened with MS Word
document.UpdateStylesOnOpen = true;
```

```vb
'Set the location of the template document
document.AttachedTemplate.Path = @"D:\Test.dot"

'Set the UpdateStylesOnOpen to 'true' to automatically update the styles from the attached template each time the document is opened with MS Word
document.UpdateStylesOnOpen = true
```

## API Reference (if applicable)
- None applicable in this example.

## Code Examples (multi-language supported)
- The above examples demonstrate attaching a template and updating styles in a Word document.

## RAG Annotations
<!-- tags: [DocIO, Word Document, Template, Attachment, Styles, C# example, VB example] keywords: [DocIO, Word Document, Template attachment, Update StylesOnOpen, C#, VB, Syncfusion, Winforms] -->

```