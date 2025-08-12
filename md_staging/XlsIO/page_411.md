```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_411.jpeg
document_name: XlsIO
page_number: 411
page_id: XlsIO#page_411
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:31Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates the integration of XlsIO with VBA in a template.
- Explains how to disable macros in the template workbook to ensure normal functionality without executing macros.

## Content

### XlsIO with VBA in Template

![Screenshot of Excel interface showing form validation template](Figure 152: XlsIO with VBA in Template)

The figure above illustrates an Excel form validation template with various input fields, some of which are marked as mandatory. Upon submission, a confirmation message is displayed, indicating the successful execution of the form.

### Disabling Macros in Template Workbooks

XlsIO provides support for disabling macros in the template workbook as follows:

"This will just ignore the macros in the template, and work normally as if there were no macros in the template."

#### Code Examples

##### C#

```csharp
Workbook.DisableMacrosStart = true;
```

##### VB.NET

```vb
Workbook.DisableMacrosStart = True
```

## RAG Annotations

<!-- tags: [XlsIO, WinForms, macros, template workbook, form validation, VBA] keywords: [disabling macros, form validation, template, workbook, Excel, mandatory fields, confirmation message] -->
```