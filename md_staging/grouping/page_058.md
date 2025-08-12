```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: grouping
page_number: 058
page_id: grouping#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:01:19Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Between: Checks if a date field value between the two values is listed in the right-hand operand.

## Content

### Between
Checks if a date field value between the two values is listed in the right-hand operand.

#### Example
[Date] between {2/25/2004, 3/2/2004} returns 1 for any record whose date field is greater than or equal to 2/25/2004 and less than 3/2/2004. To represent the current date, use the token TODAY. To represent DateTime.MinValue, leave the first argument empty. To represent DateTime.MaxValue, leave the second argument empty.

### Custom Functions
Essential Grouping lets you add custom functions to your code that can then be used in expressions.

#### Limitations on the Use of Custom Functions
- You cannot use custom functions in algebraic expressions.
- They must be used stand-alone in a simple expression that consists of only the function name and its argument list.
- The argument list can be any number of arguments separated by a delimiter.

## Code Examples

```csharp
// Example usage of custom functions
string result = CustomFunction("Argument1", "Argument2");
```

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Essential Grouping, Custom Functions, Between] keywords: [custom functions, algebraic expressions, date fields, DateTime.MinValue, DateTime.MaxValue, TODAY, stand-alone expressions, argument lists, operators] -->
``` 
