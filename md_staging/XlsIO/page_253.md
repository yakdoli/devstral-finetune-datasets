```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_253.jpeg
document_name: XlsIO
page_number: 253
page_id: XlsIO#page_253
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:34Z
fidelity: lossless
-->

## Inserting Headers and Footers in XlsIO

You can insert headers and footers through XlsIO, with the properties in the IPageSetup. Headers and footers can also be inserted to a Chart Worksheet.

The string that the header/footer takes, is a script that you can use to format the header. Please refer to the following link for more information on formatting strings:  
<http://support.microsoft.com/smarterror/default.aspx?spid=global&query=213618>

### Codes to Format Text

| Codes to Format Text | Description                                   |
|-----------------------|-----------------------------------------------|
| &L                    | Left-aligns the characters that follow.     |
| &C                    | Centers the characters that follow.         |
| &R                    | Right-aligns the characters that follow.    |
| &E                    | Turns double-underline printing on or off.  |
| &X                    | Turns superscript printing on or off.       |
| &Y                    | Turns subscript printing on or off.         |
| &B                    | Turns bold printing on or off.              |
| &I                    | Turns italic printing on or off.            |
| &U                    | Turns underline printing on or off.         |
| &S                    | Turns strikethrough printing on or off.     |
| &"fontname"           | Prints the characters that follow in the specified font. Be sure to include the quotation marks around the font name. |
| &nn                   | Prints the characters that follow in the specified font size. Use a two-digit number to specify a size in points. |

### Codes to Insert Specific Data

| Codes to Insert Specific Data | Description          |
|-------------------------------|----------------------|
| &D                            | Prints the current date. |

## Page-level Navigation/TOC (if applicable)

- Inserting Headers and Footers in XlsIO

## Cross References

See also:
- [IPageSetup]
- [Chart Worksheet]

<!-- tags: XlsIO, headers, footers, Microsoft support, formatting strings, font styles -->

```