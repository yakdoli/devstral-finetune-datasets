```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: calculate
page_number: 034
page_id: calculate#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:31Z
fidelity: lossless
-->

# Essential Calculate

Now, you have created a WPF application (refer [Creating Platform Application](https://www.syncfusion.com/documentation/windowsforms/platform-application)). This section illustrates how to deploy Essential Calculate into this WPF application.

## Deploying Essential Calculate in a WPF Application

The following steps will guide you to deploy Essential Calculate:

1. Go to **Solution Explorer** of the application you have created -> right-click **Reference** folder and then click **Add References**.
2. Add the below mentioned assemblies as references in the application:
   - Syncfusion.Core.dll
   - Syncfusion.Compression.Base.dll
   - Syncfusion.Calculate.Base.dll

**Note:** There is no toolbox support for Calculate in WPF application.

3. Then create a **CalculateEngine**. The **CalcQuickBase** class is used to create a CalculateEngine.

**[C#]**

```csharp
// Create a new CalculateQuickBase. This object represents the CalculateEngine.
CalcQuickBase cq = new CalcQuickBase();
```

**[VB.NET]**

```vb
' Create a new CalculateQuickBase. This object represents the CalculateEngine.
Dim cq As CalcQuickBase
cq = New CalcQuickBase()
```

4. Use the **ParseAndCompute** method to perform calculations by using the CalculateEngine.

**[C#]**

```csharp
// Perform calculations by using Essential Calculate.
string formula = "if(20>10,\"BIG\",\"Small\")";
string value = cq.ParseAndCompute(formula);
```

**[VB.NET]**

```
...
```

## Code Examples

**[C#]**

```csharp
// Additional C# code examples can be added here.
```

**[VB.NET]**

```vb
' Additional VB.NET code examples can be added here.
```

## API Reference

### Methods

- **ParseAndCompute(string formula)**
  - **Returns:** string
  - **Description:** Parses and computes the given formula string.
  - **Parameters:**
    - **formula (string):** The formula to be parsed and computed.

<!-- tags: [essential-calculate, wpf-application, solution-explorer, toolbox-support, calculateengine, calcquickbase, parseandcompute] keywords: [essential calculate, wpf application, add references, calculate engine, calcquickbase, parse and compute, c#, vb.net] -->
```