```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: calculate
page_number: 039
page_id: calculate#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:40Z
fidelity: lossless
-->

## Essential Calculate

### Code Example

```vb
Public Overloads Shared Sub Main()
    Dim cq As New CalcQuickBase
    Dim s As String = Console.ReadLine()
    Do While s <> ""
        Dim val As String = cq.ParseAndCompute(s)
        Console.WriteLine("value= " + val)
        Console.WriteLine("")
        
        ' Blank line
        s = Console.ReadLine()
    Loop

    ' Main
End Sub

' Class1
End Class

' CalcQuickBaseTutorial
End Namespace
```

### Instructions

3. Once the code is entered, run the application by pressing F5. Then enter an expression such as `1+2` and press Enter. Enter additional algebraic combinations of constants and named functions from the Function Library like Sin, Cos, Sum, and Pi. Press Enter without entering anything to terminate the program. Below is a typical display of this.

#### Application Display

![Figure 16: Application Display](https://example.com/path/to/image)
*Figure 16: Application Display*

- **1+2**
- `value = 3`
- `(4 + 6) / (1 + 1)`
- `value = 5`
- `Cos< Pi<> / 2 >`
- `value = -3.49148336110938E-15`
- `Sin< Pi<> / 2 >`
- `value = 1`
- `Sum(1.1, 2.1, 3.2, 4.3)`
- `value = 10.7`

## Page-level Navigation/TOC

- Essential Calculate

### Related Links

- CalcQuickBaseTutorial

### RAG Annotations

<!-- tags: [product, module, control, api, version?] keywords: [calculate, code example, essential calculate, application display, algebraic combinations, numeric functions, sin, cos, sum, pi] -->
```