```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: calculate
page_number: 153
page_id: calculate#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:20Z
fidelity: lossless
-->

## Essential Calculate

### Choose Function

**Syntax:**
Choose(index, valuearray)

**Where,**
- **index** is to specify the index from where you want to retrieve the value.
- **valuearray** is the array of values from where you want to take the value.

### 4.7.21 Column

The `Column` function returns the column index of the provided column in range.

**Syntax:**
Column(range)

**Where,**
- **range** is to provide the column in range.

### 4.7.22 COMBIN

Returns the number of combinations for a given number of items. Use `COMBIN` to determine the total possible number of groups for a given number of items.

**Syntax:**
COMBIN(number, number_chosen)

**Where:**
- **number** is the number of items.
- **number_chosen** is the number of items in each combination.

### Remarks

- Numeric arguments are truncated to integers.
- A combination is any set or subset of items, regardless of their internal order. Combinations are distinct from permutations where the internal order is significant.
- The number of combinations is as follows, where number = n and number_chosen = k:

<!-- tags: [chooose, column, combinatorics] keywords: [index, valuearray, range, number, number_chosen, combinations, permutations] -->
```