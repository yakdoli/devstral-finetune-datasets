```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_163.jpeg
document_name: calculate
page_number: 163
page_id: calculate#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:47Z
fidelity: lossless
-->

# Essential Calculate

- The fixed-declining balance method computes the depreciation at a fixed rate. DB uses the following formulas to calculate the depreciation for a period:
  - \((\text{cost} - \text{total depreciation from prior periods}) * \text{rate}\)
  - where:
    - \(\text{rate} = 1 - \left(\frac{\text{salvage}}{\text{cost}}\right)^{\left(\frac{1}{\text{life}}\right)}\), rounded to three decimal places

- Depreciation for the first and last periods is a special case. For the first period, DB uses this formula:
  - \(\text{cost} * \text{rate} * \text{month} / 12\)

- For the last period, DB uses this formula:
  - \((\text{cost} - \text{total depreciation from prior periods}) * \text{rate} * \left(12 - \text{month}\right) / 12\)

## 4.7.39 DDB

Returns the depreciation of an asset for a specified period using the double-declining balance method or some other method you specify.

### Syntax

DDB(cost, salvage, life, period, factor)

where:

- **cost** is the initial cost of the asset.
- **salvage** is the value at the end of the depreciation (sometimes called the salvage value of the asset).
- **life** is the number of periods over which the asset is being depreciated (sometimes called the useful life of the asset).
- **period** is the period for which you want to calculate the depreciation. Period must use the same units as life.
- **factor** is the rate at which the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method).

**Note:** All five arguments must be positive numbers.

### Remarks

---

© 2013 Syncfusion. All rights reserved. 163 | Page
```