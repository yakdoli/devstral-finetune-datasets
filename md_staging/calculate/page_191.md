```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_191.jpeg
document_name: calculate
page_number: 191
page_id: calculate#page_191
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:17Z
fidelity: lossless
-->

# Essential Calculate

- The equation for the lognormal cumulative distribution function is:
\[
\text{LOGNORMDIST}(x, \mu, \sigma) = \text{NORMSDIST}\left(\frac{\ln(x) - \mu}{\sigma}\right)
\]

### 4.7.94 Lower

The **Lower** function converts all characters in the specified text string to lowercase. Characters in the string that are not letters are not changed.

#### Syntax:
```text
Lower( text )
```

**where**,  
- **text** is the string you want to convert to lowercase.

### 4.7.95 Match

The **Match** function searches for a specified value in an array and returns the relative position of that item.

#### Syntax:
```text
Match( value, array, match_type )
```

**where**,  
- **this value** is the value you want to search in the array.
- **array** is a range of cells that contains the value you want to search.
- **match_type** is the type of match you want to perform.

**match_type** accepts the following values:

- **1**: The Match function will find the largest value that is less than or equal to the specified value. Ensure that the array is sorted in ascending order.
- **0**: The Match function will find the first value that is equal to the specified value. The array can be sorted in any order.
- **-1**: The Match function will find the smallest value that is greater than or equal to the specified value. Ensure that the array is sorted in descending order.

## API Reference (if applicable)
### WinForms-specific conventions
- Prefer C# samples when language is ambiguous; if VB is explicitly shown, keep both.
- Treat control names, namespaces, and types exactly.

### Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

<!-- tags: [Syncfusion Winforms, Lognormal cumulative distribution function, Lower function, Match function, Match function types] -->
```