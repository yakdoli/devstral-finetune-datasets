```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_357.jpeg
document_name: grid
page_number: 357
page_id: grid#page_357
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:12:02Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### STDEV.S

**Syntax:**

```markdown
STDEV.S(number1,[number2],...)
```

- `number1` is the first number argument corresponding to a population.
- `Number2, ...` are the arguments 2 to 254 corresponding to a population.

**Remarks:**

- Arguments can either be numbers or names, arrays, or references that contain numbers.
- The standard deviation is calculated using the "n" method.
- Arguments that are error values or text that cannot be translated into numbers cause errors.

### STEYX

**Syntax:**

```markdown
STEYX(known_y's, known_x's)
```

**Remarks:**

- `known_y's` is an array or range of dependent data points.
- `known_x's` is an array or range of independent data points.

**The equation for the standard error of the predicted y is:**

\[
\sqrt{\frac{1}{(n-2)} \left[\sum(y-\overline{y})^2 - \frac{\left[\sum(x-\overline{x})(y-\overline{y})\right]^2}{\sum(x-\overline{x})^2}\right]}
\]

Where:
- x-bar and y-bar are the sample means AVERAGE(known_x's) and AVERAGE(known_y's).
- n is the sample size.

### SUBSTITUTE
```html

<!-- tags: [stdev.s, steyx, substitute, standard deviation, regression, dependent data, independent data] keywords: [stdev.s, steyx, substitute, population, sample, standard error, sdev, known_x's, known_y's, x-bar, y-bar] -->
```