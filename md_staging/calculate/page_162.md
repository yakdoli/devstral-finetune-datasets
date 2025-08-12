```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: calculate
page_number: 162
page_id: calculate#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:38Z
fidelity: lossless
-->

### Essential Calculate

#### Syntax

**DAYS360(start_date, end_date, method)**

where:

- `start_date` and `end_date` are the two dates between which you want to know the number of days. If `start_date` occurs after `end_date`, DAYS360 returns a negative number. Dates should be entered by using the DATE function or as results of other formulas or functions.
- `method` is a logical value that specifies whether to use the U.S. or European method in the calculation. If method is:
  - **False or omitted** – The calculation uses the U.S. (NASD) method. If the starting date is the 31st of a month, it becomes equal to the 30th of the same month. If the ending date is the 31st of a month and the starting date is earlier than the 30th of a month, the ending date becomes equal to the 1st of the next month; otherwise the ending date becomes equal to the 30th of the same month.
  - **True** – The calculation uses the European method. Starting dates and ending dates that occur on the 31st of a month become equal to the 30th of the same month.

### 4.7.38 DB

Returns the depreciation of an asset for a specified period using the fixed-declining balance method.

#### Syntax

**DB(cost, salvage, life, period, month)**

where:

- `cost` is the initial cost of the asset.
- `salvage` is the value at the end of the depreciation (sometimes called the salvage value of the asset).
- `life` is the number of periods over which the asset is being depreciated (sometimes called the useful life of the asset).
- `period` is the period for which you want to calculate the depreciation. Period must use the same units as life.
- `month` is the number of months in the first year. If `month` is omitted, it is assumed to be 12.

### Remarks

---

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```