```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_161.jpeg
document_name: DocIo
page_number: 161
page_id: DocIo#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:34Z
fidelity: lossless
-->

## Fields Updating Engine

Field in a Word document is a placeholder of data that might change on field update. A field contains field code, field separator, field result, and field end. The field code contains information about how the field result is to be calculated and updated. The field result specifies the resultant value of the field. Field updating engine calculates the resultant value based on the field code information and updates the field result with the new value.

### Supported Fields

- (formula field)
- DATE
- TIME
- DOCVARIABLE
- DOCPROPERTY
- COMPARE
- IF
- NEXTIF
- MERGEREC
- MERGESEQ
- SECTION

### (formula field)

This field is an expression that contains any combination of numbers, bookmarks that refer to numbers, fields resulting in numbers, and the available operators and functions. The expression can refer to values in a table and values returned by functions.

### DATE and TIME

This field displays the current date-time, in the format specified by date-time picture switch.

#### Syntax

```
{ DATE \@ "Date-Time Picture" }
{ TIME \@ "Date-Time Picture" }
```

### DOCVARIABLE

This field displays the value of the specified document variable.

#### Syntax

```
{DOCVARIABLE "Name"}
```

### Cross References

- See also: [Document Variables and Properties (unavailable, likely a placeholder for related topics)].

<!-- tags: [product, module, control, api, version?, fields, date-time, formulas, document variables, properties] keywords: [field updating engine, placeholder, field code, field separator, field result, field end, spaced formatting expressions, date-time formatting, document variables, property fields, compare fields, if fields, nextif fields, merge fields] -->
```