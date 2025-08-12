```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_095.jpeg
document_name: DocIo
page_number: 095
page_id: DocIo#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:59Z
fidelity: lossless
-->

# Essential DocIO

Each section has its own header and footer which is set by using the HeadersFooters property. For more details, see Headers and Footers.

## Document Sections and Breaks

Document sections are divided by section breaks that define where the sections start. This is specified by using the `BreakCode` property.

### Types of Breaks

- **NewColumn**: section starts from a new column
- **NewPage**: section starts from a new page
- **EvenPage**: section starts on a new even page
- **OddPage**: section starts on a new odd page

### Breaks in MS Word

The following screenshot illustrates the breaks accessible through the `Insert` menu in the MS Word Break dialog box.

![Break Dialog Box](image_url)

- **Break types**:
  - Page break
  - Column break
  - Text wrapping break
- **Section break types**:
  - Next page
  - Continuous
  - Even page
  - Odd page

### Page Setup Options in MS Word

The following screenshot illustrates the various page setup options accessible through the `File` menu in MS Word.

<!-- tags: [DocIO, section breaks, headers footers, page setup, MS Word] keywords: [section, header, footer, break code, new column, new page, even page, odd page, insert menu, break dialog box, page break, column break, text wrapping break, next page, continuous, even page, odd page] -->
```