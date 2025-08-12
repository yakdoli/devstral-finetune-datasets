```html
<!-- source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_075.jpeg
document_name: calculate
page_number: 075
page_id: calculate#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:59Z
fidelity: lossless
-->

# Essential Calculate

```csharp
this.textBoxA,
this.textBoxB,
this.textBoxC,
this.textBoxD
});
```

```csharp
// 5) Allow the CalcQuickBase object to create dependency lists among the formula variables necessary
// for autocalculations and do the initial computations.
this.calculator.RefreshAllCalculations();
}
```

[VB]

```vb
' 1) Make sure controls have the names you want to use as variables. This can be done either
' from code as here or from the designer.
Me.textBoxA.Name = "A"
Me.textBoxB.Name = "B"
Me.textBoxC.Name = "C"
Me.textBoxD.Name = "D"

' 2) Initially populate the controls. Again, this can be done from the designer.
Me.textBoxA.Text = "12"
Me.textBoxB.Text = "3"
Me.textBoxC.Text = "= [A] + 2 * [B]"

' 3) Instantiate a CalcQuickBase object.
calculator = New CalcQuickBase

' 4) Register the controls used in calculations. The formula variables used are the Control.Name strings.
Me.calculator.RegisterControlArray(New Control() {Me.textBoxA, Me.textBoxB, Me.textBoxC, Me.textBoxD})

' 5) Allow the CalcQuickBase object to create dependency lists among the formula variables necessary for autocalculations and do the initial computations.
Me.calculator.RefreshAllCalculations()
```

## Explanation of the Numbered Steps in the Preceding Form_Load

1. Ensures that variable names are set as desired.
2. Sets the initial text into the first three text boxes.
3. Instantiates the CalcQuickBase instance.

<!-- tags: [Syncfusion Winforms, CalcQuickBase, Form_Load, Dependency Lists, Autocalculations] keywords: [variable names, initial text, text boxes, formula variables] -->
```