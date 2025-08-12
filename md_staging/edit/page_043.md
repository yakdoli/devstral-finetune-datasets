```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: edit
page_number: 043
page_id: edit#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:30Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Character Class Overview

| Metacharacter | Description |
|---------------|-------------|
| `\D` | Matches any non-digit. |
| `[.\w\s]` | Escaped built-in character classes such as `\w` and `\s` may be used in a character class. This example matches any period, word or whitespace character. |

## Quantifiers

Quantifiers add optional quantity data to a regular expression. A quantifier expression applies to the character, group, or character class that immediately precedes it. The .NET Framework regular expressions support minimal matching ("lazy") quantifiers.

The following table describes the metacharacters that affect the matching quantity.

### Quantifiers

| Quantifier | Description |
|------------|-------------|
| `*` | Specifies zero or more matches; for example, `\w*` or `(abc)*`. Same as `{0,}`. |
| `+` | Specifies one or more matches; for example, `\w+` or `(abc)+`. Same as `{1,}`. |
| `?` | Specifies zero or one matches; for example, `\w?` or `(abc)?`. Same as `{0,1}`. |
| `{n}` | Specifies exactly `n` matches; for example, `(pizza){2}`. |
| `{n,}` | Specifies at least `n` matches; for example, `(abc){2,}`. |
| `{n,m}` | Specifies at least `n`, but no more than `m`, matches. |

## Atomic Zero-Width Assertions

The metacharacters described in the following table do not cause the engine to advance through the string or consume characters. They simply cause a match to succeed or fail depending on the current position in the string. For instance, `^` specifies that the current position is at the beginning of a line or string. Thus, the regular expression `^\#region`, returns only those occurrences of the character string `\#region` that occur at the beginning of a line.

The following table lists other regular expression constructs.

<!-- tags: [syncfusion, winforms, regular expression, quantifiers, metacharacters, .NET Framework, lazy quantifiers] keywords: [metacharacters, quantifiers, regular expressions, zero-width assertions, character class, atomic] -->
```