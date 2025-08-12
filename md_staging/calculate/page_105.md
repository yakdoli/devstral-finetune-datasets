```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: calculate
page_number: 105
page_id: calculate#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:21Z
fidelity: lossless
-->

# Essential Calculate

```csharp
calculator = New CalcQuickBase();

// 2) Populate your controls.
this.textBoxA.Text = "12";
this.textBoxB.Text = "3";
this.textBoxC.Text = "= [A] + 2 * [B]";

// Must enter formula names before turning on calculations.
// 3) Assigns formula object names.
calculator("A") = this.textBoxA.Text;
calculator("B") = this.textBoxB.Text;
calculator("C") = this.textBoxC.Text;
calculator("D") = this.textBoxD.Text;
```

### [VB]

```vb
' 1) Instantiates a CalcQuickBase object.
calculator = New CalcQuickBase()

' 2) Populate your controls.
Me.textBoxA.Text = "12"
Me.textBoxB.Text = "3"
Me.textBoxC.Text = "= [A] + 2 * [B]"

' Must enter formula names before turning on calculations.
' 3) Assigns formula object names.
calculator("A") = Me.textBoxA.Text
calculator("B") = Me.textBoxB.Text
calculator("C") = Me.textBoxC.Text
calculator("D") = Me.textBoxD.Text
```

## 4.4.3 Equal Sign, the Formula Character

To indicate that a particular string should be treated as a formula, you must start the string with a special character, `CalcEngine.FormulaCharacter`. This property is static (Shared in VB), so you can change the formula character within your code. Its default value is the equal sign, `=`.

In general, in order for Essential Calculate to recognize a string as containing a formula, the string is required to start with the `CalcEngine.FormulaCharacter`. There is one exception though, if you explicitly call a `CalcEngine` Parse method like `CalcEngine.ParseFormula` or `CalcEngine.ParseAndComputeFormula`, including the formula character as the first character in the passed string, it is optional.

<!-- tags: [Essential Calculate, FormulaCharacter, Syncfusion Winforms, ParseFormula, ParseAndComputeFormula, CalcEngine] keywords: [formula character, equal sign, CalcEngine, ParseFormula, ParseAndComputeFormula] -->
```