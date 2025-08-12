```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_328.jpeg
document_name: DocIo
page_number: 328
page_id: DocIo#page_328
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:54Z
fidelity: lossless
-->

# Essential DocIO

```csharp
text.CharacterFormat.NumberForm = NumberFormType.OldStyle

' Sets the tabular type number spacing.
text = paragraph.AppendText("53127")
text.CharacterFormat.FontName = "Calibri"
text.CharacterFormat.NumberSpacing = NumberSpacingType.Tabular

' Sets the stylistic set option.
text = paragraph.AppendText("The quick red fox.")
text.CharacterFormat.FontName = "Gabriola"
text.CharacterFormat.StylisticSet = StylisticSetType.StylisticSet06
```

## Does Essential DocIO provide support for Client profile?

Yes, Essential DocIO provides support for Client profile. In order to use Essential DocIO in an application (which is targeted to the Client profile), the user should include the following assemblies:

- Syncfusion.Core.dll
- Syncfusion.Compresssion.Base.dll
- Syncfusion.DocIO.ClientProfile.dll

## How to insert section breaks?

Essential DocIO provides direct support to insert section breaks to Word documents. You can insert a section break to a Word document by using the InsertSectionBreak method of the WParagraph class.

The following code snippets illustrate how to insert a section break:

### [C#]

```csharp
// Inserting a section break and it returns a newly created section.
WSection section = paragraph.InsertSectionBreak();

// Inserting a section break of the specified type and it returns a newly created section.
WSection section = paragraph.InsertSectionBreak(SectionBreakCode.EvenPage);
```

### [VB]

```vb
' Inserting a section break and it returns a newly created section.
Dim section As WSection = paragraph.InsertSectionBreak()
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References
- If the page references other sections or pages, add cross references as shown in the body.

## RAG Annotations
```html
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```
``` html
<!-- Tags: Essential DocIO, section breaks, Client profile, Syncfusion -->
```