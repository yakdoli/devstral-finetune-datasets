```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: calculate
page_number: 041
page_id: calculate#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:17Z
fidelity: lossless
-->

# Essential Calculate

## Content

### Figure 18: Form Showing Controls

\[image of a form with controls including buttons, text boxes, and a list box labeled Compute, Name, Value, and Register\]

### Adding Form Load Event Handler

3. **Double-click the form in the designer to add a Form.Load event handler. Add the code which is shown below to the project.**

```csharp
using Syncfusion.Calculate;

// ...

private CalcQuickBase cq;
private void Form1_Load(object sender, System.EventArgs e)
{
    cq = new CalcQuickBase();

    this.button1.Click += new EventHandler(button1_Click);
    this.button2.Click += new EventHandler(button2_Click);
}
private void button1_Click(object sender, EventArgs e)
{
    // Compute
    this.label3.Text =
    cq.ParseAndCompute(this.textBox1.Text);
}
private void button2_Click(object sender, EventArgs e)
{
    // Register name.
    string key = this.textBox2.Text;
}
```

## Page-level Navigation/TOC
- Figure 18: Form Showing Controls
- Adding Form Load Event Handler
- Code Examples

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Form Load event, C#, code examples] keywords: [Syncfusion, Calculate, Form Load, event handler, C# code, UI controls] -->
```