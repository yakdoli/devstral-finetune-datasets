```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_326.jpeg
document_name: XlsIO
page_number: 326
page_id: XlsIO#page_326
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:33Z
fidelity: lossless
-->

## Content

### Examples of Formulas in XlsIO

```csharp
sheet.Range["A76"].Text = "MID(B6,A19,A19)";
sheet.Range["B76"].Formula = "MID(B6,A19,A19)";

sheet.Range["A77"].Text = "MID(\"Test string\",A19,A19*A19)";
sheet.Range["B77"].Formula = "MID(\"Test string\",A19,A19*A19)";

sheet.Range["A78"].Text = "MIDB(\"Test string\",A19,A19*A19)";
sheet.Range["B78"].Formula = "MIDB(\"Test string\",A19,A19*A19)";

sheet.Range["A79"].Text = "LOGINV(A8,A8,A8)";
sheet.Range["B79"].Formula = "LOGINV(A8,A8,A8)";

sheet.Range["A80"].Text = "LOOKUP(A3,{1,2,3,100})";
sheet.Range["B80"].Formula = "LOOKUP(A3,{1,2,3,100})";

sheet.Range["A81"].Text = "LOOKUP(A3,A3:A8)";
sheet.Range["B81"].Formula = "LOOKUP(A3,A3:A8)";

sheet.Range["A82"].Text = "LOOKUP(A3,A3:A8,A13:A18)";
sheet.Range["B82"].Formula = "LOOKUP(A3,A3:A8,A13:A18)";

sheet.Range["A83"].Text = "MATCH(A1,{1,2,3,4,5,100,200,300})";
sheet.Range["B83"].Formula = "MATCH(A1,{1,2,3,4,5,100,200,300})";

sheet.Range["A84"].Text = "MIRR(A9:A12,1,3)";
sheet.Range["B84"].Formula = "MIRR(A9:A12,1,3)";

sheet.Range["A85"].Text = "MIRR({-100,100,200,150},1,3)";
sheet.Range["B85"].Formula = "MIRR({-100,100,200,150},1,3)";

sheet.Range["A86"].Text = "MATCH(A3,A3:A8)";
sheet.Range["B86"].Formula = "MATCH(A3,A3:A8)";

sheet.Range["A87"].Text = "MDETERM({3,6,1;1,1,0;3,10,1})";
sheet.Range["B87"].Formula = "MDETERM({3,6,1;1,1,0;3,10,1})";

sheet.Range["A88"].Text = "MEDIAN({10,20,40,10,21})";
sheet.Range["B88"].Formula = "MEDIAN({10,20,40,10,21})";

sheet.Range["A89"].Text = "MIN({10,20,30;5,15,35;6,16,36})";
sheet.Range["B89"].Formula = "MIN({10,20,30;5,15,35;6,16,36})";

sheet.Range["A90"].Text = "MINA({10,20,30;5,15,35;6,16,36})";
sheet.Range["B90"].Formula = "MINA({10,20,30;5,15,35;6,16,36})";
```

## Cross References

- See also: [overviews in previous pages] for additional examples of XlsIO functionality.

<!-- tags: [XlsIO, formula, cell, range, string, number, calculation, cell reference, lookups, match, median, minimum, dataset] keywords: [range, text, formula, MID, Test string, lookup, match, median, minimum, MDETERM, MIRR] -->
```