```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_225.jpeg
document_name: calculate
page_number: 225
page_id: calculate#page_225
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:12Z
fidelity: lossless
-->

# Essential Calculate

Calculates the standard deviation based on the entire population given as arguments, including text and logical values.

## Syntax

```markdown
STDEVPA(value1, value2, ...)
```

where:  
`value1, value2, ...` are values corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

## Remarks

- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).
- STDEVPA uses the following formula:

\[
\sqrt{\frac{\sum(x - \bar{x})^2}{n}}
\]

where:  
`x-bar` is the sample mean `AVERAGE(value1, value2, ...)`.  
`n` is the sample size.

---

## 4.7.156 STEYX

Returns the standard error of the predicted y-value for each x in the regression.

### Syntax

```markdown
STEYX(known_y's, known_x's)
```

where:  
`known_y's` is an array or range of dependent data points.  
`known_x's` is an array or range of independent data points.

---

<!-- tags: [STDEVPA, STEYX, standard deviation, standard error, regression, Syncfusion Winforms] keywords: [standard deviation, population, sample size, sample mean, arguments, text values, logical values, regression analysis, dependent data points, independent data points] -->
```