```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_168.jpeg
document_name: calculate
page_number: 168
page_id: calculate#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:55Z
fidelity: lossless
-->

# Essential Calculate

degrees_freedom1 is the numerator degrees of freedom.  
degrees_freedom2 is the denominator degrees of freedom.

## Remarks

- All arguments must be numeric.
- X must be >= 0.
- Both degrees_freedom1 and degrees_freedom2 must be >= 1 and < 10^10.
- FDIS T is calculated as follows:

**FDIST = P( F>x )**

where:

F is a random variable that has an F distribution with degrees_freedom1 and degrees_freedom2 degrees of freedom.

### 4.7.50 Find

The Find function finds a portion of a string from a particular text and returns the location of the string.

#### Syntax:

**Find(lookfor, lookin, start)**

where:
- lookfor is the text you want to search.
- lookin is the text in which you want to search.
- start specifies the starting position of the text from which you want to start searching in the text. This is optional.

### 4.7.51 FINV

The Finv function returns the inverse of the F probability distribution. If p = FDIST(x,...), then FINV(p,...) = x.

Using F distribution, you can compare the degree of variability for two data sets.

#### Syntax:

**FINV(probability,deg_freedom1,deg_freedom2)**
```markdown

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```