```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_346.jpeg
document_name: DocIo
page_number: 346
page_id: DocIo#page_346
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:09Z
fidelity: lossless
-->

## Document Watermark

### Overview

The page discusses how to add page numbers to a document using VB.NET and provides an example code snippet. It also introduces the concept of document watermarks, explaining their purpose and how to insert them in Microsoft Word using the Insert Watermark command.

---

### Content

#### Adding Page Numbers to a Document

The following VB.NET code demonstrates how to add page numbers to the footer of every section in a Word document.

```vb
' Open the word document
Dim doc As WordDocument = New WordDocument("PageNumbers.docx", FormatType.Docx)

' Add page number in footer for every section
For Each sec As WSection In doc.Sections
    Dim para As IParagraph = sec.AddParagraph()
    para.AppendField("footer", FieldType.FieldPage)
    para.ParagraphFormat.HorizontalAlignment = HorizontalAlignment.Center
    sec.PageSetup.PageNumberStyle = PageNumberStyle.Arabic
    sec.HeadersFooters.Footer.Paragraphs.Add(para)
Next

' Save the document
doc.Save("PageNumbersUpdated.docx", FormatType.Docx)

' Close the document
doc.Close()
```

**Explanation:**
- The code opens an existing Word document.
- It loops through each section of the document.
- For each section, it adds a paragraph to the footer and appends a page number field.
- It centers the paragraph and sets the page number style to Arabic numerals.
- Finally, it saves the updated document and closes it.

#### Document Watermark

**Definition:**
- Watermark: Text or image used to mark a document as private, confidential, or to convey specific information about its usage and credibility.

**Usage in Microsoft Word:**
- **Insert Watermark Command:** A quick method to insert a watermark in Word documents.

---

#### Using MS Office Interop

The provided example illustrates how to insert a text watermark as a shape using Office Automation. This section will elaborate on the process using Microsoft Office Interop API.

---

### API Reference

**Classes and Methods:**
- **WordDocument**
- **WSection**
- **IParagraph**
- **HeadersFooters**
- **PageSetup**
- **FieldType**
- **HorizontalAlignment**

**Parameters:**
- `fieldName`: A string specifying the field to append.
- `fieldType`: An enumeration defining the type of field.
- `pageNumberStyle`: An enumeration defining the style of page numbering.

---

### Code Examples

The code snippet provided earlier demonstrates the complete process of adding page numbers to a Word document.

---

### Cross References

- Refer to the Microsoft Office Interop documentation for detailed information on working with Word documents programmatically.
- For more examples on inserting watermarks, consult the Syncfusion documentation on Office Automation.

### Tags and Keywords
<!-- tags: [Microsoft Office, Interop, Word, Document, Page Numbers, Footer, Watermark] keywords: [WordDocument, pageNumberStyle, IParagraph, HeadersFooters, FieldType, HorizontalAlignment] -->
```