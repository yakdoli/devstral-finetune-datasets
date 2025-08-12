```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: DocIo
page_number: 162
page_id: DocIo#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:05Z
fidelity: lossless
-->

# Essential DOCIO

## Overview
- This page describes various fields used for displaying and comparing document properties, expressions, and conditions in Syncfusion Winforms.
- Fields such as DOCPROPERTY, COMPARE, IF, NEXTIF, and MERGESEQ are explained with their respective syntax and usage.

## Content

### DOCPROPERTY
This field displays the value of the specified document property.

- **Syntax**
  ```markdown
  {DOCPROPERTY "Name"}
  ```

### COMPARE
This field compares the two expressions and displays the result "1" if the result of comparison is true or "0" (zero) if the comparison is false.

- **Syntax**
  ```markdown
  {COMPARE Expression1 Operator Expression2 }
  ```

### IF
This field compares the two expressions and displays the true text if the result of comparison is true or displays the false text if the result of comparison is false.

- **Syntax**
  ```markdown
  { IF Expression1 Operator Expression2 TrueText FalseText }
  ```

### NEXTIF
This field compares two expressions. If the comparison result is true, the next data record is merged into the current merge document. If the comparison result is false, the next data record is merged into a new merge document.

- **Syntax**
  ```markdown
  {NEXTIF Expression1 Operator Expression2 }
  ```

### MERGESEQ
This field numbers all the merged records of a mail merge. The number may be different from the value that is inserted by the MERGEREC field.

- **Syntax**
  ```markdown
  { MERGESEQ }
  ```

<!-- tags: document, properties, expressions, comparison, merge, numbering, syncfusion, winforms, mail merge, document manipulation -->
```