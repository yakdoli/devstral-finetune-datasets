```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_139.jpeg
document_name: DocIo
page_number: 139
page_id: DocIo#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:39Z
fidelity: lossless
-->

# **Essential DocIO**

```vb
Dim section As IWSection = doc.AddSection()
Dim paragraph As IParagraph = section.AddParagraph()
paragraph.AppendText("Testing writing Merge Fields into Header")

section.PageSetup.DifferentFirstPage = True
section.PageSetup.DifferentOddAndEvenPages = True

paragraph = New WParagraph(doc)
paragraph.AppendText("[ FIRST PAGE Header ]")
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

paragraph = New WParagraph(doc)
' Appends field
paragraph.AppendField("Field's Name", FieldType.FieldMergeField)
section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)

paragraph = New WParagraph(doc)
paragraph.AppendText("[ FIRST PAGE Footer ]" & Constants.vbCr)
section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)
```

## 4.4.1.2.1 Merge Field

The `WMergeField` class represents a merge field in the Word document. To add a merge field in Microsoft Word, open the Insert menu, click Field, and then click MergeField. Merge field is suitable for mail merge because it is easy to set the user's data inside it.

### Key Properties of Merge Field

- **FieldName**: defines the name of the field
- **TextBefore** and **TextAfter**: define the text that is displayed before and after the merge field
- **NumberFormat** and **DateFormat**: define the number and date format respectively

These properties are used during mail merge. `NumberFormat` and `DateFormat` properties do not have an equivalent in Word MergeField.

### Class Hierarchy

- **WTextRange**

<!-- tags: [product, essential docio, merge field, class hierarchy] keywords: [mergefield, wmergefield, word document, mail merge, field name, textbefore, textareafter, numberformat, dateformat] -->
```