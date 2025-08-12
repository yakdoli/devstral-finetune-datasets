```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: calculate
page_number: 045
page_id: calculate#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:27Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Introduces a form with controls positioned for generating data.
- Explains how to implement calculation support using the ICalcData interface.
- Describes steps to add arbitrary calculation functionality to objects in WinForms.

## Content

### Form Setup

#### Figure: Form with Controls Positioned

![](Figure%2021:_Form_with_Controls_Positioned.png)

*Figure 21: Form with Controls Positioned*

You now have your basic form. Before leaving this form in the designer, double click both buttons to add the button handler code stubs to your Form1 code. You can add the code to these stubs later.

### Adding Arbitrary Calculation Support

In order to add arbitrary calculation support to an object, that object must implement the ICalcData interface. In this sample, you may want to add calculation support to a double array. To do so, you must create a wrapper class that accepts a double object in its constructor and then returns these double values in its indexer. In addition, you can extend the wrapper class by adding an additional row that holds the sum of the column values in the double array and by adding an additional column that holds the sum of the row values in the double array.

### Steps to Implement Calculation Support

1. **Add the Class**
   - **Right-click your project in the Solution Explorer window**.
   - **Select Add**.
   - **Select Add Class**.

## API Reference

- **ICalcData**: Interface that enables objects to support calculation functionality.
- **Wrapper Class**: Custom class required to implement the ICalcData interface.
- **Indexer**: Mechanism to return double values based on the object's constructor input.

## Code Examples

This section deliberately omits specific code examples to maintain focus on the generalized steps and implementation strategy described above.

## Cross References

- Refer to Syncfusion documentation on implementing custom interfaces for detailed examples.
- Check the Solution Explorer functionalities documentation for guidance on adding classes to your project.

<!-- tags: [syncfusion-sdk, winforms, calculate, icalcdata, wrapper-class, solution-explorer, form-design] keywords: [Essential Calculate, ICalcData interface, arbitrary calculation support, wrapper class, Solution Explorer] -->
```