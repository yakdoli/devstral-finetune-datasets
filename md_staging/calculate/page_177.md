```html
<!-- 
  source: image
  domain: syncfusion-sdk
  task: pdf-ocr-to-markdown
  language: en (keep original; do not translate)
  source_filename: page_177.jpeg
  document_name: calculate
  page_number: 177
  page_id: calculate#page_177
  product: Syncfusion Winforms
  version: 11.4.0.26
  timestamp: 2025-08-09T03:09:31Z
  fidelity: lossless
  -->

# Essential Calculate

row\_index\_num is the row number in table\_array from which, the matching value will be returned. A row\_index\_num of 1 returns the first row value in table\_array, a row\_index\_num of 2 returns the second row value in table\_array and so on.

range\_lookup is a logical value that specifies whether you want HLOOKUP to find an exact match or an approximate match. If True or omitted, an approximate match is returned. In other words, if an exact match is not found, the next largest value that is less than the lookup\_value is returned. (This requires your lookup values to be sorted.) If False, HLOOKUP will find an exact match.

## 4.7.65 HOUR

Returns the hour of a time value. The hour is given as an integer, ranging from 0 (12:00 A.M.) to 23 (11:00 P.M.).

### Syntax

HOUR(serial\_number)

where:

(serial\_number is the time that contains the hour you want to find. Times may be entered as text strings within quotation marks (for example, "6:00 PM"), as decimal numbers (for example, 0.75, which represents 6:00 PM), or as results of other formulas or functions (for example, TIMEVALUE("6:00 PM")).

## 4.7.66 Hypgeomdist

The Hypgeomdist function returns the hypergeometric distribution.

### Syntax:

Hypgeomdist(sample, numberofsample, population, numberofpopulation)

where:

- sample is the number of successes in the sample.
- numberofsample is the size of the sample.
- population is the number of successes in the population.
- numberofpopulation is the population size.

<!-- tags: [syncfusion, winforms, calculate, hlookup, hour, hypgeomdist, formula] keywords: [row_index_num, range_lookup, exact match, approximate match, time, integer, hypergeometric distribution, sample, population, number of successes] -->
```