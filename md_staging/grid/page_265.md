```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_265.jpeg
document_name: grid
page_number: 265
page_id: grid#page_265
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:06:24Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Remarks

- Numeric arguments are truncated to integers.
- A combination is any set or subset of items, regardless of their internal order. Combinations are distinct from permutations where the internal order is significant.
- The number of combinations is as follows, where number = n and number_chosen = k,

\[
\binom{n}{k} = \frac{P_{k,n}}{k!} = \frac{n!}{k!(n-k)!}
\]

where:

\[
P_{k,n} = \frac{n!}{(n-k)!}
\]

## 4.1.4.6.6.34 COMBINA

For a given number of items, the COMBINA function returns the number of combinations (with reputations).

### Syntax:

```markdown
COMBINA(number1, number2)
```

where:
- number1 is greater than equal to zero and greater than equal to number2
- number2 is greater than equal to zero.

### Remarks:

- **#NUM!** - occurs if either value is outside of its constraints
- **#VALUE!** - occurs if either value is non-numeric.

The following equation is used:

\[
\binom{N + M - 1}{N - 1}
\]

## 4.1.4.6.6.35 CONCATENATE

Joins several text strings into one text string.

### Syntax

<!-- tags: [Syncfusion Winforms, Essential Grid, COMBINA, CONCATENATE] keywords: [combinations, permutations, reputations, truncation] -->
```