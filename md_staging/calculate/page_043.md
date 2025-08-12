```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: calculate
page_number: 043
page_id: calculate#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:52Z
fidelity: lossless
-->

### Essential Calculate

```vb
Me.textBox3.Text)
    End If

' Button2_Click
End Sub
```

1. Run the sample by pressing F5. Then in the Name text box, enter Rate and in the Value text box, enter .07. Now press the Register button. Similarly, enter Amount in the Name text box, 15000 in the Value text box followed by pressing the Register button.
2. In the top text box, which is empty, enter the formula: `[Rate] * [Amount]`
3. Press the Compute button. You will then see a screen similar to the one below.

![](https://syncfusion.com/essentialcalculate/form1.png)
*Figure 19: Form Showing Two Variables Registered and a Sample Calculation*

The computed product, 1050, is displayed next to the Compute button.

By examining the code, notice that you register a name with a `CalcQuickBase` object by using its name as an indexer on the `CalcQuickBase` object and assign the desired value to this indexed object. Then to use the name within a formula, you enclose it within square brackets.

## 3.5.3 Adding Calculation Support to an Array Using ICalcData

```xml
© 2013 Syncfusion. All rights reserved.
```
<!-- tags: [calculation, calcquickbase, icalcdata, syncfusion, winforms] keywords: [formula, registration, indexer, computation, array] -->
```