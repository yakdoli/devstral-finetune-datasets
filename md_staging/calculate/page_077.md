```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: calculate
page_number: 077
page_id: calculate#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:20Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- Exploring the "Working With CalcQuick Demo" feature.
- Highlighting features and methods available in the CalcQuickBase and ICalcData interfaces.

### Content

#### 2. Select Working With CalcQuick Demo from the samples provided and browse through the features.

![Figure 33: Working With CalcQuick Demo](#)

This section walks through the sample provided by "Working With CalcQuick Demo," which is part of the Essential Studio Reporting Edition for Windows Forms 2011 Vol 4. The sample includes various CalcQuick objects to perform tasks like manual and automatic calculations.

##### Features

###### Manual Calculations

```csharp
// calculator is a CalcQuick object...
Calculator calculator = new CalcQuick();

// Set the values of A, B, C, D
calculator["A"] = this.textbox1.Text;
calculator["B"] = this.textbox2.Text;
calculator["C"] = this.textbox3.Text;
calculator["D"] = this.textbox4.Text;

// Mark as dirty so any formulas will be recomputed
calculator.SetDirty();
```

#### 4.1.1.3.1 Methods

| Name         | Description                                             |
|--------------|---------------------------------------------------------|
| ResetKeys()  | Clears the keys used by the Calculate engine            |

#### 4.1.1.4 Summary

CalcQuickBase is the simplest way to add calculation support to your code. You can create an instance of it, and then just start by using it through either its `ParseAndCompute` method, or by indexing it with a variable name. You can use `CalcQuickBase` either in manual calculation mode or in an automatic calculation mode. Automatic calculations will require you to either handle certain events or use the `RegisterControlArray` method for Windows Forms text box and combo box controls.

### 4.1.2 General Calculation Support - ICalcData

#### Overview
- Discussing the general calculation support provided by the `ICalcData` interface.

---

<!-- tags: [syncfusion, winforms, essential calculate, calcquick, calcquickbase, icalcdata] keywords: [manual calculations, automatic calculations, registercontrolarray, resetkeys, iCalcData, Windows Forms, Syncfusion Winforms] -->
```