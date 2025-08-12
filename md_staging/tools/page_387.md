```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_387.jpeg
document_name: tools
page_number: 387
page_id: tools#page_387
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### TextBox Value

The behavior of the TextBox value can be controlled using the below properties.

| Calculatorcontrol Properties | Description |
|---|---|
| Culture | Specifies the culture that is used for formatting the currency display. |
| RepeatAssignAction | Indicates whether the assignment action (=) will repeat the previous action. Whenever the user assigns an action in the calculator at run time and clicks "=" button, the result will be displayed in the textbox area. If the user clicks the "=" button again, the assigned action will be repeated, with the existing result, only when RepeatAssignAction property is set to true. By default it is true. |
| UseUserOverride | Indicates whether the NumberFormatInfo used for formatting will use UseUserOverride parameter for CultureInfo. |

#### Code Examples (C#)

```csharp
this.calculatorControl1.Culture = new System.Globalization.CultureInfo("en-US");
this.calculatorControl1.RepeatAssignAction = true;
this.calculatorControl1.UseUserOverride = true;
```

#### Code Examples (VB.NET)

```vb
Me.calculatorControl1.Culture = New System.Globalization.CultureInfo("en-US")
Me.calculatorControl1.RepeatAssignAction = True
Me.calculatorControl1.UseUserOverride = True
```

### See Also

- [How to customize the calculator display text area to use NumberGroupSeparator?](How to customize the calculator display text area to use NumberGroupSeparator?)
- [3.5.2.3.3.2 Calculator Appearance](3.5.2.3.3.2 Calculator Appearance)

This section will walk you through the different appearance settings for the Calculator control.

---

<!-- tags: [calculator control, culture, number format, repeat assign action, use user override, winforms, syncfusion] keywords: [calculator control, customize display text, numbergroupseparator, appearance settings] -->
```