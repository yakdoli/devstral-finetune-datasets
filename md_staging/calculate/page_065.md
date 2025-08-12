```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: calculate
page_number: 065
page_id: calculate#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:38Z
fidelity: lossless
-->

# Essential Calculate

## Content

### ParseAndCalculate Method

If you have an algebraic expression that just contains constants and function library methods, the most straightforward way of using Essential Calculate is to invoke its ParseAndCalculate method. Using CalcQuickBase makes this very simple. Consider, for example, the below form with a text box and a button on it. When you click the button, the computed value of the formula is displayed in the text box.

![Simple Expression](image.png)

*Figure 29: Simple Expression*

The code that provides this functionality is very straightforward. Add a reference to **Syncfusion.Calculate** in your project. Then instantiate a **CalcQuickBase** object, and invoke its **ParseAndCalculate** method from the button handler. Now you can type a formula in the text box and click the button to get the computed value. The following code illustrates this.

```csharp
[C#]
using Syncfusion.Calculate;

private CalcQuickBase calculator = null;

private void Form1_Load(object sender, EventArgs e)
{
    this.calculator = new CalcQuickBase();
}

private void button1_Click(object sender, EventArgs e)
{
    string s = calculator.ParseAndCompute(this.textBox1.Text);
    this.label3.Text = s;
}
```

```vb
[VB]
Imports Syncfusion.Calculate
```

## API Reference (if applicable)

No specific API details are provided in the current content.

## Code Examples (multi-language supported)

The provided code demonstrates how to use the **ParseAndCalculate** method in C# and VB.NET to compute an expression entered into a text box.

## Page-level Navigation/TOC (if applicable)

No page-level table of contents is present in this section.

## Cross References

No cross references are provided in the current content.

## RAG Annotations

<!-- tags: [Syncfusion, Calculate, ParseAndCalculate, CalcQuickBase, algebraic expressions, text box, computed value] keywords: [ParseAndCalculate, CalcQuickBase, algebraic expression, text box, computed value, Syncfusion, Calculate] -->
```