```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_329.jpeg
document_name: DocIo
page_number: 329
page_id: DocIo#page_329
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:12Z
fidelity: lossless
-->

# Essential DocIO

```vb
' Inserting a section break of the specified type and it returns a newly created section.
Dim section As WSection = 
paragraph.InsertSectionBreak(SectionBreakCode.EvenPage)
```

## 5.12 Migration from Microsoft Office Automation to Essential DocIO

This section covers information on the following topics:

### 5.12.1 Mail Merge

Mail merge feature can be used to generate reports and letters in MS Word. The following code examples show how to generate an employee report from an MDB data source using office automation and DocIO.

#### Using MS Office Interop

Office automation performs the mail merge by executing a SQL query on the word document. The output of the mail merge can be sent to a new word document. Alternatively, it can be sent to a printer and a fax machine and forwarded to an e-mail address.

### Code Example

```vb
' Using MS Office Interop
' Perform mail merge by executing an SQL query
' Send output to a new word document or printer/fax/email
```
<!-- tags: [migration, microsoft office automation, essential docio, mail merge, ms office interop] keywords: [migration, mail merge, automation, data source, employee report, word document, printer, fax, email] -->
```