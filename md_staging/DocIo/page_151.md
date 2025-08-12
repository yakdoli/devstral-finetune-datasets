```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_151.jpeg
document_name: DocIo
page_number: 151
page_id: DocIo#page_151
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:27Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Describes how to customize the properties and behaviors of text form fields in DocIO.
- Focuses on setting default text, formatting, and enabling fill-in modes for form fields.
- Provides details on available text field types and their properties in the WinForms environment.

## Content

### Figure 53: Text Form Field Properties

![Figure 53: Text Form Field Properties](Figure 53: Text Form Field Properties)

To set the format of the DocIO text directly from the field, you can use the **StringFormat** property. To get or set the default text for the text form field, you can use the **DefaultText** property.

**Note**: Text form field will display the default text only when the text of the form field has no value, i.e., when the **TextRange** property (**TextRange.Text**) has no value.

#### TextRange and Type Properties

- **TextRange** property is used to set the text of the text form field.
- **Type** property specifies the type of the text form field. The following are the types of the text form field:
  - **RegularText**
  - **NumberText**
  - **DateText**

### Class Hierarchy

#### WTextRange
  - |
    WField

## Page-level Navigation/TOC (if applicable)
- [Link to related topics or tables of contents if present]

## Cross References
- See also: [Any applicable cross references to other sections or resources]

## RAG Annotations
<!-- tags: [DocIO, text form fields, WTextRange, WField, WinForms, Syncfusion Winforms, version: 11.4.0.26] keywords: [text form field properties, default text, form field types, text range, fill-in mode, WinForms environment] -->
```