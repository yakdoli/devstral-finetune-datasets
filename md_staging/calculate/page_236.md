```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_236.jpeg
document_name: calculate
page_number: 236
page_id: calculate#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:02Z
fidelity: lossless
-->

# Essential Calculate

## 4.7.178 Var

The Var function returns the variance of a population based on a sample of numbers.

### Syntax:
Var( number1, number2, … number_n )

Where:
number1, number2, … number_n are the sample numbers. 30 numbers can be entered.

## 4.7.179 VarA

The VarA function returns the variance of a population based on a sample of numbers, text, and logical values (ie: TRUE or FALSE).

### Syntax:
VarA( value1, value2, … value_n )

Where:
value1, value2, … value_n are the sample values. They can be numbers, text, and logical values. Values that are TRUE are evaluated as 1. Values that are FALSE or text values are evaluated as 0. 30 values can be entered.

## 4.7.180 VarP

The VarP function returns population variance of the listed values.

### Syntax:
VarP(listofvalues)

Where:
- listofvalues provides the range or values that contain the population.

## 4.7.181 VARPA

### Overview
- The Var function calculates the variance of a population based on a sample of numbers.
- The VarA function evaluates a population variance including logical and text values.
- The VarP function calculates the population variance of a list of values.

### Content
#### Variance Functions Summary
- **Var**: Computes the variance of a population using a sample of numbers.
- **VarA**: Computes the population variance including text and logical values where TRUE is treated as 1 and FALSE or text is treated as 0.
- **VarP**: Computes the population variance based on a complete population of values.
- **VARPA**: (Missing description in the image)

#### Usage Examples
```csharp
// Example for Var
double variance = Var(new double[] {10, 20, 30, 40});

// Example for VarA
double varAValue = VarA(new object[] {true, 10, "test", 20});

// Example for VarP
double varPValue = VarP(new double[] {5, 10, 15, 20});
```

### RAG Annotations
- Tags: [essential calculate, variance functions, sample variance, population variance, numerical computation, syncfusion winforms]
- Keywords: [var, vara, varp, varpa, population variance, numerical data, sample, logical values, text values, list of values]

```
