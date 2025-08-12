```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_107.jpeg
document_name: calculate
page_number: 107
page_id: calculate#page_107
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:26Z
fidelity: lossless
-->

# Essential Calculate

The first step is to write a method that actually does the calculation work for your custom function. The second step is to register this method with the CalcEngine. So, if your CalcEngine object is a member of a form, you can add your additional function methods to the form and then register these methods with the CalcEngine object after the object has been created, in Form_Load for example.

The above steps have been explained in detail in the following topics.

## 4.5.1.1 Step 1-Writing the Method

The method must have the signature specified by the delegate, Syncfusion.Calculate.CalcEngine.LibraryFunction. It accepts a string argument and returns a string value. So here is a minimal implementation. The sample found in \Windows\Calculate.Windows\Samples\2.0\ DataGridCalculator has code that adds a custom function.

### C#

```csharp
public string ComputeMymin(string args)
{
    // Computes someString using the values from args.
    return someString;
}
```

### VB

```vb
Public Function ComputeMymin(args As String) As String
    ' Computes someString using the values from args.
    Return someString
End Function
```

This is the only requirement on the method. You are free to use any kind of conventions with respect to passing arguments and within your implementation code. So, args may be a single entry like A1 or 153 or, it may be something more complex like A1:C15. It is up to your implementation code to parse args, use the information passed in, to compute the value and then return this value as a string. If you want your arguments to be standard items like cell references, numbers, other formulas, etc., `CalcEngine` exposes some parsing tools that you can use to minimize the amount of code you may need to write. But, you are not limited to what `CalcEngine` exposes, you are free to design and implement any argument conventions you want, as long as your method has the required signature.
```


<!-- tags: [product, module, control, api, version?] keywords: [custom function, CalcEngine, delegate, syncfusion, Windows Samples, DataGridCalculator, ComputeMymin, parsing, custom signature] -->
```