```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: calculate
page_number: 066
page_id: calculate#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:54Z
fidelity: lossless
-->

# Essential Calculate

```vb
Private calculator As CalcQuickBase = Nothing

Private Sub Form1_Load(sender As Object, e As EventArgs)
    Me.calculator = New CalcQuickBase()

    ' Form1_Load
End Sub

Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)
    Dim s As String = calculator.ParseAndCompute(Me.textBox1.Text)
    Me.label3.Text = s

    ' Button1_Click
End Sub
```

In this discussion, it is assumed that the formulas involved contain only constants and library references. On the other hand, you can use the `ParseAndCompute` method to explicitly parse and calculate formulas that use variables as well. But, before you do that, you need to know how to register variables and assign values to them.

### 4.1.1.1.2 Indexer Method using Variables

In this section, you will learn how to use variable names within formulas to represent particular values. A variable name must begin with an alphabetical character and can contain only letters and digits. It is not case-sensitive. To register a string as a variable name and set its value is a single step operation. You must simply index the `CalcQuickBase` object with the name and assign the value to it.

#### C#

```csharp
this.calculator["base"] = 3;
this.calculator["height"] = 2.5;
```

#### VB

```vb
Me.calculator("base") = 3
Me.calculator("height") = 2.5
```
```