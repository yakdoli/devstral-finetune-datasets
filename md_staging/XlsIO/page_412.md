```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_412.jpeg
document_name: XlsIO
page_number: 412
page_id: XlsIO#page_412
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:16:52Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Excel features for preparing and securing documents for sharing and distribution.
- Focus on Document Properties and Encryption/Decryption through XlsIO.
- Includes code examples for setting Built-In and Custom properties.

## Content

### 4.8 Prepare

Excel provides various features to prepare a document for sharing and distribution. These features help the users to add details on their report and share them in a secured way.

This section elaborates on the following features that play a vital role in preparing an Excel spreadsheet for distribution.

- **Document Properties**  
  This topic explains the various document properties that can be added to a workbook through XlsIO.

- **Encryption and Decryption**  
  This topic explains the workbook encryption and decryption with password through XlsIO.

#### 4.8.1 Document Properties

Document Properties are named values that provide information about the document, such as the date and time at which the document was last saved, the last user to modify the document, and so on. Document Properties are either built into the document, or are custom user-defined properties.

You can read, and manually add or modify some Built-In properties, and all Custom properties, by selecting the properties from the File menu. Built-in properties can be automatically updated properties such as LastSaveDate, or preset properties such as Keywords.

XlsIO allows to read and write Built-In and Custom properties through the IBuiltinDocumentProperties and ICustomDocumentProperties.

The following code example illustrates how to set the spreadsheet's Built-In and Custom properties.

```csharp
// Setting Built-in Document Properties.
IBuiltinDocumentProperties builtInProperites = book.BuiltinDocumentProperties;
builtInProperites.Author = "Essential XlsIO";
builtInProperites.Comments = "This document was generated using Essential XlsIO";
builtInProperites.ByteCount = 120;
builtInProperites.LastSaveDate = new DateTime(1950, 1, 2, 3, 4, 5, 6);
builtInProperites.Manager = "Manager";

// Setting Custom Properties.
```

<!-- tags: [Essential XlsIO, document properties, built-in properties, custom properties, encryption, decryption, XlsIO] keywords: [document properties, workbook security, Built-in properties, custom properties, last save date, encryption, decryption, XlsIO, essential xlsio, built-in document properties, custom document properties] -->
```