```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_312.jpeg
document_name: XlsIO
page_number: 312
page_id: XlsIO#page_312
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:19Z
fidelity: lossless
-->

# Essential XlsIO

Page Breaks are dividers that break a worksheet into separate pages for printing. To print a worksheet with the exact number of pages that you want, you can adjust the page breaks in the worksheet before you print it. Excel inserts automatic page breaks, based on the paper size, margin settings, scaling options, and the positions of any manual page breaks that you insert, and it also allows to insert/remove breaks at preferred locations.

![Image showing the "Insert menu -> Page Break" option](#fig-112)

Figure 112: Insert menu -> Page Break

XLsIO provides support for inserting/removing Horizontal and Vertical page breaks in a worksheet by using the `IHPagebreak` and `IVPagebreak` interfaces.

**Note:** By default, page breaks are not shown in the Normal view. However, you can view them by inserting new page breaks.

```csharp
// Entering text into the cells.
sheet.Range["A1:M20"].Text = "PageBreak";

// Giving Horizontal Page Breaks.
sheet.HPageBreaks.Add(sheet.Range["A5"]);
sheet.HPageBreaks.Add(sheet.Range["A10"]);
sheet.HPageBreaks.Add(sheet.Range["A15"]);

// Giving Vertical Page Breaks.
sheet.VPageBreaks.Add(sheet.Range["B5"]);
sheet.VPageBreaks.Add(sheet.Range["E10"]);
sheet.VPageBreaks.Add(sheet.Range["K15"]);
```

<!-- tags: [product, module, control, api, version?] keywords: [xlsl.io, page breaks, automatic breaks, manual breaks, insert page break, horizontal page breaks, vertical page breaks, Normal view, IHPagebreak, IVPagebreak] -->
```