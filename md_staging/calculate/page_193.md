```markdown
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_193.jpeg
document_name: calculate
page_number: 193
page_id: calculate#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:39Z
fidelity: lossless
-->

# Essential Calculate

## Content

### MAXA Function

Where:
- `value1, value2, ...` are values for which you want to find the largest value.

#### Remarks

- You can specify arguments that are numbers, empty cells, logical values, or text representations of numbers. Arguments that are error values cause errors. If the calculation does not include text or logical values, use the MAX worksheet function instead.
- If an argument is an array or reference, only values in that array or reference are used. Empty cells and text values in the array or reference are ignored.
- Arguments that contain `True` evaluate as `1`; arguments that contain text or `False` evaluate as `0` (zero).
- If the arguments contain no values, `MAXA` returns `0` (zero).

### **4.7.98 MEDIAN**

#### Overview
Returns the median of the given numbers. The median is the number in the middle of a set of numbers; that is, half the numbers have values that are greater than the median and half have values that are less.

#### Syntax
```markdown
MEDIAN(number1, number2, ...)
```

Where:
- `number1, number2, ...` are numbers for which you want the median.

#### Remarks
- If there is an even number of numbers in the set, then `MEDIAN` calculates the average of the two numbers in the middle.

### **4.7.99 MID**

#### Overview
MID returns a text segment of a character string. The parameters specify the starting position and the number of characters.

---

<!-- tags: [syncfusion, winforms, calculate, median, maxa, mid, function] keywords: [syncfusion, winforms, calculate, essential calculate, median, max, maxa, mid, function, largest value, median value, text segment] -->
```