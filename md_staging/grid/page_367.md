```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_367.jpeg
document_name: grid
page_number: 367
page_id: grid#page_367
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:52Z
fidelity: lossless
-->

### TODAY

Returns the serial number of the current date. The serial number is the number of days since Jan 1, 1900.

#### Syntax

```markdown
TODAY( )
```

#### Remarks

- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1 and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900.

### Trim

The Trim function returns a text value with the leading and trailing spaces removed.

#### Syntax:

```markdown
Trim(text)
```

#### where:

text is the text value for which you want to remove the leading and the trailing spaces.

### TRIMMEAN

Returns the mean of the interior of a data set. TRIMMEAN calculates the mean taken by excluding a percentage of data points from the top and bottom tails of a data set.

#### Syntax

```markdown
TRIMMEAN(array, percent), where:
```

#### Remarks

- **array** is the array or range of values to trim and average.
- **percent** is the fractional number of data points to exclude from the calculation. For example, if percent = 0.2, 4 points are trimmed from a data set of 20 points (20 x 0.2): 2 from the top and 2 from the bottom of the set.

#### Additional Notes

- TRIMMEAN calculates the mean by removing the given percentage of data points from the top and bottom of the data set. This ensures that the mean is not affected by extreme outliers.
```