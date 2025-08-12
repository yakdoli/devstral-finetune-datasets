```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: calculate
page_number: 106
page_id: calculate#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:35Z
fidelity: lossless
-->

# Essential Calculate

## Using Function Library Formulas

Function Library formulas may be used as a stand-alone formula, and they can be incorporated into more complex formulas.

### Examples of Function Library Formulas

| Formula                                 | Comment                               |
|-----------------------------------------|---------------------------------------|
| = Sin(3.14159)                         | Returns the sine of 3.14159 radians |
| = 2 * Sin(3.14159) + Sqrt(2)           | Returns $2 \times$ sine of 3.14159 radians plus the square root of 2. |
| = 2 * Pi()                             | Returns $2 \times \pi$.             |

Some library functions may not have arguments but you must still include the parentheses to indicate that you are using a library function. For example, `= 2 * Pi()`, shows the proper use of the library function Pi.

## Function Library

The Function Library contains many functions from statistics, finance, and mathematics, along with other general-purpose functions. There are more than 150 entries in the library, and it is easy to add your own calculations.

The functions are discussed in the below topics.

### Add Function

#### Overview
CalcQuickBase relies on a `Calculate.Engine` object through an `ICalcData` interface to provide its calculation support. To add functions to the Formula Library available to your `CalcQuickBase` object, you need to add them to the `CalcQuickBase` underlying Engine object. You can access this engine object through the public "read-only" property, `CalcQuickBase.Engine`. Once you have a reference to the `CalcQuickBase`'s Engine object, you can add library functions by following the steps given below.

Adding a custom function to the Formula Library is a two-step process.
```