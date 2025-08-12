```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_403.jpeg
document_name: tools
page_number: 403
page_id: tools#page_403
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Syncfusion.Windows.Forms.Tools.CalculatorPopupAlignment.Right;
    
    // Display the Calculator control.
    this.popupCalculator1.DisplayCalculator(Point.Empty);
    
    // Sets the size of the calculator
    this.popupCalculator1.Size = this.calculatorControl1.Size;
}
```

### [VB.NET]

```vb
Private popupCalculator1 As Syncfusion.Windows.Forms.Tools.PopupCalculator

Private Sub buttonAdv1_Click(ByVal sender As Object, ByVal e As EventArgs)
    ' Create the Popup Calculator.
    popupCalculator1 = New Syncfusion.Windows.Forms.Tools.PopupCalculator()
    
    ' The control that will act as the Popup's parent.
    Me.popupCalculator1.ParentControl = Me.button1
    
    ' Set the alignment.
    Me.popupCalculator1.PopupCalculatorAlignment = Syncfusion.Windows.Forms.Tools.CalculatorPopupAlignment.Right
    
    ' Display the Calculator control.
    Me.popupCalculator1.DisplayCalculator(Point.Empty)
    
    ' Sets the size of the calculator
    Me.popupCalculator1.Size = Me.calculatorControl1.Size
End Sub
```

<!-- tags: [SYNCFUSION, WINDOWSFORMS, TOOLS, POPUPCALCULATOR, 11.4.0.26] keywords: [popupcalculator, calculatorpopupalignment, calculatorcontrol, windowforms, syncfusiontools, vb.net, csharp] -->
```