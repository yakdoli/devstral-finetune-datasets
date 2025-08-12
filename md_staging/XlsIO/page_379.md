```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_379.jpeg
document_name: XlsIO
page_number: 379
page_id: XlsIO#page_379
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:35Z
fidelity: lossless
-->

# Essential XlsIO

This is another variant of the Template based approach, but the difference is that the end-user places special markers in the template spreadsheet, which gets replaced along with the data during runtime. The main advantage of this approach is that the end-user gets the flexibility of designing the Excel report.

Cells in the worksheet can be filled with single data or with multiple records. Format of these data can be changed by using the arguments of the markers.

## Marker Syntax

Each marker starts with some prefix, by default it is "%" character, and followed by the variable name and properties. There could be several arguments after the variable, which are delimited by some character, by default it is semicolon (;).

![Template Marker](https://i.imgur.com/figur.png)
**Figure 135: Template Marker**

## Source

XlsIO can be used to bind various data sources to these markers. This includes data sources such as Data Table, Data Set, Data Reader, Data View, Array, Variable and Formulas.

## Arguments

You can specify the following arguments in the marker to customize the worksheet.

- Horizontal-This argument specifies the horizontal direction of the data import for complex variables.
- Vertical-This argument specifies the vertical direction of the data import for complex variables.
- Insert-This argument inserts new rows or columns, depending on the direction argument for each new cell. Note that by default, the rows cannot be added.
- insert:copystyles-This argument copies styles from the above row or left column.
- jump:[cell reference in R1C1 notation]-This argument binds the data to the cell at the specified reference. Cell reference addresses can be relative or absolute.
- copyrange:[top-left cell reference in R1C1]:[bottom-right cell reference in R1C1]-Copies the specified cells after each cell import.

Here is the sample after dynamically filling the data during runtime.

<!-- tags: [XlsIO, Excel, Template-based approach, markers, data binding, data sources, complex variables, syncfusion, winforms] keywords: [Essential XlsIO, Template, markers, runtime, design flexibility, data formats, syntax, source, arguments, data binding, complex variables, horizontal, vertical, insertion, styles] -->
```