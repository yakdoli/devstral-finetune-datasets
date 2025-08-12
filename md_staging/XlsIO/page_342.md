```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_342.jpeg
document_name: XlsIO
page_number: 342
page_id: XlsIO#page_342
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:41Z
fidelity: lossless
-->

## Essential XlsIO

### Note:

1. **In order to use the Essential XlsIO's Calculate engine, you have to add the following namespace:**
   - `using Syncfusion.Calculate`

2. **Do not add reference to Syncfusion.Calculate.Base. It will throw conflict errors as these are already integrated with XlsIO from Version 7.2.X.X.**

3. **Only the formulas that are supported by Calculate engine can be calculated at runtime using Essential XlsIO.**

### 4.4.3 Defined Names

#### Overview
- Named Ranges is a powerful feature in Excel, which makes it possible to assign a name to a group of cells.
- XlsIO has APIs for inserting new named ranges into workbooks, and also to read existing named ranges.
- Named Ranges are mainly used in formulae.

Named Ranges enables users with better readability, and at a glance we can predict what it is, and what we're adding up with the meaningful range names.

To create named ranges, open the **Insert menu**, point to **Name** and select **Define**. Names are created at workbook-level, by default, but you can create a sheet-level name, by entering the sheet name followed by an exclamation mark (!), followed by the name of the range. For instance, to create a named range "x" on Sheet1, open the **Insert menu**, point to **Name**, select **Define**, and enter the name as 'Sheet1!x'.

<!-- tags: [XlsIO, Syncfusion, Essential XlsIO, Calculate engine, Named Ranges, APIs, workbook-level, sheet-level names, range names] keywords: [use_syncfusion_calculate, support_calculate_engine, defined_names, named_ranges_usability, workbook_level_ranges, sheet_level_ranges, meaningful_names] -->
```