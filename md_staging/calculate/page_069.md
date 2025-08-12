```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: calculate
page_number: 069
page_id: calculate#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:51Z
fidelity: lossless
-->

# Essential Calculate

By default, CalcQuickBase does not try to track any dependencies among the variables you set. Thus, if you have a formula like

"=[TestValue]+2", the computed value of this formula will not change automatically if you modify your TestValue variable. To enable automatic recalculation of dependent variables, you must set the CalcQuickBase.AutoCalc property to True. Once this is done, the CalcQuickBase object (through its embedded CalcEngine object) maintains the required dependency information.

## AutoCalc in Practice

In practice, some additional work needs to be done. When a variable is auto-changed, nothing will actually happen until you try to use it. For example, assume that you have a series of text boxes on a form with some of the text boxes holding numerical values and some text boxes holding formulas that reference these values through variables that you have registered with a CalcQuickBase object.

### AutoCalc Example

![AutoCalc](https://your_image_url.com/AutoCalc.png)
**Figure 31: AutoCalc**

In the above screenshot, Text Box C is set to a formula that references the values from Text Box A and Text Box B. So, once the value in Text Box A or Text Box B changes, the value in Text Box C should also change.

<!-- tags: [CalcQuickBase, AutoCalc, dependency tracking, automatic recalculation, formulas, variables, text boxes] keywords: [CalcQuickBase, AutoCalc, AutoCalc property, dependency tracking, automatic recalculation, formulas, variables, text boxes, Syncfusion Winforms] -->
```