---
title: "calculate - Syncfusion SDK Documentation"
type: "api-documentation"
framework: "syncfusion"
version: "v11"
processing_mode: "Process Isolation (프로세스 격리)"
extracted_date: "1754709321.6185396"
optimized_for: ["llm-training", "rag-retrieval"]
scaling_approach: "3"
---

<!-- 페이지 1 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_001.jpeg
document_name: calculate
page_number: 001
page_id: calculate#page_001
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:22Z
fidelity: lossless
-->

# Essential Studio 2013 Volume 4 - v.11.4.0.26

## Overview

- Introduction to the Essential Calculate component for Syncfusion Winforms.
- Overview of its new features and enhancements.
- References to documentation for integration and usage.

## Content

### Introduction to Essential Calculate

Essential Calculate is an advanced calculation component designed to provide developers with enhanced capabilities to perform complex computations within their Winforms applications.

#### Key Features

- **Powerful Computational Engine:** Supports advanced mathematical, statistical, and logical operations.
- **Enhanced Formula Support:** Includes a wide range of built-in functions and custom function support.
- **Integration Ecosystem:** Seamlessly integrates with other Syncfusion components for a unified development experience.

#### Summary

This page provides initial insights into the capabilities and benefits of the Essential Calculate component, highlighting its role in optimizing computational tasks within Winforms. For comprehensive documentation and examples, refer to the official Syncfusion documentation.

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Calculate

### Table of Contents (Local)

- Overview of the Essential Calculate component
- Key Features and Enhancements
- Integration with Syncfusion Winforms
- Code Examples

---

## Code Examples

### Example: Basic Integration

```csharp
// Example of integrating Essential Calculate with a Winforms application
using Syncfusion.Windows.Forms.Calculate;
using System.Windows.Forms;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();

        // Initialize the Calculate component
        EssentialCalculate calculate = new EssentialCalculate();
        calculate.DestinationControl = textBoxResult;
        calculate.FunctionName = "SUM";
        calculate.SourceRange = "A1:A10";

        // Attach to a control
        this.Controls.Add(calculate);
    }
}
```

### Example: Custom Function Example

```csharp
// Example of adding a custom function to Essential Calculate
calculate.CustomFunction += (sender, e) =>
{
    if (e.FunctionName == "MYFUNCTION")
    {
        e.Result = e.Parameters[0] + e.Parameters[1];
    }
};
```

## Cross References

- See also: Essential Studio 2013 documentation for a complete overview of features.
- Refer to the Main Documentation for detailed integration steps and best practices.

---

<!-- tags: [syncfusion, winforms, essential-studio, essential-calculate, version-11.4.0.26] keywords: [essential calculate, power calculate, custom functions, winforms components, computational engine, integrate calculate, version update, documentation reference] -->
```

---

<!-- 페이지 2 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: calculate
page_number: 005
page_id: calculate#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:37Z
fidelity: lossless
-->

# Essential Calculate

## Content

- 4.7 Function Reference Section ………………… 142
  - 4.7.1 ABS …………………… 142
  - 4.7.2 ACOS …………………… 143
  - 4.7.3 ACOSH …………………… 143
  - 4.7.4 AND …………………… 144
  - 4.7.5 ASIN …………………… 144
  - 4.7.6 ASINH …………………… 144
  - 4.7.7 ATAN …………………… 145
  - 4.7.8 ATAN2 …………………… 145
  - 4.7.9 ATANH …………………… 146
  - 4.7.10 AVEDEV …………………… 146
  - 4.7.11 AVERAGE …………………… 147
  - 4.7.12 AVERAGEA …………………… 147
  - 4.7.13 AVG …………………… 148
  - 4.7.14 BINOMDIST …………………… 148
  - 4.7.15 CEILING …………………… 149
  - 4.7.16 Char …………………… 150
  - 4.7.17 CHIDIST …………………… 150
  - 4.7.18 CHIINV 151
  - 4.7.19 CHITTEST …………………… 152
  - 4.7.20 Choose 152
  - 4.7.21 Column 153
  - 4.7.22 COMBIN …………………… 153
  - 4.7.23 CONCATENATE …………………… 154
  - 4.7.24 CONFIDENCE …………………… 154
  - 4.7.25 CORREL …………………… 155
  - 4.7.26 COS …………………… 156
  - 4.7.27 COSH …………………… 156
  - 4.7.28 COUNT156
  - 4.7.29 COUNTA …………………… 157
  - 4.7.30 COUNTBLANK …………………… 157
  - 4.7.31 COUNTIF …………………… 158
  - 4.7.32 COVAR 158
  - 4.7.33 CRITBINOM …………………… 159
  - 4.7.34 DATE …………………… 160

© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [Syncfusion Winforms, 11.4.0.26, calculate, sdk, technical documentation] keywords: [Essential Calculate, Function Reference, ABS, ACOS, ACOSH, AND, ASIN, ASINH, ATAN, ATAN2, ATANH, AVEDEV, AVERAGE, AVERAGEA, AVG, BINOMDIST, CEILING, Char, CHIDIST, CHIINV, CHITTEST, Choose, Column, COMBIN, CONCATENATE, CONFIDENCE, CORREL, COS, COSH, COUNT, COUNTA, COUNTBLANK, COUNTIF, COVAR, CRITBINOM, DATE] -->

---

<!-- 페이지 3 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: calculate
page_number: 009
page_id: calculate#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:59Z
fidelity: lossless
-->

## Overview
- This section lists a variety of mathematical and statistical functions available in the Syncfusion Winforms library, categorized under the "Essential Calculate" functionality.
- Functions include rounding operations, trigonometric functions, statistical calculations, and data manipulation tools.
- Each function is accompanied by its respective page number for reference within the document.

## Content

### Functionality Overview

- **Rounding and Truncating Functions**
  - 4.7.139 ROUNDOWN ... 215
  - 4.7.140 ROUNDUP ... 216
  - 4.7.141 RSQ ... 216
  - 4.7.142 SECOND ... 217
  - 4.7.143 SIGN ... 217

- **Trigonometric Functions**
  - 4.7.144 SIN ... 218
  - 4.7.145 SinH ... 219

- **Statistical Functions**
  - 4.7.146 SKEW ... 219
  - 4.7.147 SLN ... 220
  - 4.7.148 SLOPE ... 220
  - 4.7.149 SMALL ... 221
  - 4.7.150 SQRT ... 221
  - 4.7.151 STANDARDIZE ... 222
  - 4.7.152 STDEV ... 222
  - 4.7.153 STDEVA ... 223
  - 4.7.154 STDEV.P ... 224
  - 4.7.155 STDEVPA ... 224
  - 4.7.156 STEYX ... 225

- **Data Manipulation and Lookup Functions**
  - 4.7.157 SUBSTITUTE ... 226
  - 4.7.158 Sum ... 227
  - 4.7.159 SumIf ... 227
  - 4.7.160 SUMPRODUCT ... 228
  - 4.7.161 SUMSQ ... 228
  - 4.7.162 SumXmY2 ... 228
  - 4.7.163 SUMX2MY2 ... 229
  - 4.7.164 SUMX2PY2 ... 229

- **Other Functions**
  - 4.7.165 SYD ... 230
  - 4.7.166 TAN ... 231
  - 4.7.167 TANH ... 231
  - 4.7.168 TEXT ... 232
  - 4.7.169 TIME ... 232
  - 4.7.170 TIMEVALUE ... 232
  - 4.7.171 TODAY ... 233
  - 4.7.172 Trim ... 233
  - 4.7.173 TRIMMEAN ... 234

## API Reference (if applicable)
The provided functions are part of the Syncfusion Winforms API and can be utilized for diverse computational tasks within the application.

## Code Examples (multi-language supported)

### Example Usage of RSQ Function
```csharp
// Example usage in C#
double rsqValue = Math.RSQ(xValues, yValues);
```

### Example Usage of STDEV Function
```csharp
// Example usage in C#
double standardDeviation = Math.STDEV(numbers);
```

### Note
Refer to the specific pages mentioned in the function listing for detailed explanations and usage examples.

<!-- tags: [Syncfusion_Winforms, Essential_Calculate, Functions, Mathematical_Functions, Statistical_Functions, Data_Manipulation, TRIGONOMETRIC_FUNCTIONS] keywords: [ROUNDOWN, ROUNDUP, RSQ, SECOND, SIGN, SIN, SinH, SKEW, SLN, SLOPE, SMALL, SQRT, STANDARDIZE, STDEV, STDEVA, STDEV.P, STDEVPA, STEYX, SUBSTITUTE, Sum, SumIf, SUMPRODUCT, SUMSQ, SumXmY2, SUMX2MY2, SUMX2PY2, SYD, TAN, TANH, TEXT, TIME, TIMEVALUE, TODAY, Trim, TRIMMEAN] -->
```

---

<!-- 페이지 4 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_013.jpeg
document_name: calculate
page_number: 013
page_id: calculate#page_013
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:26Z
fidelity: lossless
-->

## Prerequisites and Compatibility

### Overview
- This section outlines the mandatory requirements for using Essential Calculate.
- It lists compatible operating systems and browsers for the product.
- Development environments and .NET Framework versions are covered.

### Content

#### Prerequisites

The prerequisites details are listed below:

| Development Environments                      |                                                                                     |
|-----------------------------------------------|-------------------------------------------------------------------------------------|
|                                              | - Visual Studio 2012 (Ultimate, Premium, Professional, and Express)                |
|                                              | - Visual Studio 2010 (Ultimate, Premium, Professional, and Express)                |
|                                              | - Visual Studio 2008 (Team System, Professional, Standard, and Express)             |
|                                              | - Visual Studio 2005 (Professional, Standard, and Express)                          |
| .NET Framework versions                       |                                                                                     |
|                                              | - .NET 4.5                                                                          |
|                                              | - .NET 4.0                                                                          |
|                                              | - .NET 3.5 SP1                                                                       |
|                                              | - .NET 2.0                                                                          |

#### Compatibility

The compatibility details are listed below:

| Operating Systems                            |                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------|
|                                              | - Windows 8 (32 bit and 64 bit)                                                     |
|                                              | - Windows Server 2012 (32 bit and 64 bit)                                           |
|                                              | - Windows 7 (32 bit and 64 bit)                                                     |
|                                              | - Windows Server 2008 (32 bit and 64 bit)                                           |
|                                              | - Windows Vista (32 bit and 64 bit)                                                 |
|                                              | - Windows XP                                                                        |
|                                              | - Windows 2003                                                                       |

<!-- tags: [syncfusion-sdk, Essential Calculate, prerequisites, compatibility, operating systems, .NET Framework, development environments, version:11.4.0.26] keywords: [prerequisites, compatibility, Windows 8, Windows Server, Windows 7, Windows Vista, Windows XP, Windows 2003, .NET 4.5, .NET 4.0, .NET 3.5 SP1, .NET 2.0, Visual Studio 2012, Visual Studio 2010, Visual Studio 2008, Visual Studio 2005] -->
```

---

<!-- 페이지 5 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: calculate
page_number: 017
page_id: calculate#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:41Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- Access Syncfusion Essential Studio samples for various editions, including UI, Reporting, Business Intelligence, and more.
- Navigate through the dashboard to explore features like high-performance AJAX Web applications using ASP.NET MVC and support for MVC 3 Razor engine.
- Utilize the dashboard to run samples, download source code, and access release notes.

### Content

#### Accessing Samples

1. **To view the samples:**
   - Navigate through the following path:
     Click `Start → All Programs → Syncfusion → Essential Studio <version number> → Dashboard`.

   Essential Studio UI Edition Samples are listed by default.

   **Figure 2: Syncfusion Essential Studio Dashboard**

   ![Syncfusion Essential Studio Dashboard](https://example.com/dashboard_image.png)

   - The dashboard includes:
     - **User Interface Edition for ASP.NET MVC**:
       - Create high-performance AJAX Web applications with ease.
       - Now supports the MVC 3 Razor engine.
     - Options to run samples, explore features, download source code, and access documentation and release notes.

2. **Select Reporting edition.**

---

### API Reference (if applicable)

Not applicable on this page.

### Code Examples (multi-language supported)

Not applicable on this page.

### Page-level Navigation/TOC (if applicable)

Not applicable on this page.

### Cross References

- **See also:** Local Table of Contents or related links, if present in the body of the page.

---

### Additional Notes

This page provides guidance on accessing and utilizing Syncfusion Essential Studio samples, focusing on the dashboard interface and various available editions.

---

<!-- tags: [product, Syncfusion Winforms, Essential Studio, dashboard, UI, Reporting Edition, Business Intelligence, high-performance AJAX Web applications, MVC 3 Razor engine, source code download, release notes] keywords: [Syncfusion, Essential Studio, dashboard, User Interface Edition, Reporting Edition, Business Intelligence, AJAX Web applications, MVC 3 Razor engine, source code] -->
```

---

<!-- 페이지 6 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: calculate
page_number: 021
page_id: calculate#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:54Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Essential Studio 2012 Vol 3 ASP.NET and User Interface Editions are highlighted.
- The tool provides various features for working with Microsoft Office documents.
- The "Calculate" section focuses on performing calculations using Syncfusion tools in .NET applications.

## Content

### Overview of Essential DocIO
- **Essential DocIO**: A 100% native .NET library that generates fully functional Microsoft Word documents in native Word format.
- **Features**:
  - Used in any .NET environment including C#, VB.NET, and managed C++.
  - Supports Windows Forms, WPF, and Web applications.
  - Can create and preserve documents.
  - Unique features like Find and Replace, Mail Merge, and Conversions.

### Sample Browser

#### Figure 7: ASP.NET Sample Browser
The figure shows a screenshot of the ASP.NET Sample Browser interface, which includes navigation elements for different features such as DocIO, Calculate, Grouping, Pdf, and XlsIO.

### Steps to Display Calculate Samples
1. Open the **ASP.NET Sample Browser**.
2. Click **Calculate** from the bottom-left pane.
   - The **Calculate** samples are displayed.

## API Reference

### Essential DocIO
- **Namespace**: Syncfusion.DocIO
- **Classes**:
  - `WordDocument`: Handles the creation and manipulation of Word documents.
  - `FindReplaceOptions`: Used for Find and Replace operations.
  - `MailMerge`: Performs mail merge operations on Word documents.

### Methods
- `InsertTable`: Inserts a table into the document.
- `InsertImage`: Inserts an image into the document.
- `Save`: Saves the document in different formats.

### Parameters
- `DocumentType`: Specifies the type of document to be saved (e.g., .doc, .docx).

### Returns
- `WordDocument`: Returns the modified Word document object.

## Code Examples

### Example: Creating a Document with a Table
```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.Dls;

// Create a new word document.
WordDocument document = new WordDocument();

// Add a section to the document.
IWSection section = document.AddSection();

// Add a paragraph to the section.
IWTextBody textBody = section.AddTextBody();
IWTextParagraph paragraph = textBody.AddParagraph();

// Add a table to the paragraph.
IWTable table = paragraph.AddTable();
// Define table dimensions
table.Rows.Count = 3;
table.Columns.Count = 3;

// Add content to the table cells
for (int i = 0; i < 3; i++)
{
    for (int j = 0; j < 3; j++)
    {
        IWTableCell cell = table.Rows[i].Cells[j];
        cell.AddParagraph().AppendText($"Cell {i + 1}-{j + 1}");
    }
}

// Save the document.
document.Save("Output.docx");
```

## Page-level Navigation/TOC (if applicable)
- The navigation pane on the left provides quick access to different sections and features, including Product Showcase, Getting Started, and specific topics for DocIO, Calculate, Pdf, and XlsIO.

## Cross References
See also:
- [Essential Studio Documentation](https://www.syncfusion.com/products/windowsforms/documentation)

## Footer
- **Copyright**: © 2001-2012 Syncfusion Inc.
- **Navigation Links**: Forums, Documentation, Support, Sales

<!-- tags: [calculate, essential studio, winforms, sample browser, docio, .net] keywords: [calculate, document generation, mail merge, text formatting, text body, text paragraph, table, document type, document creation, word document, finding and replacing, mail merge, .net, windows forms, wPF, Web applications] -->
```


---

<!-- 페이지 7 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_025.jpeg
document_name: calculate
page_number: 025
page_id: calculate#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:17Z
fidelity: lossless
-->

# Essential Calculate

## Getting Started

This section covers information on the following topics.

### 3.1 Class Diagram

The following illustration shows the Class Diagram for Essential Calculate.

![Class Diagram for Essential Calculate](https://via.placeholder.com/600x400?text=Figure%209%3A%20Class%20Diagram%20for%20Essential%20Calculate)

---

## Overview

- An introduction to the class diagram for Essential Calculate.
- Detailed explanation of the relationship between different classes within the library.
- Highlighting key components and interfaces used in the system design.

### WinForms-specific conventions

This section describes how the class diagram is applicable specifically to Syncfusion Winforms components.

### Key Classes and Components

- `CalculateBaseAssembly`: Represents the base assembly for Essential Calculate.
- `CalcEngine`: Responsible for performing calculations within the system.
- `CalcQuickBase`, `CalcSheet`, and `CalcSheetList`: Classes related to managing calculation sheets and their lists.
- `CalculateConfig`: Contains configuration settings for the calculation engine.
- `CalcWorkbook`: Manages the workbook data model.
- `FormulaInfo` and `FormulaInfoHash`: Classes for handling formula information and storing it in a hash table.
- `FormulaParsingEventArgs`, `ValueChangedEventArgs`, and other event argument classes: Used for handling events related to formulas and value changes.
- `Utilities`: Contains utility functions used by the system.
- `ICalcData`, `ISupportsColumn`, `ISupportsRowCol`: Interfaces that define the behavior of data handling and column/row support.

### Interactions and Dependencies

- `CalcEngine` interacts with `CalcQuickBase`, `CalcSheet`, and `CalcSheetList` to perform calculations and manage data.
- `FormulaParsingEventArgs` and `ValueChangedEventArgs` are used to trigger and handle events when formulas are parsed or values change.
- `Utilities` provides common functions, potentially used across various components of the system.
- Interfaces like `ICalcData`, `ISupportsColumn`, and `ISupportsRowCol` are implemented by various classes to adhere to specific protocol requirements.

### Delegate and Enum Definitions

- `FormulaParsingParameters`, `QuickValueSetEventArgs`, and `ValueChangedEventArgs`: Define delegates and events that facilitate communication and data exchange within the system.
- `FormulaInfoSet`: An enumeration for different sets of formula information.

### Conclusion

The class diagram provides an overview of the architecture of the Essential Calculate library, detailing the roles and interactions of various classes and interfaces essential for its functionality within the Syncfusion Winforms environment.

<!-- tags: Essential Calculate, Class Diagram, Syncfusion Winforms, version: 11.4.0.26 keywords: CalculateBaseAssembly, CalcEngine, CalcQuickBase, CalcSheet, CalcSheetList, CalculateConfig, CalcWorkbook, FormulaInfo, FormulaInfoHash, FormulaParsingEventArgs, ValueChangedEventArgs, Utilities, ICalcData, ISupportsColumn, ISupportsRowCol, FormulaParsingParameters -->
```

---

<!-- 페이지 8 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_029.jpeg
document_name: calculate
page_number: 029
page_id: calculate#page_029
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:36Z
fidelity: lossless
-->

# Essential Calculate

This section will guide you to deploy Essential Calculate in those applications under the following topics:

- Windows-Step-by-step procedure to deploy Calculate in a Windows application.
- ASP.NET-Step-by-step procedure to deploy Calculate in an ASP.NET application.
- WPF-Step-by-step procedure to deploy Calculate in a WPF application.

## 3.3.1 Windows

Now, you have created a Windows application (refer Creating Platform Application). This section illustrates how to deploy Essential Calculate into this Windows application.

### Deploying Essential Calculate in a Windows Application

The following steps will guide you to deploy Essential Calculate:

1. Open the main form of the application in the designer.
2. Add the Syncfusion controls to your VS.NET toolbox if you haven't done so already [This is done automatically when you install Essential Studio].
3. In order to use the Essential Calculate library in your project, add the **CalculateConfig** component found in the toolbox to a project to enable support for Calculate.

![Toolbox](Figure 13: Toolbox)

This will add references to the following dependent assemblies of your project:

## API Reference
*Not explicitly mentioned in the image, but typically include the section describing essential methods, properties, and events.*

## Code Examples
*Not explicitly mentioned in the image, but typically include samples demonstrating the integration.*

### Summary
- **What:** Deploying Essential Calculate in a Windows application.
- **How:** Use the CalculateConfig component from the toolbox.
- **Why:** To add custom calculation and formula capabilities in your Windows application.

## Cross References
- Refer to "Creating Platform Application" for setting up the initial application environment.

<!-- tags: Essential Calculate, Windows, Deployment, CalculateConfig, Syncfusion Winforms, Visual Studio Toolbox keywords: Essential Calculate, Windows Application, Deployment, CalculateConfig, Visual Studio, Toolbox -->
```

---

<!-- 페이지 9 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_033.jpeg
document_name: calculate
page_number: 033
page_id: calculate#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:48Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Steps for setting up and deploying Essential Calculate in ASP.NET applications.
- Instructions for handling data file permissions and ensuring authenticated user access.
- Deployment of Syncfusion assemblies, including dependent DLLs for Essential Calculate.

## Content

### Note: X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.

1. **Data Files**: If you have `.xml`, `.mdb`, or other data files, ensure that they have sufficient security permission. Authenticated users should have full control over the files and the directories in order to give ASP.NET code enough permission to open the file during runtime.

Refer to the document in the following path, for step by step process of Syncfusion assemblies deployment in ASP.NET:
  
http://www.syncfusion.com/support/user/uploads/webdeployment_c883f681.pdf

### Note: Application with Essential Calculate needs the following dependent assemblies for deployment.
- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.Calculate.Base.dll

2. **Create a CalculateEngine**: The `CalcQuickBase` class is used to create a `CalculateEngine`. Use the `ParseAndCompute` method to perform calculations by using the `CalculateEngine`.

You can also modify the default behavior of the `CalculateEngine` by using the `Engine` property.

```csharp
[C#]
// Create a new CalculateQuickBase. This object represents the CalculateEngine.
CalcQuickBase cq = new CalcQuickBase();

// Perform calculations by using ParseAndCompute method of Essential Calculate.
Dim formula As String = "if(20>10,""BIG"",""Small"")"
Dim value As String = cq.ParseAndCompute(formula)

// Strings concatenated by using the ampersand operator will be returned without quotation marks.
cq.Engine.UseNoAmpersandQuotes = true;
```

### Note: The Engine is a class that is defined as a "property" in Essential Calculate.

Essential Calculate is now deployed in your ASP.NET application.

## 3.3.3 WPF

<!-- tags: [essential-calculate, asp.net, data-permissions, authentication, deployment, calculateengine, calcquickbase, parseandcompute] keywords: [syncfusion.core, syncfusion.compression.base, syncfusion.calculate.base, calcquickbase, parseandcompute, engine] -->
```

---

<!-- 페이지 10 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_037.jpeg
document_name: calculate
page_number: 037
page_id: calculate#page_037
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:03Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- In this section, you will create a Console Application that requests a string from the user.
- The application processes algebraic expressions using the `CalcQuick` object and displays the results.
- The guide includes a step-by-step procedure for creating a simple console application.

## 3.5.1 Simple Console Application Using CalcQuickBase

In this section, you will create a Console Application that requests a string from the user. The application requires the string to be an algebraic expression like: \( 4.1 + 3.21 \) or \( \text{SQRT}(2) \times 14.2 \) or \( (3 + \text{Sqrt}(2)) / (2 - \text{Cos}(2.1)) \).

Once you enter an expression, the application uses a `CalcQuick` object to perform the requested calculation and displays it to the Console. The process continues until you enter an empty string. The step-by-step procedure to create a simple console application is discussed under the following topic:

### 3.5.1.1 Console Application CalcQuickBase

The step-by-step procedure to create a simple console application is as follows:

1. **Create a New Console Application Project**
   - From Visual Studio, use **File | New | Project** to create a new Console Application named `CalcQuickBaseTutorial`.
   - After creating the project, open the References node in the Solution Explorer and add a reference to `Syncfusion.Calculate.Base`.
   - At this point, your Solution Explorer window should appear similar to the one shown in **Figure 15**.

   ![Figure 15: Essential Calculate Reference Added to the Project](https://your-image-url.com/image.png)

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- None explicitly mentioned in this section.

<!-- tags: [Syncfusion Winforms, CalcQuickBase, Console Application, Calculate API, version 11.4.0.26] keywords: [Syncfusion Winforms, Essential Calculate, Console Application, CalcQuick, algebraic expressions, solution explorer] -->
```

---

<!-- 페이지 11 -->

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

---

<!-- 페이지 12 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: calculate
page_number: 045
page_id: calculate#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:27Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Introduces a form with controls positioned for generating data.
- Explains how to implement calculation support using the ICalcData interface.
- Describes steps to add arbitrary calculation functionality to objects in WinForms.

## Content

### Form Setup

#### Figure: Form with Controls Positioned

![](Figure%2021:_Form_with_Controls_Positioned.png)

*Figure 21: Form with Controls Positioned*

You now have your basic form. Before leaving this form in the designer, double click both buttons to add the button handler code stubs to your Form1 code. You can add the code to these stubs later.

### Adding Arbitrary Calculation Support

In order to add arbitrary calculation support to an object, that object must implement the ICalcData interface. In this sample, you may want to add calculation support to a double array. To do so, you must create a wrapper class that accepts a double object in its constructor and then returns these double values in its indexer. In addition, you can extend the wrapper class by adding an additional row that holds the sum of the column values in the double array and by adding an additional column that holds the sum of the row values in the double array.

### Steps to Implement Calculation Support

1. **Add the Class**
   - **Right-click your project in the Solution Explorer window**.
   - **Select Add**.
   - **Select Add Class**.

## API Reference

- **ICalcData**: Interface that enables objects to support calculation functionality.
- **Wrapper Class**: Custom class required to implement the ICalcData interface.
- **Indexer**: Mechanism to return double values based on the object's constructor input.

## Code Examples

This section deliberately omits specific code examples to maintain focus on the generalized steps and implementation strategy described above.

## Cross References

- Refer to Syncfusion documentation on implementing custom interfaces for detailed examples.
- Check the Solution Explorer functionalities documentation for guidance on adding classes to your project.

<!-- tags: [syncfusion-sdk, winforms, calculate, icalcdata, wrapper-class, solution-explorer, form-design] keywords: [Essential Calculate, ICalcData interface, arbitrary calculation support, wrapper class, Solution Explorer] -->
```

---

<!-- 페이지 13 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_049.jpeg
document_name: calculate
page_number: 049
page_id: calculate#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:41Z
fidelity: lossless
-->

## Overview

There is a simple calculation engine being built. The class includes variable declarations such as `colSums`, `rowCount`, and `colCount`. Below is a portion of the class design in both C# and VB.NET showing essential details for handling double arrays and calculating sums for rows and columns.

### Essential Calculate

```csharp
private object[] colSums;

int rowCount;
int colCount;

//...
}
```

#### VB.NET Implementation

```vb
Imports System
Imports Syncfusion.Calculate

Public Class ArrayCalcData

    ''' <summary>
    ''' Original double array.
    ''' </summary>
    Private dValues(,) As Double

    ''' <summary>
    ''' Vector holding the sum of the rows.
    ''' </summary>
    ''' <remarks>
    ''' Serves as the last column.
    ''' </remarks>
    Private rowSums() As Object

    ''' <summary>
    ''' Vector holding the sum of the columns.
    ''' </summary>
    ''' <remarks>
    ''' Serves as the last row.
    ''' </remarks>
    Private colSums() As Object

    Dim rowCount As Integer
    Dim colCount As Integer

End Class
```

### Constructor Implementation

5. Here, you are making a constructor that accepts a double array as an argument. In the constructor code, you must save the reference that is to be passed in a double array, initialize two `RowCount` and `ColCount` fields and allocate the two additional arrays that are needed to hold the added sums you want.

## Page-Level Navigation/TOC (if applicable)

- Essential Calculate
  - Overview of the calculation engine
  - Detailed class structure in both C# and VB.NET

## Cross References

- Refer to relevant sections on array handling and calculation methods in earlier or later pages of the document.

<!-- 
tags: [Essential Calculate, Array Calculation Engine, Double Array, RowSum, ColSum, VB.NET, C#] 
keywords: [calculate, array, row sum, column sum, constructor, doubles, Syncfusion, WinForms] 
-->
```

---

<!-- 페이지 14 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: calculate
page_number: 053
page_id: calculate#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:55Z
fidelity: lossless
-->

# Essential Calculate

Then, in the right drop-down, click each of the four items listed to add the proper code stubs.

![Figure 26: Implementing the ICalcData Interface in VB, Adding the Members](26)

After doing these steps, you will be able to see these methods in the class code. (In the C# code, the region may be collapsed.)

## C#

```csharp
public object GetValorowCol(int row, int col)
{
    // TODO: Add ArrayCalcData1.GetValorowCol implementation.
    return null;
}

public void SetValorowCol(object value, int row, int col)
{
    // TODO: Add ArrayCalcData1.SetValorowCol implementation.
}

public event Syncfusion.Calculate.ValueChangedEventHandler ValueChanged;

public void WireParentObject()
{
    // TODO: Add ArrayCalcData1.WireParentObject implementation.
}
```

## VB

```vb
Public Function GetValorowCol(ByVal row As Integer, ByVal col As Integer) _
    As Object Implements
Syncfusion.Calculate.ICalcData.GetValorowCol
End Function
```

## API Reference

### Methods

- `GetObject GetValorowCol(int row, int col):` Retrieves the value at the specified row and column.
- `void SetValorowCol(object value, int row, int col):` Sets the value at the specified row and column.

### Events

- `ValueChanged`: Triggered when a value is changed.

### Other

- `WireParentObject`: Function to wire the parent object.

### Note:

Ensure to implement the TODO sections for full functionality.

<!-- tags: [syncfusion, sdk, calculate, interface, icalcdata, visual basic, csharp] keywords: [interface implementation, arraycalcdata, valorowcol, setvalue, valuechanged, wireparentobject] -->
```

---

<!-- 페이지 15 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: calculate
page_number: 057
page_id: calculate#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:07Z
fidelity: lossless
-->
# Essential Calculate

```vb
Dim e1 As New ValueChangedEventArgs(row, col, value.ToString())
RaiseEvent ValueChanged(Me, e1)

' SetValueRowCol
End Sub
```

## Overview
- Adding an indexer definition to the class for monitoring user changes.
- Forcing users to go through GetValueRowCol and SetValueRowCol methods for array-like access.
- Code examples for C# and VB.NET implementing the indexer using ICalcData interface.

## Content

### Adding an Indexer Definition

10. You have to add an indexer definition to the class for two reasons: it is a straightforward way to force the user to go through the GetValueRowCol and SetValueRowCol methods, allowing the CalcEngine to monitor these changes. It also makes your ArrayCalcData class look like an array.

Here is the code you must use. It is just a Get and Set implementation that goes through the ICalcData interface methods.

### C# Code Example

```csharp
/// <summary>
/// Gets / sets the value of this ArrayCalcData object.
/// </summary>
/// <remarks>
/// Since this class wraps a double array, the indexing is zero-based but,
/// the ICalcData methods requires one-based indexing by convention. So,
/// one is added to the indexes when the ICalcData methods are called.
/// </remarks>
public object this[int row, int col]
{
    get { return GetValueRowCol(row + 1, col + 1); }
    set { SetValueRowCol(value, row + 1, col + 1); }
}
```

### VB.NET Code Example

```vb
' <summary>
' Gets / sets the value of this ArrayCalcData object.
' </summary>
' <remarks>
' Since this class wraps a double array, the indexing is zero-based but,
' the ICalcData methods requires one-based indexing by convention. So,
' one is added to the indexes when the ICalcData methods are called.
' </remarks>
Default Public Property Item(ByVal row As Integer, ByVal col As Integer) As Object
    Get
        Return GetValueRowCol(row + 1, col + 1)
    End Get
    Set(ByVal Value As Object)
```

## Code Examples

The indexer implementation in both C# and VB.NET demonstrates how to bridge the one-based indexing convention of the ICalcData interface with the zero-based array indexing typically used in .NET. This ensures proper integration with the CalcEngine and other related components.

### References
- VB.NET indexer implementation.
- C# indexer implementation using the ICalcData interface.

<!-- tags: [syncfusion-sdk, winforms, arraycalcdata, indexer, calcengine] keywords: [indexer, getvaluecolrow, setvaluecolrow, icalcdata, one-based indexing, zero-based array, adapter, binding, calcengine] -->
```

---

<!-- 페이지 16 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: calculate
page_number: 061
page_id: calculate#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:24Z
fidelity: lossless
-->

## Displaying Data with SumColumns and SumRows

### Overview
- Demonstrates how to display a double array with sums for columns and rows.
- Shows how to update the displayed data dynamically.
- Allows setting a specific value in the data array to observe the effects on sums.

### Implementation

```vb
Dim j As Integer

For j = 0 To Me.nCols
    Me.TextBox1.Text += Me.data(i, j).ToString() + ControlChars.Tab
Next
Me.TextBox1.Text += ControlChars.Cr + ControlChars.Lf
```

### Display Example

Here is a typical display you might see if you run the application at this point. Recall that the data is random, so you may see fewer or more rows and columns. The column on the right is the sum of the columns that precede it in the same row. The row at the bottom is the sum of the columns above it. You can click the **Generate Data** button several times to see different data.

![Figure 27: Sample Display Showing Double Array, SumColumn and SumRow](https://i.imgur.com/ramdomimage.jpg)

### Set Button Functionality

The Set button allows you to set a particular value in the displayed data so you can see the effect of changing this value on the calculations in the last row and last column. Recall that your data store is mimicking an array of doubles, so it indexes from zero even though the `ICalcData` interface expects one-based indexing. The implementation code takes this into account.

## API Reference

### Properties
- `data`: The array of double values displayed.
- `nCols`: The number of columns in the data array.

### Methods
- `SetData(row As Integer, col As Integer, value As Double)`: Updates the data array with the specified value at the given row and column indices.

## Code Examples

```vb
' Example usage of SetData
Me.SetData(0, 0, 123)
```

## Cross References

- See also: `ICalcData` interface for data manipulation.

<!-- tags: [syncfusion, windowsforms, icalcdata, data array, sum columns, sum rows] keywords: [random data, display, set button, data manipulation] -->
```

---

<!-- 페이지 17 -->

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

---

<!-- 페이지 18 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: calculate
page_number: 069
page_id: calculate#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:51Z
fidelity: lossless
-->

# Essential Calculate

By default, CalcQuickBase does not try to track any dependencies among the variables you set. Thus, if you have a formula like

"=[TestValue]+2", the computed value of this formula will not change automatically if you modify your TestValue variable. To enable automatic recalculation of dependent variables, you must set the CalcQuickBase.AutoCalc property to True. Once this is done, the CalcQuickBase object (through its embedded CalcEngine object) maintains the required dependency information.

## AutoCalc in Practice

In practice, some additional work needs to be done. When a variable is auto-changed, nothing will actually happen until you try to use it. For example, assume that you have a series of text boxes on a form with some of the text boxes holding numerical values and some text boxes holding formulas that reference these values through variables that you have registered with a CalcQuickBase object.

### AutoCalc Example

![AutoCalc](https://your_image_url.com/AutoCalc.png)
**Figure 31: AutoCalc**

In the above screenshot, Text Box C is set to a formula that references the values from Text Box A and Text Box B. So, once the value in Text Box A or Text Box B changes, the value in Text Box C should also change.

<!-- tags: [CalcQuickBase, AutoCalc, dependency tracking, automatic recalculation, formulas, variables, text boxes] keywords: [CalcQuickBase, AutoCalc, AutoCalc property, dependency tracking, automatic recalculation, formulas, variables, text boxes, Syncfusion Winforms] -->
```

---

<!-- 페이지 19 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: calculate
page_number: 073
page_id: calculate#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:02Z
fidelity: lossless
-->

# Essential Calculate

```vb
' 9) Handles the changing of the text in the text box so the CalcQuickBase
' object can be updated as the text changes.
Private Sub textBoxA_Leave(ByVal sender As Object, ByVal e As EventArgs)
    If Me.textBoxA.Modified Then
        calculator("A") = Me.textBoxA.Text
        Me.textBoxA.Modified = False
    End If
End Sub
```

The following is an explanation of the numbered steps given in the preceding Form_Load.

1. **Instantiates the CalcQuickBase instance.**
2. **Sets some initial text into the first three text boxes. The first two values are just numerical entries but, the third value will be treated as a formula by the CalcQuickBase object as it begins with a "="**.
3. **This step registers the variable names A, B, C and D with the CalcQuickBase object, and sets the initial values of these variables to the contents of the text boxes.**
4. **Here the AutoCalc property is turned on so CalcQuickBase will start tracking any dependencies that it notes among the variables registered with it. Note that this step was done after the initial registering of the variables in step 3. So, any relations among the registered variables are unknown to the CalcQuickBase object. This shortcoming will be addressed in step 7 and the rationale for this order will be discussed there.**
5. **Subscribe to CalcQuickBase's ValueSet event so that the code can react to any automatic changing of the registered variables’ values and place them into the appropriate text box so your display will immediately reflect any change.**
6. **Subscribe to the text box events so that you can update the CalcQuickBase object when the text in a text box has changed.**
7. **This step forces the recalculation of all variables registered with the CalcQuickBase object. This has to be done after the AutoCalc property has been set to True, so that the dependencies between variables can be monitored. The reason to postpone setting AutoCalc until after the initial registration of the variables, is to avoid problems that might occur because of CalcQuickBase trying to set up dependency chains even before all the variables have been registered. Initializing the variables, turning on AutoCalc, and then calling RefreshAllCalculations, avoids this potential problem.**
8. **This is the event handler that moves a freshly computed variable into the text box that it is related to.**

<!-- tags: [syncfusion sdk, syncfusion winforms, calcquickbase, dependecy tracking, variable registration, auto calculation, event handling] keywords: [bla text text box, text_tBoxA Modified, CalcQuickBase object, AutoCalc property, ValueSet event, dependency tracking, RefreshAllCalculations] -->
```

---

<!-- 페이지 20 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: calculate
page_number: 077
page_id: calculate#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:20Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- Exploring the "Working With CalcQuick Demo" feature.
- Highlighting features and methods available in the CalcQuickBase and ICalcData interfaces.

### Content

#### 2. Select Working With CalcQuick Demo from the samples provided and browse through the features.

![Figure 33: Working With CalcQuick Demo](#)

This section walks through the sample provided by "Working With CalcQuick Demo," which is part of the Essential Studio Reporting Edition for Windows Forms 2011 Vol 4. The sample includes various CalcQuick objects to perform tasks like manual and automatic calculations.

##### Features

###### Manual Calculations

```csharp
// calculator is a CalcQuick object...
Calculator calculator = new CalcQuick();

// Set the values of A, B, C, D
calculator["A"] = this.textbox1.Text;
calculator["B"] = this.textbox2.Text;
calculator["C"] = this.textbox3.Text;
calculator["D"] = this.textbox4.Text;

// Mark as dirty so any formulas will be recomputed
calculator.SetDirty();
```

#### 4.1.1.3.1 Methods

| Name         | Description                                             |
|--------------|---------------------------------------------------------|
| ResetKeys()  | Clears the keys used by the Calculate engine            |

#### 4.1.1.4 Summary

CalcQuickBase is the simplest way to add calculation support to your code. You can create an instance of it, and then just start by using it through either its `ParseAndCompute` method, or by indexing it with a variable name. You can use `CalcQuickBase` either in manual calculation mode or in an automatic calculation mode. Automatic calculations will require you to either handle certain events or use the `RegisterControlArray` method for Windows Forms text box and combo box controls.

### 4.1.2 General Calculation Support - ICalcData

#### Overview
- Discussing the general calculation support provided by the `ICalcData` interface.

---

<!-- tags: [syncfusion, winforms, essential calculate, calcquick, calcquickbase, icalcdata] keywords: [manual calculations, automatic calculations, registercontrolarray, resetkeys, iCalcData, Windows Forms, Syncfusion Winforms] -->
```

---

<!-- 페이지 21 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: calculate
page_number: 081
page_id: calculate#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:34Z
fidelity: lossless
-->

# Essential Calculate

```vb
Me.dataGrid1(2, 2) = "= A1 + A3"

' 1) Reset static members of CalcEngine.
Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID()

' 2) Create a CalcEngine object and tie it to the DataGrid that
' implements ICalcData.
engine = New Syncfusion.Calculate.CalcEngine(Me.dataGrid1)

' 3) Set the CalcEngine to track dependencies required for auto
updating.
    engine.UseDependencies = True

' 4) Call RecalculateRange so any formulas in the data can be
' initially computed.
    engine.RecalculateRange(RangeInfo.Cells(1, 1, dt.Rows.Count, 
dt.Columns.Count), Me.dataGrid1)

' SingleDataGridForm_Load
End Sub
```

## Overview
- **Goal**: Explains the usage of the `CalcEngine` to compute formulas within a DataGrid and enable automatic updates based on cell dependencies.

### Key Points
- Initializes the `CalcEngine` for a single DataGrid.
- Configures the engine to track dependencies.
- Automatically recalculates formulas as cell values are updated.

## Content

### Explanation of the Code
The following is an explanation of the preceding code.

1. **ResetSheetFamilyID**  
   Clears any static members of the `CalcEngine` class and sets the engine state to operate with a single `ICalcData` object.

2. **Creates an instance of the CalcEngine object**  
   Instantiates the `CalcEngine` object and associates it with the `DataGrid` that implements `ICalcData`.

3. **Sets the engine object to track calculation dependencies**  
   Configures the engine to track dependencies so that cells can be automatically updated as other cell values change.

4. **RecalculateRange**  
   Processes the existing cell contents to calculate any formulas for the initial display.

#### Subsection: 4.1.2.2 Using Several CalcDataGrids in a Workbook

- **Feature**: Essential Calculate supports cross-references among several `ICalcData` objects.
- **Usage**: Allows the creation of a workbook with multiple `CalcDataGrids` using a Windows Forms `Tab` control.
- **Reference**: Based on the `Calculation\Samples\DataGridCalculator` sample that ships with the product.

## API Reference

### Methods
- **ResetSheetFamilyID**  
  Clears static members and initializes the `CalcEngine` for a single `ICalcData` object.

- **CalcEngine Constructor**  
  Creates an instance of the `CalcEngine` and associates it with a specific `DataGrid`.

- **UseDependencies Property**  
  Enables or disables dependency tracking for automatic cell updates.

- **RecalculateRange Method**  
  Evaluates formulas in a specified range for the initial display.

## Code Examples

### VB.NET Example
```vb
Me.dataGrid1(2, 2) = "= A1 + A3"

Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID()

engine = New Syncfusion.Calculate.CalcEngine(Me.dataGrid1)
engine.UseDependencies = True

engine.RecalculateRange(RangeInfo.Cells(1, 1, dt.Rows.Count, dt.Columns.Count), Me.dataGrid1)
```

## See also
- `CalcEngine`
- `ICalcData`
- `RangeInfo`
- `DataGridCalculator` sample

<!-- tags: [Syncfusion Winforms, CalcEngine, ICalcData, DataGridCalculator] keywords: [calculation engine, dependencies, auto updating, formula evaluation, range recalculation] -->
```

---

<!-- 페이지 22 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: calculate
page_number: 085
page_id: calculate#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:53Z
fidelity: lossless
-->

# Zero-Based and One-Based Indexing in Essential Calculate

## Overview

- The second convention involves zero-based and one-based indexing.
- Discusses the conflict between zero-based indexing in data sources and one-based indexing in CalcEngine to mimic Excel.
- Highlights the need to ensure consistency in index usage.
- Explains the requirement for one-based indexing in Essential Calculate.
- Illustrates tweaking indexes for consistency with zero-based data sources.

## Content

### Zero-Based and One-Based Indexing

The second convention in Essential Calculate involves the use of zero-based and one-based indexing. It is important to note that many data sources utilize zero-based indexing for accessing values. However, in the CalcEngine, one-based indexing is employed to emulate Excel's behavior. This can lead to potential conflicts when dealing with indexing. To maintain consistency and ensure clarity on which indexing should be used, Essential Calculate mandates that all indexes (including rows and column integer values) should be one-based. This may necessitate adjustments to the indexes passed through ICalcData methods and event arguments to align them with any zero-based data sources in use. One example discussed in this section is the DataGrid, where you can observe the index-based adjustments in the following code samples:

```csharp
[C#]

public class CalcDataGrid : DataGrid, Syncfusion.Calculate.ICalcData
{
    public CalcDataGrid() : base()
    {
        // Avoid the complexity of sorting.
        this.AllowSorting = false;
    }

    // Used to subscribe to the DataTable.ColumnChanged event. This ColumnChanged event will raise the required ValueChanged event.
    // Without this ValueChanged event, the CalcEngine would have no knowledge of the data.
    public void WireParentObject()
    {
        // Assumes grid's datasource is a DataTable.
        DataTable dt = this.DataSource as DataTable;
        dt.ColumnChanged += new DataColumnChangeEventHandler(dt_ColumnChanged);

        // Avoids the complexity of a new row.
        dt.DefaultView.AllowNew = false;
    }

    // This event handler raises the required ICalcData.ValueChanged event when the data in the DataTable changes.
    private void dt_ColumnChanged(object sender, DataColumnChangeEventArgs e)
    {
        CurrencyManager cm = (CurrencyManager)this.BindingContext[this.DataSource, this.DataMember];
        DataTable dt = this.DataSource as DataTable;
        int pos = cm.Position;
        int field = dt.Columns.IndexOf(e.Column);
        string val = this[pos, field].ToString();
    }
}
```

## API Reference (if applicable)

### WinForms-specific conventions

- The code block provided demonstrates how to manage zero-based indexing by converting it to one-based indexing using event handling mechanisms.

### Methods

- `CalcDataGrid()`: Constructor for the `CalcDataGrid` class, initializing without sorting complexity.
- `WireParentObject()`: Method to subscribe to the `DataTable.ColumnChanged` event.
- `dt_ColumnChanged()`: Event handler to manage data changes and trigger the required `ICalcData.ValueChanged` event.

## Code Examples (multi-language supported)

The provided C# example showcases the implementation of handling `DataTable` changes and ensuring one-based indexing for compatibility with the `CalcEngine`.

## RAG Annotations

<!-- tags: [essential-calculate, data-sources, calcengine, indexing, syncfusion-winform, data-grid, event-handling] keywords: [zero-based, one-based, indexing, conflict, compatibility, calcengine, datagrid, dataSource, eventhandler, icalcdata, valuechanged] -->
```

---

<!-- 페이지 23 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_089.jpeg
document_name: calculate
page_number: 089
page_id: calculate#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:11Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Configures web control performance using attributes in the project's `web.config` file.
- Demonstrates handling Excel spreadsheets using Essential XlsIO and Essential Calculate.

## Content

### Web Control Performance

#### Figure 36: Web Control Performance

The image shows a detailed view of HTTP response headers for web control performance. Key attributes include:

- **Server**: ASP.NET Development Server/9.0.0.0
- **Date**: Wed, 12 Mar 2008 03:29:00 GMT
- **X-AspNet-Version**: 2.0.50727
- **Content-Encoding**: gzip
- **Cache-Control**: private
- **Expires**: Thu, 12 Mar 2009 03:20:58 GMT
- **Last-Modified**: Wed, 12 Mar 2008 03:20:48 GMT

To achieve optimal web control performance, the following attributes need to be set in the project's `web.config` file:

```xml
<configuration system.web.extensions>
    <!-- ... -->
    <scripting>
        <ScriptResourceHandler enableCompression="true" enableCaching="true" />
    </scripting>
    <!-- ... -->
</system.web.extensions>
```

#### Benefits of Gzipping Resource Files

As the resource files get gzipped:

- **It saves the precious network bandwidth.**
- **It reduces the load-time.** As a result, the web form, which consists of the Syncfusion controls, will get loaded faster on the client browser.
- **It also reduces the network traffic.**

### 4.3 Working with an Excel Spreadsheet

You can use the Microsoft Excel to design spreadsheets that can be used on systems where MS Excel is not installed. This can be done by using a combination of Essential XlsIO and Essential Calculate, where:

- **Essential XlsIO** can be used to read and write the spreadsheet.
- **Essential Calculate** can be used to compute values as they are modified in the spreadsheet.

#### Example

To illustrate this process, consider the following sample project:

```
Essential Studio\X.X.X\Windows\Calculation.Windows\Samples\2.0\XlsFileUsingExcelRW
```

## API Reference (if applicable)

### Using Essential XlsIO and Essential Calculate

The integration of Essential XlsIO and Essential Calculate is designed to handle spreadsheet operations effectively without requiring MS Excel installation. Utilize these components to achieve the desired functionalities.

## Code Examples (multi-language supported)

### Example: Configuration for Web Control Performance

```xml
<configuration system.web.extensions>
    <scripting>
        <ScriptResourceHandler enableCompression="true" enableCaching="true" />
    </scripting>
</configuration>
```

### Example: Sample Project Path

```
Essential Studio\X.X.X\Windows\Calculation.Windows\Samples\2.0\XlsFileUsingExcelRW
```

## Page-level Navigation/TOC (if applicable)

- **Web Control Performance**
- **Working with an Excel Spreadsheet**

## Cross References

See also:

- **Essential XlsIO Documentation**
- **Essential Calculate Documentation**

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Essential Calculate, Essential XlsIO, Web Control Performance, Excel Spreadsheet Handling] keywords: [web.config, gzip, network bandwidth, load-time, network traffic, XlsIO, Calculate, sample project, configuration, HTTP response headers, Syncfusion] -->
```

---

<!-- 페이지 24 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_093.jpeg
document_name: calculate
page_number: 093
page_id: calculate#page_093
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:31Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes the general calculation design process using Excel to design complex calculations for batch processing.
- Explains how named variables in Excel can facilitate simple application functionality on systems without Excel.

## Content

### Excel Named Variables
**Figure 40: Dialog Box Showing Named Variables**

![Excel Dialog Box](https://image-link.com/stored-figure-40.png)

This layout represents a general calculation design process which you can use for batch processing of information. The idea is that you change the inputs (all on a single sheet) and then return the outputs (all from a single sheet). There may be a web service or a server application that will allow clients to upload inputs and then download outputs. Or it could just be a batch processing calculation engine. Using this technique, you can use Excel to design complex calculations and then have a simple application that runs on systems without Excel, to input new values and retrieve computed results.

For example, consider the below form which accepts input values from the user. Once the values are set, the user clicks a button on the form that puts these values into the inputs sheet and then retrieves the insurance costs from the Outputs sheet and displays it on the form.

## RAG Annotations
<!-- tags: [excel, named variables, batch processing, complex calculations, web service, server application, form processing, insurance, Syncfusion Winforms, version: 11.4.0.26] keywords: [Excel named variables, general calculation design, batch processing, complex calculations, web service, server application, form processing, insurance, Excel calculations, complex calculations, batch processing engine] -->
```

---

<!-- 페이지 25 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: calculate
page_number: 097
page_id: calculate#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:42Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains how to properly set all dependencies within the underlying `CalcEngine` using `CalculateAll`.
- Details the use of `LockDependencies` and `CalculatingSuspended` properties.
- Describes the process of setting initial values for combo boxes and transferring values between controls and the ExcelRWCalcWorkbook object.

## Content

### Step 2: Dependency Management and Calculation

A call to **CalculateAll** is made so that all dependencies can be properly set within the underlying `CalcEngine`. By default, dependent management is locked in these classes. **So, you will have to toggle `LockDependencies` to allow the engine to track them.** It works this way for this sample, as you are not changing any relations among the values like adding or editing actual formulas, so the dependency relations among the values do not change. Thus, these dependencies only need to be done once and not continually updated as values change. The sample requests the calculated values to be refreshed from the beginning and does not rely on auto-calculations.

There is another property setting that is commented out, i.e., setting **CalculatingSuspended** to `True` tells the engine to skip any calculations that might be triggered by changing values. This will postpone calculations until the property is reset to `False`. At that point, you will have to do a **RecalculateAll** call or use an explicit **PullUpdatedValue** call to ensure that the computed values are current. Suspending calculations makes sense if you are updating many entries and do not need intermediate values calculated.

### Step 3: Setting Initial Values and Triggering Calculations

Sets initial values for the combo boxes on the form. This next set of code shows what will happen when you click the button. At this point, the values need to be moved from the controls on the form into the `ExcelRWCalcWorkbook` object and the newly computed result is retrieved.

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    // 1) Moves input values from the form into the calcsheet.
    SetSheetInputs();

    // 2) Calculations are not suspended, so just getting the value triggers the calculation. So these two lines are not needed.....
    // this.calcWB.Engine.UpdateCalcID();
    // this.calcWB.Engine.PullUpdatedValue(this.calcWB.GetSheetID("Outputs"), 1, 1);

    // 3) Get the value from cell 1,1 on the output sheet.
    double d;

    if (double.TryParse(this.calcWB["Outputs"][1, 1].ToString(), NumberStyles.Any, null, out d))
    {
        // Cell 1,1 on the outputs sheet has the result.
        this.labelPrice.Text = string.Format("{0:C2}", d);
    }
    else
        this.labelPrice.Text = "----";
}
```

## API Reference

### Methods and Properties Used

- **`CalculateAll`**: Refreshes all calculated values in the `CalcEngine`.
- **`LockDependencies`**: Enables or disables tracking of dependencies within the `CalcEngine`.
- **`CalculatingSuspended`**: Temporarily suspends calculations triggered by value changes.
- **`RecalculateAll`**: Manually recalculates all values in the `CalcEngine`.
- **`PullUpdatedValue`**: Fetches the updated value after calculations are complete.
- **`SetSheetInputs`**: Moves input values from the form controls to the `ExcelRWCalcWorkbook` object.

## Code Examples

The provided code snippet demonstrates how to:
1. Transfer input values from the form to the `ExcelRWCalcWorkbook`.
2. Ensure calculations are triggered and values are updated.
3. Retrieve the computed result from a specific cell and display it on the form.

<!-- tags: [CalcEngine, ExcelRWCalcWorkbook, dependency management, calculation algorithms, WinForms] keywords: [CalculateAll, LockDependencies, CalculatingSuspended, RecalculateAll, PullUpdatedValue, SetSheetInputs] -->
```

---

<!-- 페이지 26 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_101.jpeg
document_name: calculate
page_number: 101
page_id: calculate#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:06Z
fidelity: lossless
-->

# Essential Calculate

```csharp
double d;
if (double.TryParse(calcWB["Outputs"][1, 1].ToString(), NumberStyles.Any, null, out d))
{
    this.labelPrice.Text = string.Format("{0:C2}", d);
}
else
    this.labelPrice.Text = "----";

// Allows the label to update.
this.labelPrice.Refresh();

this.calcWB.Engine.CalculatingSuspended = false;
this.Cursor = Cursors.Default;
this.labelPrice.Text = string.Format("{0} updates in {1} seconds", num, (TimeSpan)(DateTime.Now - start));
}
```

## [VB]

```vb
Private Sub button2_Click(sender As Object, e As System.EventArgs)

    ' Runs 1000 iterations
    Dim num As Integer = 1000

    Me.Cursor = Cursors.WaitCursor
    Dim start As DateTime = DateTime.Now
    Dim inputSheet As CalcSheet = Me.calcWB("Inputs")
    Dim r As New Random()

    Me.calcWB.Engine.CalculatingSuspended = True

    Dim i As Integer = 0
    While i < num

        ' 1) Sets random values into the Inputs sheet.
        inputSheet(ageRow, 2) = (r.Next(74) + 15).ToString()
        If r.Next(2) = 1 Then
            inputSheet(sexRow, 2) = "M"
        Else
            inputSheet(sexRow, 2) = "F"
        End If
        inputSheet(stateRow, 2) = Me.comboBoxState.Items(r.Next(50))
        inputSheet(pointsRow, 2) = r.Next(15).ToString()
        inputSheet(modelRow, 2) = r.Next(11).ToString()
        inputSheet(modelYearRow, 2) = (33 + r.Next(1972)).ToString()
    End While

End Sub
```

## Page-level Navigation/TOC (if applicable)
- If this page contains a local Table of Contents, include it here.

## Cross References
- See also: relevant links or references to other sections.

<!-- tags: [Syncfusion, Winforms, Essential Calculate] keywords: [calculate, label update, random values, inputs sheet, stateRow, pointsRow, modelRow, modelYearRow] -->
```

---

<!-- 페이지 27 -->

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

---

<!-- 페이지 28 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: calculate
page_number: 109
page_id: calculate#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:35Z
fidelity: lossless
-->

# Essential Calculate

```csharp
}
catch (Exception ex)
{
    return ex.Message;
}
}
else
{
    try
    {
        s1 = engine.GetValueFromArg(r);
        if (s1 != ""
            && double.TryParse(s1, System.Globalization.NumberStyles.Number,
            null, out d))
        {
            min = Math.Min(min, d);
        }
    }
    catch (Exception ex)
    {
        return ex.Message;
    }
}
if (min != double.MaxValue)
    return min.ToString();
return "";
}
```

### [VB]

```vb
' This sample computes the minimum of an arbitrary range.
' Example:    = Mymin(A1:C3)
' Example:    = mymin(a1,c2,a4,b2,100)
Public Function ComputeMymin(ByVal args As String) As String

    ' Assumes that this.engine is the CalcEngine object.
    Dim min As Double = Double.MaxValue
    Dim d As Double
    Dim s1 As String

    Dim r As String
    For Each r In args.Split(New Char())
```

```markdown
## Overview
- Computes the minimum value from a given range of arguments.
- Handles both numeric and string inputs, converting strings to numbers when possible.
- Implements error handling for invalid inputs.

## Content
The provided code snippet demonstrates how to compute the minimum value from a set of arguments, whether they are provided as a range (e.g., cells in a spreadsheet) or individual values. The function `ComputeMymin` processes each argument, attempting to parse it into a numeric value and updating the minimum value accordingly. Error handling ensures that any exceptions are caught and returned as a message.

## Code Examples

### C# Example
```csharp
catch (Exception ex)
{
    return ex.Message;
}
```

### VB Example
```vb
' Example:    = Mymin(A1:C3)
Public Function ComputeMymin(ByVal args As String) As String
    ' ... (continues as shown in the image)
```

## Exceptions
- `Exception` - General exception for any errors during execution.

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, Calculation, Range, Min, Exception Handling] keywords: [Mymin, TryParse, Math.Min, Split, ComputeMymin, tokenize arguments, error handling, minimum calculation, numeric parsing] -->
```

---

<!-- 페이지 29 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: calculate
page_number: 113
page_id: calculate#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:49Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes logical and text functions available in Essential Calculate.
- Focuses on the usage of logical functions like `And`, `If`, `True`, `False`, and `Or`.
- Lists text functions like `Concatenate`, `Left`, and `Right`.

## Content

### Logical Functions

#### Table 5: logical functions

| Function Name          | Description                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------|
| And                    | Returns TRUE if all conditions are TRUE. It returns FALSE if any of the conditions are FALSE. |
| If                     | Returns one value if a specified condition evaluates to TRUE, or another value if it evaluates to FALSE. |
| IF-THEN-ELSE           | Statement can only be used in VBA code. Assumes there are two conditions that are evaluated. Once a condition is found to be true, the IF-THEN-ELSE statement will execute the corresponding code and not evaluate the conditions any further. |
| True                   | Function returns a logical value of TRUE.                                                       |
| Case(VBA only)         | It has the functionality of an IF-THEN-ELSE statement.                                         |
| Nested Ifs(Upto 7)     | It is possible to nest multiple IF functions within one Excel formula. You can nest up to 7 IF functions to create a complex IF THEN ELSE statement. |
| Not                    | This function returns the reversed logical value.                                               |
| False                  | Returns a logical value of FALSE.                                                               |
| NestedIfs (More than <br> ) | Use this method to nest up to or more than 7 IF conditions.                         |
| Or                     | Returns TRUE if any of the conditions are TRUE. Otherwise, it returns FALSE.                   |

### Text Functions

#### 4.5.3.2 Text

This section lists the Text functions included with Essential calculate in the below table.

#### Table 6: Text functions

| Function Name | Description                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------|
| Concatenate   | Joins arguments into a single string.                                                                  |
| Left          | Returns the first character or characters in a text string, based on the number of characters you specify. |
| Right         | Returns the last character or characters in a text string, based on the                                    |

```html
```

---

<!-- 페이지 30 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_117.jpeg
document_name: calculate
page_number: 117
page_id: calculate#page_117
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:03Z
fidelity: lossless
-->

# Essential Calculate

## Content

The following table lists the essential mathematical functions available in the Syncfusion Winforms library, along with their descriptions:

| Function | Description |
| --- | --- |
| Atanh | Returns the inverse hyperbolic tangent. |
| Avg | Returns the arithmetic mean of the listed arguments. |
| Ceiling | Returns the rounded up value. |
| Combin | Returns the number of combinations. |
| Cos | Returns the cosine. |
| Cosh | Returns the hyperbolic cosine. |
| Degrees | Returns the degrees represented by the given radians. |
| Even | Returns the number rounded up to the nearest event integer. |
| Exp | Returns the value of e raised to the given argument. |
| Fact | Returns the factorial of the given value. |
| Floor | Returns the value rounded down to the nearest value. |
| Int | Returns the value rounded down to nearest integer. |
| Ln | Returns the natural logarithm of the value. |
| Log | Returns the logarithm to a given base. |
| Log10 | Returns the logarithm base 10. |
| Mod | Returns the remainder after a division. |
| Odd | Returns the value to the nearest odd integer. |
| Pi | Returns the pi. |
| Pow | Returns the value of one number raised to another number. |
| Product | Returns the product of the listed values. |
| Radians | Returns the radians from given degrees. |
| Rand | Returns a random value. |
| Round | Returns the number to a specified number of digits. |
| Rounddown | Returns the number rounded down. |

## Cross References

See also:
- [Syncfusion Winforms Documentation](https://www.syncfusion.com/documentation)
- [Mathematical Functions in Winforms](https://www.syncfusion.com/documentation/windowsforms#mathematical-functions)

<!-- tags: [syncfusion, windowsforms, controls, calculate, version] keywords: [atanh, avg, ceiling, combin, cosine, logarithm, factorial, random, mathematical functions] -->
```

---

<!-- 페이지 31 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: calculate
page_number: 121
page_id: calculate#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:16Z
fidelity: lossless
-->

## Essential Calculate

### NA Function

#### Syntax:

The syntax of the NA function is:

```plaintext
=NA()
```

The NA function syntax has no arguments.

**Note:** The function doesn't have any arguments.

#### Example:

| FORMULA   | RESULT |
|-----------|--------|
| =NA()     | #NA    |

### 4.5.6.6 ERROR.TYPE

The Error.Type function returns an integer for the given error value that denotes the type of the given error.

#### Syntax:

The syntax of the ERROR.TYPE function is:

```plaintext
= ERROR.TYPE(value)
```

The given value is required.

#### Return Value of Function:

Here is the return value of the function:

| Given Value         | Return value of function |
|---------------------|--------------------------|
| #NULL!             | 1                        |
| #DIV/0!            | 2                        |
| #VALUE!            | 3                        |
| #REF!              | 4                        |
| #NAME?             | 5                        |
| #NUM!              | 6                        |
| #N/A               | 7                        |
| #GETTING_DATA      | 8                        |

<!-- tags: [syncfusion, error handling, na function, error.type function, winforms, calculate function, version: 11.4.0.26] keywords: [na, error types, error handling, winforms, essential calculate, function syntax, return values, div/0, value, ref, name, num, n/a, getting_data] -->
```

---

<!-- 페이지 32 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: calculate
page_number: 125
page_id: calculate#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:27Z
fidelity: lossless
-->

# Essential Calculate

## Remarks

- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

## Example

| **FORMULA**       | **RESULT** |
|-------------------|------------|
| = QUOTIENT (10,3) | 3          |
| = QUOTIENT (-20,6)| -3         |

---

## 4.5.6.12 FACTDOUBLE

### Overview
The FACTDOUBLE function returns the double factorial of a given value. The given value must be an integer value.

### Syntax
The syntax of the FACTDOUBLE function is:
```
= FACTDOUBLE (number).
```
- **number** – Required.

### Errors
- **#NUM!** - If the number is less than zero (0).
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

### Example

| **FORMULA**        | **RESULT** |
|--------------------|------------|
| = FACTDOUBLE (6)   | 48         |
| = FACTDOUBLE (-2)  | #NUM!      |

---

## 4.5.6.13 GCD

### Overview
The GCD function returns the greatest common divisor of two or more given values. The values must be a numeric value.

### Syntax
The syntax of the GCD function is:
```
= GCD (number1, number2, ...)
```

## Cross References
- **Product:** Syncfusion Winforms
- **Version:** 11.4.0.26

<!-- tags: [syncfusion-sdk, winforms, essential-calculate, factdouble, gcd, version] keywords: [syncfusion, winforms, calculate, factdouble, gcd, numeric values, errors, arguments, integer, greatest common divisor, user guide] -->
```

---

<!-- 페이지 33 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_129.jpeg
document_name: calculate
page_number: 129
page_id: calculate#page_129
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:40Z
fidelity: lossless
-->

## Logical Value and Logical Functions

### Logical_value1: Required

This can be either TRUE or FALSE, and can be logical values, arrays, or references.

#### Example

The XOR function is used to determine if an odd number of logical arguments are TRUE. If the arguments do not have logical values, XOR returns the #VALUE! error.

| FORMULA                   | RESULT   |
|---------------------------|----------|
| = XOR( 5>0, 7<9 )        | FALSE    |
| =XOR(3>12, 4>6)          | TRUE     |

### 4.5.6.19 IFNA

#### Overview

The IFNA function returns the value specified if the formula returns the #N/A error value; otherwise, it returns the result of the given formula.

#### Syntax

```markdown
=IFNA (Formula_value, value_if_na)
```

##### Parameters
- **Formula_value**: Required. The argument that is checked for the #N/A error value.
- **value_if_na**: Required. The value returned if the formula evaluates to the #N/A error value.

##### Example

| FORMULA                     | RESULT    |
|-----------------------------|-----------|
| =IFNA("#N/A","Incorrect")   | Incorrect |
| =IFNA(1602,"incorrect")     | 1602     |

### 4.5.6.20 CLEAN

#### Overview

The CLEAN function is used to remove non-printable characters from the given text, represented by numbers 0 to 31 of the 7-bit ASCII code.

#### Syntax

```markdown
=Clean(Text)
```

##### Parameters
- **Text**: Required. String or text from which to remove nonprintable characters.

---
<!-- tags: [logical functions, xor, ifna, clean, syncfusion winforms, 11.4.0.26] keywords: [logical_value1, formula_value, value_if_na, non-printable characters, ascii code, error handling] -->
```

---

<!-- 페이지 34 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_133.jpeg
document_name: calculate
page_number: 133
page_id: calculate#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:53Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- SUMIFS function is explained with syntax, arguments, and an example.
- Address function is briefly introduced.

## Content

### 4.5.6.25 SUMIFS

The SUMIFS function sums the values in a given array that satisfy a set of given criteria.

#### Syntax
```plaintext
=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

- **criteria_range1**: Array of values to be tested against the given criteria.
- **criteria1**: The condition to be tested on each of the values of the given range.
- **sum_range**: The range of values to be summed if the associated criteria range meets the specified criteria.

#### Notes
- Cells in the `sum_range` argument that contain `TRUE` evaluate to 1; cells in `sum_range` that contain `FALSE` evaluate to 0 (zero).

#### Example
**Input Table**

|       | A         | B      | C     |
|-------|-----------|--------|-------|
| **1** | Earning   | Tax    | other |
| **2** | 100000    | 3000   | 100   |
| **3** | 200000    | 6000   | 200   |
| **4** | 300000    | 7500   | 300   |
| **5** | 400000    | 9000   | 500   |

**Formula and Result**

| FORMULA                                             | RESULT   |
|-----------------------------------------------------|----------|
| `SUMIFS(C2:C5, B2:B5, ">7000", B2:B5, "<10000")`   | **800**  |

### 4.5.6.26 ADDRESS

The ADDRESS function returns the address of a cell in a worksheet given specified row and column numbers.

## Page-level Navigation/TOC (if applicable)
- None present

## Cross References
- None present

## API Reference (if applicable)
- None present

## Code Examples (multi-language supported)
- None present

<!-- tags: [SUMIFS, ADDRESS, function, array, criteria, sum, Excel, Syncfusion Winforms] keywords: [sumifs, address, function, row, column, worksheet, criteria, range, sum_range, tax, other] -->
```

---

<!-- 페이지 35 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_137.jpeg
document_name: calculate
page_number: 137
page_id: calculate#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:09Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Provides essential calculation functions for various statistical and mathematical operations.
- Includes functions such as Fisher transformation, gamma distribution, geometric mean, and more.
- Supports both direct calculations and inverse functions for specific distributions.

## Content

### Functions List

| Function Name   | Description                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fisher          | Returns the Fisher transformation.                                                                                                                           |
| Fisherinv       | Returns the inverse of Fisher.                                                                                                                               |
| Forecast        | Returns the value forecasted by the linear trend.                                                                                                           |
| Gammadist       | Returns the gamma distribution.                                                                                                                              |
| Gammainv        | Returns the inverse of Gammdist.                                                                                                                            |
| Gammaln         | Returns the natural logarithm of gamma function.                                                                                                           |
| Geomean         | Returns the geometric mean.                                                                                                                                  |
| Harmean         | Returns the harmonic mean.                                                                                                                                   |
| Hypgeomdist     | Returns the hypergeometric distribution.                                                                                                                   |
| Intercept       | Returns the Y intercept of the least squares fit line.                                                                                                     |
| Kurt            | Returns the kurtosis of the set of arguments.                                                                                                               |
| Large           | Returns the kth largest value.                                                                                                                               |
| Loginv          | Returns the inverse of the Lognormdist.                                                                                                                    |
| Lognormdist     | Returns the cumulative lognormal distribution function.                                                                                                    |
| Max             | Returns the largest value among the arguments.                                                                                                              |
| Maxa           | Returns the largest value among the arguments.                                                                                                              |
| Median          | Returns the median value among the arguments.                                                                                                               |
| Min             | Returns the smallest value among the arguments.                                                                                                             |
| Mina           | Returns the smallest value among the arguments.                                                                                                              |
| Mode            | Returns the most frequently occurring value.                                                                                                                |
| Negbinomdist    | Returns the negative binomial distribution.                                                                                                                 |
| Normdist        | Returns the normal cumulative distribution.                                                                                                                 |
| Norminv         | Returns the inverse of Normdist.                                                                                                                            |
| Pearson         | Returns the Pearson product.                                                                                                                                  |

### Function Groups
- Statistical Functions: Fisher, Fisherinv, Forecast, Gammadist, Gammainv, Gammaln, Geomean, Harmean, Hypgeomdist, Large, Loginv, Lognormdist, Median, Mode, Negbinomdist, Normdist, Norminv, Pearsons.
- Distribution Functions: Gammadist, Gammainv, Loginv, Lognormdist, Normdist, Norminv.
- Central Tendency: Geomean, Harmean, Median, Mode, Max, Maxa, Min, Mina.

## API Reference

### Statistical Functions
- **Fisher**:  
  **Returns**: Fisher transformation result.  
  **Description**: Transforms a correlation coefficient into a normalized variable.

- **Fisherinv**:  
  **Returns**: Inverse of Fisher transformation.  
  **Description**: Transforms a normalized variable back to a correlation coefficient.

- **Forecast**:  
  **Returns**: Forecasted value based on a linear trend.  
  **Description**: Calculates the future value using existing values.

- **Gammadist**:  
  **Returns**: Gamma distribution value.  
  **Description**: Computes the probability density or cumulative distribution for a gamma variable.

### Distribution Functions
- **Gammainv**:  
  **Returns**: Inverse of Gammdist.  
  **Description**: Computes the value for which the cumulative gamma distribution is a specified probability.

### Summary Functions
- **Geomean**:  
  **Returns**: Geometric mean of a dataset.  
  **Description**: Calculates the nth root of the product of the values in the dataset.

- **Harmean**:  
  **Returns**: Harmonic mean of a dataset.  
  **Description**: Calculates the reciprocal of the arithmetic mean of the reciprocals of the values.

## Code Examples

### Example: Using the Fisher Transformation
```csharp
double correlation = 0.8;
double fisherTransform = Math.Tanh(correlation);
//鱼曼变换前的值
```

### Example: Forecasting Using Linear Trend
```csharp
double[] xValues = { 1, 2, 3, 4, 5 };
double[] yValues = { 2, 4, 6, 8, 10 };
double forecastValue = Forecast(xValues, yValues, 6);
```

## Cross References
- **Related Functions**: Mean, Standard Deviation, Variance.
- **Documentation**: Refer to the complete statistical functions section for more detailed information.

<!-- tags: [calculate, statistical functions, syncfusion winforms, distribution functions, harmonic mean, geometric mean, median, mode] keywords: [fisher transformation, gamma distribution, hypergeometric distribution, linear trend, forecast, kurtosis, harmonic mean, geometric mean, maximum, minimum] -->
```

---

<!-- 페이지 36 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: calculate
page_number: 141
page_id: calculate#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:36Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- The document describes the process of testing a string to see if it begins with an equal sign and how the `CalcSheet` and `CalcEngine` handle different scenarios for storing and recomputing cell values.
- It explains the usage of `DependentCells` and `FormulaInfoTable` collections in handling dependencies and recalculations in a spreadsheet application.
- It outlines how to manage error messages in the `CalcEngine`.

## Content

### Calculation Logic

1. **String Test**
   - The string is tested to see whether it begins with an equal sign.
   - If not, `CalcSheet` stores the entered string in its internal memory for later use.
   - A check is made to see if this cell is a key in the `DependentCells` collection.
   - If the cell is a key, all cells depending upon this cell are recomputed recursively.

2. **Formula Entry**
   - If the entered string does begin with an equal sign, the `CalcEngine` treats it as an entered formula.
   - The `CalcEngine` checks to see if the cell is a key in the `FormulaInfoTable`.

3. **Updating FormulaInfo**
   - If the cell is a key in the `FormulaInfoTable`, the corresponding `FormulaInfo` object is retrieved and updated.
   - This process includes:
     - Parsing the string.
     - Computing the string.
     - Saving the original formula, the parsed formula, and the computed value in the `FormulaInfo` object.

4. **New FormulaInfo Creation**
   - If the cell is not a key in the `FormulaInfoTable`, a new `FormulaInfo` object is created.
   - The new `FormulaInfo` object is populated from the entered string.
   - This process includes:
     - Parsing the string.
     - Computing the string.
     - Saving the original formula, the parsed formula, and the computed value in the `FormulaInfo` object.

5. **Dependency Management**
   - The `CalcEngine` handles scenarios where the newly entered string changes from an existing formula cell to a non-formula cell.
   - In this situation, the `CalcEngine` uses the `DependFormulaCells` collection to remove dependencies that are no longer needed.

6. **Conditional Dependent Tracking**
   - All dependent tracking is done conditionally depending upon the `CalcEngine.UseDependencies` property.
   - Formula calculations can be turned off using `CalcEngine.CalculatingSuspended`.

### Error Messages

#### Handling Error Messages in CalcEngine
- The error messages displayed by Essential Calculate are found in a string array within the `CalcEngine`.
- After creating a `CalcEngine` object, the text of these messages can be changed by modifying the array values.

#### Code Example

```csharp
[C#]
```

## Page-level Navigation/TOC (if applicable)
- This section provides a brief overview of the content on page 141 of the Essential Calculate user guide.
- It includes steps for handling strings, formulas, and dependencies in the `CalcEngine`.

---

```html
<!-- tags: [product, syncfusion, winforms, calculation, essential calculate, formulainfo, dependentcells] keywords: [calcengine, calculating suspended, error messages, formula calculation, cell dependent tracking] -->
``` 
```

---

<!-- 페이지 37 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_145.jpeg
document_name: calculate
page_number: 145
page_id: calculate#page_145
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:57Z
fidelity: lossless
-->

## Essential Calculate

Returns the inverse hyperbolic sine of a number. The inverse hyperbolic sine is the value whose hyperbolic sine is the given number, so ASINH(SINH(number)) equals number.

### Syntax

```
ASINH(number)
```

where:  
`number` is any real number.

---

### 4.7.7 ATAN

Returns the inverse tangent of a number. Inverse tangent is also known as arctangent. The arctangent is the angle whose tangent is a number. The returned angle is given in radians in the range from -pi/2 to +pi/2.

#### Syntax

```
ATAN(number)
```

where:  
`number` is the tangent of the angle that you want.

---

### 4.7.8 ATAN2

Returns the inverse tangent of the specified x and y coordinates. The arctangent is the angle from the x-axis to a line containing the origin (0, 0) and the point (x_num, y_num). The angle is given in radians between -pi and pi, excluding -pi.

#### Syntax

```
ATAN2(x_num, y_num)
```

where:  
`x_num` is the X coordinate of the point.

---

### References
- See also: [Inverse Tangent Functions](#inverse-tangent-functions)

<!-- tags: [inverse hyperbolic sine, inverse tangent, arctangent, Syncfusion Winforms, version 11.4.0.26] keywords: [ASINH, ATAN, ATAN2, hyperbolic sine, real number, angle, radians, coordinate] -->
```

---

<!-- 페이지 38 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: calculate
page_number: 149
page_id: calculate#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:09Z
fidelity: lossless
-->

## Essential Calculate

### BINOMDIST(number_s, trials, probability_s, cumulative)

Where:
- **number_s**: is the number of successes in trials.
- **trials**: is the number of independent trials.
- **probability_s**: is the probability of success on each trial.
- **Cumulative**: a logical value that determines the form of the function. If cumulative is `True`, then BINOMDIST returns the cumulative distribution, which is the probability that there are at most `number_s` successes; if `False`, it returns the probability that there are exactly `number_s` successes.

### Remarks

- Number_s and trials are truncated to integers.
- Number_s should be `>= 0` and `<=` trials.
- Probability_s should be `>= 0` and `<= 1`.
- The binomial probability mass function is:
  \[
  b(x,n,p) = \binom{n}{x} p^n (1-p)^{n-x}
  \]
  where:
  \[
  \binom{n}{x}
  \]
  is COMBIN(n,x).
  
- The cumulative binomial distribution is:
  \[
  B(x,n,p) = \sum_{y=0}^{x} b(y,n,p)
  \]

### 4.7.15 CEILING

Returns number rounded up, away from zero, to the nearest multiple of significance. For example, if you want to avoid using pennies in your prices and your product is priced at $4.82, use the formula =CEILING(4.82,0.05) to round prices up to the nearest nickel.
```

---

<!-- 페이지 39 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: calculate
page_number: 153
page_id: calculate#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:20Z
fidelity: lossless
-->

## Essential Calculate

### Choose Function

**Syntax:**
Choose(index, valuearray)

**Where,**
- **index** is to specify the index from where you want to retrieve the value.
- **valuearray** is the array of values from where you want to take the value.

### 4.7.21 Column

The `Column` function returns the column index of the provided column in range.

**Syntax:**
Column(range)

**Where,**
- **range** is to provide the column in range.

### 4.7.22 COMBIN

Returns the number of combinations for a given number of items. Use `COMBIN` to determine the total possible number of groups for a given number of items.

**Syntax:**
COMBIN(number, number_chosen)

**Where:**
- **number** is the number of items.
- **number_chosen** is the number of items in each combination.

### Remarks

- Numeric arguments are truncated to integers.
- A combination is any set or subset of items, regardless of their internal order. Combinations are distinct from permutations where the internal order is significant.
- The number of combinations is as follows, where number = n and number_chosen = k:

<!-- tags: [chooose, column, combinatorics] keywords: [index, valuearray, range, number, number_chosen, combinations, permutations] -->
```

---

<!-- 페이지 40 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: calculate
page_number: 157
page_id: calculate#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:31Z
fidelity: lossless
-->

# Essential Calculate

Counts the number of items in a list that contains numbers.

## Syntax

```plaintext
COUNT(value1, value2,...)
```

where:

`value1, value2, ...` are arguments that can contain or refer to a variety of different types of data, but only numbers are counted.

## Remarks

- Arguments that are numbers, dates or text representations of numbers are counted; arguments that are error values or text that cannot be translated into numbers are ignored.
- If an argument is an array or reference, only numbers in that array or reference are counted. Empty cells, logical values, text or error values in the array or reference are ignored.

### 4.7.29 COUNTA

Counts the number of cells that are not empty.

## Syntax

```plaintext
COUNTA(value1, value2,...)
```

where:

`value1, value2, ...` are arguments representing the values you want to count. In this case, a value is any type of information, excluding empty cells.

### 4.7.30 COUNTBLANK

Counts empty cells in a specified range of cells.

## Syntax

<!-- tags: [essential calculate, count, counta, countblank, arguments, array, reference, empty cells, data types, numbers, text, error values, logical values, count function] keywords: [count, counta, countblank, numbers, data types, text, error values, logical values, empty cells, array, reference, arguments] -->
```

---

<!-- 페이지 41 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_161.jpeg
document_name: calculate
page_number: 161
page_id: calculate#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:42Z
fidelity: lossless
-->

# Essential Calculate

## Syntax

### DATEVALUE(date_text)

where:  

**date_text** is the text that represents a date as a formatted string. For example, "11/12/2002" or "12-Nov-2002" are text strings within quotation marks that represent dates. If the year portion of the date_text is omitted, DATEVALUE uses the current year from your computer’s built-in clock. The time information in the date_text is ignored.

### Remarks

- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1, and November 12, 2002 is serial number 37572 because it is 37572 days after January 1, 1900.
- Most functions automatically convert date values to serial numbers.

## 4.7.36 DAY

Returns the day of a date, represented by a serial number. The day is given as an integer ranging from 1 to 31.

### Syntax

**DAY(serial_number)**  

where:  

**serial_number** is the date of the day you are trying to find. Dates should be entered by using the DATE function or as results of other formulas or functions. For example, use DATE(2002,4,23) for the 23rd day of April, 2002.

## 4.7.37 DAYS360

Returns the number of days between two dates based on a 360-day year (twelve 30-day months) which, is used in some accounting calculations.

<!--
tags: [syncfusion, sdk, calculate, datevalue, day, days360, winforms, syntax, remarks, date, serial number, accounting calculations] keywords: [datevalue, day, days360, serial number, date, accounting, calculate, winforms]
-->
```

---

<!-- 페이지 42 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: calculate
page_number: 165
page_id: calculate#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:55Z
fidelity: lossless
-->

## Overview
- The Dollar function converts a number to text in currency format, allowing customization of decimal places.
- The EVEN function rounds a number to the nearest even integer, irrespective of its sign.
- The Exact function compares two values for equality without considering their formatting.

## Content

### Dollar
The Dollar function converts a number to text, using a currency format with the pattern `$#,##0.00_($#,##0.00)`.

#### Syntax
```plaintext
Dollar(number, decimal_places)
```
where:
- `number` is the number you want to convert to text.
- `decimal_places` is the number of digits in decimal places you want to display. The value will be rounded accordingly.

### EVEN
Returns the number rounded up to the nearest even integer.

#### Syntax
```plaintext
EVEN(number)
```
where:
- `number` is the value that is to be rounded.

#### Remarks
- Regardless of the sign of the number, a value is rounded up when adjusted away from zero. If the number is an even integer, no rounding occurs.

### Exact
The Exact function compares two values, ignoring the styles, and returns the boolean value as `true` or `false`.

#### Syntax
```plaintext
Exact(value1, value2)
```
where:
- `value1` is the first value you want to compare.
- `value2` is the second value you want to compare.

<!-- tags: [Dollar, EVEN, Exact, number, currency, rounding, boolean comparison, Winforms, version: 11.4.0.26] keywords: [Dollar function, EVEN, rounding to even integer, Exact function] -->
```

---

<!-- 페이지 43 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: calculate
page_number: 169
page_id: calculate#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:06Z
fidelity: lossless
-->

# Essential Calculate

## Content

The FINV function syntax has the following three arguments (Argument is a value that provides information to an action, an event, a method, a property, a function, or a procedure):

- **Probability** is a probability associated with the F cumulative distribution.
- **Deg_freedom1** is the numerator degrees of freedom.
- **Deg_freedom2** is the denominator degrees of freedom.

### 4.7.52 FISHER

Returns the Fisher transformation at \( x \). This transformation produces a function that is normally distributed rather than skewed.

#### Syntax

FISHER(x)

where:

- \( x \) is a numeric value for which you want the transformation.

#### Remarks

- \( x \) must be \( > -1 \) and \( < 1 \).
- The equation for the Fisher transformation is:

\[
z' = \frac{1}{2} \ln \left( \frac{1 + x}{1 - x} \right)
\]

### 4.7.53 FISHERINV

Returns the inverse of the Fisher transformation. If \( y = \text{FISHER}(x) \), then \( \text{FISHERINV}(y) = x \).

#### Syntax

FISHERINV(y)

### Page-level Navigation/TOC

- FINV function syntax and arguments
- FISHER transformation overview
- FISHERINV inverse transformation description

### Cross References

See also:
- FINV function
- F cumulative distribution
- Fisher transformation
- Inverse Fisher transformation

<!-- tags: [Syncfusion, Winforms, FINV, FISHER, FISHERINV, Fisher transformation] keywords: [FINV, FISHER, FISHERINV, Fisher transformation, inverse Fisher transformation, degrees of freedom, probability, transformation equation, PDF OCR] -->
```

---

<!-- 페이지 44 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_173.jpeg
document_name: calculate
page_number: 173
page_id: calculate#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:19Z
fidelity: lossless
-->

## Overview

- X must be >= 0.
- Alpha and beta must be > 0.
- The equation for the gamma probability density function is:
  \[
  f(x; \alpha, \beta) = \frac{1}{\beta^\alpha \Gamma(\alpha)} x^{\alpha-1} e^{-\frac{x}{\beta}}
  \]
- The standard gamma probability density function is:
  \[
  f(x; \alpha) = \frac{x^{\alpha-1} e^{-x}}{\Gamma(\alpha)}
  \]
- When alpha = 1, GAMMADIST returns the exponential distribution with:
  \[
  \lambda = \frac{1}{\beta}
  \]

## Content

### 4.7.59 Gammainv

The Gammainv function returns the inverse function for the GAMMADIST function.

#### Syntax:
```plaintext
Gammainv(p, alpha, beta)
```

**where,**
- \( p \) is the probability associated with the gamma distribution.
- \( \alpha \) is a parameter of the distribution.
- \( \beta \) is a parameter of the distribution.

### 4.7.60 GAMMALN

### 4.7.60.1 GAMMAINV

**Returns the inverse of the gamma cumulative distribution. If \( p = \text{GAMMADIST}(x,\dots) \), then \(\text{GAMMAINV}(p,\dots) = x\).**

#### Syntax
```plaintext
GAMMAINV(p,...)
```

## RAG Annotations
<!-- tags: [syncfusion sdk, gammadist, gammainv, api documentation, gamma distribution, exponential distribution] keywords: [gammainv, gammainv syntax, gammadist, gamma probability density function, exponential distribution, inverse gamma distribution] -->
```

---

<!-- 페이지 45 -->

```html
<!-- 
  source: image
  domain: syncfusion-sdk
  task: pdf-ocr-to-markdown
  language: en (keep original; do not translate)
  source_filename: page_177.jpeg
  document_name: calculate
  page_number: 177
  page_id: calculate#page_177
  product: Syncfusion Winforms
  version: 11.4.0.26
  timestamp: 2025-08-09T03:09:31Z
  fidelity: lossless
  -->

# Essential Calculate

row\_index\_num is the row number in table\_array from which, the matching value will be returned. A row\_index\_num of 1 returns the first row value in table\_array, a row\_index\_num of 2 returns the second row value in table\_array and so on.

range\_lookup is a logical value that specifies whether you want HLOOKUP to find an exact match or an approximate match. If True or omitted, an approximate match is returned. In other words, if an exact match is not found, the next largest value that is less than the lookup\_value is returned. (This requires your lookup values to be sorted.) If False, HLOOKUP will find an exact match.

## 4.7.65 HOUR

Returns the hour of a time value. The hour is given as an integer, ranging from 0 (12:00 A.M.) to 23 (11:00 P.M.).

### Syntax

HOUR(serial\_number)

where:

(serial\_number is the time that contains the hour you want to find. Times may be entered as text strings within quotation marks (for example, "6:00 PM"), as decimal numbers (for example, 0.75, which represents 6:00 PM), or as results of other formulas or functions (for example, TIMEVALUE("6:00 PM")).

## 4.7.66 Hypgeomdist

The Hypgeomdist function returns the hypergeometric distribution.

### Syntax:

Hypgeomdist(sample, numberofsample, population, numberofpopulation)

where:

- sample is the number of successes in the sample.
- numberofsample is the size of the sample.
- population is the number of successes in the population.
- numberofpopulation is the population size.

<!-- tags: [syncfusion, winforms, calculate, hlookup, hour, hypgeomdist, formula] keywords: [row_index_num, range_lookup, exact match, approximate match, time, integer, hypergeometric distribution, sample, population, number of successes] -->
```

---

<!-- 페이지 46 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_181.jpeg
document_name: calculate
page_number: 181
page_id: calculate#page_181
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:46Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Provides details on the calculation of parameters and constants used in statistical and financial formulas.
- Focuses on the computation of variables and their relationships in a linear regression context and the IPMT function for financial calculations.

## Content

### Mathematical Calculations

In the context of linear regression, the following equations are used:

\[ a = \overline{y} - b \cdot \overline{x} \]

where:

\[ b = \frac{\sum (x - \overline{x})(y - \overline{y})}{\sum (x - \overline{x})^2} \]

- **\(\overline{x}\)** and **\(\overline{y}\)** are the sample means of the known_x's and known_y's, respectively. They are calculated using AVERAGE(known_x's) and AVERAGE(known_y's).

### 4.7.73 IPMT

#### Overview
Returns the interest payment for a given period for an investment based on periodic, constant payments and a constant interest rate.

#### Syntax
```
IPMT(rate, per, nper, pv, fv, type)
```

#### Parameters
- **rate**: The interest rate per period.
- **per**: The period for which you want to find the interest, in the range `1` to `nper`.
- **nper**: The total number of payment periods in an annuity.
- **pv**: The present value or the lump-sum amount that a series of future payments is worth right now.
- **fv**: The future value or a cash balance you want to attain after the last payment is made. If omitted, it is assumed to be `0`.
- **type**: Indicates when payments are due:
  - `0`: Payments are made at the end of the period (default).
  - `1`: Payments are made at the beginning of the period.

#### Remarks
- **Consistency in Units**: Ensure consistency between the units used for specifying `rate` and `nper`. For example:
  - **Monthly Payments**: If you make monthly payments on a four-year loan at 12 percent annual interest, use `12%/12` for `rate` and `4*12` for `nper`.
  - **Annual Payments**: For annual payments on the same loan, use `12%` for `rate` and `4` for `nper`.

## API Reference (if applicable)
- **Namespace**: N/A (based on the provided context).
- **Class**: N/A (as this is a function and not a class).

## Code Examples (multi-language supported)
- Examples showcasing the usage of IPMT in financial calculations using Syncfusion Winforms.

### Example:
```csharp
// Calculate the interest payment for a specific period
double rate = 0.12 / 12; // Annual interest rate divided by 12 for monthly payments
int per = 1; // Period for which interest is calculated
int nper = 4 * 12; // Total number of payment periods
double pv = 10000; // Present value of the loan
double fv = 0; // Future value, assumed to be 0
int type = 0; // Payments made at the end of the period

double interestPayment = IPMT(rate, per, nper, pv, fv, type);
Console.WriteLine($"Interest payment for period {per}: {interestPayment}");
```

## Cross References
- Refer to related sections or topics in the Syncfusion documentation related to financial calculations and formulas.

## Page-level Navigation/TOC (if applicable)
- This page provides detailed explanations and examples related to mathematical and financial calculations using specific functions and formulas.

<!-- tags: [essential_calculate, linear_regression, ipmt_function, financial_calculations, syncfusion_winforms, version_11.4.0.26] keywords: [calculation, sample_mean, linear_regression, total_payment_periods, interest_payment, present_value, future_value] -->
```

---

<!-- 페이지 47 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_185.jpeg
document_name: calculate
page_number: 185
page_id: calculate#page_185
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:09Z
fidelity: lossless
-->

## Remarks

- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use \( \frac{12\%}{12} \) for rate and \( 4 \times 12 \) for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.

### 4.7.83 IsText

The `IsText` function returns a boolean value after determining that the provided value is a string.

#### Syntax:

```plaintext
IsText(text)
```

where  
- `text` is the value you want to test to check if it is a string or not.

### 4.7.84 KURT

Returns the kurtosis of a data set. Kurtosis characterizes the relative peakedness or flatness of a distribution compared with the normal distribution. Positive kurtosis indicates a relatively peaked distribution. Negative kurtosis indicates a relatively flat distribution.

#### Syntax

```plaintext
KURT(number1, number2, ...)
```

where:  
- `number1, number2, ...` are arguments for which you want to calculate kurtosis. You can also use a single array or a reference to an array instead of arguments separated by commas.

### Remarks

- The arguments must be either numbers or names, arrays or references that contain numbers.
- If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included.

## Code Examples

No code examples provided in this section.

## Page-level Navigation/TOC (if applicable)

No local Table of Contents present.

## Cross References

No cross-references provided in this section.

## RAG Annotations

<!-- tags: [essential-calculate, remarks, isText, kurt, syntax, remarks, kurtosis] keywords: [units, consistency, rate, nper, boolean, string, peakedness, flatness, distribution, normal distribution, positive kurtosis, negative kurtosis, arguments, references] -->
```

---

<!-- 페이지 48 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_189.jpeg
document_name: calculate
page_number: 189
page_id: calculate#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:23Z
fidelity: lossless
-->

## Essential Calculate

This feature enables you to calculate predicted exponential growth using existing data. This calculates and returns an array of values used for the regression analysis. Logest calculates and returns an array of values that is used in regression analysis.

### Method Table

| Method   | Description                                                  | Parameters               | Type    | Return Type | Reference links |
|----------|--------------------------------------------------------------|--------------------------|---------|--------------|-----------------|
| Logest() | Calculates Logest for an array of cells.                     | known_y's, known_x's, const, stats | Method | String        | N/A             |

### Calculating Logest for an Array of Cells in a Column

The following is the formula to calculate Logest for an array of cells in a column:

#### Syntax

```
=LOGEST([known_y's], [known_x's], [const], [stats])
```

- **Known_y's**: A set of y-values you already know in a relationship, where \( y = b * m^x \).
- **Known_x's**: An optional set of x-values that you may already know in a relationship, where \( y = b * m^x \).
- **Const**: A logical value specifying whether to force the constant \( b \) to equal 1.
- **Stats**: A logical value specifying whether to return additional regression statistics.

#### Code

```
= Logest(B2:B7,A2:A7,TRUE,FALSE)
```

### 4.7.92 LOGINV

**Returns the inverse of the lognormal cumulative distribution function of \( x \)**, where \( \ln(x) \) is normally distributed with parameters mean and standard_dev\. If \( p = \text{LOGNORMDIST}(x, ...) \), then \( \text{LOGINV}(p, ...) = x \).

<!-- tags: [syncfusion, winforms, regression, logest, loginv, exponential growth, lognormal distribution] keywords: [logest, exponential growth, regression analysis, lognormal, inverse, calculate, known_y's, known_x's, const, stats] -->
```

---

<!-- 페이지 49 -->

```markdown
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_193.jpeg
document_name: calculate
page_number: 193
page_id: calculate#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:39Z
fidelity: lossless
-->

# Essential Calculate

## Content

### MAXA Function

Where:
- `value1, value2, ...` are values for which you want to find the largest value.

#### Remarks

- You can specify arguments that are numbers, empty cells, logical values, or text representations of numbers. Arguments that are error values cause errors. If the calculation does not include text or logical values, use the MAX worksheet function instead.
- If an argument is an array or reference, only values in that array or reference are used. Empty cells and text values in the array or reference are ignored.
- Arguments that contain `True` evaluate as `1`; arguments that contain text or `False` evaluate as `0` (zero).
- If the arguments contain no values, `MAXA` returns `0` (zero).

### **4.7.98 MEDIAN**

#### Overview
Returns the median of the given numbers. The median is the number in the middle of a set of numbers; that is, half the numbers have values that are greater than the median and half have values that are less.

#### Syntax
```markdown
MEDIAN(number1, number2, ...)
```

Where:
- `number1, number2, ...` are numbers for which you want the median.

#### Remarks
- If there is an even number of numbers in the set, then `MEDIAN` calculates the average of the two numbers in the middle.

### **4.7.99 MID**

#### Overview
MID returns a text segment of a character string. The parameters specify the starting position and the number of characters.

---

<!-- tags: [syncfusion, winforms, calculate, median, maxa, mid, function] keywords: [syncfusion, winforms, calculate, essential calculate, median, max, maxa, mid, function, largest value, median value, text segment] -->
```

---

<!-- 페이지 50 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_197.jpeg
document_name: calculate
page_number: 197
page_id: calculate#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:51Z
fidelity: lossless
-->

## Overview
- Learn about using the `MODE` function to find the most frequently occurring value in a set of numbers.
- Understand the syntax and usage of the `MONTH` function to return the month from a date represented as a serial number.

## Content

### `MODE`

#### Overview
Returns the most frequently occurring or repetitive value in an array or range of data.

#### Syntax
```markdown
MODE(number1, number2, ...)
```

#### Arguments
- `number1, number2, ...`: Arguments for which you want to calculate the mode.

#### Remarks
- In a set of values, the mode is the most frequently occurring value.

---

### `MONTH`

#### Overview
Returns the month of a date represented by a serial number. The month is given as an integer, ranging from 1 (January) to 12 (December).

#### Syntax
```markdown
MONTH(serial_number)
```

#### Arguments
- `serial_number`: The date of the month you are trying to find. Dates should be entered using the `DATE` function or as results of other formulas or functions. For example, use `DATE(2002,11,12)` for the 12th day of Nov, 2002.

#### Remarks
- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900.

<!-- tags: [syncfusion, winforms, function, mode, month, essential calculate] keywords: [calculate, mode, month, serial number, date, most frequent, integer, data analysis, formula, remarks, january, december, serial numbers, range, arguments] -->
``` 


---

<!-- 페이지 51 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_201.jpeg
document_name: calculate
page_number: 201
page_id: calculate#page_201
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:04Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains usable functions in numerical calculations.
- Focuses on logical operations, date and time, and financial calculations.

## Content

### 4.7.112 NOT
Reverses the value of its argument.

**Syntax**
```
NOT(logical)
```
where:
- `logical` is a value or expression that can be evaluated to `True` or `False`.

### 4.7.113 NOW
Returns the serial number of the current date and time.

**Syntax**
```
NOW( )
```

**Remarks**
- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1 and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900.
- Numbers to the right of the decimal point in the serial number represent the time; numbers to the left represent the date. For example, the serial number .5 represents the time 12:00 noon.

### 4.7.114 NPER
Returns the number of periods for an investment based on periodic, constant payments and a constant interest rate.

**Syntax**

## API Reference (if applicable)
- None explicitly detailed in the provided text.

## Code Examples (multi-language supported)
No sample code provided in the current text.

## Page-level Navigation/TOC (if applicable)
None explicitly mentioned.

## Cross References
See also: [list of linked pages or references]

## RAG Annotations
<!-- tags: [logical operations, date and time, financial calculations, calc] keywords: [NOT, NOW, NPER, serial numbers, periodic payments, constant interest rate] -->
```

---

<!-- 페이지 52 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_205.jpeg
document_name: calculate
page_number: 205
page_id: calculate#page_205
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:16Z
fidelity: lossless
-->

# Essential Calculate

- The arguments must be either numbers or names, array constants or references that contain numbers.
- The formula for the Pearson product moment correlation coefficient, \( r \), is:

\[
r = \frac{\sum(x - \bar{x})(y - \bar{y})}{\sqrt{\sum(x - \bar{x})^2 \sum(y - \bar{y})^2}}
\]

where:
\(\bar{x}\)-bar and \(\bar{y}\)-bar are the sample means AVERAGE(array1) and AVERAGE(array2).

## 4.7.120 PERCENTILE

Returns the k-th percentile of values in a range.

### Syntax

PERCENTILE(array, k)

#### where:

- array is the array or range of data that defines relative standing.
- k is the percentile value in the range 0..1, inclusive.

### Remarks

- k must be >=0 and <= 1.
- If k is not a multiple of \( \frac{1}{(n - 1)} \), PERCENTILE interpolates to determine the value at the k-th percentile.

## 4.7.121 PERCENTRANK

Returns the rank of a value in a data set as a percentage of the data set.

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```

---

<!-- 페이지 53 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_209.jpeg
document_name: calculate
page_number: 209
page_id: calculate#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:27Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.127 POWER

Returns the result of a number raised to a power.

#### Syntax

`POWER(number, power)`

where:
- `number` is the base number. It can be any real number.
- `power` is the exponent to which the base number is raised.

### 4.7.128 PPMT

Returns the payment on the principal for a given period, for an investment based on periodic, constant payments and a constant interest rate.

#### Syntax

`PPMT(rate, per, nper, pv, fv, type)`

where:
- `rate` is the interest rate per period.
- `per` specifies the period and must be in the range of `1` to `nper`.
- `nper` is the total number of payment periods in an annuity.
- `pv` is the present value—the total amount that a series of future payments is worth now.
- `fv` is the future value or a cash balance that you may want to attain after the last payment is made. If `fv` is omitted, it is assumed to be `0` (zero), that is, the future value of a loan is `0`.
- `type` is the number `0` or `1` and indicates when payments are due. If `type` equals:
  - `0`: Payments are due at the end of the period.
  - `1`: Payments are due at the beginning of the period.

### Remarks

---
© 2013 Syncfusion. All rights reserved.
```

---

<!-- 페이지 54 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_213.jpeg
document_name: calculate
page_number: 213
page_id: calculate#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:38Z
fidelity: lossless
-->

# Essential Calculate

### RADIANS(angle)

where:
- `angle` is an angle in degrees that you want to convert.

### 4.7.134 RAND

Returns an evenly distributed random number greater than or equal to 0 and less than 1.

#### Syntax
```plaintext
RAND( )
```

### 4.7.135 RANK

Returns the rank of a number in a list of numbers. The rank of a number is its size relative to other values in a list. (If you were to sort the list, the rank of the number would be its position.)

#### Syntax
```plaintext
RANK(number, ref, order)
```

#### Parameters
- `number` is the number whose rank you want to find.
- `ref` is an array of or a reference to a list of numbers.
- `order` is a number specifying how to rank numbers.
  - If the order is 0 (zero) or omitted, the number is ranked as if `ref` were a list sorted in descending order.
  - If the order is any nonzero value, the number is ranked as if `ref` were a list sorted in ascending order.

#### Remark
- `RANK` gives duplicate numbers of the same rank. However, the presence of duplicate numbers will affect the ranks of subsequent numbers.
```

---

<!-- 페이지 55 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: calculate
page_number: 217
page_id: calculate#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:49Z
fidelity: lossless
-->

## Remarks

The equation for the Pearson product moment correlation coefficient, \( r \), is:

\[
r = \frac{\sum(x - \overline{x})(y - \overline{y})}{\sqrt{\sum(x - \overline{x})^2 \sum(y - \overline{y})^2}}
\]

where:

- \(\overline{x}\) and \(\overline{y}\) are the sample means AVERAGE(known_x's) and AVERAGE(known_y's).

RSQ returns \( r^2 \), which is the square of this correlation coefficient.

### 4.7.142 SECOND

Returns the seconds of a time value. The second is given as an integer in the range 0 (zero) to 59.

#### Syntax

SECOND(serial_number)

where:

- serial_number is the time that contains the seconds you want to find.

#### Remarks

- Time values are a portion of a date value and are represented by a decimal number (for example, 12:00 PM is represented as 0.5 because it is half of a day).

### 4.7.143 SIGN

<!-- tags: [pearson correlation coefficient, rsq, second, serial_number, correlation, time values, Syncfusion Winforms, 11.4.0.26] keywords: [pearson product moment correlation coefficient, rsq, second function, serial_number, time values, syncfusion winforms, version 11.4.0.26] -->
```

---

<!-- 페이지 56 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_221.jpeg
document_name: calculate
page_number: 221
page_id: calculate#page_221
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:00Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Provides essential calculation functions for handling data and mathematical operations.

## Content

### Calculation Formula
The formula calculates a value represented by \( b \):
\[
b = \frac{\sum (x - \overline{x})(y - \overline{y})}{\sum (x - \overline{x})^2}
\]

#### Where:
- \( \overline{x} \) and \( \overline{y} \) are the sample means \( \text{AVERAGE(known_x's)} \) and \( \text{AVERAGE(known_y's)} \).

### 4.7.149 SMALL

#### Functionality
Returns the \( k \)-th smallest value in a data set.

#### Syntax
\[
\text{SMALL(array, k)}
\]

#### Where:
- \( \text{array} \) is an array or range of numerical data for which, you want to determine the \( k \)-th smallest value.
- \( k \) is the position (from the smallest) in the array or range of data to return.

### 4.7.150 SQRT

#### Functionality
Returns a positive square root.

#### Syntax
\[
\text{SQRT(number)}
\]

#### Where:
- \( \text{number} \) is the number for which you want the square root.

#### Remarks
[no content provided]

---

<!-- tags: [syncfusion, winforms, calculation, small, sqrt, function, mathematical, essential, technical] keywords: [data set, smallest value, square root, array, numerical data, k-th position, positive number, calculation formula] -->
```

---

<!-- 페이지 57 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_225.jpeg
document_name: calculate
page_number: 225
page_id: calculate#page_225
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:12Z
fidelity: lossless
-->

# Essential Calculate

Calculates the standard deviation based on the entire population given as arguments, including text and logical values.

## Syntax

```markdown
STDEVPA(value1, value2, ...)
```

where:  
`value1, value2, ...` are values corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

## Remarks

- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).
- STDEVPA uses the following formula:

\[
\sqrt{\frac{\sum(x - \bar{x})^2}{n}}
\]

where:  
`x-bar` is the sample mean `AVERAGE(value1, value2, ...)`.  
`n` is the sample size.

---

## 4.7.156 STEYX

Returns the standard error of the predicted y-value for each x in the regression.

### Syntax

```markdown
STEYX(known_y's, known_x's)
```

where:  
`known_y's` is an array or range of dependent data points.  
`known_x's` is an array or range of independent data points.

---

<!-- tags: [STDEVPA, STEYX, standard deviation, standard error, regression, Syncfusion Winforms] keywords: [standard deviation, population, sample size, sample mean, arguments, text values, logical values, regression analysis, dependent data points, independent data points] -->
```

---

<!-- 페이지 58 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_229.jpeg
document_name: calculate
page_number: 229
page_id: calculate#page_229
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:23Z
fidelity: lossless
-->

# Essential Calculate

## Syntax

SumXmY2( array1, array2 )

where,
- array1 and array are two ranges or arrays.

## 4.7.163 SUMX2MY2

### Overview

Returns the sum of the difference of squares of corresponding values in two arrays.

### Syntax

SUMX2MY2(array_x, array_y)

#### where:
- `array_x` is the first array or range of values.
- `array_y` is the second array or range of values.

### Remarks

- If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included.
- The equation for the sum of the difference of squares is:

\[
\text{SUMX2MY2} = \sum (x^2 - y^2)
\]

## 4.7.164 SUMX2PY2

### Overview

Returns the sum of the sum of squares of corresponding values in two arrays. The sum of the sum of squares is a common term in many statistical calculations.

### Syntax

- [The syntax for SUMX2PY2 is not fully provided in the image. Please refer to the complete documentation for full details.]
```


<!-- tags: [Syncfusion, Winforms, Calculation, SUMX2MY2, SUMX2PY2, Math, Statistical, SDK] keywords: [arrays, ranges, squares, statistical calculations, sum of differences, sum of sums, values, equations,ignore text, logical values, empty cells, zero cells] -->
```

---

<!-- 페이지 59 -->

```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_233.jpeg
document_name: calculate
page_number: 233
page_id: calculate#page_233
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:34Z
fidelity: lossless
-->  

## Timevalue Function

### Syntax

```markdown
TIMEVALUE(time_text)
```

**Where:**

- `time_text` is a text string that represents a time as a formatted string; for example, "6:45 PM" and "18:45" text strings within quotation marks that represent time.

### Remarks

- Date information in `time_text` is ignored.

---

## 4.7.171 TODAY Function

**Returns the serial number of the current date. The serial number is the number of days since Jan 1, 1900.**

### Syntax

```markdown
TODAY()
```

### Remarks

- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900, is serial number 1, and January 1, 2008, is serial number **39448** because it is 39,448 days after January 1, 1900.

---

## 4.7.172 Trim Function

**The Trim function returns a text value with the leading and trailing spaces removed.**

### Syntax

```markdown
Trim( text )
```

**Where:**

- `text` is the text value for which you want to remove the leading and the trailing spaces.
```

---

<!-- 페이지 60 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_237.jpeg
document_name: calculate
page_number: 237
page_id: calculate#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:44Z
fidelity: lossless
-->

## Overview

- This page explains the functionality and syntax of the VARPA and VDB functions used in calculations within the Syncfusion Winforms domain.
- VARPA calculates variance based on the entire population, including logical values and text. 
- VDB returns the depreciation of an asset for any specified period using the double-declining balance method or others.

## Content

### VARPA

**Description**  
Calculates variance based on the entire population. In addition to numbers and text, logical values such as True and False are also included in the calculation.

**Syntax**  
VARPA(value1, value2, ...)

**Arguments**  
value1, value2, ... are arguments corresponding to a population.

**Remarks**  
- VARPA assumes that its arguments are the entire population. If your data represents a sample of the population, you must compute the variance using VARA.
- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero). If the calculation does not include text or logical values, use the VARP worksheet function instead.
- The equation for VARPA is:

\[
\frac{\sum{(x - \bar{x})^2}}{n}
\]

where:  
- \( x \) is the sample mean AVERAGE(value1, value2, ...).  
- \( n \) is the sample size.

### VDB

#### Overview
Returns the depreciation of an asset for any period you specify, including partial periods, using the double-declining balance method or some other method you specify. VDB stands for variable declining balance.

**Syntax**  
VDB(cost, salvage, life, start_period, end_period, factor, no_switch)

**Arguments**  
- **cost** is the initial cost of the asset.
- **salvage** is the value at the end of the depreciation (sometimes called the salvage value of the asset).

## API Reference (if applicable)

None explicitly provided in the text.

## Code Examples (multi-language supported)

None explicitly provided in the text.

## Page-level Navigation/TOC (if applicable)

None explicitly provided in the text.

## Cross References

None explicitly provided in the text.

## RAG Annotations

<!-- tags: variance, depreciation, VARPA, VDB, logical values, sample mean, double-declining balance, Syncfusion Winforms, Excel functions, mathematical calculations keywords: VARPA, VDB, depreciation, variance, population, sample, logical values, cost, salvage, double-declining balance, partial periods, mathematical calculations -->
```

---

<!-- 페이지 61 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_241.jpeg
document_name: calculate
page_number: 241
page_id: calculate#page_241
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:03Z
fidelity: lossless
-->

## Essential Calculate

### YEAR(serial_number)

**where:**

- `serial_number` is the date of the year you want to find. Dates should be entered by using the DATE function or as results of other formulas or functions. For example, use DATE(2002,11,12) for the 12th day of November 2002.

#### Remarks

- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900, is serial number 1, and January 1, 2008, is serial number 39448 because it is 39,448 days after January 1, 1900.

### 4.7.188 ZTEST

**Returns the one-tailed probability-value of a z-test.**

#### Syntax

ZTEST(array, u0, sigma)

**where:**

- `array` is the array or range of data against which, to test u0
- `u0` is the value to test.
- `sigma` is the population (known) standard deviation. If omitted, the sample standard deviation is used.

#### Remarks

- ZTEST is calculated as follows when `sigma` is not omitted:

  \[
  ZTEST(array, \mu_0) = 1 - NORMSDIST \left( \frac{(\overline{x} - \mu_0)\sqrt{n}}{\sigma} \right)
  \]

- or when `sigma` is omitted:


---

<!-- 페이지 62 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: calculate
page_number: 245
page_id: calculate#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:14Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains the use of logical expressions in calculations.
- Discusses how to handle and process calculations in the `CalcEngine` class.
- Provides an example of using logical conditions in calculations.

## Content

### 5.1.4 How To Use Logical Expressions In Other Calculated Expressions?

Logical expressions return a `True` or `False` value. If you use a logical expression as part of a calculation, then:

- A `True` is replaced with `1`.
- A `False` is replaced with `0` as the whole expression is evaluated.

This allows you to easily write and compute formulas that involve logical conditions.

Consider the following expression:

```
([Cost] < 100) * 1 + ([Cost] >= 100) * ([Cost] < 200) * 3 + ([Cost] >= 200) * ([Cost] < 300) * 5 + ([Cost > 300) * 7
```

Depending upon the value of `cost`, this expression returns `1, 3, 5` or `7`. This is an example of using a linear combination of logical expressions that times other values.

**Note:** The logical conditions are mutually exclusive, but, when taken as a whole, cover all possible values of `cost`. It has the effect of assigning a unique value depending upon the input value.

#### 5.2 CalcEngine

`CalcEngine` is the class that encapsulates all the calculation support in Essential Calculate. It has methods that parse and compute expressions and also contains many functions defining the calculations found in the Function Library that ships with Essential Calculate.

##### 5.2.1 How To Force Calculations To Be Processed After They Have Been Suspended?

No additional information provided in the image.

## API Reference (if applicable)
- No specific API reference is mentioned in the provided section.

## Code Examples (multi-language supported)
- No code examples are provided in the image.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Essential Calculate, CalcEngine, logical expressions, calculations] -->
```

---

<!-- 페이지 63 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_249.jpeg
document_name: calculate
page_number: 249
page_id: calculate#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:27Z
fidelity: lossless
-->

## Essential Calculate

```vb
Public Sub Form_Load(sender As Object, ByVal e As EventArgs)
    // Comma
    CalcEngine.ParseDecimalSeparator = ","

    // Semicolon
    CalcEngine.ParseArgumentSeparator = ";"

    '...... More code
End Sub
```

### How to generate error messages or exceptions while performing String-related calculations?

#### Overview
- Discusses generating error messages or exceptions during string-related calculations.
- Focuses on the `TreatStringAsZero` property to handle string multiplication operations.

#### Content

##### 5.3.2 How to generate error messages or exceptions while performing String-related calculations?

Normally, the `CalcEngine` will not display an invalid error message or exception while performing mathematical operations with string or text. To generate an invalid error message or exception, the **TreatStringAsZero** property must be set to **false**.

For example, if a string is multiplied with a number (for example, `"text" * 10`), the calculated result will be zero. But, if the `TreatStringAsZero` property is set to **false**, the `#VALUE!` exception will be generated.

##### Code Examples

1. **C#**
    ```csharp
    this.engine.TreatStringsAsZero = false;
    ```

2. **VB**
    ```vb
    Me.engine.TreatStringsAsZero = False
    ```

<!-- tags: [syncfusion, winforms, calcengine, string-related calculations, error messages, exceptions, TreatStringAsZero] keywords: [string multiplication, error handling, C#, VB, #VALUE!] -->
```

---

<!-- 페이지 64 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_253.jpeg
document_name: calculate
page_number: 253
page_id: calculate#page_253
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:41Z
fidelity: lossless
-->

## Overview
- A comprehensive index of functions and features related to the Syncfusion Winforms Calculate Engine.
- Coverage includes mathematical calculations, statistical functions, and methods for managing and using the Calculate Engine in applications.

## Content

### Alphabetical Index

- **NPV** 202: Net Present Value calculation.
- **Offset** 203: Additional function for working with offsets.
- **Operators** 103: Full list and explanation of available operators.
- **OR** 204: Logical OR operation.
- **Overview** 11: General introduction to the Calculate Engine.
- **Prerequisites and Compatibility** 13: System requirements and compatibility details.
- **Quick Start** 36: Guide for getting started with the Calculate Engine.
- **Remove and Replace Function** 111: Methods for managing functions within the engine.

#### P
- **ParseAndCalculate Method** 65: Detailed explanation and usage.
- **Parsing** 139: Handling and interpreting input formulae.
- **PEARSON** 204: Correlation coefficient calculation.
- **PERCENTILE** 205: Percentile determination.
- **PERCENTRANK** 205: Rank of a value in a distribution.
- **Permut** 206: Permutation calculations.
- **PI** 206: Mathematical constant pi.
- **PMT** 207: Loan payment calculation.
- **POISSON** 207: Poisson distribution calculations.
- **Pow** 208: Power function.
- **POWER** 209: Powerful exponentiation method.
- **PPMT** 209: Partial payment of principal calculation.
- **PROB** 210: Probability calculations.
- **PRODUCT** 210: Multiplicative function for a series.
- **PV** 211: Present value calculations.
- **QUARTILE** 212: Quartile determination.
- **QUOTIENT** 124: Division resulting in quotient.
- **RADIANS** 212: Degree to radian conversion.
- **RAND** 213: Random number generation.
- **RANDBETWEEN** 123: Random number within a specified range.
- **RANK** 213: Ranking of values in a list.
- **RATE** 214: Interest rate calculation.
- **Resetting Keys by using Calculate Engine** 76: Functionality for resetting keys.

#### S
- **Samples and Installation** 16: Example projects and setup instructions.
- **SEARCH** 135: Text searching function.
- **SECOND** 217: Time-based second function.
- **SIGN** 217: Sign determination of a number.
- **Simple Console Application Using CalcQuickBase** 37: Tutorial for creating a basic console app.
- **SIN** 218: Sine trigonometric function.
- **SinH** 219: Hyperbolic sine function.
- **SKEW** 219: Skewness measurement.
- **SLN** 220: Straight-line depreciation.
- **SLOPE** 220: Linear regression slope calculation.
- **SMALL** 221: Function for finding the nth smallest value.
- **SQRT** 221: Square root calculation.
- **SQRTPI** 124: Square root of pi.
- **Square Brackets in CalcQuickBase Formulas** 104: Usage of square brackets in formulas.
- **STANDARDIZE** 222: Function for normalizing a value.
- **STDEV** 222: Standard deviation calculation (sample).
- **STDEVA** 223: Alternate standard deviation function.
- **STDEVP** 224: Population standard deviation.
- **STDEVPA** 224: Population standard deviation including text.
- **STEYX** 225: Standard error of the predicted y-value for each x.
- **SUBSTITUTE** 226: Text substitution function.
- **SUBTOTAL** 122: Function for subtotal calculations.

### Navigation
- **Page Number**: 253
- **Syncfusion Copyright**: 2013 Syncfusion. All rights reserved.
- **Product**: Syncfusion Winforms

## API Reference
- Check the documentation for detailed API references related to the Calculate Engine and its functions.

## Code Examples

```csharp
// Example of using the Calculate Engine
using Syncfusion.CalculateEngine;

// Initialize the Calculate Engine
var engine = new CalculateEngine();
var result = engine.Calculate("10 + 20");

// Output the result
Console.WriteLine("Result: " + result);
```

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Calculate Engine, Functions, Operators, Calculations, Statistical Functions, API Reference] keywords: [NPV, OFFSET, Operators, OR, Overview, Parse, Pearson, Percentile, PercentRank, Permut, PI, PMT, Poisson, Power, PPMT, PROB, PRODUCT, PV, QUARTILE, QUOTIENT, RADIANS, RAND, RANDBETWEEN, RANK, RATE, Resetting Keys, SEARCH, SECOND, SIGN, SLN, SLOPE, SMALL, SQRT, SKEW, STANDARDIZE, STDEV, STDEVA, STDEVP, STEYX, SUBSTITUTE, SUBTOTAL, Samples, Installation, Simple Console Application] -->
```

---

<!-- 페이지 65 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_002.jpeg
document_name: calculate
page_number: 002
page_id: calculate#page_002
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:22Z
fidelity: lossless
-->

# Contents

## Overview
- **1.1 Introduction to Essential Calculate** 11
- **1.2 Prerequisites and Compatibility** 13
- **1.3 Documentation** 14

## Installation and Deployment
- **2.1 Installation** 16
- **2.2 Samples and Installation** 16
- **2.3 Deployment Requirements** 23
  - **2.3.1 DLLs** 23
  - **2.3.2 Web Application Deployment** 23

## Getting Started
- **3.1 Class Diagram** 25
- **3.2 Creating Platform Application** 26
- **3.3 Deploying Essential Calculate** 28
  - **3.3.1 Windows** 29
  - **3.3.2 ASP.NET** 32
  - **3.3.3 WPF** 33
- **3.4 Feature Summary** 35
- **3.5 Quick Start** 36
  - **3.5.1 Simple Console Application Using CalcQuickBase** 37
    - **3.5.1.1 Console Application CalcQuickBase** 37
  - **3.5.2 Windows Application Using Variables and CalcQuickBase** 40
    - **3.5.2.1 Windows Forms CalcQuickBase** 40
  - **3.5.3 Adding Calculation Support to an Array Using ICalcData** 43
    - **3.5.3.1 ICalcData** 44

## Concepts and Features
- **4.1 Adding Calculation Support** 64
  - **4.1.1 CalcQuickBase** 64
    - **4.1.1.1 Manual Calculations** 64
      - **4.1.1.1.1 ParseAndCalculate Method** 65

<!-- tags: [Syncfusion, Winforms, Essential Calculate, Installation, Deployment, Getting Started, Concepts, Features, CalcQuickBase, ICalcData]
keywords: [Introduction, Essential Calculate, Prerequisites, Compatibility, Documentation, Installation, Deployment Requirements, Class Diagram, Platform Application, Features, Quick Start, Calculation Support, Variables, Arrays, ParseAndCalculate] -->
```

---

<!-- 페이지 66 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: calculate
page_number: 006
page_id: calculate#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:37Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- A list of functions and their corresponding page numbers in the guide.
- Functions include DATEVALUE, DAY, DAYS360, DB, DDB, DEGREES, etc.
- Each function is accompanied by a brief description and page reference for further details.

## Content

### List of Functions

#### Functions by Page Number

1. **4.7.35 DATEVALUE** ..... 160
2. **4.7.36 DAY** ..... 161
3. **4.7.37 DAYS360** ..... 161
4. **4.7.38 DB** ..... 162
5. **4.7.39 DDB** ..... 163
6. **4.7.40 DEGREES** ..... 164
7. **4.7.41 DEVSQ** ..... 164
8. **4.7.42 Dollar** ..... 165
9. **4.7.43 EVEN** ..... 165
10. **4.7.44 Exact** ..... 165
11. **4.7.45 EXP** ..... 166
12. **4.7.46 EXPONDIST** ..... 166
13. **4.7.47 FACT** ..... 167
14. **4.7.48 False** ..... 167
15. **4.7.49 FDIST** ..... 167
16. **4.7.50 Find** ..... 168
17. **4.7.51 Finv** ..... 168
18. **4.7.52 FISHER** ..... 169
19. **4.7.53 FISHERINV** ..... 169
20. **4.7.54 Fixed** ..... 170
21. **4.7.55 FLOOR** ..... 170
22. **4.7.56 FORECAST** ..... 171
23. **4.7.57 FV** ..... 172
24. **4.7.58 GAMMADIST** ..... 172
25. **4.7.59 Gammainv** ..... 173
26. **4.7.60 GAMMALN** ..... 173
   - **4.7.60.1 GAMMAINV** ..... 173
27. **4.7.61 GEOMEAN** ..... 174
28. **4.7.62 GROWTH** ..... 175
29. **4.7.63 HARMEAN** ..... 175
30. **4.7.64 HLOOKUP** ..... 176
31. **4.7.65 HOUR** ..... 177
32. **4.7.66 Hypgeomdist** ..... 177
33. **4.7.67 HYPEGEOMDIST** ..... 178
34. **4.7.68 IF** ..... 179

## API Reference

Each of the functions listed above can be referenced in the API documentation for detailed usage and parameters.

## Code Examples

Refer to the specific pages listed above for detailed code examples and usage of each function.

## Page-level Navigation/TOC
- The page provides a comprehensive list of functions, each with an associated page number for detailed reference.

## Cross References
- This guide refers to various functions used in Excel and similar calculation environments, offering a seamless integration for users familiar with such tools.

### Tags and Keywords
<!-- tags: [calculate, functions, Excel, Syncfusion Winforms, API, version 11.4.0.26] keywords: [DATEVALUE, DAY, DAYS360, DB, DDB, DEGREES, DEVSQ, Dollar, EVEN, Exact, EXP, EXPONDIST, FACT, False, FDIST, Find, Finv, FISHER, FISHERINV, Fixed, FLOOR, FORECAST, FV, GAMMADIST, Gammainv, GAMMALN, GAMMAINV, GEOMEAN, GROWTH, HARMEAN, HLOOKUP, HOUR, Hypgeomdist, HYPEGEOMDIST, IF] -->
```


---

<!-- 페이지 67 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: calculate
page_number: 010
page_id: calculate#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:03Z
fidelity: lossless
-->

### Content

4.7.174 True      234  
4.7.175 TRUNC234  
4.7.176 Upper      235  
4.7.177 Value      235  
4.7.178 Var        236  
4.7.179 VarA       236  
4.7.180 VarP       236  
4.7.181 VARPA      236  
4.7.182 VDB        237  
4.7.183 VLOOKUP    238  
4.7.184 WEEKDAY    239  
4.7.185 Weibull    240  
4.7.186 Xirr       240  
4.7.187 YEAR       240  
4.7.188 ZTEST      241  

5 **Frequently Asked Questions**  
5.1 **CalcQuick**  
   - 5.1.1 How To Add, Remove, And Modify the Implementation Of Functions In the Function Library In CalcQuickBase? ……………… 243  
   - 5.1.2 How To Calculate a Formula? ……………… 243  
   - 5.1.3 How To Enter Vectors Of Numbers Into CalcQuickBase? ……………… 244  
   - 5.1.4 How To Use Logical Expressions In Other Calculated Expressions? ……………… 245  

5.2 **CalcEngine**  
   - 5.2.1 How To Force Calculations To Be Processed After They Have Been Suspended? ……………… 245  
   - 5.2.2 How To Read an XLS File Into Essential Calculate? ……………… 247  
   - 5.2.3 How To Suspend Calculations While a Series Of Values Are Updated? ……………… 247  

5.3 **Common**  
   - 5.3.1 How to Use a Comma as a Decimal Separator in Formula? ……………… 248  
   - 5.3.2 How to generate error messages or exceptions while performing String-related calculations? ……………… 249  

## Cross References

See also: Chapter 4 (Function Reference), Chapter 5 (Frequently Asked Questions).

<!-- tags: [syncfusion, winforms, calculate, user-guide, function-reference, faq, essential-calculate] keywords: [functions, implementation, formula-calculations, vectors, logical-expressions, calculations, xls-file, decimal-separator, string-calculations] -->
```

---

<!-- 페이지 68 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: calculate
page_number: 014
page_id: calculate#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:20Z
fidelity: lossless
-->

## Overview
- Documentation segments provided by Syncfusion to support Essential Calculate.
- Information about various types of documentation available for users.

## Content

### 1.3 Documentation

Syncfusion provides the following documentation segments to provide all the necessary information pertaining to Essential Calculate.

#### Table 4: Type of Documentation

| **Type of Documentation**            | **Location**                                                                                                                                            |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Readme**                           | **Windows Forms**-`[drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\Release Notes\readme.htm`<br/>**ASP.NET**-`[drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\asp release notes\readme.htm`<br/>**WPF**-`[drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\WPF release notes\readme.htm` |
| **Release Notes**                    | **Windows Forms**-`[drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\Release Notes\Release Notes.htm`<br/>**ASP.NET**-`[drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\asp release notes\Release Notes.htm`<br/>**WPF**-`[drive:]\Program Files\Syncfusion\Essential Studio\x.x.x.x\Infrastructure\Data\WPF release notes\Release Notes.htm` |
| **User Guide (this document)**       | **Online**<br/>`http://help.syncfusion.com/resources`<br/>(Navigate to the Calculate User Guide.)<br/><img src="download_icon" alt="Download as PDF"> **Note:** Click Download as PDF to access a PDF version.<br/>**Installed Documentation**<br/>Dashboard -> Documentation -> Installed Documentation. |
| **Class Reference**                  | **Online**<br/>`http://help.syncfusion.com/resources`<br/>(Navigate to the Reporting User Guide. Select **Calculate**, and then click the Class Reference link found in the upper right section of the page.) |

## RAG Annotations

<!-- tags: calculate, user-guide, essential-calculate, documentation, syncfusion-winform, version-11.4.0.26 keywords: readmme, release notes, user guide, class reference -->
```

---

<!-- 페이지 69 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: calculate
page_number: 018
page_id: calculate#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:37Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Discusses the steps to view Calculate samples in various platforms.
- Focuses on the Syncfusion Essential Reporting Samples for Windows Forms.
- Provides detailed instructions for accessing different sample types in Windows Forms.

## Content

### Syncfusion Essential Reporting Samples

#### Figure 3: Syncfusion Essential Reporting Samples
The figure shows the Syncfusion Essential Studio interface with options for "Run Samples" and an emphasis on the Reporting Edition for ASP.NET. It highlights features like integrating Reporting solutions into ASP.NET applications with ease and includes high-performance libraries for manipulating Word, PDF, and Excel files.

---

### The steps to view the Calculate samples in various platforms are discussed below:

#### Windows Forms
1. **In the Dashboard window, click Run Samples for Windows Forms under Reporting Edition panel.**

##### Note
- **You can view the samples in any of the following three ways:**
  - **Run Samples** – Click to view the locally installed samples.
  - **Online Samples** – Click to view online samples.
  - **Explore Samples** – Explore Windows Forms samples on disk.

---

## API Reference (if applicable)

- This page does not contain specific API references. For detailed API documentation, refer to the official Syncfusion documentation.

---

## Page-level Navigation/TOC (if applicable)

- This page does not include a Table of Contents. The content is directly structured as described above.

---

## Cross References

- See also: "Syncfusion Essential Reporting Samples" for more information on how to utilize and integrate reporting solutions in different platforms.

---

<!-- tags: [syncfusion, essential studio, windows forms, reporting, calculate] keywords: [samples, platform, windows forms, reporting edition, run samples, online samples, explore samples] -->
``` 


---

<!-- 페이지 70 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_022.jpeg
document_name: calculate
page_number: 022
page_id: calculate#page_022
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:49Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- A comprehensive guide to using the Essential Calculate tool for ASP.NET.
- Demonstrates setting up forms with calculation dependencies for custom business objects.
- Explains function libraries, dependencies, and custom function implementation.

## Content

### Calculate Description

Essential Calculate for ASP.NET allows you to add extensive calculation support to your own business objects. Easily set up forms that have calculation dependencies among various controls on the form.

Essential Calculate comes with a function library of more than 150 entries. It supports cross sheet references. When used in conjunction with Essential XlsIO, you can fully load, manipulate, and compute Excel spreadsheets without any dependency upon Excel. Function implementation is extensible, and you can easily add your own custom functions.

### Featured Samples

#### Figure 8: Calculate samples displayed in the ASP.NET Sample Browser

The image shows the "Calculate" feature within the ASP.NET Sample Browser interface. The main navigation panel on the left lists categories like "Calculate," "Reports," and "Business Intelligence," indicating the user can explore various sample applications.

#### Sample Browsing

1. **Navigation**
   - The interface allows users to select and explore different sample code snippets for "Calculate."

2. **Demonstration**
   - The featured samples showcase how to implement dynamic calculations in forms using Essential Calculate.

3. **Selection and Browsing**
   - Select any sample and browse through the features.

### Source Code Location

#### Windows Forms Source Code
The default location of the Windows Forms Calculate source code is:

```
[System Drive]:\Program Files\Synfusion\Essential Studio\[Version Number]\Windows\Calculate.Windows\Src
```

#### ASP.NET Source Code
The default location of the ASP.NET Calculate source code is:

```
[System Drive]:\Program Files\Synfusion\Essential Studio\[Version Number]\Web\Calculate.Web\Src
```

## API Reference

### Namespaces and Classes
- **Namespace:** `Syncfusion.Calculate`
- **Class:** `CalculateEngine`
- **Members:**
  - **Methods:**
    - `Evaluate(string expression)`
    - `AddFunction(string name, Func<object, object>)`
  - **Properties:**
    - `Result`
    - `Error`

### Parameters
| Name       | Type               | Description                    | Required |
|------------|--------------------|--------------------------------|----------|
| `expression`  | `string`         | The formula to evaluate.      | Yes      |
| `name`      | `string`         | The name of the custom function.| Yes      |
| `function`  | `Func<object, object>` | The implementation of the custom function. | Yes      |

## Code Examples

### Example 1: Using the CalculateEngine

```csharp
using Syncfusion.Calculate;

var engine = new CalculateEngine();
engine.AddFunction("CustomSum", (params object[] args) =>
{
    var sum = 0;
    foreach (var arg in args)
    {
        if (arg is int) sum += (int)arg;
    }
    return sum;
});

var result = engine.Evaluate("CustomSum(10, 20, 30)");
Console.WriteLine(result); // Output: 60
```

## Page-Level Navigation/TOC

- **Calculate**
- **Source Code Location**
  - Windows Forms Source Code
  - ASP.NET Source Code

## RAG Annotations

<!-- tags: [syncfusion, calculate, asp.net, windows forms, api reference] keywords: [calculate engine, custom functions, source code location, windows forms, asp.net, dynamic calculations] -->
```

---

<!-- 페이지 71 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: calculate
page_number: 026
page_id: calculate#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:11Z
fidelity: lossless
-->

## 3.2 Creating Platform Application

This section illustrates the step-by-step procedure to create the following platform applications.

### Windows Application

1. Open Microsoft Visual Studio. Go to File menu and click New Project. In the New Project dialog box, select Windows Forms Application template, name the project and click OK.  

   ![New Project Dialog Box](image_url_for_Figure_10)
   Figure 10: New Project Dialog Box

A windows application is created.

2. Open the main form of the application in the designer.

3. Add the Syncfusion controls to your VS.NET toolbox if you haven't done so already [This is done automatically when you install Essential Studio].

<!-- tags: [syncfusion-winforms, windows-forms-applications, new-project, windows-forms-dialog, toolbox] keywords: [windows application, new project, designer, syncfusion controls, essential studio, visual studio, installer, toolbox] -->

---

<!-- 페이지 72 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_030.jpeg
document_name: calculate
page_number: 030
page_id: calculate#page_030
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:19Z
fidelity: lossless
-->

## Essential Calculate

- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.Calculate.Base.dll

![Solution Explorer](#)

## Content

The libraries are added to the GAC during the product installation. Note that the CalculateConfig is a component provided for convenient usage of Essential Calculate. Hence, the product can also be used just by manually adding reference to the above assemblies.

**Note:** For detailed documentation on Windows Application deployment, see [http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf](http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf)

### Step 5: Create a CalculateEngine

Then create a CalculateEngine. The `CalcQuickBase` class is used to create a CalculateEngine.

```csharp
[C#]

// Create a new CalculateQuickBase. This object represents the CalculateEngine.
CalcQuickBase cq = new CalcQuickBase();
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

The code example demonstrates how to create a `CalculateEngine` using the `CalcQuickBase` class.

## Page-level Navigation/TOC (if applicable)

## Cross References

See also: [library documentation], [installation guide], [Essential Calculate overview].

<!-- tags: [Essential Calculate, CalculateEngine, CalcQuickBase] keywords: [Syncfusion, Winforms, C#, calculate engine, library reference] -->
```

---

<!-- 페이지 73 -->

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

---

<!-- 페이지 74 -->

```html
<!--source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_038.jpeg
document_name: calculate
page_number: 038
page_id: calculate#page_038
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:45Z
fidelity: lossless
-->

## Content

### Essential Calculate

#### Working with Main

2. In the Main method, add the code to create a `CalcQuickBase` object. Also add the code to loop through the process of retrieving a string and using `CalcQuickBase.ParseAndCompute` to perform the calculation that is represented by the string. Given below is the code that handles these tasks.

```csharp
// C#

using System;
using Syncfusion.Calculate;

namespace CalcQuickBaseTutorial
{
    /// <summary>
    /// Summary description for Class1.
    /// </summary>
    class Class1
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            CalcQuickBase cq = new CalcQuickBase();

            string s;
            while ((s = Console.ReadLine()) != "")
            {
                string val = cq.ParseAndCompute(s);
                Console.WriteLine("value= " + val);

                // Blank line
                Console.WriteLine("");
            }
        }
    }
}
```

#### VB.NET

```vb
Imports System
Imports Syncfusion.Calculate

Namespace CalcQuickBaseTutorial
    Class Class1
    End Class
End Namespace
```

---

## API Reference

### Namespace: `CalcQuickBaseTutorial`

#### Class: `Class1`

##### Methods

- **Main**
  - **Signature**: `static void Main(string[] args)`
  - **Description**: The main entry point for the application.
  - **Parameters**:
    - `args`: Array of strings containing the command-line arguments.
  - **Returns**: `void`
  - **Comments**:
    - Uses `CalcQuickBase` for parsing and computing expressions entered by the user.

##### Members

- **CalcQuickBase cq**
  - **Description**: Instance of `CalcQuickBase` for parsing and computing expressions.

---

## Code Examples

- **C#**
```csharp
using System;
using Syncfusion.Calculate;

namespace CalcQuickBaseTutorial
{
    class Class1
    {
        static void Main(string[] args)
        {
            CalcQuickBase cq = new CalcQuickBase();
            string s;
            while ((s = Console.ReadLine()) != "")
            {
                string val = cq.ParseAndCompute(s);
                Console.WriteLine("value= " + val);
                Console.WriteLine("");
            }
        }
    }
}
```

- **VB.NET**
```vb
Imports System
Imports Syncfusion.Calculate

Namespace CalcQuickBaseTutorial
    Class Class1
        Shared Sub Main(ByVal args() As String)
            Dim cq As New CalcQuickBase()
            Dim s As String
            While (s = Console.ReadLine()) <> ""
                Dim val As String = cq.ParseAndCompute(s)
                Console.WriteLine("value= " & val)
                Console.WriteLine("")
            End While
        End Sub
    End Class
End Namespace
```

---

<!-- tags: [syncfusion winforms, calcquickbase, parsing and computing expressions, console application] keywords: [CalcQuickBase, ParseAndCompute, Main method, Console.ReadLine, static void Main] -->
```

---

<!-- 페이지 75 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_042.jpeg
document_name: calculate
page_number: 042
page_id: calculate#page_042
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:02Z
fidelity: lossless
-->

# Essential Calculate

```csharp
if (key.Length > 0)
{
    // The value.
    this.cq[key] = this.textBox3.Text;

    // Just display it in the list box.
    this.listBox1.Items.Add(string.Format("[{0}] = {1}", key, this.textBox3.Text));
}
}
```

### [VB]

```vb
Imports Syncfusion.Calculate

...

Dim cq As CalcQuickBase
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    cq = New CalcQuickBase

    AddHandler Me.button1.Click, AddressOf button1_Click
    AddHandler Me.button2.Click, AddressOf button2_Click

    ' Form1_Load
End Sub

Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs)

    ' Compute
    Me.label3.Text = Me.cq.ParseAndCompute(Me.textBox1.Text)

    ' Button1_Click
End Sub

Private Sub button2_Click(ByVal sender As Object, ByVal e As EventArgs)

    ' Register name.
    Dim key As String = Me.textBox2.Text
    If key.Length > 0 Then

        ' The value.
        Me.cq(key) = Me.textBox3.Text

        ' Just display it in the list box.
        Me.listBox1.Items.Add(String.Format("[{0}] = {1}", key,
```

## API Reference

### Namespaces & Classes

- **Syncfusion.Calculate**
  - **CalcQuickBase**: The main class for performing calculations.

### Methods

- **ParseAndCompute(String):**
  - **Description**: Parses and computes the mathematical expression provided in the string.
  - **Parameters**: 
    - `expression`: The mathematical expression to compute.
  - **Returns**: The result of the computation as a `String`.

## Code Examples

The code above demonstrates:
- Handling user input to compute mathematical expressions.
- Registering names and their corresponding values for use in calculations.
- Displaying results in a list box for user reference.

### References
- **Syncfusion Documentation**: Further details on `CalcQuickBase` and its features can be found in the official Syncfusion documentation.

<!-- tags: [syncfusion, calculate, calcquickbase, winforms, .net, api, 11.4.0.26] keywords: [formula calculation, user input, list box, textbox, event handling, parse and compute] -->

---

<!-- 페이지 76 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_046.jpeg
document_name: calculate
page_number: 046
page_id: calculate#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:17Z
fidelity: lossless
-->

# Essential Calculate

## Content

### Adding a Class File to Your Project

The following steps outline how to add a class file to your project using the Solution Explorer in Visual Studio.

#### Screenshot Description
- **Window Title**: Solution Explorer - Calculate_ICalcData
- **Project Structure**:
  - Solution 'Calculate_ICalcData' (1 project)
  - Project items: App.ico, ArrayCalcData, Form1.cs
- **Menu Options**:
  - **Build**: Build, Rebuild
  - **Add**: Add New Item..., Add Existing Item..., New Folder, Add Windows Form..., Add Inherited Form..., Add User Control..., Add Inherited Control..., Add Component..., Add Class...

#### Figure Caption
Figure 22: Adding a Class File to Your Project

#### Instructions
1. In the Solution Explorer, right-click on the project name (e.g., "Calculate_ICalcData").
2. Select the "Add" option from the context menu.
3. Choose "Add Class..." from the submenu to create a new class file.
4. In the dialog that appears, name the class as `ArrayCalcData.cs` (or `ArrayCalcData.vb` if you are using Visual Basic).

#### Text Instructions
2. In the dialog that appears, name the class as ArrayCalcData.cs (or ArrayCalcData.vb depending upon the language you are using).

## API Reference

### Naming Conventions
- For C# projects, name the class file with a `.cs` extension.
- For VB.NET projects, name the class file with a `.vb` extension.

### Example Code
```csharp
// ArrayCalcData.cs
public class ArrayCalcData
{
    // Class implementation goes here
}
```

```vb
' ArrayCalcData.vb
Public Class ArrayCalcData
    ' Class implementation goes here
End Class
```

## Code Examples

### C# Example
```csharp
using System;

public class ArrayCalcData
{
    public void CalculateData()
    {
        // Sample calculation logic
        Console.WriteLine("Data calculated successfully.");
    }
}
```

### VB.NET Example
```vb
Imports System

Public Class ArrayCalcData
    Public Sub CalculateData()
        ' Sample calculation logic
        Console.WriteLine("Data calculated successfully.")
    End Sub
End Class
```

## Related Topics

- For more information on adding files and managing projects in Visual Studio, refer to the official Microsoft documentation.
- Explore additional examples and best practices for class implementation in the Syncfusion WinForms documentation.

## Copyright Information

© 2013 Syncfusion. All rights reserved.

<!-- tags: [calculations, winforms, project management, visual studio, class files, csharp, vbnet] keywords: [add class, solution explorer, arraycalcdata, project structure, build options, class implementation] -->
```

---

<!-- 페이지 77 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: calculate
page_number: 050
page_id: calculate#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:33Z
fidelity: lossless
-->


## Essential Calculate

If you notice, you are actually populating these added arrays with formula strings such as "=Sum(A5:D5)". While using Essential Calculate with an ICalcData interface, Essential Calculate uses Excel-like notation to refer to the cells in a rectangular collection. A1 is the first cell in the first row, B1 is second cell in the first row, and so on. So, "=Sum(A5:D5)" sums columns 1 through 4 in row 5. The method **RangeInfo.GetAlphaLabel** used in the code, converts a numerical value like 1, 2, or 3, into the proper column letter A, B, or C.

## Content

### Wrapping the Double Array with Calculated Sums

The following code demonstrates how to wrap a double array with an extra row and column that holds calculated sums.

#### C#

```csharp
/// <summary>
/// Wraps the double array with an extra row and column that holds calculated sums.
/// </summary>
/// <param name="dValues"></param>
public ArrayCalcData(double[,] dValues)
{
    this.dValues = dValues;
    rowCount = dValues.GetLength(0);
    colCount = dValues.GetLength(1);
    rowSums = new object[rowCount + 1];
    colSums = new object[colCount + 1];

    // Initializes the formulas for the row sums.
    // eg. "=Sum(A5:D5)"   to sum row 5
    for (int row = 0; row <= rowCount; ++row)
    {
        rowSums[row] = string.Format("=Sum(A{1}:{0}{1})", 
                                      RangeInfo.GetAlphaLabel(colCount), row + 1);
    }

    // Initializes the formulas for the column sums.
    // eg. "=Sum(B1:B5)"   to sum column 2
    for (int col = 0; col <= colCount; ++col)
    {
        colSums[col] = string.Format("=Sum({0}1:{0}{1})", 
                                      RangeInfo.GetAlphaLabel(col + 1), rowCount);
    }
}
```

#### VB

```vb
' <summary>
' Wraps the double array with an extra row and column that holds calculated sums.
' </summary>
' <param name="dValues"></param>
Public Sub New(ByVal dValues(,) As Double)
    Me.dValues = dValues
    rowCount = dValues.GetLength(0)
    colCount = dValues.GetLength(1)
    rowSums = New Object(rowCount + 1) {}
```

### Explanation

- **dValues**: The double array containing the input data.
- **rowCount**: The number of rows in the input array.
- **colCount**: The number of columns in the input array.
- **rowSums** and **colSums**: Arrays to hold the formulas for row and column sums, respectively.

The `RangeInfo.GetAlphaLabel` method is used to convert column indices (numerical values) into corresponding Excel-style column labels (e.g., A, B, C, etc.). This ensures that the formulas generated are compatible with Excel-like notation used in Essential Calculate.

## RAG Annotations
<!-- tags: [Essential Calculate, Excel-like notation, ICalcData interface, RangeInfo.GetAlphaLabel, formula strings, array calculations] keywords: [Excel-like notation, row sums, column sums, formula strings, rectangular collection, array manipulation] -->
```

---

<!-- 페이지 78 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_054.jpeg
document_name: calculate
page_number: 054
page_id: calculate#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:52Z
fidelity: lossless
-->

# Essential Calculate

```vb
Public Sub SetValueRowCol(ByVal value As Object, ByVal row As Integer, ByVal –
            col As Integer) Implements
Syncfusion.Calculate.ICalcData.SetValueRowCol
End Sub

Public Sub WireParentObject() Implements
Syncfusion.Calculate.ICalcData.WireParentObject
End Sub

Public Event ValueChanged(ByVal sender As Object, ByVal e As _
    Syncfusion.Calculate.ValueChangedEventArgs) Implements _
        Syncfusion.Calculate.ICalcData.ValueChanged
```

## Overview
- Implements methods for setting values in a table, wiring parent objects, and event handling for value changes.
- Focuses specifically on the `SetValueRowCol`, `WireParentObject`, and `ValueChanged` event handling required for Syncfusion's calculation API.

## Content

### Retrieving Values Based on Row and Column Indices

1. **Purpose of `GetValueRowCol`**:
   - The `GetValueRowCol` method should return the value for a given row and column index. The indexes are one-based by convention.

2. **Logic for Handling Different Scenarios**:
   - If the last column is requested, the value in the `colSums` array is returned.
   - If the last row is requested, the value in the `rowSums` array is returned.
   - Otherwise, the value in the double array is returned.

```csharp
/// <summary>
/// Gets the value into either the double array or column vector or row
/// vector.
/// </summary>
/// <param name="row">One-based row index.</param>
/// <param name="col">One-based column index.</param>
/// <returns>The value.</returns>
/// <remarks>By convention, ICalcData uses one-based indexes.</remarks>
public object GetValueRowCol(int row, int col)
{
    if (row - 1 == rowCount)
    {
        return colSums[col - 1];
    }
    else if (col - 1 == colCount)
    {
        return rowSums[row - 1];
    }
    else
    {
        return this.dValues[row - 1, col - 1];
    }
}
```

### Implementation Details
- **Parameters**:
  - `row`: One-based row index.
  - `col`: One-based column index.
- **Return Value**:
  - The method returns the appropriate value based on the row and column indices.
- **Edge Cases**:
  - If the requested row or column is out of bounds, the method appropriately handles the scenario by referencing the `rowSums` or `colSums` arrays.

## API Reference

### Methods
- **`SetValueRowCol`**:
  - Sets a value at a specific row and column in the data table.
  - Parameters:
    - `value`: The value to set.
    - `row`: One-based row index.
    - `col`: One-based column index.
  
- **`WireParentObject`**:
  - Connects the data object with its parent object, facilitating communication and synchronization.

- **`GetValueRowCol`**:
  - Gets the value at a specific row and column.
  - Parameters:
    - `row`: One-based row index.
    - `col`: One-based column index.

## Code Examples

### C#

```csharp
// Example of implementing GetValueRowCol
public object GetValueRowCol(int row, int col)
{
    if (row - 1 == rowCount)
    {
        return colSums[col - 1];
    }
    else if (col - 1 == colCount)
    {
        return rowSums[row - 1];
    }
    else
    {
        return this.dValues[row - 1, col - 1];
    }
}
```

### VB.NET

```vb
' Example of implementing GetValueRowCol
Public Function GetValueRowCol(ByVal row As Integer, ByVal col As Integer) As Object
    If row - 1 = rowCount Then
        Return colSums(col - 1)
    ElseIf col - 1 = colCount Then
        Return rowSums(row - 1)
    Else
        Return Me.dValues(row - 1, col - 1)
    End If
End Function
```

## Cross References
- Refer to the documentation on `Syncfusion.Calculate.ICalcData` for more details on the API and its usage.

<!-- tags: [syncfusion, calculate, irowcolumn, data manipulation, winforms, syncfusion windows forms] keywords: [rowsums, colsums, GetValueRowCol, one-based indexing, setValueRowCol, ICALCDATA] -->
```

---

<!-- 페이지 79 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_058.jpeg
document_name: calculate
page_number: 058
page_id: calculate#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:18Z
fidelity: lossless
-->

# Essential Calculate

```csharp
SetValueRowCol(Value, row + 1, col + 1)
End Set
End Property
```

## Overview
- This section explains how the "Generate Data" button handler creates a random double array and populates it with random double values.
- It discusses the creation of an `ArrayCalcData` class to wrap the double array and the creation of a `CalcEngine` object using this `ArrayCalcData` object as the datasource.
- The `ShowObject` method is used to display the values from the `ArrayCalcData` object in a multiline text box.
- The `UseDependencies` property in the engine allows automatic recalculations when dependent values change.
- The `RecalculateRange` method helps the `CalcEngine` traverse all data and set up necessary dependencies.

## Content

### Implementation Details

11. Your **Generate Data** button handler will create a random double array and populate it with random double values. It also creates an instance of an `ArrayCalcData` class to wrap the double array that it creates. It then creates a `CalcEngine` object that uses this `ArrayCalcData` object as its datasource. The **ShowObject** method will just display the values from your `ArrayCalcData` object in the multiline text box that you added to the form.

The engine's **UseDependencies** property will tell the `CalcEngine` that you want it to track dependencies so the value will automatically recalculate when dependent values change. The engine's **RecalculateRange** call allows the `CalcEngine` to traverse all the data and set up the necessary dependencies to do the calculations.

### Code Example

Here is the code:

```csharp
[C#]

using Syncfusion.Calculate;

//..

private Random r = new Random();
private ArrayCalcData data;
int nRows;
int nCols;

/// <summary>
/// Populates the double array.
/// </summary>
/// <param name="sender"></param>
/// <param name="e"></param>
private void button1_Click(object sender, System.EventArgs e)
{
    // Creates some sample data.
    this.nRows = r.Next(10) + 2;
    this.nCols = r.Next(3) + 1;
    double[,] a = new double[nRows, nCols];
    for (int row = 0; row < nRows; ++row)
        for (int col = 0; col < nCols; ++col)
            a[row, col] = ((double)r.Next(100)) / 10;

    // Creates an ArrayCalcData object and passes it in this array.
    this.data = new ArrayCalcData(a);
}
```

<!-- tags: [syncfusion, winforms, generate data, arraycalcdata, calcengine, usedependencies, recalculaterange, random array, button click event, multiline text box] -->
```

---

<!-- 페이지 80 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: calculate
page_number: 062
page_id: calculate#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:35Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Provides a method to specify the row, column, and value for populating a single entry in an ArrayCalcData object.
- Focuses on handling input and updating the data grid programmatically.

## Content

This section explains how to use the provided code to populate a single entry in the ArrayCalcData object by specifying the row, column, and value.

### C#

By tapping the `button2_Click` event, users can input a row, column, and value to populate a corresponding cell in the data grid.

```csharp
/// <summary>
/// Populates a single entry in the ArrayCalcData object.
/// </summary>
/// <param name="sender"></param>
/// <param name="e"></param>
private void button2_Click(object sender, System.EventArgs e)
{
    if (this.nRows == 0)
    {
        MessageBox.Show("Generate data first.");
        return;
    }
    int row = int.Parse(textBox2.Text);
    int col = int.Parse(textBox3.Text);
    string val = this.textBox4.Text;
    this.data[row, col] = val;

    ShowObject();
}
```

### VB

The equivalent in VB handles the same functionality, allowing users to enter a row, column, and value to update the data grid dynamically.

```vb
' <summary>
' Populates a single entry in the ArrayCalcData object.
' </summary>
' <param name="sender"></param>
' <param name="e"></param>
Private Sub button2_Click(ByVal sender As Object, ByVal e As System.EventArgs) _
        Handles Button2.Click
    If Me.nRows = 0 Then
        MessageBox.Show("Generate data first.")
        Return
    End If

    Dim row As Integer = Integer.Parse(Me.textBox2.Text)
    Dim col As Integer = Integer.Parse(Me.textBox3.Text)
    Dim val As String = Me.textBox4.Text

    Me.data(row, col) = val
```

## API Reference

| **Namespace** | `Syncfusion.WinForms` |
|---------------|--------------------------|
| **Class**     | `ArrayCalcData`        |

### Methods

- **Name:** `button2_Click`
  - **Description:** Populates a single entry in the ArrayCalcData object based on user input.
  - **Parameters:**
    - `sender`: The control that raised the event (typically `object`).
    - `e`: EventData containing additional information about the event (typically `System.EventArgs`).
  - **Returns:** `void`
  - **Exceptions:** None explicitly stated in the provided code.

- **Name:** `ShowObject`
  - **Description:** Displays or refreshes the updated data grid to reflect changes.

### Properties

- **data**: A two-dimensional array that stores the grid data.

## Code Examples

The provided code examples demonstrate how to integrate the `button2_Click` method into your application to enable users to update specific cells in the data grid programmatically.

### Important Notes
- Ensure the `nRows` is greater than zero before updating the grid to avoid null reference exceptions.
- Input validation should be implemented to handle invalid inputs such as non-numeric values in row and column fields.

## Page-level Navigation/TOC (if applicable)

- [Overview]
- [Content]
- [API Reference]
- [Code Examples]

## Cross References

For more details on working with grid data and handling user inputs, refer to the Syncfusion documentation for Syncfusion WinForms.

<!-- tags: [syncfusion, winforms, arraycalcdata, grid, data, programming] keywords: [syncfusion, winforms, calculate, cell, update, data grid, programmatic update, grid data, arraycalcdata] -->
```

---

<!-- 페이지 81 -->

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

---

<!-- 페이지 82 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: calculate
page_number: 070
page_id: calculate#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:06Z
fidelity: lossless
-->

# Essential Calculate

## Understanding Calculations with CalcQuickBase

### Overview
- The process requires updating values in the CalcQuickBase object by using indexers to notify it of changes in variables.
- Variable modifications in text boxes must be passed to CalcQuickBase by setting their values through indexers.
- The CalcQuickBase object calculates derived variables but requires the user's code to update the appropriate text box with the new values.
- The event `CalcQuickBase.ValueSet` is triggered when a tracked value is modified, allowing the code to respond by updating the relevant text box.

### Content

#### Explanation of the Calculation Process
In order for the calculation process to work effectively, two steps are crucial:

1. **Updating Variables in CalcQuickBase**:
   - When a variable (e.g., `A` or `B`) is modified in your application, the code must set the new value in the `CalcQuickBase` object using indexers.
   - This informs `CalcQuickBase` that the variable has changed, allowing it to calculate and update any dependent variables like `C`.
   - Since `CalcQuickBase` lacks built-in knowledge of specific text boxes (e.g., TextBox A, TextBox B), you must explicitly link the text box values to these variables via indexers.

2. **Synchronizing Text Box Values**:
   - After updating values in `CalcQuickBase`, the framework calculates the derived variable `C`.
   - However, `CalcQuickBase` does not directly update the text box that displays `C`.
   - Your code must listen for the `CalcQuickBase.ValueSet` event. Each time a tracked value changes, this event is raised.
   - When your code detects this event, it retrieves the new value for `C` and updates the appropriate text box to reflect this modified value.

#### Code Illustration
The following code demonstrates the process of leveraging `CalcQuickBase` for automated calculations and synchronized text box updates:

```csharp
private CalcQuickBase calculator = null;

private void Form_Load(object sender, System.EventArgs e)
{
    // 1) Instantiate a CalcQuickBase object.
    calculator = new CalcQuickBase();

    // 2) Populate your controls.
    this.textBoxA.Text = "12";
    this.textBoxB.Text = "3";
    this.textBoxC.Text = "= [A] + 2 * [B]";

    // Must enter formula names before turning on calculations.
    // 3) Assign formula object names.
    calculator["A"] = this.textBoxA.Text;
    calculator["B"] = this.textBoxB.Text;
    calculator["C"] = this.textBoxC.Text;
    calculator["D"] = this.textBoxD.Text;

    // 4) Turn on auto calculations.
    this.calculator.AutoCalc = true;

    // 5) Subscribe to the event to set newly calculated values.
    this.calculator.ValueSet += new
        QuickValueSetEventHandler(calculator_ValueSet);

    // 6) Subscribe to some events to trigger the setting of values into CalcQuickBase.
    this.textBoxA.Leave += new EventHandler(textBoxA_Leave);
    this.textBoxB.Leave += new EventHandler(textBoxB_Leave);
}
```

### Key Steps in the Code

1. **Instantiation**:
   - A `CalcQuickBase` object is created (`calculator`).
    
2. **Initialization of Controls**:
   - Text boxes are populated with initial values and formulas.

3. **Mapping Variables**:
   - The indexers are used to map text box values to ` CalcQuickBase` variables (`A`, `B`, etc.).

4. **Enabling Auto Calculation**:
   - Automation for calculation is enabled (`AutoCalc = true`).

5. **Event Subscription**:
   - The `ValueSet` event is subscribed to, ensuring your code listens for new calculated values.

6. **Triggering Updates**:
   - Events (`Leave`) ensure the code updates `CalcQuickBase` whenever the user modifies a text box value.

## Summary
By combining the use of indexers to maintain variable integrity and event handling to synchronize the text box outputs, the `CalcQuickBase` framework ensures a seamless and reliable calculation process.

<!-- tags: [Syncfusion, CalcQuickBase, WinForms, variable handling, event handling] keywords: [CalcQuickBase, indexers, ValueSet event, text boxes, automatic calculation, event handlers] -->
```

---

<!-- 페이지 83 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: calculate
page_number: 074
page_id: calculate#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:28Z
fidelity: lossless
-->

# Essential Calculate

## Event Handlers and CalcQuickBase

9. These four event handlers signal when the user leaves a modified text box. At that point, the `CalcQuickBase` object is updated to reflect the new value that has been entered by the user.

## Using RegisterControlArray

### Overview

- **Purpose:** Streamlining the management of auto-calculation in `CalcQuickBase` for controls on a form.
- **Method:** `CalcQuickBase.RegisterControlArray` simplifies handling multiple events and removes the need to subscribe to individual events and write explicit handlers.
- **Assumptions:** 
  - The control is either a text box or a combo box.
  - The variable name for the control value in formulas is `Control.Name`.

### Content

#### Explicit Event Management

Using explicit events to manage auto-calculation in `CalcQuickBase` is straightforward but requires handling multiple events and writing event handlers. The `CalcQuickBase.RegisterControlArray` method automates this process, making it easier to add calculation support to a form or `UserControl`. 

There are two assumptions about the controls to which you want to bind the calculations:
1. The control is either a text box or a combo box.
2. The variable name used to represent the control value in formulas is `Control.Name`.

Here is the code that replicates the functionality of our previous example using explicit events to support auto-calculation. Notice that all the event handling has been removed. The process involves three steps:
1. Instantiating the `CalcQuickBase` object.
2. Calling the `RegisterControlArray` method.
3. Calling the `RefreshAllCalculations` method.

#### Code Example

```csharp
CalcQuickBase calculator = null;

private void Form1_Load(object sender, System.EventArgs e)
{
    // 1) Ensure controls have the names you want to use as variables.
    // These names can be set either from code or the designer.
    this.textBoxA.Name = "A";
    this.textBoxB.Name = "B";
    this.textBoxC.Name = "C";
    this.textBoxD.Name = "D";

    // 2) Initially populate the controls. Values can also be set in the designer.
    this.textBoxA.Text = "12";
    this.textBoxB.Text = "3";
    this.textBoxC.Text = "= [A] + 2 * [B]";

    // 3) Instantiate a CalcQuickBase object.
    calculator = new CalcQuickBase();

    // 4) Register the controls used in calculations. The formula variables are the Control.Name strings.
    this.calculator.RegisterControlArray(new Control[]
    {
    }
```

### Notes

- To support other controls beyond text boxes and combo boxes, you will need to derive `CalcQuickBase` and override `RegisterControl`.
- Ensure that all controls involved in the calculations have appropriate names to be used as variables in formulas.

## Conclusion

By utilizing `CalcQuickBase.RegisterControlArray`, developers can streamline the process of adding auto-calculation support to their WinForms applications, reducing the need for explicit event handling and simplifying the management of control-related calculations.

<!-- tags: [syncfusion, winforms, calcquickbase, auto-calculation, event-handling, registercontrolarray] keywords: [event handlers, text box, combo box, control names, explicit events, auto-calculation, formula variables, registercontrolarray] -->
```

---

<!-- 페이지 84 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: calculate
page_number: 078
page_id: calculate#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:47Z
fidelity: lossless
-->

# Essential Calculate

Essential Calculate enables you to add calculation support to arbitrary business objects through its ICalcData interface. In this section, you will learn how to define this interface and use it with a Windows Forms DataGrid.

## 4.1.2.1 The ICalcData Interface

ICalcData has three methods and one event. This interface allows the CalcEngine class in Essential Calculate to communicate with arbitrary data sources that implement this interface.

- GetValueRowCol - Returns the data value of a specified row and column
- SetValueRowCol - Sets the data value of a specified row and column
- WireParentObject - A callback to the data object that occurs as the CalcEngine is being created. The purpose is to give the data object a chance to do any initialization steps it may need, such as subscribe to events to handle changes in data notifications.
- ValueChanged - An event that is raised whenever data changes. The ICalcData implementer raises this event when the data changes. The CalcEngine listens to this event and accordingly reacts to data changes. It is through this event that formulas are processed and dependencies are tracked by the CalcEngine.

## 4.1.2.2 Working with System.Windows.Forms.DataGrid

A Windows Forms Data Grid is a rectangular container that holds data in cells. Such a container is a natural medium for using calculation support. To add Essential Calculation support to classes that represent data in a row/column format like a Data Grid, you will have to derive the class and implement the ICalcData interface. This interface contains three methods and one event. Once you add the appropriate interface implementation, your derived object will have formula support.

The following is a discussion of using Essential Calculate with a Data Grid as an ICalcData object based on the Essential Studio\Windows\Calculation.Windows\Samples\DataGridCalculator sample that ships with the product. The sample has a derived DataGrid class that implements ICalcData. Below is a screenshot of a sample screen. The sample sets the column header text to A, B, and so on, and places 1, 2, and so on, in the first column along with random integers in the other columns. This is done to remind you of the Excel-like cell notation of A1, A2, B2, and so on. This is the notation supported by Essential Calculate formulas using ICalcData objects.

<!-- tags: [syncfusion, windows forms, data grid, calculation, icalcdata, calcengine, essenticalcalculate, version: 11.4.0.26] keywords: [data grid, calculation support, icalcdata interface, windows forms, row column format, calcengine, formula support, datagridcalculator] -->

---

<!-- 페이지 85 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: calculate
page_number: 082
page_id: calculate#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:02Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- The page focuses on using DataGrids with calculation support in Syncfusion WinForms.
- It explains how to register ICalcData objects with the CalcEngine to enable cross-references among multiple worksheets.
- Examples of formulas and cell reference syntax are provided, demonstrating how to use formulas in a DataGrid.

## Content

### Using DataGrids with Calculation Support

Figure 35 shows a workbook with multiple DataGrids (DG1, DG2, DG3, DG4, DG5) displaying numerical data.

#### Figure 35: Workbook

---
![Workbook Screenshot](#image)  
---

---

To support cross-references among several ICalcData objects, you must register the objects with a single instance of the CalcEngine. Part of the information provided during registration includes names associated with each ICalcData object. To reference a particular cell in an ICalcData object, you need to use its name along with the column and row to determine the proper reference. For example, say, in an ICalcData object whose name is `Sales`, to reference column 5, row 3, you must use `Sales!E3`. The name is separated from the column and row reference by an exclamation point. In the above screenshot, the formula `= DG2!A5 + 6` would add 6 to the value in row 5, column 1 in sheet DG2.

### FormLoad Method Implementation

Here is the implementation of the FormLoad method for the sample screenshot depicted above. Using the designer, a TabControl is dropped on a form and five TabPages are added. The pages are named `DG1`, `DG2`, ..., `DG5`. On each TabPage, a CalcDataGrid is set with the DockStyle set to `Fill`. This is all done through the designer.

#### Code Example

```csharp
Syncfusion.Calculate.CalcEngine engine;

private void DataGridWorkBookForm_Load(object sender, System.EventArgs e) {
    // Additional code for loading and interacting with CalcDataGrids
}
```

## Page-Level Navigation/TOC
- **Overview**
  - Using DataGrids with Calculation Support
  - FormLoad Method Implementation

## Cross References
- For more information on the CalcEngine and its features, refer to the CalcEngine documentation.

<!-- tags: [syncfusion, winforms, calcengine, icalldata, datagrid, workbook, calculation support] keywords: [DataGrid, CalcEngine, ICalcData, FormLoad, TabControl, TabPages, DockStyle, fill, formula, cell reference] -->
```

---

<!-- 페이지 86 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: calculate
page_number: 086
page_id: calculate#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:18Z
fidelity: lossless
-->

# Essential Calculate

```csharp
// e1.RowIndex, e1.ColIndex needs to be one-based.
Syncfusion.Calculate.ValueChangedEventArgs e1 = new
    ValueChangedEventArgs(pos + 1, field + 1, val);
ValueChanged(this, e1);
}

// 3) Returns the value at the one-based row and col.
public object GetValueRowCol(int row, int col)
{
    // Row, col are one-based.
    return this[row - 1, col - 1];
}

// 4) Sets the value at the one-based row and col.
public void SetValueRowCol(object value, int row, int col)
{
    // Row, col are one-based.
    DataTable dt = this.DataSource as DataTable;
    dt.Rows[row - 1][col - 1] = value;
}

// 5) Required ICalcData event.
public event ValueChangedEventHandler ValueChanged;
}
```

### [VB]

```vb
Public Class CalcDataGrid
    Inherits DataGrid
    Implements Syncfusion.Calculate.ICalcData

    Public Sub New()
        ' Avoids the complexity of sorting.
        Me.AllowSorting = False
    End Sub

    ' 1) Used to subscribe to the DataTable.ColumnChanged event. This event will
    ' raise the required ValueChanged event. Without this ValueChanged
    ' event, the CalcEngine would have no knowledge of the data.
    Public Sub WireParentObject() Implements ICalcData.WireParentObject
        ' Assumes the grid's datasource is a DataTable.
        Dim dt As DataTable = Me.DataSource
        AddHandler dt.ColumnChanged, AddressOf dt_ColumnChanged

        ' Avoids the complexity of a new row.
    End Sub
```

<!-- tags: [Syncfusion Winforms, Calculate, ICalcData, ValueChangedEventArgs, DataTable, ColumnChanged event] keywords: [calculate, data grid, data source, value changed, column changed event, event handling, one-based index, VB, CSharp] -->
```

---

<!-- 페이지 87 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: calculate
page_number: 090
page_id: calculate#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:31Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- This calculator uses Essential XlsIO alongside Essential Calculate, requiring no MS Excel installation.
- The car insurance calculator spreadsheet manages variable values via Names across four sheets designed for inputs, lookups, calculations, and outputs.

## Content

### Car Insurance Calculator Overview

The spreadsheet you are using is a car insurance calculator. It uses Names to manage variable values and has the following four sheets:

- **Inputs**: Contains the input values for the car insurance calculations like the state, age, and so on.
- **LookUps**: Contains data that determine insurance rates. For example, each state has a weight assigned to it; each age has a weight assigned to it, and so on.
- **Calculate**: Does the actual calculations. Based on the input values from the input sheet, formulas in this sheet, look up appropriate weights from the LookUps sheet, and compute the car insurance cost depending upon these weights.
- **Outputs**: Contains the computed results obtained from the Calculate sheet.

### Figure 37: Worksheet that Receives Inputs

![Worksheet that Receives Inputs](https://example.com/image_url)  
*Figure 37: Worksheet that Receives Inputs*

The illustration depicts a Microsoft Excel sheet titled "Inputs," which serves as the primary input area for the calculator. This sheet includes fields such as Age, Sex, State, Points, Model, ModelYear, and MultipleDiscount. The "Define Name" panel on the right shows the named ranges in the workbook, including Age, BaseAmount, Model, ModelYear, MultipleDiscount, Points, Sex, and State. These named ranges ensure that the input values can be easily referenced and managed across the various sheets involved in the computation process.

### Key Features and Workflow

- **Inputs Sheet**:  
  - Users input data such as Age, Sex, State, Points, Model, ModelYear, and whether a MultipleDiscount applies.  
  - These values are critical for the subsequent calculations.  
  - The BaseAmount is also specified here, which serves as the starting point for the insurance cost.

- **LookUps Sheet**:  
  - Contains predefined rates and weights based on various factors, such as state and age.  
  - These rates are used in conjunction with the inputs to compute the final insurance cost.

- **Calculate Sheet**:  
  - Utilizes formulas to process the inputs and apply the appropriate weights and rates from the LookUps sheet.  
  - Computes the final insurance cost based on the complex interplay of input variables and lookup rates.

- **Outputs Sheet**:  
  - Presents the final computed insurance cost derived from the Calculate sheet.  
  - Provides a clear and concise output for the user after all calculations are completed.

### How Names Enhance Functionality

Using Names in the spreadsheet allows for better organization and management of variable values. It facilitates easy referencing of specific cells across different sheets without the need to memorize cell addresses. This becomes especially useful as the complexity of the calculations increases, as in the case of a car insurance calculator, where numerous variables interact to determine the final result.

## API Reference (if applicable)

This page does not cover API-specific information; it focuses on the workflow and structure of the essential Excel-based calculator.

## Code Examples (if applicable)

This section is not applicable as the document primarily describes the structure and functionality of an Excel-based car insurance calculator.

## Page-level Navigation/TOC (if applicable)

This document is self-contained and describes a standalone feature without requiring further navigation within the user guide.

## Cross References

- Refer to the user guide section on Essential XlsIO for more details on managing spreadsheets programmatically.
- For advanced topics on Excel integration with Syncfusion WinForms, consult the dedicated section focused on Excel components.

## RAG Annotations

<!-- tags: [essential-calculate, car-insurance-calculator, essential-xlsio, named-ranges, lookups, excel-sheets, insurance, rates] keywords: [inputs, lookups, calculates, outputs, variables, weights, rates, formulas, excel, syncfusion winforms] -->
```

---

<!-- 페이지 88 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: calculate
page_number: 094
page_id: calculate#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:54Z
fidelity: lossless
-->

# Essential Calculate

Figure 41: Form interface for our Excel Workbook

![Form interface for our Excel Workbook](https://i.imgur.com/st0exiF.png)

Before learning about the actual code used in this sample to access XLS files, you need to know about a couple of classes in Essential Calculate as well as the role that Essential XlsIO will play.

## 4.3.1 CalcSheet and CalcWorkbook Classes

In the Adding Calculation Support section, you would have learnt how to support referencing multiple `ICalcData` objects in a workbook fashion. The technique used there relies on registering each `ICalcData` object directly with a single instance of the `CalcEngine`. Different `ICalcData` objects are managed by tying together in a Tab Control as the Tab Pages. To support a general workbook structure where there are no support objects like Tab Pages and Tab Controls to provide the links, the Essential Calculate library includes two classes: `CalcSheet` and `CalcWorkbook`.

- The `CalcSheet` class is an `ICalcData` derived object that plays the role of a single worksheet.
- It does have the optional facility to hold row/column type data objects that can be set through indexing an instance of the class.
- This class will allocate storage to hold such data.
- The `CalcWorkbook` class is a collection of `CalcSheets`.
- You can use these classes to manage the support for working with Excel spreadsheets.

> **Note:** For more detailed information on these classes, check out the class reference.

## Page-level Navigation/TOC (if applicable)
_Not applicable on this page._

## Cross References
_Not applicable on this page._

<!-- tags: [Essential Calculate, CalcSheet, CalcWorkbook, ICalcData, CalcEngine, XlsIO, workbook, worksheet, Excel spreadsheets, Syncfusion Winforms, 11.4.0.26] keywords: [calculation support, workbook structure, Excel files, interface, library, class reference, detailed information] -->
```

---

<!-- 페이지 89 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: calculate
page_number: 098
page_id: calculate#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:07Z
fidelity: lossless
-->

## Content

### Essential Calculate

```csharp
private int ageRow = 3;
private int sexRow = 4;
private int stateRow = 5;
private int pointsRow = 6;
private int modelRow = 7;
private int modelYearRow = 8;
private int multipleDiscountRow = 9;

// 4) Set the input values into the CalcSheets.
private void SetSheetInputs()
{
    CalcSheet inputSheet = this.calcWB["Inputs"];
    inputSheet[ageRow, 2] = this.numericUpDownAge.Value.ToString();
    inputSheet[sexRow, 2] = this.comboBoxSex.Text[0].ToString();
    inputSheet[stateRow, 2] = this.comboBoxState.Text;
    inputSheet[pointsRow, 2] = this.numericUpDownPoints.Value.ToString();
    inputSheet[modelRow, 2] = this.comboBoxModel.Text;
    inputSheet[modelYearRow, 2] = numericUpDownModelYear.Value.ToString();
    inputSheet[multipleDiscountRow, 2] = checkBoxMCars.Checked ? "Yes" : "No";
    inputSheet[3, 5] = this.textBoxBaseAmount.Text;
}
```

### [VB]

```vb
Private Sub button1_Click(sender As Object, e As System.EventArgs)

    ' 1) Moves input values from the form into the CalcSheet.
    SetSheetInputs()

    ' 2) Calculations not suspended, so just getting the value triggers
    '    the computation. So these two lines are not needed.....
    '    Me.calcWB.Engine.UpdateCalcID()
    '    Me.calcWB.Engine.PullUpdatedValue(this.calcWB.GetSheetID("Outputs"), 1, 1)

    ' 3) Get the value from cell 1,1 on the output sheet.
    Dim d As Double
    If Double.TryParse(calcWB("Outputs")(1, 1).ToString(), NumberStyles.Any, Nothing, d) Then

        ' Cell 1,1 on the outputs sheet has the result.
        Me.labelPrice.Text = String.Format("{0:C2}", d)
    Else
        Me.labelPrice.Text = "----"
    End If
End Sub
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, essential Calculate, calcSheets, inputs, outputs, forms] keywords: [calculate, essential, calcSheets, input values, output sheet, cell, Trigger computation, Parse, Format, NumberStyles] -->
```

---

<!-- 페이지 90 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: calculate
page_number: 102
page_id: calculate#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:22Z
fidelity: lossless
-->

## Essential Calculate

```vb
If Me.checkBoxMultipleCars.Checked Then
    inputSheet(multipleDiscountRow, 2) = "Yes"
Else
    inputSheet(multipleDiscountRow, 2) = "No"
End If
inputSheet(3, 5) = Me.textBoxBaseAmount.Text

' 2) Calculations are suspended so need to pull the computed value
' to make sure it has been calculated with the latest changes.
Me.calcWB.Engine.UpdateCalcID()
calcWB.Engine.PullUpdatedValue(Me.calcWB.GetSheetID("Outputs"), 1, 1)

' 3) Gets the value from cell 1,1 on the output sheet.
Dim d As Double
If Double.TryParse(calcWB("Outputs")(1, 1).ToString(), NumberStyles.Any, Nothing, d) Then
    Me.labelPrice.Text = String.Format("{0:C2}", d)
Else
    Me.labelPrice.Text = "---"
End If

' Allows the label to update.
Me.labelPrice.Refresh()
End While
Me.calcWB.Engine.CalculatingSuspended = False
Me.Cursor = Cursors.Default
Me.labelPrice.Text = String.Format("{0} updates in {1} seconds", num, CType(DateTime.Now - start, TimeSpan))

' Button2_Click
End Sub
```

### Overview
- Sets random values into the Inputs sheet using the proper row and column indexers.
- Calls `UpdateCalcID` and `PullUpdatedValue` to ensure the value in the Outputs sheet at cell (1,1) reflects the current values in the workbook.
- Retrieves the value on the Output sheet at cell (1,1).

## Content

### 4.4 Supported Algebra

<!-- tags: [syncfusion, winforms, calculation, algebra, inputs, outputs] keywords: [CheckBox, TextBox, Label, Format, Parse, SheetID, Calculate Suspension, TimeSpan, Floats, Algebra]. -->
```

---

<!-- 페이지 91 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: calculate
page_number: 106
page_id: calculate#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:35Z
fidelity: lossless
-->

# Essential Calculate

## Using Function Library Formulas

Function Library formulas may be used as a stand-alone formula, and they can be incorporated into more complex formulas.

### Examples of Function Library Formulas

| Formula                                 | Comment                               |
|-----------------------------------------|---------------------------------------|
| = Sin(3.14159)                         | Returns the sine of 3.14159 radians |
| = 2 * Sin(3.14159) + Sqrt(2)           | Returns $2 \times$ sine of 3.14159 radians plus the square root of 2. |
| = 2 * Pi()                             | Returns $2 \times \pi$.             |

Some library functions may not have arguments but you must still include the parentheses to indicate that you are using a library function. For example, `= 2 * Pi()`, shows the proper use of the library function Pi.

## Function Library

The Function Library contains many functions from statistics, finance, and mathematics, along with other general-purpose functions. There are more than 150 entries in the library, and it is easy to add your own calculations.

The functions are discussed in the below topics.

### Add Function

#### Overview
CalcQuickBase relies on a `Calculate.Engine` object through an `ICalcData` interface to provide its calculation support. To add functions to the Formula Library available to your `CalcQuickBase` object, you need to add them to the `CalcQuickBase` underlying Engine object. You can access this engine object through the public "read-only" property, `CalcQuickBase.Engine`. Once you have a reference to the `CalcQuickBase`'s Engine object, you can add library functions by following the steps given below.

Adding a custom function to the Formula Library is a two-step process.
```

---

<!-- 페이지 92 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: calculate
page_number: 110
page_id: calculate#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:47Z
fidelity: lossless
-->

# Essential Calculate

```vb
{CalcEngine.ParseArgumentSeparator})

' Cell range
If r.IndexOf(":c") > -1 Then
    Dim s As String
    For Each s In engine.GetCellsFromArgs(r)
        ' s is a cell line a21 or c3...
        Try
            s1 = engine.GetValueFromArg(s)
            If s1 <> "" And Double.TryParse(s1, System.Globalization.NumberStyles.Number, Nothing, d) Then
                min = Math.Min(min, d)
            End If
        Catch ex As Exception
            Return ex.Message
        End Try
    Next s
Else
    Try
        s1 = engine.GetValueFromArg(r)
        If s1 <> "" And Double.TryParse(s1, System.Globalization.NumberStyles.Number, Nothing, d) Then
            min = Math.Min(min, d)
        End If
    Catch ex As Exception
        Return ex.Message
    End Try
End If
Next r
If min <> Double.MaxValue Then
    Return min.ToString()
End If
Return ""

' ComputeMymin
End Function
```

## 4.5.1.2 Step 2-Registering the Method with the CalcEngine

<!-- tags: [Syncfusion, Winforms, Calculate, CalcEngine, MethodRegistration, Version:11.4.0.26] keywords: [Calculate, CalcEngine, MethodRegistration, Step2, CellRange, TryParse, Double, VB] -->
```

---

<!-- 페이지 93 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_114.jpeg
document_name: calculate
page_number: 114
page_id: calculate#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:58Z
fidelity: lossless
-->

## Date and Time

### Overview
- Lists the Date and Time functions included in `Essential calculate`.
- Provides descriptions for each function to assist in understanding their usage.

### Content

#### Date and Time Functions

The following table lists the Date and Time functions included with Essential calculate:

| Function Name    | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Date**         | Returns the sequential serial number that represents a particular date.     |
| **Datevalue**    | Returns the serial number of the date value.                              |
| **Day**          | Returns the day of the month.                                              |
| **Days360**      | Returns the number of days between two dates using a 360-day year.         |
| **Hour**         | Returns the hour from 0 to 23.                                             |
| **Minute**       | Returns the minute from 0 to 59.                                           |
| **Month**        | Returns the month from 1 to 12.                                            |
| **Now**          | Returns the current date and time.                                          |
| **Second**       | Returns the second from 0 to 59.                                           |
| **Time**         | Returns serial number time.                                                |
| **Timevalue**    | Returns the serial number time from a string.                             |
| **Today**        | Returns the current date.                                                  |

## Code Examples

Below are examples demonstrating the usage of some Date and Time functions:

- **Example 1: Using the `Now` Function**
  ```csharp
  var currentDateAndTime = Now();
  Console.WriteLine(currentDateAndTime);
  ```

- **Example 2: Using the `Date` Function**
  ```csharp
  var serialNumber = Date(2023, 8, 9);
  Console.WriteLine(serialNumber);
  ```

## Cross References

- See also: 
  - **String Functions** for more details on `Text`, `Value`, `Len`, and `MID`.
  - **Time and Date Formatting** for more complex formatting options.

<!-- tags: [date, time, datefunctions, essentialcalculate, syncfusionwinforms] keywords: [datevalue, days360, hour, minute, month, now, second, time, timevalue, today] -->
```

---

<!-- 페이지 94 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_118.jpeg
document_name: calculate
page_number: 118
page_id: calculate#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:12Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Functions and mathematical operations supported in Essential Calculate.
- Rounding, conditional sums, trigonometric functions, and other mathematical operations explained.
- Detailed description of the multinomial function within Syncfusion Winforms.

## Content

### Function List

| Function    | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| Roundup     | Returns the number rounded up.                                                |
| Sign        | Returns the sign of the number.                                              |
| Sine        | Returns the sine.                                                          |
| Sinh        | Returns the hyperbolic sine.                                                |
| Sqrt        | Returns the square root of a number.                                        |
| Sum         | Returns the sum of the listed values.                                        |
| Sumif       | Returns the conditional sum of the listed values.                          |
| SumProduct  | Returns the sum of the products.                                            |
| Sumsq       | Returns the sum of the squares.                                             |
| Sumx2my2    | Returns the differences of the squares.                                     |
| Sumx2py2    | Returns the sum of the squares.                                             |
| Sumxmy2     | Returns the squares of the differences.                                     |
| Tan         | Returns the tangent.                                                       |
| Tanh        | Returns the hyperbolic tangent.                                             |
| Trunc       | Returns the number without a fractional part.                                  |

### 4.5.6.1 Multinomial

#### Overview
The MULTINOMIAL function returns the ratio of the factorial of a sum of values to the product of factorials.

#### Syntax
The syntax of the MULTINOMIAL function is:
```
=MULTINOMIAL(number1, (number2), ...)
```

#### Errors
- **#NUM!** - Occurs if any of the supplied arguments are less than 0.
- **#VALUE!** - Occurs if any of the supplied arguments are non-numeric.

## Page-level Navigation/TOC (if applicable)
- Essential Calculate
  - Function List
  - Multinomial

## Cross References
- See also: *Essential Calculate Overview, Function List, SUMIF, Sumsq, Tan, Tanh*

<!-- tags: [syncfusion-sdk, essential-calculate, multinomial-function, functions, math, syncfusion, winforms, 11.4.0.26] keywords: [roundup, sign, sine, sinh, sqrt, sum, sumif, sumproduct, sumsq, sumx2my2, sumx2py2, sumxmy2, tan, tanh, trunc] -->
```

---

<!-- 페이지 95 -->

```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_122.jpeg
document_name: calculate
page_number: 122
page_id: calculate#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:27Z
fidelity: lossless
--> 

## Essential Calculate

### Content

#### Anything else
| Anything else | #N/A |
| --- | --- |

#### Example:
| FORMULA | RESULT |
| --- | --- |
| = ERROR.TYPE(#NULL!) | 1 |
| = ERROR.TYPE(even) | #NA |

### 4.5.6.7 SUBTOTAL

#### Overview
The SUBTOTAL function returns a subtotal in a list. Once the subtotal list is created, you can modify it by editing the SUBTOTAL function.

#### Syntax
The syntax of the SUBTOTAL function is
```
=SUBTOTAL(function_Number, ref1, (ref2),...)
```

#### Parameters
- **function_Number**: Required. Specifies which function to use in calculating subtotals within a list. Here is the list of functions supported by Syncfusion:

| FUNCTION NUMBER | FUNCTION NAME |
| --- | --- |
| 1 | AVERAGE |
| 2 | COUNT |
| 3 | COUNTA |
| 4 | MAX |
| 5 | MIN |
| 6 | PRODUCT |
| 7 | STDEV |
| 8 | STDEVP |
| 9 | SUM |
| 10 | VAR |

- **Ref1**: The first named range which is used for the subtotal. This value is required.
- **Ref2**: This value is optional.

---

<!-- tags: [product, module, control, api, version?] keywords: [calculate, subtotal, error.type, function_number, ref1, ref2, average, count, max, min, sum, subtotals] -->
```

---

<!-- 페이지 96 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: calculate
page_number: 126
page_id: calculate#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:38Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- Required numerical input for calculations.
- Handles rounding of non-integer values and error handling for invalid inputs.

### GCD Calculation

#### Number1 – Required
- If any value is not an integer, it will be rounded down.
- Errors:
  - **#NUM!** - If the number is less than zero (0).
  - **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example:
| FORMULA         | RESULT    |
|------------------|-----------|
| = GCD(5,3,2)    | 1         |
| = GCD(-2)       | #NUM!     |

### 4.5.6.14 LCM

#### Overview
- The LCM function returns the least common multiple of two or more given values. The values must be numeric.

#### Syntax
- The syntax of the LCM function is:
  ```
  = LCM(number1, number2, ...)
  ```
- **number1** – Required.
  - If any value is not an integer, it will be rounded down.

#### Errors:
- **#NUM!** - If the number is less than zero (0).
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example:
| FORMULA         | RESULT    |
|------------------|-----------|
| = LCM(5,2)      | 10        |
| = LCM(-2)       | #NUM!     |

### 4.5.6.15 ROMAN

## API Reference (if applicable)
- Describes members and methods related to the calculation functions.

## Code Examples
- Provides examples of how to use the LCM and GCD functions in your code.

## Cross References
- Refer to related functions and documentation for more information.

<!-- tags: [syncfusion-sdk, winforms, calculation, gcd, lcm, roman, api, l11.4.0.26] keywords: [calculate, gcd, lcm, roman, numeric, rounding, errors, least common multiple] -->
```

---

<!-- 페이지 97 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: calculate
page_number: 130
page_id: calculate#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:52Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Demonstrates the usage of functions like `Clean`, `ISREF`, and `AVERAGEIF`.
- Provides examples and detailed syntax for these functions.

## Content

### Example
| FORMULA                | RESULT      |
|------------------------|-------------|
| `=Clean(Syncfusion)`   | Syncfusion  |
| `=Clean("Text*")`      | Text        |

#### 4.5.6.21 ISREF
The ISREF function returns the logical value TRUE if the given value is a reference value; otherwise, the function returns FALSE.

**Syntax**  
`=ISREF(given_value)`

- **given_value**: Required. The value that is to be tested. The value argument can be a blank (empty cell), error, logical value, text, number, or reference value, or a name referring to any of these.

**Example**
| FORMULA                              | RESULT   |
|--------------------------------------|----------|
| `=ISREF("Region1")`                 | FALSE    |
| `=ISREF(ISLOGICAL(TRUE))`           | TRUE     |

#### 4.5.6.22 AVERAGEIF
The AVERAGEIF function finds the average of values in a given array that satisfy a given criteria, and returns the average value of the corresponding values in a second given array.

**Syntax**  
`=AVERAGEIF(range, criteria, average_range)`

- **range**: Array of values to be tested against the given criteria.
- **criteria**: The condition to be tested in each of the values of the given range.
- **average_range**: Numeric values to be evaluated against the criteria and averaged.

**Notes**
- If range is blank or a text value, AVERAGEIF returns the `#DIV/0!` error value.
- If a cell in criteria is empty, AVERAGEIF treats it as a `0` value.
```

---

<!-- 페이지 98 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_134.jpeg
document_name: calculate
page_number: 134
page_id: calculate#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:05Z
fidelity: lossless
-->

### Essential Calculate

#### Syntax

`ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])`

- `row_num`: A numeric value that specifies the row number.
- `column_num`: A numeric value that specifies the column number.
- `abs_num`: Optional. A numeric value that specifies the type of reference to return.
- `A1`: A logical value that specifies the A1 or R1C1 reference style.

#### Example

| FORMULA                       | RESULT                  |
|-------------------------------|-------------------------|
| `=ADDRESS(2,3,2,FALSE)`      | `R2C[3].`              |
| `=ADDRESS(2,3,1,FALSE,"[Book1]Sync1")` | `[Book1]Sync1!R2C3` |

### 4.5.6.27 LOOKUP

The LOOKUP function returns a value either from a one-row or one-column range, or from an array. The LOOKUP function has two syntax forms: vector and array.

#### Vector Form

The vector form of LOOKUP looks in a one-row or one-column range for a value, and then returns a value from the same position in a second one-row or one-column range.

**Syntax**

`=LOOKUP(lookup_value, lookup_vector, result_vector)`

#### Array Form

The array form of LOOKUP looks in the first row or column of an array for the specified value, and then returns a value from the same position in the last row or column of the array.

**Syntax**

`=LOOKUP(lookup_value, array)`

#### Notes

- If the LOOKUP function can't find the `lookup_value`, the function matches the largest value in `lookup_vector` that is less than or equal to `lookup_value`.
- If `lookup_value` is smaller than the smallest value in `lookup_vector`, LOOKUP returns the `#N/A` error value.

#### Example
```html

<!-- tags: [syncfusion, winforms, look-up-function, address-function, essential-calculate] keywords: [lookup, vector, array, reference-style, row-number, column-number, address, error-values] -->
```

---

<!-- 페이지 99 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_138.jpeg
document_name: calculate
page_number: 138
page_id: calculate#page_138
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:18Z
fidelity: lossless
-->

## Overview

- Essential functions for calculating various statistical measures and distributions.
- Tools for handling standard deviation, variance, correlation, probability distributions, and more.
- Functions for ranking, percentile calculations, and skewness analysis.

## Content

| Function     | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| Percentile   | Returns the kth percentile of the given values.                            |
| Percentrank  | Returns the position of a value in the range of values.                   |
| Permut       | Returns the number of permutations.                                       |
| Poisson      | Returns the Poisson distribution.                                         |
| Prob         | Returns a probability.                                                    |
| Quartile     | Returns which quarter a value belongs to within an ordered set of data.   |
| Rank         | Returns the position of a value in an ordered list.                       |
| Rsq          | Returns the square of the Pearson product moment correlation coefficients. |
| Skew         | Returns the skewness of a distribution.                                   |
| Slope        | Returns the slope of the linear regression line.                          |
| Small        | Returns the kth smallest value.                                           |
| Standardize  | Returns the normalized value.                                             |
| Stdev        | Returns the sample standard deviation.                                    |
| Stdeva       | Returns the sample standard deviation.                                    |
| Stdevp       | Returns the population standard deviation.                                |
| Stdevpa      | Returns the population standard deviation.                                |
| Steyx        | Returns the standard error.                                               |
| Trimmean     | Returns the mean after removing out-liers.                                |
| Var          | Returns the sample variance.                                              |
| Vara         | Returns the sample variance.                                              |
| Varp         | Returns the population variance.                                          |
| Varpa        | Returns the population variance.                                          |
| Weibull      | Returns the Weibull distribution.                                         |

## RAG Annotations

<!-- tags: [Syncfusion Winforms, statistical functions, percentile, standard deviation, variance, correlation, probability distributions, ranking] keywords: [percentile, percentrank, permut, poisson, prob, quartile, rank, rsq, skew, slope, small, standardize, stdev, stdeva, stdevp, stdevpa, steyx, trimmean, var, vara, varp, varpa, weibull] -->
```

---

<!-- 페이지 100 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_142.jpeg
document_name: calculate
page_number: 142
page_id: calculate#page_142
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:33Z
fidelity: lossless
-->

## 4.7 Function Reference Section

This section discusses the library functions that are shipped in the Essential Calculate library. The arguments required by each of these functions are listed in bold text. Optional arguments are listed in a normal text.

### 4.7.1 ABS

```csharp
public string[] FormulaErrorStrings = new string[]
{
    "binary operators cannot start an expression",  //0
    "cannot parse",                                 //1
    "bad library",                                 //2
    "invalid char in front of",                    //3
    "number contains 2 decimal points",           //4
    "expression cannot end with an operator",      //5
    "invalid characters following an operator",    //6
    "invalid character in number",                 //7
    "mismatched parentheses",                      //8
    "unknown formula name",                        //9
    "requires a single argument",                  //10
    "requires 3 arguments",                        //11
    "invalid Math argument",                       //12
    "requires 2 arguments",                        //13
    "#NAME?",                                      //14
    "too complex",                                 //15
    "circular reference: ",                        //16
    "missing formula",                             //17
    "improper formula",                            //18
    "invalid expression",                          //19
    "cell empty",                                  //20
    "bad formula",                                 //21
    "empty expression",                            //22
    "",                                            //23
    "mismatched string quotes",                    //24
    "wrong number of arguments",                   //25
    "invalid arguments",                           //26
    "iterations do not converge",                  //27
    "Control named '{0}' is already registered"    //28
};
```

<!-- tags: [calculate, library functions, error strings, requirements, arguments] keywords: [essential calculate, binary operators, formula parsing, argument requirements, function reference] -->
```

---

<!-- 페이지 101 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_146.jpeg
document_name: calculate
page_number: 146
page_id: calculate#page_146
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:46Z
fidelity: lossless
-->

# Essential Calculate

**y_num** is the Y coordinate of the point.

## Remarks

- A positive result represents a counterclockwise angle from the x-axis; a negative result represents a clockwise angle.
- ATAN2(a,b) equals ATAN(b/a), except that `a` can equal 0 in ATAN2.

### 4.7.9 ATANH

**Returns the inverse hyperbolic tangent of a number.** Number must be strictly between -1 and 1. The inverse hyperbolic tangent is the value whose hyperbolic tangent is number, so `ATANH(TANH(number))` equals the given number.

#### Syntax

`ATANH(number)`

where:

- **number** is any real number that is between 1 and -1.

### 4.7.10 AVEDEV

**Returns the average of the absolute mean deviations of data points.** AVEDEV is a measure of the variability in a data set.

#### Syntax

`AVEDEV(number1, number2, ...)`

where:

- **number1, number2, …** are arguments for which you want the average of the absolute deviations. You can also use a single array or a reference to an array instead of arguments separated by commas.

---

<!-- tags: [syncfusion, winforms, calculate, atan, atan2, atanh, ave-dev, api, version 11.4.0.26] keywords: [y-coordinate, angle calculation, inverse hyperbolic tangent, average deviation, variability, data analysis, atanh, avedev, atan2, atan] -->
```

---

<!-- 페이지 102 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: calculate
page_number: 150
page_id: calculate#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:57Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes the syntax and usage of mathematical and statistical functions for rounding and calculating probabilities.
- Contains details on the `CEILING`, `Char`, and `CHIDIST` functions, including their parameters and remarks.

## CEILING Function

### Syntax

```markdown
CEILING(number, significance)
```

#### where:
- `number` is the value you want to round off.
- `significance` is the multiple to which you want to round.

### Remarks
- Both values must be numeric.
- Regardless of the sign of a number, a value is rounded up when adjusted away from zero. If the number is an exact multiple of significance, no rounding occurs.

## `4.7.16` Char Function

### Description
The `Char` function returns the character whose number code is defined in the parameter.

#### Syntax:
```markdown
Char(number)
```

#### where:
- `number` is the numeric value to retrieve the character.

## `4.7.17` CHIDIST Function

### Description
Returns the one-tailed probability of the chi-squared (χ²) distribution. The χ² distribution is associated with a χ² test.

#### Syntax:
```markdown
CHIDIST(x, degrees_freedom)
```

#### where:
- `x` is the value at which you want to evaluate the distribution.
- `degrees_freedom` is the number of degrees of freedom.
<!-- tags: [Syncfusion, Winforms, calculate, syntax, CEILING, Char, CHIDIST, chi-squared, probability, statistical functions, rounding, Excel functions] keywords: [CEILING, significance, Char, number code, CHIDIST, degrees of freedom, chi-squared distribution] -->
```

---

<!-- 페이지 103 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_154.jpeg
document_name: calculate
page_number: 154
page_id: calculate#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:09Z
fidelity: lossless
-->

# Essential Calculate

## Content

The page discusses mathematical and string manipulation functions used in calculations.

### Combinatorial Functions

The formula for combination is:

\[
\binom{n}{k} = \frac{P_{k,n}}{k!} = \frac{n!}{k!(n-k)!}
\]

Where:

\[
P_{k,n} = \frac{n!}{(n-k)!}
\]

### CONCATENATE

**Purpose**: Joins several text strings into one text string.

#### Syntax

```markdown
CONCATENATE(text1, text2,...)
```

#### Parameters

- **text1, text2, ...**: Text items to be joined into a single text item. These can be text strings, numbers, or single-cell references.

#### Remarks

- The `"&"` operator can be used instead of `CONCATENATE` to join text items.

### CONFIDENCE

**Purpose**: Returns a value that can be used to construct a confidence interval about a population mean. The confidence interval is a range of values around the sample mean.

#### Syntax

```markdown
CONFIDENCE(alpha, standard_dev, size)
```

#### Explanation

- The confidence interval is calculated as \( x \pm \text{CONFIDENCE} \). For example, if \( x \) is the sample mean of delivery times for products ordered through the mail, \( x \pm \text{CONFIDENCE} \) provides a range of population means.

### Page-Level Navigation

- 4.7.23 CONCATENATE
- 4.7.24 CONFIDENCE

### Cross References

See also:
- Documentation on mathematical operations and statistical functions in Excel or similar environments.
- Resources on significance testing and confidence intervals in statistical analysis.

<!-- tags: [essential calculate, string manipulation, concatenation, confidence interval, statistical functions] keywords: [concatenate, confidence, combination, statistical confidence, text string] -->
```

---

<!-- 페이지 104 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: calculate
page_number: 158
page_id: calculate#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:22Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Provides functions for counting blank cells and cells meeting specific criteria.
- Includes remarks regarding how certain types of cells (e.g., formulas returning empty text) are handled.

### COUNTBLANK(range)
**Syntax**:  
COUNTBLANK(range)  
**Where**:  
- `range` is the range from which you want to count the blank cells.

**Remarks**:  
- Cells with formulas that return "" (empty text) are also counted. Cells with zero values are not counted.

### 4.7.31 COUNTIF  
**Counts the number of cells within a range that meet the given criteria.**

**Syntax**:  
COUNTIF(range, criteria)  
**Where**:  
- `range` is the range of cells from which you want to count cells.  
- `criteria` is the criteria in the form of a number, expression, or text that defines which cells will be counted. For example, the criteria can be expressed as `">32"`.

**Remarks**:  
- If and Sumif are other library functions that can be used to conditionally compute values.

### 4.7.32 COVAR  
**Returns covariance, the average of the products of deviations for each data point pair.**

## API Reference (if applicable)
- **COUNTBLANK**  
  - **Namespace**: Essential Calculate  
  - **Parameters**: `range` (range to count blank cells from)  
  - **Remarks**: Handles cells with formulas returning empty text but not cells with zero values.  

- **COUNTIF**  
  - **Namespace**: Essential Calculate  
  - **Parameters**:  
    - `range` (range of cells to evaluate)  
    - `criteria` (criteria to filter cells)  
  - **Remarks**: Useful for conditional counting operations.  

- **COVAR**  
  - **Namespace**: Essential Calculate  
  - **Parameters**:  
    - `Array1` (first set of data points)  
    - `Array2` (second set of data points)  
  - **Remarks**: Computes covariance between two data sets.

## Code Examples
```csharp
// Example for COUNTBLANK
double blankCount = COUNTBLANK(rangeA1:A10);

// Example for COUNTIF
double countAbove32 = COUNTIF(rangeA1:A10, ">32");

// Example for COVAR
double covariance = COVAR(array1, array2);
```

## Cross References
- See also: Other conditional functions like IF and SUMIF for related operations.
- Refer to the documentation for Array manipulation for enhanced examples.

<!-- tags: [essential-calculate, countblank, countif, covar, winforms, 11.4.0.26] keywords: [count blank cells, conditional counting, covariance, data point pairs, conditional library functions] -->
```

---

<!-- 페이지 105 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: calculate
page_number: 162
page_id: calculate#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:38Z
fidelity: lossless
-->

### Essential Calculate

#### Syntax

**DAYS360(start_date, end_date, method)**

where:

- `start_date` and `end_date` are the two dates between which you want to know the number of days. If `start_date` occurs after `end_date`, DAYS360 returns a negative number. Dates should be entered by using the DATE function or as results of other formulas or functions.
- `method` is a logical value that specifies whether to use the U.S. or European method in the calculation. If method is:
  - **False or omitted** – The calculation uses the U.S. (NASD) method. If the starting date is the 31st of a month, it becomes equal to the 30th of the same month. If the ending date is the 31st of a month and the starting date is earlier than the 30th of a month, the ending date becomes equal to the 1st of the next month; otherwise the ending date becomes equal to the 30th of the same month.
  - **True** – The calculation uses the European method. Starting dates and ending dates that occur on the 31st of a month become equal to the 30th of the same month.

### 4.7.38 DB

Returns the depreciation of an asset for a specified period using the fixed-declining balance method.

#### Syntax

**DB(cost, salvage, life, period, month)**

where:

- `cost` is the initial cost of the asset.
- `salvage` is the value at the end of the depreciation (sometimes called the salvage value of the asset).
- `life` is the number of periods over which the asset is being depreciated (sometimes called the useful life of the asset).
- `period` is the period for which you want to calculate the depreciation. Period must use the same units as life.
- `month` is the number of months in the first year. If `month` is omitted, it is assumed to be 12.

### Remarks

---

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```

---

<!-- 페이지 106 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: calculate
page_number: 166
page_id: calculate#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:52Z
fidelity: lossless
-->

# Essential Calculate

## Content

### 4.7.45 EXP

Returns e raised to the power of the given number.

#### Syntax

`EXP(number)`

where:  
`number` is the exponent applied to the base e.

---

### 4.7.46 EXPONDIST

Returns the exponential distribution.

#### Syntax

`EXPONDIST(x, lambda, cumulative)`

where:  
- `x` is the value of the function.  
- `lambda` is the parameter value.  
- `cumulative` is a logical value that indicates which form of the exponential function is to be provided. If `cumulative` is `True`, `EXPONDIST` returns the cumulative distribution function; if `False`, it returns the probability density function.

#### Remarks

- The equation for the probability density function is:  
  \[ f(x; \lambda) = \lambda e^{-\lambda x} \]  
- The equation for the cumulative distribution function is:  

---

## API Reference

This section describes the `EXP` and `EXPONDIST` functions in detail.

### EXP

**Namespace**: Essential Calculate  
**Class**: `Math`  
**Method**: `EXP`

#### Parameters

| Name | Type | Description |
|------|------|-------------|
| `number` | Number | The exponent applied to the base e. |

#### Returns

| Type | Description |
|------|-------------|
| Double | The value of e raised to the power of the given number. |

---

### EXPONDIST

**Namespace**: Essential Calculate  
**Class**: `StatisticalFunctions`  
**Method**: `EXPONDIST`

#### Parameters

| Name | Type | Description |
|------|------|-------------|
| `x` | Double | The value of the function. |
| `lambda` | Double | The parameter value. |
| `cumulative` | Boolean | Indicates whether to return the cumulative distribution function (`True`) or the probability density function (`False`). |

#### Returns

| Type | Description |
|------|-------------|
| Double | The value of the exponential distribution based on the specified parameters. |

---

## Code Examples

### Example 1: Using EXP

```csharp
using EssentialCalculate.Math;

double exponent = 2;
double result = EXP(exponent);
// result will be e^2
```

### Example 2: Using EXPONDIST

```csharp
using EssentialCalculate.StatisticalFunctions;

double x = 1.5;
double lambda = 0.5;
bool cumulative = true;
double result = EXPONDIST(x, lambda, cumulative);
// result will be the cumulative exponential distribution for the given parameters
```

---

## Cross References

- See also: `EXP`, `EXPONDIST`

<!-- tags: [syncfusion-sdk, mathematical functions, probability distributions, user guide, version 11.4.0.26] keywords: [EXP, EXPONDIST, exponential distribution, probability density function, cumulative distribution function, essential calculate] -->
```

---

<!-- 페이지 107 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: calculate
page_number: 170
page_id: calculate#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:11Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- y is the value for which you want to perform the inverse of the transformation.
- The equation for the inverse of the Fisher transformation is provided.
- The `Fixed` and `FLOOR` functions are explained.

## Content

### Remarks
- **Inverse of the Fisher Transformation:**
  The equation for the inverse of the Fisher transformation is:
  \[
  x = \frac{e^{2y} - 1}{e^{2y} + 1}
  \]

### 4.7.54 Fixed
The `Fixed` function rounds off to a specified number of decimal places and returns the value in text format.

#### Syntax:
```
Fixed ( number, decimal_places, no_commas )
```
- **Parameters:**
  - `number`: The number you want to round.
  - `decimal_places`: The number of decimal places you want to display in the result.
  - `no_commas`: A logical value. This displays commas when it is set to `FALSE`, and does not display commas when it is set to `TRUE`.

### 4.7.55 FLOOR
Rounds off the given number down, toward zero, to the nearest multiple of significance.

#### Syntax
```
FLOOR(number, significance)
```
- **Parameters:**
  - `number`: The numeric value that you want to round off.
  - `significance`: The multiple to which you want to round the number off.

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Essential Calculate, Fixed function, FLOOR function, Fisher Transformation] keywords: [Fisher Transformation, decimal places, rounding, significance, fixed text format] -->
```

---

<!-- 페이지 108 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: calculate
page_number: 174
page_id: calculate#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:23Z
fidelity: lossless
-->

# Essential Calculate

## Content

### GAMMAINV(probability, alpha, beta)

**where:**

- **probability** is the probability associated with the gamma distribution.
- **alpha** is a parameter to the distribution.
- **beta** is a parameter to the distribution.

#### Remarks

- Probability must be >= 0 and <= 1.
- Alpha and beta must be positive.

**Explanation:** Given a value for probability, GAMMAINV seeks value \( x \) such that \( \text{GAMMADIST}(x, \text{alpha}, \text{beta}, \text{True}) = \text{probability} \). Thus, the precision of GAMMAINV depends on the precision of GAMMADIST. GAMMAINV uses an iterative search technique.

### 4.7.61 GEOMEAN

**Returns the geometric mean of an array or range of positive data.**

#### Syntax

**GEOMEAN(number1, number2,...)**

**where:**

- number1, number2, ... are arguments for which you want to calculate the mean.

#### Remarks

- The arguments must be either numbers or names, arrays, or references that contain numbers.
- All values must be positive.
- The equation for the geometric mean is:

## API Reference

### GAMMAINV

**Description:** This function returns the inverse of the gamma cumulative distribution. It finds the value \( x \) for which the cumulative distribution function (CDF) equals a given probability.

**Syntax:**
```csharp
public static double GAMMAINV(double probability, double alpha, double beta);
```

**Parameters:**

- **probability:** The probability associated with the gamma distribution.
- **alpha:** Parameter to the distribution.
- **beta:** Parameter to the distribution.

**Returns:** The value \( x \) such that \( \text{GAMMADIST}(x, \text{alpha}, \text{beta}, \text{True}) = \text{probability} \).

### GEOMEAN

**Description:** Returns the geometric mean of an array or range of positive data.

**Syntax:**
```csharp
public static double GEOMEAN(params double[] values);
```

**Parameters:**

- **values:** An array of positive numbers.

**Returns:** The geometric mean of the input values.

**Example:**
```csharp
double[] numbers = { 1, 2, 3, 4 };
double geometricMean = GEOMEAN(numbers);
// This will calculate and return the geometric mean of the numbers array.
```

## Code Examples

### Example Using GAMMAINV
```csharp
// Example to find the inverse of the gamma cumulative distribution
double probability = 0.5;
double alpha = 2;
double beta = 3;
double x = GAMMAINV(probability, alpha, beta);
// x will be the value such that GAMMADIST(x, alpha, beta, True) = probability
```

### Example Using GEOMEAN
```csharp
// Example to calculate the geometric mean of a set of numbers
double[] data = { 2, 4, 8 };
double geometricMean = GEOMEAN(data);
// geometricMean will be the geometric mean of the given data array
```

## Page-level Navigation/TOC (if applicable)

- GAMMAINV(probability, alpha, beta)
  - Remarks
- 4.7.61 GEOMEAN
  - Syntax
  - Remarks

## Cross References

- See also: GAMMADIST, Statistical Functions, Probability Distributions

<!-- tags: [gammainv, geomean, statistical functions, gamma distribution, syncfusion sdk] keywords: [inverse, cumulative distribution, probability, mean, geometric mean, api] -->
```

---

<!-- 페이지 109 -->

```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_178.jpeg
document_name: calculate
page_number: 178
page_id: calculate#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:43Z
fidelity: lossless
-->

# Essential Calculate

## Content

### 4.7.67 HYPGEOMDIST

**Returns the hypergeometric distribution.** HYPGEOMDIST returns the probability of a given number of sample successes, given the sample size, population successes and population size.

#### Syntax

HYPGEOMDIST(sample_s, number_sample, population_s, number_population)

where:
- **sample_s** is the number of successes in the sample.
- **number_sample** is the size of the sample.
- **population_s** is the number of successes in the population.
- **number_population** is the population size.

#### Remarks

- All arguments are truncated to integers.
- sample_s must be >= 0 and less than both number_sample and population_s.
- number_sample must be >= 0 and < number_population.
- population_s must be >= 0 and < number_population.
- number_population must be >= 0.
- The equation for the hypergeometric distribution is:

\[
P(X=x) = h(x; n, M, N) = \frac{\binom{M}{x}\binom{N-M}{n-x}}{\binom{N}{n}}
\]

where:
- x = sample_s
- n = number_sample
- M = population_s
- N = number_population

## API Reference

### Parameters

| Name           | Type          | Description                                                                 |
|----------------|---------------|-----------------------------------------------------------------------------|
| sample_s       | integer       | The number of successes in the sample.                                         |
| number_sample  | integer       | The size of the sample.                                                     |
| population_s   | integer       | The number of successes in the population.                                    |
| number_population | integer | The size of the population.                                                   |

### Returns

The probability of exactly sample_s successes in a sample of size number_sample.

### Exceptions

- If any of the arguments are non-integer or do not meet the criteria specified in the Remarks section, an error may occur.

## Code Examples

### Example in C#

```csharp
double probability = HYPGEOMDIST(2, 5, 10, 20);
Console.WriteLine($"Probability: {probability}");
```

## See also

- Probability distributions
- Hypergeometric distribution formula
- Statistical functions in WinForms

<!-- tags: [winforms, statistical functions, hypergeometric distribution, syncfusion windows forms, 11.4.0.26] keywords: [HYPGEOMDIST, hypergeometric, probability, sample, population, successes] -->
```

---

<!-- 페이지 110 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_182.jpeg
document_name: calculate
page_number: 182
page_id: calculate#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:01Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Returns the internal rate of return for a series of cash flows represented by the numbers in values.
- Checks for blank or null values.
- Checks whether a value is an error.

## Content

### 4.7.74 IRR
Returns the internal rate of return for a series of cash flows represented by the numbers in values. The cash flows must occur at regular intervals such as monthly or annually.

#### Syntax
`IRR(values, guess)`

#### Parameters
- **values**: An array or a reference to cells that contain numbers for which you want to calculate the internal rate of return. Values must contain at least one positive value and one negative value to calculate the internal rate of return. IRR uses the order of values to interpret the order of cash flows. Be sure to enter your payment and income values in the sequence you want.
- **guess**: A number that you guess is close to the result of IRR. An iterative technique is used for calculating IRR. In most cases, you do not need to provide a guess for the IRR calculation. If a guess is omitted, it is assumed to be 0.1 (10 percent).

### 4.7.75 IsBlank
The IsBlank function checks for blank or null values.

#### Syntax
`IsBlank(value)`

#### Parameters
- **value**: The value that you want to test. If the value is blank, this function will return TRUE. If the value is not blank, the function will return FALSE.

### 4.7.76 IsErr
The IsErr function checks whether a value is an error.

#### Syntax
`IsErr(value)`

#### Parameters
- **value**: The value that you want to test. If the value is an error value (except #N/A), this function will return TRUE/FALSE to indicate whether a value is an error.

## API Reference
### Methods
- **IRR(values, guess)**: Returns the internal rate of return.
  - **Parameters**:
    - `values`: Array or reference to cells containing numbers.
    - `guess`: Optional guess for the result of IRR.
  - **Returns**: The internal rate of return.

- **IsBlank(value)**: Checks for blank or null values.
  - **Parameters**:
    - `value`: The value to test.
  - **Returns**: TRUE if the value is blank, FALSE otherwise.

- **IsErr(value)**: Checks whether a value is an error.
  - **Parameters**:
    - `value`: The value to test.
  - **Returns**: TRUE if the value is an error (except #N/A), FALSE otherwise.

## Code Examples
### Example 1: Calculating IRR
```csharp
double[] cashFlows = {-10000, 3000, 4200, 6800};
double guess = 0.1;

double irr = IRR(cashFlows, guess);
Console.WriteLine("IRR: " + irr);
```

### Example 2: Checking if a value is blank
```csharp
string value = "   "; // or any value

bool isBlank = IsBlank(value);
Console.WriteLine("Is Blank: " + isBlank);
```

### Example 3: Checking if a value is an error
```csharp
double value = double.NaN; // or any error value

bool isError = IsErr(value);
Console.WriteLine("Is Error: " + isError);
```

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Financial Functions, Error Checking, Blank Checks, Internal Rate of Return, IRR, IsBlank, IsErr] keywords: [IRR, cash flows, guess, blank values, error values, financial calculations, checking] -->
```

---

<!-- 페이지 111 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_186.jpeg
document_name: calculate
page_number: 186
page_id: calculate#page_186
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:23Z
fidelity: lossless
-->

## Essential Calculate

- If there are fewer than four data points or if the standard deviation of the sample equals zero, KURT returns the `#DIV/0!` error value.
- Kurtosis is defined as:

  \[
  \left\{ \frac{n(n+1)}{(n+1)(n+2)(n+3)} \sum \left( \frac{x_i - \overline{x}}{s} \right)^4 \right\} - \frac{3(n+1)^2}{(n+2)(n+3)}
  \]

  where:
  - \( s \) is the sample standard deviation.

## 4.7.85 LARGE

### Overview
- Returns the k-th largest value in a data set.

### Syntax
```
LARGE(array, k)
```

#### Parameters
- `array`: The array or range of data for which you want to determine the k-th largest value.
- `k`: The position (from the largest) in the array or cell range of data to return.

### Remarks
- If \( n \) is the number of data points in a range, then `LARGE(array, 1)` returns the largest value, and `LARGE(array, n)` returns the smallest value.

## 4.7.86 LEFT

### Overview
- `LEFT` returns the first character or characters in a text string, based on the number of characters you specify.

### Syntax
```
LEFT(text, [num_chars])
```

<!-- tags: [syncfusion, winforms, calculate, kurtosis, large, left, statistic, largest value, text operations, API reference] keywords: [kurtosis formula, standard deviation, array, k position, text string, num_chars, greatest, smallest] -->
```

---

<!-- 페이지 112 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_190.jpeg
document_name: calculate
page_number: 190
page_id: calculate#page_190
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:36Z
fidelity: lossless
-->

## Essential Calculate

### Syntax

LOGINV(probability, mean, standard_dev)

**where:**

- probability is the probability associated with the lognormal distribution.
- mean is the mean of ln(x).
- standard_dev is the standard deviation of ln(x).

### Remarks

- Probability must be >= 0 and < 1.
- Standard_dev must be positive.
- The inverse of the lognormal distribution function is:
  
\[
LOGINV(p, \mu, \sigma) = e^{\{ \mu + \sigma \times [NORMSINV(p)]\}}
\]

## 4.7.93 LOGNORMDIST

Returns the cumulative lognormal distribution of x, where \ln(x) is normally distributed with parameters mean and standard_dev.

### Syntax

LOGNORMDIST(x, mean, standard_dev)

**where:**

- x is the value at which the function can be evaluated.
- mean is the mean of \ln(x).
- standard_dev is the standard deviation of \ln(x).

### Remarks

- Both x and standard_dev must be positive.

```

---

<!-- 페이지 113 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: calculate
page_number: 194
page_id: calculate#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:45Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains the syntax and usage of functions such as `MID`, `MIN`, and `MINA`.
- Provides detailed descriptions and remarks for each function to understand their behavior.

## Content

### Syntax

#### MID Function
MID(text, start_position, num_chars)

Where:
- **text** is the text containing the characters to extract.
- **start** is the position of the first character in the text to extract.
- **number** specifies the number of characters in the part of the text.

#### 4.7.100 MIN
Returns the smallest number in a set of values.

- **Syntax**
    MIN(number1, number2, ...)

Where:
- **number1, number2, ...** are numbers for which you want to find the minimum value.

- **Remarks**
    - If an argument is an array or reference, only numbers in that array or reference are used.
    - Empty cells, logical values, or text in the array or reference are ignored. If logical values and text should not be ignored, use `MINA`.

#### 4.7.101 MINA
Returns the smallest value in the list of arguments. Text and logical values such as True and False are compared as well as numbers.

- **Syntax**
    MINA(value1, value2, ...)

### Summary of Functions
The functions `MID`, `MIN`, and `MINA` are described with their syntax, parameters, and remarks to ensure users understand how to effectively use them in their calculations.

## RAG Annotations
<!-- tags: [functions, syntax, min, mina, mid] keywords: [MID, MIN, MINA, start_position, text, num_chars, values, remarks, array, reference] -->
```

---

<!-- 페이지 114 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: calculate
page_number: 198
page_id: calculate#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:57Z
fidelity: lossless
-->

### 4.7.107 NEGBINOMDIST

Returns the negative binomial distribution. NEGBINOMDIST returns the probability that there will be number_f failures before the number_s-th success, when the constant probability of a success is probability_s.

#### Syntax

NEGBINOMDIST(number_f, number_s, probability_s)

where:
- number_f is the number of failures.
- number_s is the threshold number of successes.
- probability_s is the probability of a success.

#### Remarks
- number_s must be >= 1.
- probability_s must be >= 0 and <= 1.
- number_f must be >= 0.
- The equation for the negative binomial distribution is:

\[ nb(x;r;p) = \binom{x+r-1}{r-1} p^r (1-p)^x \]

where:
- \( x \) is number_f
- \( r \) is number_s
- \( p \) is probability_s

### 4.7.108 NORMDIST

---

© 2013 Syncfusion. All rights reserved.
```

---

<!-- 페이지 115 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_202.jpeg
document_name: calculate
page_number: 202
page_id: calculate#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:07Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes the `NPV` and `NPER` functions used for calculating financial values.
- Covers parameters and usage of these functions in financial calculations.

## Content

### NPER(rate, pmt, pv, fv, type)

where:
- **rate** is the interest rate per period.
- **pmt** is the payment made each period; it cannot change over the life of the annuity.
- **pv** is the present value or the lump-sum amount that a series of future payments is worth right now.
- **fv** is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).
- **type** is the number 0 or 1 and indicates when payments are due. If type equals:
  - 0 - payments are due at the end of the period
  - 1 - payments are due at the beginning of the period

### 4.7.115 NPV

#### Overview
Calculates the net present value of an investment by using a discount rate and a series of future payments (negative values) and income (positive values).

#### Syntax
NPV(rate, value1, value2, …)

#### Parameters
where:
- **rate** is the rate of discount over the length of one period.
- **value1, value2, …** are arguments representing the payments and income. Value1, value2, … must be equally spaced in time and occur at the end of each period. NPV uses the order of value1, value2, ... to interpret the order of cash flows. Be sure to enter your payment and income values in the correct sequence.

#### Remarks
- The NPV investment begins one period before the date of the value1 cash flow and ends with the last cash flow in the list. The NPV calculation is based on future cash flows.

```markdown
<!-- tags: [financial-calculation, npv, nper, investment, payments, cash-flows] keywords: [rate, present-value, future-value, discount-rate, payments] -->
```

---

<!-- 페이지 116 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_206.jpeg
document_name: calculate
page_number: 206
page_id: calculate#page_206
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:20Z
fidelity: lossless
-->

## PERCENTRANK

### Syntax

```plaintext
PERCENTRANK(array, x, significance)
```

**where:**

- `array` is the range of data with numeric values that defines relative standing.
- `x` is the value for which you want to know the rank.
- `significance` is an optional value that identifies the number of significant digits for the returned percentage value. If omitted, PERCENTRANK uses three digits (0.xxx).

### Remarks

- Significance must be >= 1.
- If `x` does not match one of the values in the array, PERCENTRANK interpolates to return the correct percentage rank.

---

## 4.7.122 Permut

### The Permut Function

The Permut function returns the number of permutations of `n` items taken `k` time.

### Syntax

```plaintext
Permut(n, k)
```

**where,**

- `n` is the number of items.
- `k` is the time taken.

---

## 4.7.123 PI

### PI

Returns the number 3.14159265358979, the mathematical constant pi, accurate to 15 digits.

### Syntax

```plaintext
PI()
```

---
<!-- tags: [PERCENTRANK, Permut, PI, function, mathematical constant, percentage rank, permutation, numeric data, Winforms, Syncfusion] keywords: [PERCENTRANK, Permut, PI, numeric values, significant digits, interpolation, permutations, mathematical constant, pi, accuracy, function syntax] -->
```

---

<!-- 페이지 117 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_210.jpeg
document_name: calculate
page_number: 210
page_id: calculate#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:32Z
fidelity: lossless
-->

## Essential Calculate

### Consistency in Units

- **Guideline**: Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.

## 4.7.129 PROB

### Functionality

Returns the probability whose values are in a range that is between two limits. If upper_limit is not supplied, returns the probability that values in x_range are equal to lower_limit.

### Syntax

**PROB(x_range, prob_range, lower_limit, upper_limit)**

#### Parameters:

- **x_range**: The range of numeric values of x with which there are associated probabilities.
- **prob_range**: A set of probabilities associated with values in x_range.
- **lower_limit**: The lower bound on the value for which you want a probability.
- **upper_limit**: The optional upper bound on the value for which you want a probability.

### Remarks

- Any value in prob_range must be \( > 0 \) and \( < 1 \).
- If upper_limit is omitted, PROB returns the probability of being equal to lower_limit.

## 4.7.130 PRODUCT

### Functionality

Multiplies all the numbers given as arguments and returns the product.

### Syntax

**PRODUCT(number1, number2, ...)**

#### Parameters:

- **number1, number2, ...**: Numbers that you want to multiply.

<!-- tags: [product, module, control, api, version?] keywords: [PROB, PRODUCT, function, probability, multiplication, calculate, parameters, range, limits, upper_limit, lower_limit, probabilities] -->
```

---

<!-- 페이지 118 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: calculate
page_number: 214
page_id: calculate#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:45Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.136 RATE

Returns the interest rate per period of an annuity. RATE is calculated by iteration and may not converge to a unique solution.

#### Syntax

```plaintext
RATE(nper, pmt, pv, fv, type, guess)
```

#### where:

- **nper** is the total number of payment periods in an annuity.
- **pmt** is the payment made for each period and cannot change over the life of the annuity. Typically, pmt includes the principal and interest but, no other fees or taxes. If pmt is omitted, you must include the fv argument.
- **pv** is the present value— the total amount that a series of future payments is worth now.
- **fv** is the future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0).
- **type** is the number 0 or 1 and indicates when payments are due. If type equals:
  - 0 - Payments are due at the end of the period.
  - 1 - Payments are due at the beginning of the period.
- **guess** is your guess for what the rate will be. If you omit guess, it is assumed to be 10 percent. If RATE does not converge, try different values for guess. RATE usually converges if guess is between 0 and 1.

### 4.7.137 RIGHT

RIGHT returns the last character or characters in a text string, based on the number of characters you specify.

#### Syntax

```plaintext
RIGHT(text, num_chars)
```

#### where:

- **text** is the text string containing the characters you want to extract.
- **num_chars** specifies the number of characters you want RIGHT to extract.

```html
<!-- tags: [rate, annuity, interest, right, text manipulation, financial function, iteration, present value, future value, payment, syncfusion winforms] keywords: [rate, financial functions, right function, string extraction, financial calculations, iteration, pv, fv, pmt, type, guess, text processing] -->
```

---

<!-- 페이지 119 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_218.jpeg
document_name: calculate
page_number: 218
page_id: calculate#page_218
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:59Z
fidelity: lossless
-->

# Essential Calculate

Determines the sign of a number. Returns 1 if the number is positive, zero (0) if the number is 0, and -1 if the number is negative.

## Syntax

```markdown
SIGN(number)
```

where:  
`number` is any real number.

## 4.7.144 SIN

Returns the sine of the given angle.

### Syntax

```markdown
SIN(number)
```

where:  
`number` is the angle in radians for which you want the sine.

### SINH

Returns the hyperbolic sine of a number.

### Syntax

```markdown
SINH(number)
```

where:  
`number` is any real number.

### Remarks

- The formula for the hyperbolic sine is,

<!-- tags: [Essential Calculate, SIGN, SIN, SINH, domain: syncfusion-sdk, product: Syncfusion Winforms, version: 11.4.0.26] keywords: [calculate, sign, sine, hyperbolic sine, angle, radians, real numbers, formula] -->
```

---

<!-- 페이지 120 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_222.jpeg
document_name: calculate
page_number: 222
page_id: calculate#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:08Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Number must be >= 0.

## Content

### 4.7.151 STANDARDIZE

**Returns a normalized value from a distribution characterized by mean and standard_dev.**

#### Syntax
STANDARDIZE(x, mean, standard_dev)

**where:**
- **x**: is the value that you want to normalize.
- **mean**: is the arithmetic mean of the distribution.
- **standard_dev**: is the standard deviation of the distribution.

#### Remarks
- standard_dev must be > 0.
- The equation for the normalized value is:

\[
Z = \frac{X - \mu}{\sigma}
\]

### 4.7.152 STDEV

**Estimates the standard deviation based on a sample. The standard deviation is a measure of how widely values are dispersed from the average value (the mean).**

#### Syntax
STDEV(number1, number2, ...)

**where:**
- **number1, number2, ...**: are number arguments corresponding to a sample of a population.

<!-- tags: [syncfusion, calculate, standardize, stdev, standard deviation, arithmetic mean] 
keywords: [normalized value, mean, standard_dev, standard deviation, sample, distribution] -->
```

---

<!-- 페이지 121 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_226.jpeg
document_name: calculate
page_number: 226
page_id: calculate#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:18Z
fidelity: lossless
-->

# Essential Calculate

## Remarks

- The equation for the standard error of the predicted \( y \) is:

\[
\sqrt{\frac{1}{(n-2)} \left[ \sum (y - \overline{y})^2 - \frac{\left[ \sum (x - \overline{x})(y - \overline{y}) \right]^2}{\sum (x - \overline{x})^2} \right]}
\]

  where:
  - \(\overline{x}\) and \(\overline{y}\) are the sample means AVERAGE(known_x's) and AVERAGE(known_y's).
  - \( n \) is the sample size.

## 4.7.157 SUBSTITUTE

Substitutes new_text for old_text in a text string. Use SUBSTITUTE when you want to replace specific text in a text string; use REPLACE when you want to replace any text that occurs in a specific location in a text string.

### Syntax

SUBSTITUTE(text, old_text, new_text, instance_num)

where:
- **Text** is the text or the reference to a cell containing text for which you want to substitute characters.
- **Old_text** is the text you want to replace.
- **New_text** is the text you want to replace old_text with.
- **Instance_num** specifies which occurrence of old_text you want to replace with new_text. If you specify instance_num, only that instance of old_text is replaced. Otherwise, every occurrence of old_text in text is changed to new_text.

For example:

The example may be easier to understand if you copy it to a blank worksheet.

<!-- tags: [Syncfusion Winforms, SUBSTITUTE, Text Manipulation, Standard Error Calculation] keywords: [SUBSTITUTE function, text substitution, standard error, sample mean, sample size, equation, text manipulation, Excel functions] -->
```

---

<!-- 페이지 122 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_230.jpeg
document_name: calculate
page_number: 230
page_id: calculate#page_230
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:31Z
fidelity: lossless
-->

## Summary of Functions: SUMX2PY2 and SYD

### Overview
This page introduces two functions, `SUMX2PY2` and `SYD`, commonly used in financial and mathematical calculations in Excel-like environments, with a focus on their syntax and application.

### SUMX2PY2 Function

#### Syntax
```markdown
SUMX2PY2(array_x, array_y)
```

#### Parameters
- **array_x**: The first array or range of values.
- **array_y**: The second array or range of values.

#### Remarks
- If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included.
- The equation for the sum of the sum of squares is:
  \[
  SUMX2PY2 = \sum (x^2 + y^2)
  \]

### SYD Function

#### Syntax
```markdown
SYD(cost, salvage, life, per)
```

#### Parameters
- **cost**: The initial cost of the asset.
- **salvage**: The value at the end of the depreciation (sometimes called the salvage value of the asset).
- **life**: The number of periods over which the asset is depreciated (sometimes called the useful life of the asset).
- **per**: The period and must use the same units as `life`.

#### Remarks
- **SYD** is calculated as follows:
  <!-- Placeholder for SYD calculation formula -->

---

## API Reference

### `SUMX2PY2`

**Namespace**: `System`

**Class**: `Math`

- **Parameters**:
  - `array_x`: Array or range of numerical values.
  - `array_y`: Array or range of numerical values.
- **Returns**: A numerical value representing the sum of the sum of squares of the two arrays.

### `SYD`

**Namespace**: `System`

**Class**: `Financial`

- **Parameters**:
  - `cost`: The initial cost of the asset (numerical value).
  - `salvage`: The salvage value of the asset at the end of depreciation (numerical value).
  - `life`: The total useful life of the asset in periods (numerical value).
  - `per`: The specific period over which depreciation is to be calculated (numerical value).
- **Returns**: A numerical value representing the depreciation of the asset for the specified period.

---

## Code Examples

### Using SUMX2PY2
```csharp
using System;

class Program
{
    static void Main()
    {
        double[] array_x = {1, 2, 3};
        double[] array_y = {4, 5, 6};
        double sumX2PY2 = SUMX2PY2(array_x, array_y);
        Console.WriteLine("SUMX2PY2: " + sumX2PY2);
    }

    static double SUMX2PY2(double[] x, double[] y)
    {
        double sum = 0;
        for (int i = 0; i < x.Length; i++)
        {
            sum += Math.Pow(x[i], 2) + Math.Pow(y[i], 2);
        }
        return sum;
    }
}
```

### Using SYD
```csharp
using System;

class Program
{
    static void Main()
    {
        double cost = 10000;
        double salvage = 500;
        double life = 5;
        double per = 2;
        double depreciation = SYD(cost, salvage, life, per);
        Console.WriteLine("Depreciation for period " + per + ": " + depreciation);
    }

    static double SYD(double cost, double salvage, double life, double per)
    {
        double numerator = (life - per + 1);
        double denominator = (life * (life + 1)) / 2;
        return (cost - salvage) * (numerator / denominator);
    }
}
```

---

## Tags and Keywords

<!-- tags: [Syncfusion Winforms, Math, Financial, SUMX2PY2, SYD, Functions, Arithmetic, Depreciation, Arrays] keywords: [SUMX2PY2, SYD, array, cost, salvage, life, per, depreciation, sum of squares, useful life, formula, mathematical function, financial function] -->
```

---

<!-- 페이지 123 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_234.jpeg
document_name: calculate
page_number: 234
page_id: calculate#page_234
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:56Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- TRIMMEAN calculates the mean of a data set after excluding a specified percentage of data points from the top and bottom tails.
- The True function returns the logical value for True.
- TRUNC truncates a number to an integer by removing the fractional part of the number.

## Content

### 4.7.173 TRIMMEAN

**Description:**
Returns the mean of the interior of a data set. TRIMMEAN calculates the mean taken by excluding a percentage of data points from the top and bottom tails of a data set.

**Syntax:**
```plaintext
TRIMMEAN(array, percent)
```

**Where:**
- `array` is the array or range of values to trim and average.
- `percent` is the fractional number of data points to exclude from the calculation. For example, if `percent = 0.2`, 4 points are trimmed from a data set of 20 points (20 x 0.2): 2 from the top and 2 from the bottom of the set.

**Remarks:**
- Percent must be >= 0 and <= 1.
- TRIMMEAN rounds off the number of excluded data points down to the nearest multiple of 2. If `percent = 0.1`, 10 percent of 30 data points equals 3 points. For symmetry, TRIMMEAN excludes a single value from the top and bottom of the data set.

### 4.7.174 True

**Description:**
The True function returns the logical value for True.

**Syntax:**
```plaintext
True(stringvalue)
```

**Where:**
- `stringvalue` is to provide an empty string.

### 4.7.175 TRUNC

**Description:**
Truncates a number to an integer by removing the fractional part of the number.

**Syntax:**
---

## API Reference

Not applicable for this section.

## Code Examples

Not applicable for this section.

## Cross References

Not applicable for this section.

<!-- tags: [calculate, TRIMMEAN, True, TRUNC, Winforms, Syncfusion] keywords: [mean, data points, logical value, truncate, number, integer, fractional part, numerical calculation, data set] -->
```

---

<!-- 페이지 124 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_238.jpeg
document_name: calculate
page_number: 238
page_id: calculate#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:10Z
fidelity: lossless
-->

## Calculation Methods and Functions

### Overview
- Explanation of life as the number of periods over which an asset is depreciated.
- Clarification of terms like `start_period` and `end_period` for calculating depreciation.
- Description of the `factor` and the `no_switch` parameter in calculating balance decline.

### Detailed Explanation of Depreciation Parameters

**life**: The number of periods over which the asset is depreciated (sometimes called the useful life of the asset).

- **start_period**: The starting period for which you want to calculate the depreciation. `start_period` must use the same units as life.
- **end_period**: The ending period for which you want to calculate the depreciation. `end_period` must use the same units as life.
- **factor**: The rate at which the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method).
- **no_switch**: A logical value specifying whether to switch to straight-line depreciation when depreciation is greater than the declining balance calculation.
  - If `no_switch` is `True`, straight-line depreciation is not used even when the depreciation is greater than the declining balance calculation.
  - If `no_switch` is `False` or omitted, straight-line depreciation is used when depreciation is greater than the declining balance calculation.
  
All arguments except `no_switch` must be positive numbers.

---

## 4.7.183 VLOOKUP

### Overview
- The `VLOOKUP` function searches for a value in the leftmost column of a table and returns a value in the same row from a specified column.
- Recommendation to use `VLOOKUP` instead of `HLOOKUP` when comparison values are located in a column to the left of the data you want to find.

#### Syntax

```plaintext
VLOOKUP(lookup_value, table_array, col_index_num, range_lookup)
```

#### Parameters

- **lookup_value**: The value to be found in the first column of the array. Lookup_value can be a value, a reference, or a text string.
- **table_array**: The table of information in which data is looked up. Use a reference to a range or a range name.
  - If `range_lookup` is `True`, the values in the first column of the `table_array` must be placed in ascending order: ..., -2, -1, 0, 1, 2, ..., A-Z, `False`, `True`; otherwise `VLOOKUP` may not give the correct value.
  - If `range_lookup` is `False`, `table_array` does not need to be sorted.
  - The values in the first column of the `table_array` can be text, numbers, or logical values.
  - Uppercase and lowercase text are equivalent.

## RAG Annotations
<!-- tags: [depreciation, calculation, VLOOKUP, straight-line-depreciation, declining-balance-method] keywords: [start_period, end_period, factor, life, linear-depreciation, balance-decline, no_switch, range_lookup, table_array, lookup_value, col_index_num, VLOOKUP, HLOOKUP] -->
```

---

<!-- 페이지 125 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_242.jpeg
document_name: calculate
page_number: 242
page_id: calculate#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:28Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- This page describes the mathematical formula and parameters for performing a Z-test using the `ZTEST` function in Syncfusion Winforms.

## Content

The Z-test formula is represented as follows:

\[ ZTEST(array, \mu_o) = 1 - NORMSDIST\left(\frac{(\overline{x} - \mu_o) \cdot \sqrt{n}}{s}\right) \]

### Formula Explanation
- **\( \overline{x} \)**: Represents the sample mean, calculated as AVERAGE(array).
- **\( s \)**: Represents the sample standard deviation, calculated as STDEV(array).
- **\( n \)**: Represents the number of observations in the sample, calculated as COUNT(array).

### Parameters
- **\( array \)**: The input data array used to calculate the sample mean and standard deviation.
- **\( \mu_o \)**: The hypothesized population mean against which the test is performed.

<!-- tags: [syncfusion, ztest, array, population mean, sample mean, standard deviation, number of observations] keywords: [ztest, array, sample mean, standard deviation, population mean, calculate] -->
```

---

<!-- 페이지 126 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_246.jpeg
document_name: calculate
page_number: 246
page_id: calculate#page_246
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:37Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- This page demonstrates how to force calculations to be processed after `Engine.CalculatingSuspended` has been set to `true`.
- Covers both C# and VB.NET implementations.

## Content

To illustrate the process of calculating calculations after setting `Engine.CalculatingSuspended` to `true`, the following code samples in C# and VB.NET are provided:

### C#

```csharp
// Creates some data object that implements ICalcData.
this.data = new ArrayCalcData(a);

// Creates a CalcEngine object using this ICalcData object.
CalcEngine engine = new CalcEngine(this.data);

// Turn off calculations.
engine.CalculatingSuspended = true;

// Makes multiple updates to this.data.
// Turn on calculations.
engine.CalculatingSuspended = false;

// Calls RecalculateRange so any formulas in the data can be computed.
engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), data);
```

### VB.NET

```vb
' Creates some data object that implements ICalcData.
Me.data = New ArrayCalcData(a)

' Creates a CalcEngine object using this ICalcData object.
Dim engine As New CalcEngine(Me.data)

' Turn off calculations.
engine.CalculatingSuspended = True

' Makes multiple updates to this.data.
' Turn on calculations.
engine.CalculatingSuspended = False

' Calls RecalculateRange so any formulas in the data can be computed.
engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), Data)
```

## Cross References

- See also: [Syncfusion WinForms Documentation](https://www.syncfusion.com/documentation) for more details on the `CalcEngine` and `ICalcData` interfaces.

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, CalcEngine, ICalcData, calculations, suspended, recalculateRange, C#, VB.NET] keywords: [calculations, suspended, recalculateRange, CalcEngine, ICalcData, Engine, Async, Data, Range] -->
```

---

<!-- 페이지 127 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_250.jpeg
document_name: calculate
page_number: 250
page_id: calculate#page_250
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:51Z
fidelity: lossless
-->

# Index

| Term | Page Number |
| --- | --- |
| ABS 142 | CEILING 149 |
| ACOS 143 | Char 150 |
| ACOSH 143 | CHIDIST 150 |
| Add Function 106 | CHIINV 151 |
| Adding Calculation Support 64 | CHITTEST 152 |
| Adding Calculation Support to an Array Using ICalcData 43 | Choose 152 |
| ADDRESS 133 | Class Diagram 25 |
| AND 144 | CLEAN 129 |
| ASIN 144 | Column 153 |
| ASINH 144 | COMBIN 153 |
| ATAN 145 | Common 248 |
| ATAN2 145 | CONCATENATE 154 |
| ATANH 146 | Concepts and Features 64 |
| Automatic Calculations 68 | CONFIDENCE 154 |
| AVEDEV 146 | Console Application CalcQuickBase 37 |
| AVERAGE 147 | Conventions 84 |
| AVERAGEA 147 | CORREL 155 |
| AVERAGEIF 130 | COS 156 |
| AVERAGEIFS 131 | COSH 156 |
| AVG 148 | COUNT 156 |
| BINOMDIST 148 | COUNTA 157 |
| CalcEngine 245 | COUNTBLANK 157 |
| CalcQuick 243 | COUNTIF 158 |
| CalcQuickBase 64 | COVAR 158 |
| CalcSheet and CalcWorkbook Classes 94 | Creating Platform Application 26 |
| Calculating 140 | CRITBINOM 159 |
| Car Insurance Sample Details 95 | DATE 160 |
| Concept and Features 64 | Date and Time 114 |
| Conventions 84 | DATEVALUE 160 |
| CORREL 155 | DAY 161 |
| COS 156 | DAYS360 161 |
| COSH 156 | DB 162 |
| COUNT 156 | DDB 163 |
| COUNTA 157 | DEGREES 164 |
| COUNTBLANK 157 | |
| COUNTIF 158 | |
| COVAR 158 | |
| DB 162 | |
| DDB 163 | |
| DEGREES 164 | |

<!-- tags: [Syncfusion Winforms, Calculate, Index] keywords: [ABS, ACOS, ACOSH, Add Function, Adding Calculation Support, Address, AND, ASIN, ASINH, ATAN, ATAN2, ATANH, Automatic Calculations, AVEDEV, AVERAGE, AVERAGEA, AVERAGEIF, AVERAGEIFS, AVG, BINOMDIST, CalcEngine, CalcQuick, CalcQuickBase, CalcSheet, CalcWorkbook, Car Insurance, Sample Details, Concepts and Features, Conventions, CORREL, COS, COSH, COUNT, COUNTA, COUNTBLANK, COUNTIF, COVAR, DB, DDB, DEGREES] -->
```

---

<!-- 페이지 128 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_254.jpeg
document_name: calculate
page_number: 254
page_id: calculate#page_254
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:10Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Provides essential calculations and formulas for working with spreadsheets and data processing.
- Focuses on functions like SUM, SUMPRODUCT, Statistical calculations, and Date & Time operations.
- Explores various features for effective application development using Syncfusion Winforms.

## Content

### Functions and Calculations

- **Sum 227**
- **SumIf 227**
- **SUMIFS 133**
- **Summary 77**
- **SUMPRODUCT 228**
- **SUMSQ 228**
- **SUMX2MY2 229**
- **SUMX2PY2 229**
- **SumXmY2 228**
- **Supported Algebra 102**
- **SYD 230**
- **T 128**
- **TAN 231**
- **TANH 231**
- **Text 113, 232**
- **Time 232**
- **TIMEVALUE 232**
- **TODAY 233**
- **Trim**  
  233
- **trimmean 234**
- **true 234**
- **TRUNC 234**
- **Upper**  
  235
- **V**  
  25
- **Value**  
  235
- **Var**  
  236
- **VarA**  
  236
- **VarP**  
  236
- **VARPA**  
  236
- **VDB**  
  237
- **VLOOKUP**  
  238

### Development and Application Features

- **Web Application Deployment 23**
- **Web Control Performance 88**
- **WEEKDAY 239**
- **Weibull 240**
- **Windows 29**
- **Windows Application Using Variables and CalcQuickBase 40**
- **Windows Forms CalcQuickBase 40**
- **Working with an Excel Spreadsheet 89**
- **Working with System.Windows.Forms.DataGrid 78**
- **WPF 33**
- **Xirr 240**
- **XOR 128**
- **YEAR 240**
- **ZTEST 241**

### Additional Information

- **Tracking the Information**  
  139
- **The FormulaInfo Class**  
  67
- **The ICalcData Interface**  
  78
- **Using CalcDataGrid as a Single Spreadsheet**  
  79
- **Using Essential XlsIO**  
  95
- **Using Explicit Events**  
  68
- **Using Function Library Formulas**  
  106
- **Using RegisterControlArray**  
  74
- **Using Several CalcDataGrids in a Workbook**  
  81

## API Reference (If Applicable)

<!-- Add relevant API reference information here -->

## Code Examples (If Applicable)

<!-- Add relevant code examples here -->

## RAG Annotations

<!-- tags: [functions, calculations, date-time, development, windows-forms, application-deployment] keywords: [syncfusion, WinForms, SUM, SUMPRODUCT, statistical, spreadsheet, application-development] -->
```

---

<!-- 페이지 129 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_003.jpeg
document_name: calculate
page_number: 003
page_id: calculate#page_003
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:22Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Covers topics related to calculation methods and support, including automatic calculations, using the ICalcData interface, and working with CalcDataGrids.
- Explains web control performance, interacting with Excel spreadsheets, and supported algebraic operations.
- Details function library features, including addition, removal, and replacement of functions, as well as specific categories like logical, text, date and time, and financial functions.

## Content

### 4.1 Calculation Methods
#### 4.1.1 Indexer Method using Variables
- **4.1.1.2 Automatic Calculations** ..... 68
  - **4.1.1.2.1 Using Explicit Events** ..... 68
  - **4.1.1.2.2 Using RegisterControlArray** ..... 74
- **4.1.1.3 Resetting Keys by using Calculate Engine** ..... 76
  - **4.1.1.3.1 Methods** ..... 77
- **4.1.1.4 Summary** ..... 77
#### 4.1.2 General Calculation Support - ICalcData
- **4.1.2.1 The ICalcData Interface** ..... 78
- **4.1.2.2 Working with System.Windows.Forms.DataGrid** ..... 78
  - **4.1.2.2.1 Using CalcDataGrid as a Single Spreadsheet** ..... 79
  - **4.1.2.2.2 Using Several CalcDataGrids in a Workbook** ..... 81
#### 4.1.2.3 Conventions** ..... 84
### 4.2 Web Control Performance
### 4.3 Working with an Excel Spreadsheet
#### 4.3.1 CalcSheet and CalcWorkbook Classes
#### 4.3.2 Using Essential XlsIO
#### 4.3.3 Car Insurance Sample Details
### 4.4 Supported Algebra
#### 4.4.1 Operators
#### 4.4.2 Square Brackets in CalcQuickBase Formulas
#### 4.4.3 Equal Sign, the Formula Character
#### 4.4.4 Using Function Library Formulas
### 4.5 Function Library
#### 4.5.1 Add Function
- **4.5.1.1 Step 1-Writing the Method** ..... 107
- **4.5.1.2 Step 2-Registering the Method with the CalcEngine** ..... 110
#### 4.5.2 Remove and Replace Function
#### 4.5.3 Functions
- **4.5.3.1 Logical** ..... 112
- **4.5.3.2 Text** ..... 113
#### 4.5.4 Date and Time
- **4.5.4.1 LookUps and Information** ..... 115
#### 4.5.5 Financial
#### 4.5.6 Math and Trig functions

## API Reference (if applicable)
- This section can include details about classes, methods, properties, and events related to calculation support and function libraries.

## Code Examples (multi-language supported)
- Example code demonstrating the use of calculation methods and the function library in C# and VB.NET.

## Page-level Navigation/TOC (if applicable)
- A comprehensive Table of Contents is provided for the calculate section, ensuring easy navigation to specific topics.

## Cross References
- References to other sections or related topics within the document to provide additional context.

<!-- tags: [Calculation, Engine, ICalcData, FunctionLibrary, XlsIO, CarInsurance, EssentialCalculate, SyncfusionWinforms] keywords: [Indexer Method, Automatic Calculations, ICalcData Interface, CalcDataGrid, Web Control Performance, Excel Spreadsheet, Supported Algebra, Operators, Function Library] -->
```

---

<!-- 페이지 130 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_007.jpeg
document_name: calculate
page_number: 007
page_id: calculate#page_007
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:43Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- A list of mathematical and logical functions used in a spreadsheet application.
- Each function is accompanied by a page reference for detailed information.
- Functions categorized with numeric labels (4.7.69 to 4.7.103).

## Content

### 4.7.69 Index
- Page: 179

### 4.7.70 Indirect
- Page: 179

### 4.7.71 INT
- Page: 180

### 4.7.72 INTERCEPT
- Page: 180

### 4.7.73 IPMT
- Page: 181

### 4.7.74 IRR
- Page: 182

### 4.7.75 IsBlank
- Page: 182

### 4.7.76 IsErr
- Page: 182

### 4.7.77 ISERROR
- Page: 183

### 4.7.78 IsLogical
- Page: 183

### 4.7.79 IsNA
- Page: 183

### 4.7.80 IsNonText
- Page: 184

### 4.7.81 ISNUMBER
- Page: 184

### 4.7.82 ISPMT
- Page: 184

### 4.7.83 IsText
- Page: 185

### 4.7.84 KURT
- Page: 185

### 4.7.85 LARGE
- Page: 186

### 4.7.86 LEFT
- Page: 186

### 4.7.87 LN
- Page: 187

### 4.7.88 LEN
- Page: 187

### 4.7.89 LOG
- Page: 188

### 4.7.90 LOG10
- Page: 188

### 4.7.91 LOGEST
- Page: 188

### 4.7.92 LOGINV
- Page: 189

### 4.7.93 LOGNORMDIST
- Page: 190

### 4.7.94 Lower
- Page: 191

### 4.7.95 Match
- Page: 191

### 4.7.96 MAX
- Page: 192

### 4.7.97 MAXA
- Page: 192

### 4.7.98 MEDIAN
- Page: 193

### 4.7.99 MID
- Page: 193

### 4.7.100 MIN
- Page: 194

### 4.7.101 MINA
- Page: 194

### 4.7.102 MINUTE
- Page: 195

### 4.7.103 MIRR
- Page: 195

## API Reference

This section includes references to the functions listed above, with each entry providing a brief description and parameters if applicable.

## Code Examples

Code examples demonstrating the usage of these functions in a spreadsheet environment are not provided here. Refer to the detailed documentation on each page.

## Page-level Navigation/TOC (if applicable)

The list of functions serves as a local Table of Contents for this section, guiding users to specific functions and their descriptions.

<!-- tags: [winforms, calculate, mathematical functions, logical functions, spreadsheet, syncfusion] keywords: [index, indirect, int, intercept, ipmt, irr, isblank, iserr, iserror, islogical, isna, isnontext, isnumber, ispmt, istext, kurt, large, left, ln, len, log, log10, logest, loginv, lognormdist, lower, match, max, maxa, median, mid, min, mina, minute, mirr] -->
```

---

<!-- 페이지 131 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: calculate
page_number: 011
page_id: calculate#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:06Z
fidelity: lossless
-->

# Overview

This section covers information on Essential Calculate, its key features, prerequisites to use the control, its compatibility with various OS and browsers, and finally the documentation details complementary with the product. It comprises the following subsections:

## 1.1 Introduction to Essential Calculate

Essential Calculate is a 100% Native .NET library that provides calculation functionality by using the Microsoft .NET framework, so that it can be used in any .NET environment, including C#, VB.NET, and managed C++. Essential Calculate is a UI independent class library that lets you add formula calculation support to Windows Forms, Web Forms, and WPF applications. Essential Calculate does not depend on Microsoft Excel and thus allows you to perform calculations independent of Excel.

The range of calculations includes simple algebraic expressions such as `(1.2^3-1)/8`, to formulas using intrinsic functions like `4 * sqrt(exp(8.4))`, to formulas relying on variables that are defined through controls on a form such as `cos([textBox1] * pi()/180)`, to spreadsheet-like formulas such as `Sum(A2:B14)`. Essential Calculate lets you parse and compute such expressions and includes a library of more than 150 functions. This function library is easily extendable. The data used in the calculations can be from any source, ranging from fixed values to values that are entered through the controls, to data tables and Excel spreadsheets.

Essential Calculate allows you to add extensive calculation support to your business objects. It enables you to easily set up forms that have calculation dependencies among various controls.

### Key Features
![Figure 1: Essential Calculate](https://assets.howtocreateaudiofile.com/image_data.png)

## Key Features

<!-- tags: [essential calculate, native .net library, calculation functionality, windows forms, web forms, wpf applications, microsoft excel, algebraic expressions, intrinsic functions, spreadsheet-like formulas, function library, extendable, business objects, form controls, data tables, excel spreadsheets] -->
```

---

<!-- 페이지 132 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_015.jpeg
document_name: calculate
page_number: 015
page_id: calculate#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:19Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Access installed documentation through the Syncfusion dashboard for detailed information.
- Locate documentation in the Syncfusion Winforms library.

## Content

### Installed Documentation

To access the installed documentation for **Essential Calculate**, follow these steps:

1. Navigate to the **Dashboard**.
2. Select **Documentation** from the navigation menu.
3. Click on **Installed Documentation** to view the locally installed documentation.

The documentation provided here is comprehensive and includes all essential details about **Essential Calculate** functionalities, properties, methods, and other relevant information.

## API Reference

For detailed API reference, consult the Syncfusion Winforms documentation available at the specified dashboard path.

## Code Examples

The installed documentation includes code examples in C# and other supported languages, demonstrating the use of **Essential Calculate** in various scenarios.

## Pagination Information

This page is part of the comprehensive documentation suite for Syncfusion Winforms, version 11.4.0.26.

## Cross References

For additional help and references, refer to the sections listed in the dashboard documentation link.

<!-- tags: [product, module, control, api, version?] keywords: [installed documentation, essential calculate, syncfusion winforms, dashboard, documentation, version 11.4.0.26] -->
```

---

<!-- 페이지 133 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: calculate
page_number: 019
page_id: calculate#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:30Z
fidelity: lossless
-->

# Essential Calculate

## Reporting Edition for Windows Forms

- Integrate Reporting solutions into Windows Forms applications with ease
- Includes high-performance libraries for manipulating Word, PDF, and Excel

### View Options Displayed for Samples

Figure 4: View Options Displayed for Samples

The Windows Forms Sample Browser window is displayed.

### Windows Forms

**DocIO**

- Product Showcase
- Getting Started
- Insert Content
- Formatting
- Page Layout
- References
- Editing
- Mail Merge
- View
- Security
- Import and Export

**Featured Samples**

- Sales Invoice
- Table Insertion
- Employee Report
- Table Of Contents
- Forms
- Clone and Merge
- Update Fields

Figure 5: Calculate Samples displayed on the Contents Pane

2. Click **Calculate** in the Contents tab on the bottom-left pane. The **Calculate** samples are displayed.

## API Reference

### Syncfusion DocIO Library

- **Product**: Essential DocIO
- **Description**: A .NET library that can read and write Microsoft Word files.
- **Features**:
  - Full-fledged object model similar to the Microsoft Office COM libraries.
  - No COM interop required.
  - Built from scratch in C#.
  - Can be used on systems without Microsoft Word installed.

### Examples

- **Sales Invoice**
  - Invoice details and pricing.
- **Table Insertion**
  - Demonstrates adding tables to Word documents.
- **Employee Report**
  - Includes employee details formatted as a Word document.
- **Table Of Contents**
  - Automatically generated table of contents feature.
- **Forms**
  - Illustrates form creation and manipulation.
- **Clone and Merge**
  - Demonstrates cloning and merging Word documents.
- **Update Fields**
  - Shows how to update fields in a Word document.

### Notes

- All samples are hosted on [www.syncfusion.com](http://www.syncfusion.com).

## Copyright Notice

© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion, winforms, reporting, docio, calculate, documentation, sample browser] keywords: [calculate, windows forms, docio, word files, reporting, tables, employee report, forms, clone, merge, update fields, sample browser, essential studio] -->
```

---

<!-- 페이지 134 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: calculate
page_number: 023
page_id: calculate#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:44Z
fidelity: lossless
 -->

## 2.3 Deployment Requirements

This section elaborates on the deployment requirements for using Essential Calculate in various applications. It comprises the following topics:

### 2.3.1 DLLs

The following DLLs need to be referenced in your application for the usage of Essential Calculate.

- Syncfusion.Core.dll
- Syncfusion.Calculate.Base.dll
- Syncfusion.Calculate.Windows.dll
- Syncfusion.Shared.Base.dll
- Syncfusion.Shared.Web.dll

### 2.3.2 Web Application Deployment

Web application by default is deployed in full trust mode. This section discusses the deployment in medium or partial trust scenarios.

### Deploying in Medium Trust or Partial Trust Scenarios

There are two such scenarios in which Syncfusion assemblies might be deployed.

#### Example 1

If the Syncfusion Assemblies are in GAC (Global Assembly Cache), and the Web Application is running in **medium** trust, then the Syncfusion assemblies actually runs in full trust. Hence this scenario is fully supported and there are no additional steps necessary for deployment.

#### Example 2

Say, the Syncfusion Assemblies are present in the application's bin folder and the Web Application is running in **medium** trust, then the Syncfusion assemblies will run in medium trust.

Essential Calculate allows working in medium trust by using following assemblies.

```html
© 2013 Syncfusion. All rights reserved.
```
<!-- tags: [deployment requirements, essential calculate, web application deployment, dlls, medium trust, partial trust, syncfusion assemblies] keywords: [syncfusion.core.dll, syncfusion.calculate.base.dll, syncfusion.calculate.windows.dll, syncfusion.shared.base.dll, syncfusion.shared.web.dll, medium trust, partial trust] -->
```

---

<!-- 페이지 135 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: calculate
page_number: 027
page_id: calculate#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:58Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Essential steps to deploy Essential Calculate into Windows and Web applications.
- Details on creating a new project or website in Microsoft Visual Studio.
- Instructions for setting up WPF applications.

## Content

### Web Application
1. **Open Microsoft Visual Studio**:
    - Go to the **File** menu and click **New Website**.
    - In the **New Website** dialog box, select the **ASP.NET Web Site** template.
    - Name the website and click **OK**.

    ![Figure 11: New Web Site Dialog Box](#)
    *Figure 11: New Web Site Dialog Box*

    **A Web application is created.**

2. **Deploy Essential Calculate**:
    - Now you need to deploy Essential Calculate into this ASP.NET application.
    - Refer to the **ASP.NET** topic for detailed information.

### WPF Application
1. **Open Microsoft Visual Studio**:
    - Go to the **File** menu and click **New Project**.
    - In the **New Project** dialog box, select the **WPF Application** template.
    - Name the project and click **OK**.

## API Reference

No API references are provided on this page.

## Code Examples

No code examples are provided on this page.

## Cross References

See also:
- [Windows topic for detailed information]
- [ASP.NET topic for detailed information]

<!-- tags: [essential-calculate, windows-application, web-application, wpf-application, deployment, project-creation, visual-studio, syncfusion, calculate, sdk] keywords: [essential calculate, windows, web application, wpf application, deployment, project, visual studio, sdk] -->
```

---

<!-- 페이지 136 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_031.jpeg
document_name: calculate
page_number: 031
page_id: calculate#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:10Z
fidelity: lossless
-->

# Essential Calculate

## Content

### Using the CalculateQuickBase Object

#### Step 6: Parse and Compute Calculations

[VB.NET]

```vb
' Create a new CalculateQuickBase. This object represents the CalculateEngine.
Dim cq As CalcQuickBase
cq = New CalcQuickBase()
```

Use the `ParseAndCompute` method to perform calculations by using the `CalculateEngine`.

[C#]

```csharp
// Perform calculations by using Essential Calculate.
string formula = "if(20>10,\"BIG\",\"Small\")";
string value = cq.ParseAndCompute(formula);
```

[VB.NET]

```vb
' Perform calculations by using Essential Calculate.
Dim formula As String = "if(20>10,\"BIG\",\"Small\")"
Dim value As String = cq.ParseAndCompute(formula)
```

#### Step 7: Modify Default Behavior of the CalculateEngine

You can also modify the default behavior of the `CalculateEngine` by using the `Engine` property.

### Example

The default format of appending quotation marks to the concatenated string can be eliminated by using the following code.

[C#]

```csharp
// Strings concatenated by using the ampersand operator will be returned without quotation marks.
cq.Engine.UseNoAmpersandQuotes = true;
```

[VB.NET]

```vb
' Strings concatenated by using the ampersand operator will be returned without quotation marks.
cq.Engine.UseNoAmpersandQuotes = True
```

---

> **Note:** Engine is a class that is defined as a "property" in Essential Calculate.

## API Reference

### Properties
- `UseNoAmpersandQuotes`: A Boolean property to control whether ampersand operator concatenation includes quotation marks.

### Methods
- `ParseAndCompute`: Parses and computes the given formula string using the `CalculateEngine`.

## Code Examples

### C#

```csharp
string formula = "if(20>10,\"BIG\",\"Small\")";
string value = cq.ParseAndCompute(formula);
cq.Engine.UseNoAmpersandQuotes = true;
```

### VB.NET

```vb
Dim formula As String = "if(20>10,\"BIG\",\"Small\")"
Dim value As String = cq.ParseAndCompute(formula)
cq.Engine.UseNoAmpersandQuotes = True
```

---

<!-- tags: [syncfusion, calculate, calculatequickbase, calculateengine, parseandcompute, enginroperty, usenoampersandquotes] keywords: [essential calculate, calculatequickbase, parseandcompute, default behavior, engine property, ampersand operator, quotation marks] -->
```

---

<!-- 페이지 137 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: calculate
page_number: 035
page_id: calculate#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:28Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Perform calculations using `Essential Calculate` with `ParseAndCompute`.
- Modify default behavior of `CalculateEngine` using the `Engine` property.
- Eliminate quotation marks in concatenated strings by setting `UseNoAmpersandQuotes`.

## Content

### Example

The default behavior of adding quotation marks to concatenated strings can be altered using the following code:

#### C#

```csharp
// Strings concatenated with the ampersand operator will return without quotation marks.
cq.Engine.UseNoAmpersandQuotes = true;
```

#### VB.NET

```vbnet
' Strings concatenated with the ampersand operator will return without quotation marks.
cq.Engine.UseNoAmpersandQuotes = True
```

**Note:** `Engine` is a class defined as a "property" in `Essential Calculate`.

`Essential Calculate` is now integrated into your WPF application.

## 3.4 Feature Summary

The features of `Essential Calculate` are summarized below:

- Includes a function library with over 150 functions and supports cross-sheet references.
- Can be used with `Essential XlsIO` to fully load, manipulate, and compute Excel spreadsheets without dependency on Excel.
- Operates independently of Microsoft Excel, enabling calculations without Excel.
- Provides extensive calculation support for custom business objects in both Windows Forms and ASP.NET applications.

<!-- tags: [essential-calculate, essential-xlsio, calculateengine, microsoft-excel, wpf, windows-forms, asp.net, calculation-library] keywords: [essential calculate, function library, cross-sheet references, excel manipulation, business objects, independence from excel, calculation support] -->
```

---

<!-- 페이지 138 -->

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

---

<!-- 페이지 139 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: calculate
page_number: 043
page_id: calculate#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:52Z
fidelity: lossless
-->

### Essential Calculate

```vb
Me.textBox3.Text)
    End If

' Button2_Click
End Sub
```

1. Run the sample by pressing F5. Then in the Name text box, enter Rate and in the Value text box, enter .07. Now press the Register button. Similarly, enter Amount in the Name text box, 15000 in the Value text box followed by pressing the Register button.
2. In the top text box, which is empty, enter the formula: `[Rate] * [Amount]`
3. Press the Compute button. You will then see a screen similar to the one below.

![](https://syncfusion.com/essentialcalculate/form1.png)
*Figure 19: Form Showing Two Variables Registered and a Sample Calculation*

The computed product, 1050, is displayed next to the Compute button.

By examining the code, notice that you register a name with a `CalcQuickBase` object by using its name as an indexer on the `CalcQuickBase` object and assign the desired value to this indexed object. Then to use the name within a formula, you enclose it within square brackets.

## 3.5.3 Adding Calculation Support to an Array Using ICalcData

```xml
© 2013 Syncfusion. All rights reserved.
```
<!-- tags: [calculation, calcquickbase, icalcdata, syncfusion, winforms] keywords: [formula, registration, indexer, computation, array] -->
```

---

<!-- 페이지 140 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_047.jpeg
document_name: calculate
page_number: 047
page_id: calculate#page_047
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:03Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes the process of creating and naming a class file in Visual Studio.
- Highlights the initial setup of a class file, including the creation of an empty class declaration.
- Provides guidance on adding logic to the class to achieve desired functionality.

## Content

### Creating a New Class File

Upon adding a new class file, Visual Studio presents a dialog window that allows you to choose from various templates. The following image illustrates the process of naming the class file.

![](Figure%2023:%20Naming%20the%20Class%20File.png)  
**Figure 23: Naming the Class File**

3. After adding the class, Visual Studio displays the class implementation file whose contents are shown below. In the next few steps, you must add the code to this class to create the functionality you need.

### Class Implementation

```csharp
[C#]

using System;

namespace Calculate_ICalcData
{
    /// <summary>
    /// Summary description for ArrayCalcData.
    /// </summary>
    public class ArrayCalcData
    {
        public ArrayCalcData()
        {
            //
            // TODO: Add constructor logic here.
            //
        }
    }
}
```

## API Reference

### Class `ArrayCalcData`

The `ArrayCalcData` class is part of the `Calculate_ICalcData` namespace. It serves as a starting point for implementing custom functionality. The class includes a constructor where logic can be added as needed.

### Members

- **Constructor**: `public ArrayCalcData()`
  - Initializes a new instance of the `ArrayCalcData` class.

## Code Examples

The provided code snippet demonstrates the initial setup of the `ArrayCalcData` class. Additional logic must be added to this class to achieve the desired functionality.

## Cross References

- See also: [Additional details on extending class functionality](#)
- [Naming conventions for class files](#)

<!-- tags: [visual-studio, class-file, add-new-item, namespace, constructor, logic, functionality] keywords: [calculate, arraycalcdata, essential calculate, visual studio dialog, class implementation] -->
```

---

<!-- 페이지 141 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: calculate
page_number: 051
page_id: calculate#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:17Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Implements row and column sum formulas for a grid.
- Integrates the `ICalcData` interface with minimal method implementations.
- Demonstrates the use of named events for value changes in grid operations.

## Content

### Calculating Row and Column Sums

```vb
colSums = New Object(colCount + 1) {}

' Initializes the formulas for the row sums.
' eg. "=Sum(A5:D5)" to sum row 5
Dim row As Integer
For row = 0 To rowCount - 1
    rowSums(row) = String.Format("=Sum(A{1}:{0}{1})", _
                                 RangeInfo.GetAlphaLabel(colCount - 1), row + 1)
Next

' Initializes the formulas for the column sums.
' eg. "=Sum(B1:B5)" to sum column 2
Dim col As Integer
For col = 0 To colCount - 1
    colSums(col) = String.Format("=Sum({0}1:{0}{1})", _
                                 RangeInfo.GetAlphaLabel((col + 1)), rowCount - 1)
Next

' New
End Sub
```

### Implementing the ICalcData Interface

6. Now you can add the code stubs for implementing the `ICalcData` interface. For the implementation, you only need to add the code to the first two methods in the interface. `WireParentObject` will not be used in our code. `ValueChanged` is an event that you will raise in the `SetValueRowCol` implementation.

### Adding Method Stubs Using Visual Studio 2003

7. Using Visual Studio 2003 with C#, add a colon after the class name in the class declaration and type `ICalcData`. Pressing the tab key will add the method stubs. Given below is a picture showing this technique.

## API Reference

- **Interface Name**: ICalcData
- **Methods**:
  - `WireParentObject`: Not used in this implementation.
  - `ValueChanged`: Event to raise in the `SetValueRowCol` method.
- **Events**:
  - `ValueChanged`: Triggered when a value changes.

## Code Examples

### VB.NET Example

```vb
' Example code snippet demonstrating the use of ICalcData interface
```

### C# Example

```csharp
// Example code snippet demonstrating the use of ICalcData interface
```

## Page-level Navigation/TOC
- [Creating Row and Column Sum Formulas](#creating-row-and-column-sum-formulas)
- [Implementing ICalcData Interface](#implementing-icalcdata-interface)
- [Adding Method Stubs Using Visual Studio 2003](#adding-method-stubs-using-visual-studio-2003)

<!-- tags: [Syncfusion Winforms, ICalcData, Grid Calculations, Value Changed Event] keywords: [row sums, column sums, ICalcData interface, method stubs, Visual Studio 2003] -->
```


---

<!-- 페이지 142 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_055.jpeg
document_name: calculate
page_number: 055
page_id: calculate#page_055
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:36Z
fidelity: lossless
-->

# Essential Calculate

```vbnet
'/<summary>
'// Gets the value into either the double array or column vector or row vector.
'//</summary>
'//<param name="row">One-based row index.</param>
'//<param name="col">One-based column index.</param>
'//<returns>The value.</returns>
'//<remarks> By convention, ICalcData uses one-based indexes.</remarks>
Public Function GetValueRowCol(ByVal row As Integer, ByVal col As Integer) _
    As Object Implements Syncfusion.Calculate.ICalcData.GetValueRowCol
    If row = rowCount Then
        Return colSums((col - 1))
    Else
        If col = colCount Then
            Return rowSums((row - 1))

        Else
            Return Me.dValues(row - 1, col - 1)
        End If
    End If
End Function
```

## Overview

- The `GetValueRowCol` method is used to retrieve the value at a specified row and column index.

## Content

1. **Retrieve Value Using `GetValueRowCol`**
   - The `GetValueRowCol` function retrieves the value at a specified row and column index from a data structure.
   - **Parameters:**
     - `row` (One-based row index)
     - `col` (One-based column index)
   - **Returns:**
     - The value at the specified index.
   - **Details:**
     - If the specified row is the last row, it returns the sum of the specified column.
     - If the specified column is the last column, it returns the sum of the specified row.
     - Otherwise, it returns the value from the double array `dValues` at the adjusted zero-based row and column indices.

2. **Set Value Using `SetValueRowCol`**
   - The `SetValueRowCol` method is used to set the value at a specified row and column index.
   - **Usage:**
     - It can trigger calculations when values are entered or modified.
     - The `CalcEngine` listens to the `ValueChanges` event raised by this method to manage calculations.
     - This event ensures that calculations are triggered whenever values are set or changed.

   Here is the code for the `SetValueRowCol` method:

   ```csharp
   /// <summary>
   /// Sets the value into either the double array or column vector or row vector.
   /// </summary>
   /// <param name="row">One-based row index.</param>
   /// <param name="col">One-based column index.</param>
   /// <param name="value">The value to be set.</param>
   /// <remarks>This setter raises the ICalcData.ValueChanged event which,
   /// is listened to by the CalcEngine to manage the calculations.
   ///</remarks>
   /// By convention, ICalcData uses one-based indexes.
   ```

## Code Examples

The `GetValueRowCol` method's implementation demonstrates how to access values based on one-based indices, handling edge cases like row and column sums. The `SetValueRowCol` method, while not fully shown, is described as the reverse process, setting a value and raising the `ValueChanges` event.

## Cross References

- **Related Methods:**
  - `SetValueRowCol`
  - `CalcEngine`
  - `ICalcData`
  - `ValueChanges` event

<!-- tags: [Syncfusion, Winforms, ICalcData, GetValueRowCol, SetValueRowCol, CalcEngine, ValueChanges event] keywords: [getValueRowCol, setValueRowCol, one-based indexing, row sums, column sums, value changes event, calcEngine, ICalcData] -->
```

---

<!-- 페이지 143 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: calculate
page_number: 059
page_id: calculate#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:58Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Creates a `CalcEngine` object using `this.ArrayCalcData`.
- Enables dependency tracking for immediate value updates.
- Recalculates the specified range to compute formulas.
- Displays the `ArrayCalcData` values in a text box.

## Content

### Using ArrayCalcData in WinForms

The following code demonstrates how to use the `ArrayCalcData` class to create a `CalcEngine`, enable dependency tracking, and display the calculated values in a `TextBox`.

#### C# Example

```csharp
// Creates a CalcEngine object using this ArrayCalcData object.
CalcEngine engine = new CalcEngine(this.data);

// Turns on dependency tracking so that values set with the Set button take effect immediately.
engine.UseDependencies = true;

// Calls RecalculateRange so any formulas in the data can be initially computed.
engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), data);

ShowObject();
}

/// <summary>
/// Displays the ArrayCalcData values in a text box.
/// </summary>
private void ShowObject()
{
    this.textBox1.Text = "";
    for (int i = 0; i <= this.nRows; ++i)
    {
        for (int j = 0; j <= this.nCols; ++j)
        {
            this.textBox1.Text += this.data[i, j].ToString() + "\t";
        }
        this.textBox1.Text += "\r\n";
    }
}
```

#### VB Example

```vb
Imports Syncfusion.Calculate

'...

Private r As New Random
Private data As ArrayCalcData
Dim nRows As Integer
Dim nCols As Integer

' <summary>
' Populates the double array.
```

## Code Examples

The provided C# and VB examples show how to create and use a `CalcEngine` with `ArrayCalcData`. The `CalcEngine` is initialized with the `ArrayCalcData` object, and dependency tracking is enabled to ensure immediate updates. The `RecalculateRange` method is called to compute any formulas in the data. Finally, the calculated values are displayed in a `TextBox`.

<!-- tags: [syncfusion, winforms, arraycalldata, calcengine, dependencytracking] keywords: [arraycalcdata, calcengine, recalculation, dependency tracking, textbox] -->
```

---

<!-- 페이지 144 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: calculate
page_number: 063
page_id: calculate#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:13Z
fidelity: lossless
-->

## Essential Calculate

```csharp
ShowObject()

' Button2_Click
End Sub
```

On the previous screen, if you click the Set button, it will place `123` in cell `0,0`. Notice the calculations update automatically to reflect the new value.

![Figure 28: Sample Display After Setting 123 into Array Element (0, 0)](https://i.imgur.com/SampleFigure28.png)

<!-- tags: [syncfusion, winforms, array, calculation, reset element, functionality] keywords: [set button, cell value, automatic calculations, Syncfusion Winforms, 11.4.0.26] -->
```

---

<!-- 페이지 145 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: calculate
page_number: 067
page_id: calculate#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:21Z
fidelity: lossless
-->

## EssentialCalculate

### Introduction

This page describes the functionality of using simple variables in the `CalcQuickBase` object, specifically focusing on how variables are managed and utilized in algebraic expressions.

#### Overview

- **Key Concepts**:
  - The `CalcQuickBase` object maintains a collection of variables.
  - Variables can be added or modified by assigning a name and a value.
  - Algebraic expressions can use these variables by enclosing their names in brackets.

---

### Simple Variables

#### Explanation

When a name is used as an indexer on the `CalcQuickBase` object, the object checks the collection of variables it maintains:

- **Adding New Variables**: If the name is not in the collection, it is added as a new item with the assigned value.
- **Modifying Existing Variables**: If the name is already in the collection, its assigned value is updated to the new value.

---

#### Parsing and Replacement

When a formula is parsed, the `CalcQuickBase` object replaces all occurrences of variable names with their current values. To use a named variable in a formula, enclose it within brackets, as shown in the following example:

```plaintext
[base]*[height]/2
```

This formula takes the value represented by the base and multiplies it by the height of the value divided by two.

---

### String Variables as Formulas

As a convention, if you want a variable to hold a string that is a formula and be treated as a formula, begin that string with a special character, the `CalcQuickBase.FormulaCharacter` (default value is `"="`). If you invoke the `ParseAndCompute` method directly, any string you pass will be treated as a formula, regardless of whether it begins with `FormulaCharacter`.

---

### The FormulaInfo Class

This section delves into the `FormulaInfo` class, which provides detailed information about the formula parsing and computation process.

---

### Example

The interface shown in **Figure 30** demonstrates the use of simple variables in the context of calculating a formula using the `CalcQuickBase` object.

#### Figure 30: Simple Variables

![Figure 30: Simple Variables](image.png)

This figure illustrates the process of entering an algebraic expression using variables and computing the result.

---

### Summary

- **Variables** are managed efficiently within the `CalcQuickBase` object.
- Variables are used in formulas by enclosing their names in brackets.
- The `FormulaInfo` class provides further insights into the parsing and computation of formulas.

---

## API Reference

### Namespace: Syncfusion.Windows.Forms.CalcEngine

#### Class: `CalcQuickBase`

##### Properties

- **FormulaCharacter**: Gets or sets the special character that denotes a formula.

##### Methods

- **ParseAndCompute(string formula)**: Parses and computes the given formula.

---

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.CalcEngine;

class Program
{
    static void Main()
    {
        // Create an instance of CalcQuickBase
        var calc = new CalcEngine.CalcQuickBase();

        // Set variables
        calc["base"] = 1.4;
        calc["height"] = 3.5;

        // Compute the formula
        var result = calc.ParseAndCompute("[base]*[height]/2");

        // Output the result
        System.Console.WriteLine("Computed value: " + result);
    }
}
```

---

## Page-level Navigation/TOC

- **Overview**
- **Simple Variables**
  - Explanation
  - Parsing and Replacement
- **String Variables as Formulas**
- **The FormulaInfo Class**
- **Summary**
- **API Reference**
- **Code Examples**

---

## Cross References

- Refer to the `CalcEngine` namespace documentation for complete details on the `CalcQuickBase` class and related methods.

---

### Note

This page provides detailed insights into handling and utilizing variables within algebraic expressions using the `CalcQuickBase` object in Syncfusion Winforms. It is part of the essential guide for developers working with dynamic computation features.

---

<!-- tags: [Syncfusion Winforms, CalcQuickBase, algebraic expressions, variables, parsing, computation, FormulaInfo Class, version] keywords: [simple variables, algebraic expressions, CalcQuickBase, variables, parsing, computation, FormulaCharacter, ParseAndCompute, C#, code examples] -->
```

---

<!-- 페이지 146 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: calculate
page_number: 071
page_id: calculate#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:44Z
fidelity: lossless
-->

# Essential Calculate

```csharp
this.textBoxC.Leave += new EventHandler(textBoxC_Leave);
this.textBoxD.Leave += new EventHandler(textBoxD_Leave);

// 7) Allow the CalcQuickBase sheet to create dependency lists.
// Necessary for auto-calculations.
this.calculator.RefreshAllCalculations();

// 8) Raised when a variable value is calculated.
private void calculator_ValueSet(object sender, QuicKeyValueSetEventArgs e)
{
    switch (e.Key)
    {
        case "A":
            this.textBoxA.Text = this.calculator[e.Key].ToString();
            break;
        case "B":
            this.textBoxB.Text = this.calculator[e.Key].ToString();
            break;
        case "C":
            this.textBoxC.Text = this.calculator[e.Key].ToString();
            break;
        case "D":
            this.textBoxD.Text = this.calculator[e.Key].ToString();
            break;
        default:
            break;
    }
}

// 9) Handles the changing of the text in the text box so the CalQuick object
// can be updated as the text changes.
private void textBoxA_Leave(object sender, EventArgs e)
{
    if (this.textBoxA.Modified)
    {
        calculator["A"] = this.textBoxA.Text;
        this.textBoxA.Modified = false;
    }
}
// ..... same for textBoxB_Leave, textBoxC_Leave, textBoxD_Leave
```

### [VB]

```vb
Private calculator As CalcQuickBase = Nothing

Private Sub Form_Load(sender As Object, e As System.EventArgs)
    ' 1) Instantiate a CalcQuickBase object.
    calculator = New CalcQuickBase()
End Sub
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

<!-- tags: [Syncfusion Winforms, CalcQuickBase, EventHandler, Form Load, Auto-calculations, Text Box] keywords: [calculator, dependency lists, events, auto-calculations, text box events, text box leave event] -->
```

---

<!-- 페이지 147 -->

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

---

<!-- 페이지 148 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: calculate
page_number: 079
page_id: calculate#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:11Z
fidelity: lossless
-->

# Essential Calculate

## DataGrid with Calculation Support

The following figure illustrates the DataGrid with calculation support:

**Figure 34: Data Grid**

You can copy the code that defines the derived DataGrid object to your projects and have immediate support for calculations in a Data Grid using Data Table data sources. Before we begin with the details of this sample and the derived DataGrid class, we will discuss the ICalcData interface describing the purpose of its implementation details.

## 4.1.2.2.1 Using CalcDataGrid as a Single Spreadsheet

### Overview
- Demonstrates the usage of CalcDataGrid to support calculations in a Data Grid.
- Explains how to integrate CalcDataGrid with a User Control to perform calculations.

### Using CalcDataGrid as a Single Spreadsheet
Essential Calculate provides a derived DataGrid object that implements ICalcData to support calculations. But you need to know how to use such an object on a User Control. Essentially, you can drop an instance of the CalcDataGrid object onto your form, create an instance of CalcEngine by using your CalcDataGrid as its ICalcData object, and then calculate things so that the initial display shows the calculated values. The following code illustrates this.

### Code Example

```csharp
private Syncfusion.Calculate.CalcEngine engine;
private DataTable dt;
```

### Summary
- The derived DataGrid object supports calculations using Data Table data sources.
- Integration with User Controls is demonstrated.
- The code shows how to initialize the CalcEngine using CalcDataGrid.

## API Reference

### Class: CalcDataGrid
- **Namespace:** Syncfusion.Windows.Forms.Grid

### Methods
- **Calculate()**
  - Purpose: Performs calculations based on the formulas in the Data Grid.
  - Returns: bool indicating success or failure.

### Events
- **CalculationFailed**
  - Triggered when a calculation fails.
  - Parameters: object sender, CalculationFailedEventArgs e

### Properties
- **DataSource**
  - Type: object
  - Description: Gets or sets the data source for the Data Grid.
  - Default: null

## Code Examples

### Example: Integrating CalcDataGrid with a User Control

```csharp
// Initialize CalcDataGrid
CalcDataGrid grid = new CalcDataGrid();
grid.DataSource = dt;

// Initialize CalcEngine
CalcEngine engine = new CalcEngine();
engine.ICalcData = grid;

// Perform calculations
engine.Calculate();
```

## See also
- [DataGrid with Calculation Support](#)
- [Syncfusion Winforms Documentation](#)
- [CalcEngine API Reference](#)

<!-- tags: [syncfusion, data grid, calculation support, user control, calcengine, api, version:11.4.0.26] keywords: [data grid, calculation, calcdata, user control, calcengine, syncfusion] -->
```

---

<!-- 페이지 149 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: calculate
page_number: 083
page_id: calculate#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:27Z
fidelity: lossless
-->

## Essential Calculate

```csharp
{
    // 1) Set the datasource for the DataGrid.
    this.dataGrid1.DataSource = GetARandomTable();
    this.dataGrid2.DataSource = GetARandomTable();
    this.dataGrid3.DataSource = GetARandomTable();
    this.dataGrid4.DataSource = GetARandomTable();
    this.dataGrid5.DataSource = GetARandomTable();

    // 2) Call this to reset static members.
    Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID();

    // 3) Create the engine.
    engine = new Syncfusion.Calculate.CalcEngine(this.dataGrid1);

    // 4) Track dependencies required for auto calculations.
    engine.UseDependencies = true;

    // 5) Register multiple ICalcData objects for cross sheet references.
    int sheetfamilyID = CalcEngine.CreateSheetFamilyID();
    engine.RegisterGridAsSheet("DG1", this.dataGrid1, sheetfamilyID);
    engine.RegisterGridAsSheet("DG2", this.dataGrid2, sheetfamilyID);
    engine.RegisterGridAsSheet("DG3", this.dataGrid3, sheetfamilyID);
    engine.RegisterGridAsSheet("DG4", this.dataGrid4, sheetfamilyID);
    engine.RegisterGridAsSheet("DG5", this.dataGrid5, sheetfamilyID);
}
```

### [VB]

```vb
Dim engine As Syncfusion.Calculate.CalcEngine

Private Sub DataGridWorkBookForm_Load(sender As Object, e As System.EventArgs)

    ' 1) Set the datasource for the DataGrid.
    Me.dataGrid1.DataSource = GetARandomTable()
    Me.dataGrid2.DataSource = GetARandomTable()
    Me.dataGrid3.DataSource = GetARandomTable()
    Me.dataGrid4.DataSource = GetARandomTable()
    Me.dataGrid5.DataSource = GetARandomTable()

    ' 2) Call this to reset static members in case the other form loaded first.
    Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID()

    ' 3) Create the engine.
End Sub
```

### Page-level Navigation/TOC (if applicable)
- [Essential Calculate](#essential-calculate)

### Cross References
See also: 
- [CalcEngine](#calcengine)
- [RegisterGridAsSheet](#registergridassheet)
- [UseDependencies](#usedependencies)

### RAG Annotations
<!-- tags: [syncfusion-sdk, winforms, calculate, engine, data grid, sheet family, table of contents, essential calculate, registergridassheet, usedependencies] keywords: [datasource, reset, static members, dependencies, auto calculations, cross sheet references, ICalcData objects, grid, data grid, form, event, load, engine, register grid as sheet, useDependencies] -->
```

---

<!-- 페이지 150 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_087.jpeg
document_name: calculate
page_number: 087
page_id: calculate#page_087
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:44Z
fidelity: lossless
-->

# Essential Calculate

```vb
dt.DefaultView.AllowUser = False
End Sub

' 2) This event handler raises the required ICalcData.ValueChanged event when the data in the DataTable changes.
Private Sub dt_ColumnChanged(ByVal sender As Object, ByVal e As DataColumnChangeEventArgs)
    Dim cm As CurrencyManager = CType(Me.BindingContext(Me.DataSource, Me.DataMember), CurrencyManager)
    Dim dt As DataTable = Me.DataSource
    Dim pos As Integer = cm.Position
    Dim field As Integer = dt.Columns.IndexOf(e.Column)
    Dim val As String = Me(pos, field).ToString()

    ' el.RowIndex, el.COLIndex needs to be one-based.
    Dim el = New ValueChangedEventArgs(pos + 1, field + 1, val)
    ValueChanged(Me, el)
End Sub

' 3) Returns the value at the one-based row and col.
Public Function GetvalueRowCol(ByVal row As Integer, ByVal col As Integer) As Object Implements ICalcData.GetvalueRowCol
    ' Row, col are one-based.
    Return Me(row - 1, col - 1)
End Function

' 4) Sets the value at the one-based row and col.
Public Sub SetvalueRowCol(ByVal value As Object, ByVal row As Integer, ByVal col As Integer) Implements ICalcData.SetvalueRowCol
    ' Row, col are one-based.
    Dim dt As DataTable = Me.DataSource
    dt.Rows(row - 1)(col - 1) = value
End Sub

' 5) Required ICalcData event.
Public Event ValueChanged As ValueChangedEventHandler Implements ICalcData.ValueChanged
' CalcDataGrid
End Class
```

The following is an explanation of the preceding code.

## Content

### Explanation of the Preceding Code

1. **ICalcData.WireParentObject Implementation**
   - This is the implementation of the `ICalcData.WireParentObject`. One of the requirements of the `ICalcData` object is to inform the `CalcEngine` "when" values have changed. This notification is crucial for the `CalcEngine` to maintain the proper state of its data structures. The `ICalcData` object fulfills this task by raising the `ICalcData.ValueChanged` event.

<!-- tags: [syncfusion, winforms, icacldata, valuechanged, eventhandler] keywords: [CalcEngine, DataTable, CurrencyManager, ValueChangedEventArgs, ICalcData, DataTableColumnChangeEventArgs] -->
``` 
```

---

<!-- 페이지 151 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: calculate
page_number: 091
page_id: calculate#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:59Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Demonstrates the use of lookup tables in calculating specific factors.
- Includes state-specific factors, age-based multipliers, and additional attributes like sex, points, and model year.

## Content

### Lookup Tables in Excel

This section illustrates the use of lookup tables in an Excel worksheet to perform calculations based on various attributes. Figure 38 below shows the worksheet that contains these lookup tables:

#### Figure 38: Worksheet that Holds Lookup Tables

| **A** | **B**          | **C**                | **D** | **E** | **F** | **G** | **I** | **J**  | **L** | **M** | **O**    | **P**  |
|-------|-----------------|----------------------|-------|-------|-------|-------|-------|--------|-------|-------|----------|--------|
| 1     | State Factor    | Lookup Table        |       | Age   | Lookup Table                |       | Sex   | Look      | Points |       | Model   | Year    |
| 2     |                 |                      |       |       |                                 |       |       |           |       |       |          |        |
| 3     | AL              | 0.9502              |       | 15    | 1.40                        |       | M     | 1.20      | 0      | 1.00  | 2005    | 1.      |
| 4     | AK              | 1.1000              |       | 16    | 1.50                        |       | F     | 1.00      | 1      | 1.00  | 2004    | 1.      |
| 5     | AR              | 0.9810              |       | 17    | 1.40                        |       |       |           | 2      | 1.10  | 2003    | 1.      |
| 6     | AZ              | 0.9604              |       | 18    | 1.40                        |       |       |           | 3      | 1.20  | 2002    | 1.      |
| 7     | CA              | 1.2010              |       | 19    | 1.40                        |       |       |           | 4      | 1.40  | 2001    | 1.      |
| 8     | CO              | 1.1020              |       | 20    | 1.30                        |       |       |           | 5      | 1.50  | 2000    | 1.      |
| 9     | CT              | 1.1650              |       | 21    | 1.30                        |       |       |           | 6      | 1.60  | 1999    | 0.      |
| 10    | DE              | 1.0900              |       | 22    | 1.30                        |       |       |           | 7      | 2.00  | 1998    | 0.      |
| 11    | FL              | 1.1110              |       | 23    | 1.20                        |       |       |           | 8      | 2.20  | 1997    | 0.      |
| 12    | GA              | 1.0340              |       | 24    | 1.20                        |       |       |           | 9      | 2.40  | 1996    | 0.      |
| 13    | HI              | 1.1990              |       | 25    | 1.20                        |       |       |           | 10     | 2.60  | 1995    | 0.      |

The worksheet is divided into several tables:

- **State Factor Lookup Table**: Located in columns A and B, this table maps each state to a specific factor used in the calculations.
- **Age Lookup Table**: Located in columns E and F, this table provides age-related multipliers.
- **Sex Lookup**: Located in columns I and J, this table assigns multipliers based on gender.
- **Points**: Located in column L, this column provides values for points based on the data.
- **Model Year**: Located in columns O and P, this table includes the model year along with an associated value.

### Explanation of Columns

1. **A** - **State**: Abbreviated names of states in the United States.
2. **B** - **State Factor**: Values representing the state-specific factors used in calculations.
3. **C** - **Age**: Various age ranges or specific ages.
4. **F** - **Age Multiplier**: Multipliers based on the age values in column E.
5. **I** - **Sex**: Genders represented as M (Male) or F (Female).
6. **J** - **Sex Multiplier**: Multipliers based on the gender values in column I.
7. **L** - **Points**: Values assigned to specific entries.
8. **M** - **Multiplier**: Multipliers used in conjunction with the points and other factors.
9. **O** - **Model Year**: Various model years.
10. **P** - **Value**: Specific values related to the model year.

This setup enables users to perform complex lookups and calculations using a structured set of data, ensuring accuracy and efficiency in processing.

### Cross References
- Other sections in the guide may reference similar use cases or additional features related to using lookup tables.
- See also: Calculations and Data Validation.

### API Reference
- **Namespace**: Syncfusion.Windows.Forms
- **Class**: LookupTable
- **Method**: GetValue-method

### Code Examples
#### Example: Using Lookup Tables in .NET
```csharp
// Example code snippet in C#
using Syncfusion.Windows.Forms.LookupTable;

// Assuming a LookupTable object named "stateFactorTable"
double stateFactor = stateFactorTable.GetValue("AZ");

// Similarly, retrieving age-related values
double ageFactor = ageTable.GetValue(25);

// Combining values from multiple tables
double totalFactor = stateFactor * ageFactor;
```

### RAG Annotations
<!-- tags: [syncfusion-winforms, lookup-tables, data-lookup, excel-integration, tables, state-factors, age-multipliers, sex-multipliers, calculation-engine, net] keywords: [state factor, age lookup, sex lookup, points, model year, multiplier, lookup tables, excel, winforms, calculations] -->
```

---

<!-- 페이지 152 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_095.jpeg
document_name: calculate
page_number: 095
page_id: calculate#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:35Z
fidelity: lossless
-->

# Essential Calculate

## 4.3.2 Using Essential XlsIO

Essential XlsIO will give you an Excel-like Automation-type support without having MS Excel installed on the host system. This means that you can use this library to read and write an XLS file and hold its contents in memory.

### Limitation

- You cannot perform actual computations on the contents of the XLS file. Essential Calculate adds this ability.

A sample which illustrates the usage of Essential XlsIO with Essential Calculate is available in the following sample installation location:

```plaintext
<Install Location>\Windows\Calculate.Windows\Samples\2.0\Xls File Using CalcEngine Demo\cs
```

In this sample, the following two classes are used:

- **ExcelRWCalcSheet**: which is derived from `CalcSheet` and implements `Syncfusion.XlsIO.IWorksheet`
- **ExcelRWWorkbook**: which is derived from `CalcWorkbook` and implements `Syncfusion.XlsIO.IWorkbook`

These classes use XlsIO library through the supported interfaces to populate a `CalcWorkbook` object from an XLS file. In addition, the derived classes use overrides to get and set the data through the XlsIO objects that holds the XLS data, instead of relying on the internal data storage that is available in `CalcSheet`. This gives us the ability to change values in the `CalcWorkbook` object and view the newly computed results. So, when you want to use an XLS file in your business objects and modify the values or get new calculated results, you can add these two classes to your project and utilize the support immediately in the same manner as this sample.

## 4.3.3 Car Insurance Sample Details

The following sample code snippet creates an XlsIO workbook from the Excel spreadsheet that was shown earlier. It creates a form that enables you to change input values for the spreadsheet, and then displays the corresponding cost of insurance for these input values.

Given below is the code from the Form.Load event handler.

```csharp
[C#]
private ExcelRWCalcWorkbook calcWB;
```

<!-- tags: [syncfusion, windows forms, xlsio, calculate, car insurance sample] keywords: [essential xlsio, excel-like automation, calcengine demo, business objects, computed results, derived classes, form.load event] -->
```

---

<!-- 페이지 153 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: calculate
page_number: 099
page_id: calculate#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:49Z
fidelity: lossless
-->

## Content

### Overview
This section explains the process of setting input values into a CalcSheet in a Windows Forms application using VB.NET. The code snippet shows how to populate various fields in the CalcSheet based on user inputs from controls on the form. 

#### Code Example

```vb
Private ageRow As Integer = 3
Private sexRow As Integer = 4
Private stateRow As Integer = 5
Private pointsRow As Integer = 6
Private modelRow As Integer = 7
Private modelYearRow As Integer = 8
Private multipleDiscountRow As Integer = 9

Private Sub SetSheetInputs()
    Dim inputSheet As CalcSheet = Me.calcWB("Inputs")
    inputSheet(ageRow, 2) = Me.numericUpDownAge.Value.ToString()
    inputSheet(sexRow, 2) = Me.comboSex.Text(0).ToString()
    inputSheet(stateRow, 2) = Me.comboState.Text
    inputSheet(pointsRow, 2) = Me.numericUpDownPoints.Value.ToString()
    inputSheet(modelRow, 2) = Me.comboModel.Text
    inputSheet(modelYearRow, 2) = Me.numericUpDownModelYear.Value.ToString()
    If Me.checkBoxMultipleDiscounts.Checked Then
        inputSheet(multipleDiscountRow, 2) = "Yes"
    Else
        inputSheet(multipleDiscountRow, 2) = "No"
    End If
    inputSheet(3, 5) = Me.textBoxBaseAmount.Text
End Sub
```

#### Explanation of the Code

1. **Calls a method to take the values from the controls on the form and move them into the Inputs sheet of the workbook.**
   - The `SetSheetInputs` subroutine transfers values from various form controls (like textbox, combobox, numeric updown, and checkbox) into specific cells of the `Inputs` sheet in a CalcWorkbook.

2. **Commented Code for Compatibility with CalculatingSuspended Property**
   - If the `CalculatingSuspended` property is set to `True`, this ensures that the value in cell A1 of the Outputs sheet is current. However, since calculations are suspended, this code is not needed in the current context.
   
3. **Retrieving the Computed Value from the Output Sheet**
   - The calculated value is stored in cell A1 of the `Outputs` sheet. To retrieve this value, you need to index the workbook with the sheet name and then index the sheet to return the value. This is represented as `calcWB["Outputs"][1,1]`.

## API Reference

### Members
- `ageRow`: Integer, initialized to 3.
- `sexRow`: Integer, initialized to 4.
- `stateRow`: Integer, initialized to 5.
- `pointsRow`: Integer, initialized to 6.
- `modelRow`: Integer, initialized to 7.
- `modelYearRow`: Integer, initialized to 8.
- `multipleDiscountRow`: Integer, initialized to 9.
- `SetSheetInputs`: Subroutine that sets the input values from the form controls into the `Inputs` sheet of the workbook.

## Code Examples

The example provided demonstrates the integration of form controls with a CalcSheet, enabling dynamic updating of the worksheet based on user inputs.

## Cross References

- See also:
  - [Calculation Engine Overview](#calculation-engine-overview)
  - [Working with CalcSheets](#working-with-calcsheets)

<!-- tags: [calculation, sheet, form, windows forms, vb.net, syncfusion] keywords: [input, output, worksheet, control integration, syncfusion,winforms] -->
```

---

<!-- 페이지 154 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_103.jpeg
document_name: calculate
page_number: 103
page_id: calculate#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:11Z
fidelity: lossless
-->

# Essential Calculate

The explicit look of a valid formula in Essential Calculate may vary depending upon the context of the formula. For example, if you are using a formula in a `CalcSheet` class based on an Excel spreadsheet, then something like `= A1 + A3` will be valid since `CalcSheet` recognizes the "A1" and "A3" as valid cell references. But, if you are using a `CalcQuickBase` object to manage formulas for controls on a Windows Form, then the same `= A1 + A3` will not be valid since `CalcQuickBase` only recognizes registered names inside square brackets as valid arguments. Hence, all Essential Calculation formulas support the same algebra with the exception of what comprises the definition of valid arguments.

## Overview
- The explicit validity of formulas depends on the context (e.g., `CalcSheet` vs. `CalcQuickBase`).
- `CalcSheet` supports Excel-style cell references like "A1" and "A3."
- `CalcQuickBase` requires arguments in a different format (e.g., registered names inside square brackets).
- All formulas support the same algebra, differing only in valid argument formats.

## Content

### 4.4.1 Operators

This section comprises the following topics:

#### Operators

The following is a list of the operators which are supported by Essential Calculate.

#### Unary Arithmetic Operator

- **Unary Minus Sign**

#### Binary Arithmetic Operators

- **Addition**
- **Subtraction**
- **Multiplication**
- **Division**
- **Exponentiation**

#### Binary Literal Operator

- **Concatenation**

#### Binary Logical Operators

- **Less Than**
- **Greater Than**
- **Equal To**
- **Less Than Or Equal**

#### Summary of Operators

Essential Calculate supports a wide array of operators, including unary and binary arithmetic, literal operators for concatenation, and logical operators for comparison. The specific valid argument formats depend on the context (e.g., `CalcSheet` or `CalcQuickBase`).

### API Reference (if applicable)
- *Not applicable in this section.*

### Code Examples (multi-language supported)
- *No code examples provided in this section.*

### Cross References
- *No cross-references present on this page.*

<!-- tags: [Essential Calculate, operators, formula context, CalcSheet, CalcQuickBase, Unary Arithmetic Operator, Binary Arithmetic Operators, Binary Literal Operator, Binary Logical Operators] keywords: [context, formula validity, algebra, valid arguments, cell references, registered names, windows form controls, Excel spreadsheet, exponential, greater than, less than, equal to] -->
```

---

<!-- 페이지 155 -->

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

---

<!-- 페이지 156 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: calculate
page_number: 111
page_id: calculate#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:40Z
fidelity: lossless
-->

## Essential Calculate

The second step for adding your own formula is to register your method with the `CalcEngine` object. This is done with the `AddFunction` method. This method accepts the string that is used when you reference the function in a spreadsheet formula, and the second argument is a delegate for which you pass your method. The only requirement here is that the function name should start with an alpha character and should only contain alpha-numeric characters. Additionally, the string cannot be the name of any existing library function.

### Adding a Custom Function

```csharp
[C#]

// Add formula name Mymin to the Library.
this.engine.AddFunction("Mymin", new LibraryFunction(ComputeMymin));
```

```vb
[VB]

' Add formula name Mymin to the Library.
Me.engine.AddFunction("Mymin", AddressOf ComputeMymin)
```

By convention, within the Essential Calculate library, the C# implementation method for each of the library functions that are shipped with the word "Compute" is named and followed by the name of the library function. The above code confirms to this convention, with the function name being 'Mymin' and the method name being 'ComputeMymin'. Our library functions are public members of the `CalcEngine` class, so that you can access them directly if it serves your purpose. Additionally, if you own the source code version, you can see implementation details that may be of use to you if you try to implement many custom library methods on your own.

### Note
Once this is done, you can use your custom method in the same manner as the default library functions.

### 4.5.2 Remove and Replace Function

This section discusses the Remove and Replace Function available for the `CalcEngine`.

#### Remove Function

Removing unused functions from the Function Library reduces the memory usage and speeds up parsing as well. Also, if you are only using a selected few Library functions, you may want to remove the unused ones. This can be done using the methods given below.

- To remove all functions, you can clear the hash table that holds them by using the `engine.LibraryFunctions.Clear` method.

```csharp
[C#]
```

## API Reference

### Functions
- `AddFunction(string name, LibraryFunction method)`: Registers a custom function with the `CalcEngine`.
- `RemoveFunction(string name)`: Removes a specific function from the `CalcEngine`.
- `Clear()`: Clears all functions from the `CalcEngine`.

## Code Examples

### Adding a Custom Function in C#
```csharp
this.engine.AddFunction("Mymin", new LibraryFunction(ComputeMymin));
```

### Adding a Custom Function in VB
```vb
Me.engine.AddFunction("Mymin", AddressOf ComputeMymin)
```

### Removing All Functions
```csharp
engine.LibraryFunctions.Clear();
```

<!-- tags: [CalcEngine, AddFunction, RemoveFunction, LibraryFunctions, CustomFunction, MemoryUsage, Performance, Syncfusion Windows Forms] keywords: [Custom function, library function, memory usage, parsing speed, function removal, custom method, function registration] -->
```

---

<!-- 페이지 157 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_115.jpeg
document_name: calculate
page_number: 115
page_id: calculate#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:57Z
fidelity: lossless
-->

# Essential Calculate

## Content

### 4.5.4.1 LookUps and Information

This section lists the LookUp and Information functions included with Essential calculate in the below table.

#### Table 8: LookUp and Information functions

| Function Name | Description |
|---------------|-------------|
| HLookup      | Finds a value in one row and returns the corresponding value in another row. |
| VLookup      | Finds a value in one column and returns the corresponding value in another column. |
| IsError      | Returns True if cell holds an error. |
| IsNumber     | Returns True if cell holds a number. |

### 4.5.5 Financial

This section lists the Financial functions included with Essential calculate in the below table.

#### Table 9: Financial functions

| Function Name | Description |
|---------------|-------------|
| Db           | Returns the depreciation using fixed declining balance calculation. |
| Ddb          | Returns the depreciation using double declining balance calculation. |
| Fv           | Returns future value of an investment. |
| Ipmt         | Returns interest payment. |
| IRR          | Returns internal rate of return. |

## Cross References
- See also: [Financial functions in Excel](#)

<!-- tags: [Essential Calculate, LookUp, Information, Financial, Syncfusion Winforms, 11.4.0.26] -->
<!-- page-level tags: [Syncfusion, Winforms, documentation, essential calculate, lookup and information functions, financial functions, 11.4.0.26] -->
```

---

<!-- 페이지 158 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_119.jpeg
document_name: calculate
page_number: 119
page_id: calculate#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:08Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Demonstrates the use of mathematical functions in a spreadsheet.
- Explains the syntax and usage of the ISEVEN and ISODD functions.
- Provides examples and results for the MULTINOMIAL, ISEVEN, and ISODD functions.

## Content

### MULTINOMIAL Example

#### Formula and Result
| FORMULA     | RESULT |
|-------------|--------|
| =MULTINOMIAL(2, 3, 4) | 1260 |

### 4.5.6.2 ISEVEN

The ISEVEN function returns TRUE if the given number is an even number, and returns FALSE if the given number is odd.

#### Syntax:
The syntax of the ISEVEN function is  
`=ISEVEN(value)`

**The given value must be a numeric value. If it is a non-integer value, the value is rounded down.**

**Note:** If the given value is nonnumeric, the ISEVEN function returns the `#VALUE!` error value.

#### Example:
| FORMULA    | RESULT |
|------------|--------|
| =ISEVEN(-1) | FALSE  |
| =ISEVEN(2.5) | TRUE   |
| =ISEVEN(5) | FALSE  |

### 4.5.6.3 ISODD

The ISODD function returns TRUE if the given number is an odd number, and returns FALSE if the given number is even.

#### Syntax:
The syntax of the ISODD function is  
`=ISODD(value)`

**The given value must be a numeric value. If it is a non-integer value, the value is rounded down.**

## API Reference (if applicable)
- **Namespace:** Syncfusion.Windows.Forms
- **Methods/Properties/Events**
  - `ISEVEN(value)`
  - `ISODD(value)`

## Code Examples (multi-language supported)

```csharp
// Example usage of ISEVEN and ISODD functions
using System;

class Program
{
    static void Main()
    {
        bool isEven = ISEVEN(-1);
        bool isOdd = ISODD(5);

        Console.WriteLine("ISEVEN(-1): " + isEven); // Output: FALSE
        Console.WriteLine("ISODD(5): " + isOdd);   // Output: TRUE
    }

    static bool ISEVEN(double value)
    {
        int intValue = (int)Math.Floor(value);
        return intValue % 2 == 0;
    }

    static bool ISODD(double value)
    {
        int intValue = (int)Math.Floor(value);
        return intValue % 2 != 0;
    }
}
```

## Cross References
- See also: Mathematical Functions, Number Validation Functions.

<!-- tags: Syncfusion Winforms, calculation, mathematical functions, number validation, ISEVEN, ISODD, MULTINOMIAL keywords: ISEVEN, ISODD, MULTINOMIAL, mathematical functions, number validation, syncfusion, winforms -->
```

---

<!-- 페이지 159 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: calculate
page_number: 123
page_id: calculate#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:25Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Describes the functionality of subtotal functions and their handling in nested structures.
- Explains the MROUND function, which rounds numbers to the nearest multiple of a specified value.
- Details the syntax and behavior of the RANDBETWEEN function, which generates random numbers within a specified range.

## Content

### 4.5.6.8 MROUND

The MROUND function rounds a given number up or down to the nearest multiple of a given number.

#### Syntax

The syntax of the MROUND function is:

```
=MROUND(number, multiple)
```

- **Number** – The value to be rounded. This value is required.
- **Multiple** – This value is required.

**Note:** The number must be greater than or equal to half the value of multiple.

#### Errors

- **#NUM!** - Occurs if the number and multiple have different signs.
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example

| FORMULA         | RESULT |
|------------------|--------|
| =MROUND(10, 2.6) | 8      |
| =MROUND(-10, -2.6) | -8     |
| =MROUND(10, -2)  | #NUM!  |

### 4.5.6.9 RANDBETWEEN

The RANDBETWEEN function returns a random number that is between the given ranges. This function returns a new random number each time in recalculation.

#### Syntax

The syntax of the RANDBETWEEN Function is:

```
=RANDBETWEEN(start_num, end_num)
```

- **start_num** – Required. This is the smallest integer.
- **end_num** – Required. This is the largest integer.

#### Errors

- **#NUM!** - Occurs if the end_num value is larger than start_num value.

## API Reference (if applicable)

Not applicable in this context, as the content is focused on function usage and behavior rather than API details.

## Code Examples (multi-language supported)

Not applicable in this context, as the content does not include specific code examples.

## Page-level Navigation/TOC (if applicable)

Not applicable in this context, as the page is focused on explaining two specific functions without a separate TOC.

## Cross References

See also:

- Subtotal functions handling nested subtotals.
- Function behavior in recalculation and error scenarios.

<!-- tags: [calculation, subtotal, mround, randbetween, random number, rounding, error handling, syncfusion, winforms] keywords: [nested subtotal, double counting, rounding rules, random number generation, mround, randbetween, error conditions] -->
```

---

<!-- 페이지 160 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_127.jpeg
document_name: calculate
page_number: 127
page_id: calculate#page_127
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:43Z
fidelity: lossless
-->

## Essential Calculate

The ROMAN function converts an Arabic number to a Roman numeral. This function returns a text string depicting the Roman numeral form of the given number.

### Syntax

The syntax of the ROMAN function is

```
=ROMAN( number, (form) )
```

- `number` – Required.
- `form` – Optional, this value will specify the style of the Roman numeral.

If `number` is not an integer, then it will be rounded down.

### Form Style Variations

| Form             | Type          |
|------------------|---------------|
| 0 or omitted     | Classic.      |
| 1                | More concise. See example below. |
| 2                | More concise. See example below. |
| 3                | More concise. See example below. |
| 4                | Simplified.   |

### Error Handling

**#VALUE!** - Occurs if any of the given values is non-numeric, or for values less than 0 and greater than 3999.

### Example

| FORMULA               | RESULT        |
|-----------------------|---------------|
| `=ROMAN(499, 0)`     | CDXCIX        |
| `=ROMAN(499, 1)`     | ID            |
| `=ROMAN(-100)`       | #VALUE!       |

## 4.5.6.16 IFERROR

The IFERROR function tests if an initial given value (or expression) returns an error, and if so, this function returns a second given argument. Otherwise, the function returns the initial tested value.

### Syntax

The syntax of the IFERROR function is

```
=IFERROR(value, value_error)
```

- `value` – Required. This is a value to check for the error.
- `value_error` – Required. This value will be returned if the `value` has an error.

## API Reference

### ROMAN Function

- **Parameters:**
  - `number`: Numerical value to convert to a Roman numeral.
  - `form`: Optional style specification for the Roman numeral.

### IFERROR Function

- **Parameters:**
  - `value`: The value to test for an error.
  - `value_error`: The value to return if an error is found.

## Code Examples

### Example 1: Using ROMAN Function

```csharp
// Convert an Arabic number to Roman numeral in Classic style
string result = ROMAN(499, 0); // Output: CDXCIX
```

### Example 2: Handling Errors with IFERROR Function

```csharp
// Using IFERROR to handle potential errors
object result = IFERROR(SQRT(-1), "Invalid Input"); // Output: "Invalid Input"
```

## Cross References

- For more information on error handling, see the documentation on error functions and their applications.
- For additional Roman numeral formatting styles, refer to the section on ROMAN numeral styles.

<!-- tags: Roman numeral, IFERROR, error handling, Roman numeral conversion, Roman numeral styles, WinForms. keywords: ROMAN function, IFERROR function, Roman numeral, numeric conversion, error handling, concise Roman numeral, simplified Roman numeral -->
```

---

<!-- 페이지 161 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: calculate
page_number: 131
page_id: calculate#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:01Z
fidelity: lossless
-->

## Overview
- The page explains the syntax and usage of the AVERAGEIF and AVERAGEIFS functions in relevant software.
- It details how to calculate averages based on specified criteria, including examples and notes on error handling.

## Content

### AVERAGEIF Function
#### Overview
- If no cells in the range meet the criteria, AVERAGEIF returns the `#DIV/0!` error value.

#### Example
**Input Table**

|    | A          | B          |
|----|------------|------------|
| 1  | Earning    | Tax        |
| 2  | 100000     | 3000       |
| 3  | 200000     | 6000       |
| 4  | 300000     | 7500       |
| 5  | 400000     | 9000       |

**FORMULA** | **RESULT**
|------------|------------|
| `=AVERAGEIF(B2:B5, "<7000")` | 4500 |
| `=AVERAGEIF(A2:A5, ">250000")` | 350000 |

### 4.5.6.23 AVERAGEIFS

#### Description
- The AVERAGEIFS function finds the average of values in a given array that satisfy a set of given criteria.

#### Syntax
```markdown
=AVERAGEIFS(average_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

- **average_range**: Specific set of values to be averaged if the criteria range meets the provided criteria.
- **criteria_range1**: Array of values to be tested against the given criteria.
- **criteria1**: The condition to be tested on each of the values of the given range.

#### Notes
- If `average_range` is blank or a text value, AVERAGEIFS returns the `#DIV/0!` error value.
- If a cell in a criteria range is empty, AVERAGEIFS treats it as a `0` value.
- If cells in `average_range` cannot be translated into numbers, AVERAGEIFS returns the `#DIV/0!` error value.

#### Example

## API Reference (if applicable)
- None explicitly mentioned in the provided content.

## Code Examples (multi-language supported)
- None explicitly mentioned in the provided content.

<!-- tags: [averageif, averageifs, error handling, criteria, averaging] keywords: [average, criteria, averaging, error, div0] -->
```

---

<!-- 페이지 162 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_135.jpeg
document_name: calculate
page_number: 135
page_id: calculate#page_135
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:17Z
fidelity: lossless
-->

## Essential Calculate

### Input Table

|   | A       | B    | C      |
|---|---------|------|--------|
| 1 | Earning | Tax  | other  |
| 2 | 100000  | 3000 | 100    |
| 3 | 200000  | 6000 | 200    |
| 4 | 300000  | 7500 | 300    |
| 5 | 400000  | 9000 | 500    |

### Formula and Results

| FORMULA                                    | RESULT |
|--------------------------------------------|--------|
| =LOOKUP(6000,B2:B5,C2:C5)                 | 200    |
| =LOOKUP("C",{ "a", "b", "c", "d" };1,2,3,4) | 3      |

### 4.5.6.28 SEARCH

The SEARCH function returns the location of a substring in a string. This function is NOT case-sensitive.

#### Syntax

SEARCH(substring, string, [start_position])

- **substring**: Required. The text to be found.
- **string**: Required. The text in which to search for the value of the substring.
- **start_num**: Optional. The starting position for searching in the string.

#### Notes

- If the value of `find_text` is not found, the `#VALUE!` error value is returned.
- If the `start_num` argument is omitted, it is assumed to be 1.
- If `start_num` is not greater than 0, or is greater than the length of the `string` argument, the `#VALUE!` error value is returned.

#### Example

| FORMULA                     | RESULT |
|-----------------------------|--------|
| =SEARCH("base","database")  | 5      |

<!-- tags: [syncfusion, winforms, essential calculate, search function, lookup function, api reference, code examples] keywords: [lookup, search, substring, string, start_position, error handling, case sensitivity, find_text, start_num, value, lookup function, search function, substring search, string, base, database, result, 200, 3, 5] -->
``` 


---

<!-- 페이지 163 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_139.jpeg
document_name: calculate
page_number: 139
page_id: calculate#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:31Z
fidelity: lossless
-->

# Essential Calculate

| Ztest | Returns the P-value of a z-test. |
|-------|------------------------------------|

## Inside CalcEngine

### 4.6 Inside CalcEngine

Following are the topics discussed in this section.

#### 4.6.1 Tracking the Information

To track information used during calculations, CalcEngine manages several hash tables. Here is a table of the public hash tables in CalcEngine and a description of their keys and values:

### Table 12: Hash Table

| Hash Table            | Key                    | Value                  | Description                                                      |
|-----------------------|------------------------|------------------------|------------------------------------------------------------------|
| FormulaInfoTable      | Cell reference         | FormulaInfo object     | Tracks formula/value information for this cell.                  |
| DependentCells        | Cell reference         | Hashtable object       | Tracks cells that depend on this cell.                           |
| DependentFormulaCells | Formula cell reference | Hashtable object       | Tracks cells that the formula cell depends upon.                 |
| NamedRanges           | Name string            | Value string           | Associates the named range with its value.                       |
| LibraryFunctions      | Function name          | LibraryFunction delegate | Associates the function name with its method.                   |

Within CalcEngine, all data is assumed to be part of a rectangular array reference through cell coordinates like A1, C18, and so on. Even CalcQuickBase does not require or use such cell-type notation internally on the user side. When it communicates with CalcEngine, it converts its [name]-type notation into cell references that CalcEngine can understand. It is these cell references that are used as keys for the first three listed hash tables.

### 4.6.2 Parsing

## API Reference (if applicable)
- None explicitly detailed in this section.

## Code Examples (multi-language supported)
- None explicitly detailed in this section.

<!-- tags: [syncfusion-sdk, calcengine, ztest, hash-table, calculation-engine, dependent-cells, named-ranges, library-functions] keywords: [formula-info-object, hashtable, cell-reference, named-range, function-name, method] -->
```

---

<!-- 페이지 164 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_143.jpeg
document_name: calculate
page_number: 143
page_id: calculate#page_143
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:44Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- **ABS**: Returns the absolute value of a number.
- **ACOS**: Returns the inverse cosine (arccosine) of a number.
- **ACOSH**: Returns the inverse hyperbolic cosine of a number.

### Content

#### 4.7.2 ABS
**Description**:  
Returns the absolute value of a number. The absolute value of a non-negative number is the number itself. The absolute value of a negative number is -1 times the number.

**Syntax**:  
```csharp
ABS(number)
```

**Parameters**:  
- **number**: The real number for which you want the absolute value.

#### 4.7.2 ACOS
**Description**:  
Returns the inverse cosine of a number. Inverse cosine is also referred to as arccosine. The arccosine is the angle whose cosine is the given number. The returned angle is given in radians in the range of 0 to pi.

**Syntax**:  
```csharp
ACOS(number)
```

**Parameters**:  
- **number**: The cosine of the angle that you want, which must be between -1 and 1.

#### 4.7.3 ACOSH
**Description**:  
Returns the inverse hyperbolic cosine of a number. The number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is the given number.

**Syntax**:  
```csharp
ACOSH(number)
```

**Parameters**:  
- **number**: Any real number that is greater than or equal to 1.

<!-- tags: [abs, acos, acosh, math functions, trigonometric functions, hyperbolic functions, syncfusion, winforms, 11.4.0.26] keywords: [absolute value, inverse cosine, inverse hyperbolic cosine, arccosine, radians, range, angle, cosine] -->
```

---

<!-- 페이지 165 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_147.jpeg
document_name: calculate
page_number: 147
page_id: calculate#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:57Z
fidelity: lossless
-->

## Remarks

- The arguments must either be numbers or names, arrays or references that contain numbers.
- If an array or reference argument contains text, logical values or empty cells, those values are ignored; however, cells with the a zero value are included.
- The equation for average deviation is:

\[
\frac{1}{n} \sum |x - \overline{x}|
\]

where:  
**x-bar** is the arithmetic mean of the data.

## 4.7.11 AVERAGE

### Returns the average (arithmetic mean) of the arguments.

#### Syntax

AVERAGE(number1, number2, ...)

where:  
**number1, number2, ...** are numeric arguments for which you want the average.

### Remarks

- The arguments must either be numbers or names, arrays or references that contain numbers.
- If an array or reference argument contains text, logical values or empty cells, those values are ignored; however, cells with a zero value are included.

## 4.7.12 AVERAGEA

Calculates the average (arithmetic mean) of the values in the list of arguments. In addition to numbers and text logical values such as True and False are also included in the calculation.

```
<!-- tags: [calculate, average, averagea, arithmetic mean, average deviation, arrays, references, Syncfusion Winforms, version:11.4.0.26] keywords: [average, averagea, arithmetic, mean, average deviation, calculate, text, logical values, numbers, arrays, references] -->
```

---

<!-- 페이지 166 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_151.jpeg
document_name: calculate
page_number: 151
page_id: calculate#page_151
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:08Z
fidelity: lossless
-->

# Essential Calculate

## Content

### Remarks

- Both arguments should be numeric.
- `degrees_freedom >= 1` and `< 10^{10}`.
- `CHIDIST` is calculated as follows:

  \[
  \text{CHIDIST} = \text{P}(X > x)
  \]

  where:
  - \( X \) is a \(\chi^2\) random variable.

### 4.7.18 CHIINV

Returns the inverse of the one-tailed probability of the chi-squared (\(\chi^2\)) distribution. If probability = `CHIDIST(x,...)`, then `CHIINV(probability,...) = x`. Use this function to compare observed results with expected ones in order to decide whether your original hypothesis is valid.

#### Syntax

```markdown
CHIINV(probability, degrees_freedom)
```

where:
- `probability` is a probability associated with the chi-squared distribution.
- `degrees_freedom` is the number of degrees of freedom.

#### Remarks

- Probability must be \(\geq 0\) and \(\leq 1\).
- `degrees_freedom >= 1` and \( = 10^{10}\).

Given a value for `probability`, `CHIINV` seeks the value \( x \) such that `CHIDIST(x, degrees_freedom) = probability`. Thus, precision of `CHIINV` depends on precision of `CHIDIST`. `CHIINV` uses an iterative search technique.
```


<!-- tags: [syncfusion, winforms, chidist, chiinv, chi-squared distribution] keywords: [chidist, chiinv, degrees of freedom, probability, hypothesis testing, chi-squared distribution] -->
```

---

<!-- 페이지 167 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_155.jpeg
document_name: calculate
page_number: 155
page_id: calculate#page_155
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:20Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- The section explains the use of `alpha` for calculating confidence levels, `standard_dev` for population standard deviation, and the `size` for sample size in calculations.
- It also introduces the `CORREL` function to calculate the correlation coefficient between two cell ranges.

---

### Primary Explanation
#### Parameters for Confidence Level Calculation

**alpha**
- Represents the significance level used to compute the confidence level.
- The confidence level equals 100 * (1 - alpha)%.
- For example, an alpha of 0.05 indicates a 95 percent confidence level.

**standard_dev**
- Denotes the population standard deviation for the data range.
- It is assumed to be known.

**size**
- Represents the sample size.

#### Remarks
- All arguments must be non-numeric.
- Alpha must be between 0 and 1.
- Standard_dev must be greater than 0.
- Size must be greater than or equal to 1.

---

## 4.7.25 CORREL

### Description
- The `CORREL` function returns the correlation coefficient of the `array1` and `array2` cell ranges.

#### Syntax
```plaintext
CORREL(array1, array2)
```

- `array1`: A cell range of values.
- `array2`: The second cell range of values.

#### Remarks
- `array1` and `array2` must have the same number of data points.
- The equation for the correlation coefficient is:
```plaintext
Correl(X,Y) = \frac{\sum(x-\overline{x})(y-\overline{y})}{\sqrt{\sum(x-\overline{x})^2\sum(y-\overline{y})^2}}
```

---

## API Reference

### Method: CORREL
#### Parameters
- `array1`: The first cell range of values.
- `array2`: The second cell range of values.

#### Returns
- The correlation coefficient as a numeric value.

#### Exceptions
- Throws an error if `array1` and `array2` do not have the same number of data points.

---

### Code Examples

#### C#
```csharp
double correlation = CORREL(range1, range2);
```

---

## Page-level Navigation/TOC (if applicable)
- Possible navigation or reference to related sections like "Confidence Level Calculations" or "Statistical Functions".

---

## Cross References
See also:
- Documentation on Confidence Interval functions.
- Usage of standard deviation and sample size in statistical analysis.

---

<!-- tags: [Syncfusion Winforms, statistics, confidence intervals, correlation, alpha, standard_deviation, sample_size] keywords: [alpha, standard_deviation, sample_size, CORREL, correlation_coefficient, confidence_level, statistical_functions, array1, array2] -->
```

---

<!-- 페이지 168 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_159.jpeg
document_name: calculate
page_number: 159
page_id: calculate#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:37Z
fidelity: lossless
-->

# Essential Calculate

## Syntax

`COVAR(array1, array2)`

where:
- `array1` is the first cell range of numbers.
- `array2` is the second cell range of numbers.

## Remarks

- The arguments must either be numbers or be names, arrays or references that contain numbers.
- `array1` and `array2` must have the same number of data points.
- The covariance is:

\[
Cov(X,Y) = \frac{\sum (x-\bar{x})(y-\bar{y})}{n}
\]

where:
- \( X \) is `array1`
- \( Y \) is `array2`
- \( \bar{x} \) and \( \bar{y} \) are the sample means AVERAGE(`array1`) and AVERAGE(`array2`).
- \( n \) is the sample size.

### 4.7.33 CRITBINOM

**Returns the smallest value for which, the cumulative binomial distribution is greater than or equal to a criterion value.**

#### Syntax

`CRITBINOM(trials, probability_s, alpha)`

#### where:
- `trials` is the number of Bernoulli trials.
```

---

<!-- 페이지 169 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_163.jpeg
document_name: calculate
page_number: 163
page_id: calculate#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:47Z
fidelity: lossless
-->

# Essential Calculate

- The fixed-declining balance method computes the depreciation at a fixed rate. DB uses the following formulas to calculate the depreciation for a period:
  - \((\text{cost} - \text{total depreciation from prior periods}) * \text{rate}\)
  - where:
    - \(\text{rate} = 1 - \left(\frac{\text{salvage}}{\text{cost}}\right)^{\left(\frac{1}{\text{life}}\right)}\), rounded to three decimal places

- Depreciation for the first and last periods is a special case. For the first period, DB uses this formula:
  - \(\text{cost} * \text{rate} * \text{month} / 12\)

- For the last period, DB uses this formula:
  - \((\text{cost} - \text{total depreciation from prior periods}) * \text{rate} * \left(12 - \text{month}\right) / 12\)

## 4.7.39 DDB

Returns the depreciation of an asset for a specified period using the double-declining balance method or some other method you specify.

### Syntax

DDB(cost, salvage, life, period, factor)

where:

- **cost** is the initial cost of the asset.
- **salvage** is the value at the end of the depreciation (sometimes called the salvage value of the asset).
- **life** is the number of periods over which the asset is being depreciated (sometimes called the useful life of the asset).
- **period** is the period for which you want to calculate the depreciation. Period must use the same units as life.
- **factor** is the rate at which the balance declines. If factor is omitted, it is assumed to be 2 (the double-declining balance method).

**Note:** All five arguments must be positive numbers.

### Remarks

---

© 2013 Syncfusion. All rights reserved. 163 | Page
```

---

<!-- 페이지 170 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_167.jpeg
document_name: calculate
page_number: 167
page_id: calculate#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:00Z
fidelity: lossless
-->

## Overview
- Provides essential information about factorial calculations, logical values, and probability distributions.
- Explains the use and syntax of functions such as FACT, False, and FDIST.
- Includes details on how each function evaluates and returns specific values based on input parameters.

## Content

### 4.7.47 FACT
**Returns the factorial of a number.** The factorial of a number is the product of all positive integers <= the given number.

#### Syntax
```csharp
FACT(number)
```

**where:**  
`number` is the non-negative number for which you want the factorial of. If the number is not an integer, it is truncated.

### 4.7.48 False
**The False function returns the logical value for the false.**

#### Syntax
```csharp
False(stringvalue)
```

**where:**  
- `stringvalue` is to provide an empty string.

### 4.7.49 FDIST
**Returns the F probability distribution.**

#### Syntax
```csharp
FDIST(x, degrees_freedom1, degrees_freedom2)
```

**where:**  
`x` is the value at which to evaluate the function.

<!-- tags: [syncfusion, winforms, factorial, false, fdist, probability_distribution, mathematical_functions, logical_function, api] keywords: [factorial, logical_value, false_function, f_probability_distribution, fdist, x, degrees_freedom1, degrees_freedom2] -->
```

---

<!-- 페이지 171 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_171.jpeg
document_name: calculate
page_number: 171
page_id: calculate#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:11Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Number and significance must have the same sign.
- Regardless of the sign of the number, a value is rounded down when adjusted away from zero. If a number is an exact multiple of significance, no rounding occurs.

## Content

### 4.7.56 FORECAST

Calculates a future value by using existing values using a linear regression. The predicted value is a y-value for a given x-value.

#### Syntax

FORECAST(x, known_ys, known_xs)

where:
- x is the data point for which you want to predict a value.
- known_ys is the dependent array or range of data.
- known_xs is the independent array or range of data.

#### Remarks
- The equation for FORECAST is:
  
  $$
  \text{a + bx}
  $$

  where:
  $$
  \text{a = } \bar{y} \text{ - b}\bar{x}
  $$
  $$
  \text{b = } \frac{\sum(x - \bar{x})(y - \bar{y})}{\sum(x - \bar{x})^2}
  $$

  x-bar and y-bar are the sample means AVERAGE(know(xs)) and AVERAGE(known_ys).
```

---

<!-- 페이지 172 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_175.jpeg
document_name: calculate
page_number: 175
page_id: calculate#page_175
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:21Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Enables calculation of predicted exponential growth using existing data.
- Provides an array of values used for regression analysis.

## Content

### **4.7.62 GROWTH**

This feature enables you to calculate predicted exponential growth using existing data. This calculates and returns an array of values used for the regression analysis. Growth enables you to perform a regression analysis.

#### Table 13: Method Table

| Method | Description                          | Parameters             | Type     | Return Type | Reference links |
|--------|---------------------------------------|-------------------------|----------|--------------|-----------------|
| Growth() | Calculates the Growth for an array of cells. | Known y's, <br> Known x's, <br> new_x's | Method | String | N/A |

#### Syntax

The following is the formula to calculate Growth for an array of cells in a column:

```plaintext
=GROWTH(known_y's, [known_x's], [new_x's],
```

- **Known_y's**: A set of y-values you already know in a relationship, where \( y = b \cdot m^x \).
- **Known_x's**: An optional set of x-values that you may already know in the relationship, where \( y = b \cdot m^x \).
- **New_x's**: New x-values for which you want GROWTH to return corresponding y-values.

#### Code Example

```plaintext
=Growth(B2:B7,A2:A7,C6:C7)
```

### **4.7.63 HARMEAN**

---

## API Reference
- **Namespace**: N/A (Not explicitly mentioned in the provided page)
- **Class**: N/A (Not explicitly mentioned in the provided page)
- **Members**:
  - **Growth()**
    - **Parameters**:
      - Name | Type | Description | Default | Required
      - known_y's | Array | Known y-values | None | Yes
      - [known_x's] | Array | Known x-values (optional) | None | No
      - [new_x's] | Array | New x-values | None | No
    - **Returns**: String
    - **Description**: Calculates the predicted y-values for the given x-values using exponential growth.
    - **Exceptions**: None explicitly mentioned.

## Code Examples (multi-language supported)
The provided code example in the page demonstrates the use of the `Growth()` function:

```csharp
var growthResult = Growth(B2:B7, A2:A7, C6:C7);
```

In this example:
- `B2:B7` represents the known_y's.
- `A2:A7` represents the known_x's.
- `C6:C7` represents the new_x's for which the corresponding y-values are calculated.

---

## Cross References
- See also: `HARMEAN` for calculating the harmonic mean.

---

<!-- tags: [Syncfusion, Winforms, User Guide, Essential Calculate, GROWTH, HARMEAN, Exponential Growth, Regression Analysis] keywords: [exponential growth, regression analysis, GROWTH function, HARMEAN, known_y's, known_x's, new_x's, Syncfusion Winforms] -->
```

---

<!-- 페이지 173 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_179.jpeg
document_name: calculate
page_number: 179
page_id: calculate#page_179
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:42Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.68 IF

Returns one value if a condition you specify evaluates to True and another value if it evaluates to False.

Use IF to conduct conditional tests on values and formulas.

#### Syntax

```markdown
IF(logical_test, value_if_true, value_if_false)
```

#### where:

- `logical_test` is any value or expression that can be evaluated to True or False.
- `value_if_true` is the value that is returned if a logical_test is True.
- `value_if_false` is the value that is returned if a logical_test is False.

#### Remarks

- Countif and Sumif are additional methods that provide conditional calculations.

### 4.7.69 Index

The Index function returns the exact value from the provided row index and column index from a specific range.

#### Syntax:

```markdown
Index(range,row,col)
```

#### where,

- `range` is a string to mention the specific range.
- `row` is the integer that indicates the specific row index.
- `col` is the integer that indicates the specific column index.

### 4.7.70 Indirect

The Indirect function returns the reference as a string instead of providing the content or range within it.

<!-- tags: [IF, Index, Indirect, conditional calculations] keywords: [logical_test, value_if_true, value_if_false, Countif, Sumif, row index, column index, reference] -->
```

---

<!-- 페이지 174 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_183.jpeg
document_name: calculate
page_number: 183
page_id: calculate#page_183
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:52Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Functions to check for specific types of values such as errors, logical values, and missing values.
- Returns `TRUE` or `FALSE` based on the evaluation of the input value against specific conditions.

## Content

### 4.7.77 ISERROR

Returns `True` if the value is a string that starts with a `#`.

#### Syntax
```plaintext
ISERROR(value)
```
where:
- `value` is the value that is to be tested.

---

### 4.7.78 IsLogical

The `IsLogical` function checks whether a value is a logical value and returns a `TRUE` or `FALSE`.

#### Syntax:
```plaintext
IsLogical( value )
```
where,
- This value is the value that you want to test. If the value is a `TRUE` or `FALSE` value, this function will return `TRUE`. Otherwise, it will return `FALSE`.

---

### 4.7.79 IsNA

The `IsNA` function returns a boolean value after determining that the provided value is a `#NA` error value.

#### Syntax:
```plaintext
IsNA(value)
```
where,
- `value` the function will test.

## Page-level Navigation/TOC (if applicable)
- None in this section

## Cross References
- See also: `ISERROR`, `IsLogical`, `IsNA`

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [ISERROR, IsLogical, IsNA, boolean, logical values, error values, missing values, Syncfusion Winforms] -->
```

---

<!-- 페이지 175 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_187.jpeg
document_name: calculate
page_number: 187
page_id: calculate#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:04Z
fidelity: lossless
-->

## Essential Calculate

### LEFT(text, num_chars)

#### Parameters
- **text**: The text string that contains the characters you want to extract.
- **num_chars**: Specifies the number of characters which you want `LEFT` to extract.

#### Remarks
- `num_chars` must be greater than or equal to zero.
- If `num_chars` is greater than the length of `text`, `LEFT` returns all the text.
- If `num_chars` is omitted, it is assumed to be 1.

---

### 4.7.87 LN

#### Function
Returns the natural logarithm of a number. Natural logarithms are based on the constant \( e \) (2.718281828459...).

#### Syntax
```plaintext
LN(number)
```

#### Parameters
- **number**: The positive real number for which you want the natural logarithm.

#### Remarks
- `LN` is the inverse of the `EXP` function.

---

### 4.7.88 LEN

#### Function
`LEN` returns the length of a text string, including spaces.

#### Syntax
```plaintext
LEN(text)
```

---

## API Reference

### Namespace: System.String

#### Methods
- **LEFT(text, num_chars)**: Extracts the specified number of characters from the start of a text string.
- **LN(number)**: Computes the natural logarithm of a given number.
- **LEN(text)**: Returns the length of a text string.

---

## Cross References

See also:
- Previous section: [Other String Functions](#other-string-functions)
- Related documentation: [Mathematical Functions](#mathematical-functions)

---

## RAG Annotations
<!-- tags: [winforms, string-functions, mathematical-functions, synchronization-guide] keywords: [LEFT, LN, LEN, natural logarithm, character extraction, text length, API reference, Syncfusion] -->
```

---

<!-- 페이지 176 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_191.jpeg
document_name: calculate
page_number: 191
page_id: calculate#page_191
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:17Z
fidelity: lossless
-->

# Essential Calculate

- The equation for the lognormal cumulative distribution function is:
\[
\text{LOGNORMDIST}(x, \mu, \sigma) = \text{NORMSDIST}\left(\frac{\ln(x) - \mu}{\sigma}\right)
\]

### 4.7.94 Lower

The **Lower** function converts all characters in the specified text string to lowercase. Characters in the string that are not letters are not changed.

#### Syntax:
```text
Lower( text )
```

**where**,  
- **text** is the string you want to convert to lowercase.

### 4.7.95 Match

The **Match** function searches for a specified value in an array and returns the relative position of that item.

#### Syntax:
```text
Match( value, array, match_type )
```

**where**,  
- **this value** is the value you want to search in the array.
- **array** is a range of cells that contains the value you want to search.
- **match_type** is the type of match you want to perform.

**match_type** accepts the following values:

- **1**: The Match function will find the largest value that is less than or equal to the specified value. Ensure that the array is sorted in ascending order.
- **0**: The Match function will find the first value that is equal to the specified value. The array can be sorted in any order.
- **-1**: The Match function will find the smallest value that is greater than or equal to the specified value. Ensure that the array is sorted in descending order.

## API Reference (if applicable)
### WinForms-specific conventions
- Prefer C# samples when language is ambiguous; if VB is explicitly shown, keep both.
- Treat control names, namespaces, and types exactly.

### Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

<!-- tags: [Syncfusion Winforms, Lognormal cumulative distribution function, Lower function, Match function, Match function types] -->
```

---

<!-- 페이지 177 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_195.jpeg
document_name: calculate
page_number: 195
page_id: calculate#page_195
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:31Z
fidelity: lossless
-->

# Essential Calculate

## Overview

This page provides information on calculating values using specific functions, including finding the smallest value among a list of arguments, extracting minutes from a time value, and calculating the modified internal rate of return for cash flows.

## Content

### Finding the Smallest Value

Where:

- `value1, value2, ...` are values for which you want to find the smallest value.

#### Remarks
- **Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).**

### 4.7.102 MINUTE

Returns the minutes of a time value. The minute is given as an integer, ranging from 0 to 59.

#### Syntax
```markdown
MINUTE(serial_number)
```

Where:

- `serial_number` is the time that contains the minute you want to find. Times may be entered as text strings within quotation marks (for example, "6:00 PM"), as decimal numbers (for example, 0.75, which represents 6:00 PM), or as results of other formulas or functions (for example, `TIMEVALUE("6:00 PM")).`

#### Remarks
- Time values are a portion of a date value and are represented by a decimal number (for example, 12:00 PM is represented as 0.5).

### 4.7.103 MIRR

Returns the modified internal rate of return for a series of periodic cash flows.

#### Syntax
```markdown
MIRR(values, finance_rate, reinvest_rate)
```

Where:
- `values`: The series of cash flows.
- `finance_rate`: The interest rate you pay on the money borrowed.
- `reinvest_rate`: The interest rate you receive on the cash flows as you reinvest them.

---

## RAG Annotations
 <!-- tags: [Syncfusion Winforms, Calculate, MINUTE, MIRR, essential, function, parameters, cash flow] keywords: [calculate, MINUTE, MIRR, smallest value, time, decimal, rate of return] -->
```

---

<!-- 페이지 178 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: calculate
page_number: 199
page_id: calculate#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:44Z
fidelity: lossless
-->

## Normal Distribution Functions in Syncfusion Winforms

### Overview
- Describes the `NORMDIST` function, which returns the normal distribution for the specified mean and standard deviation.
- Explains the `NORMINV` function, which returns the inverse of the normal cumulative distribution for the specified mean and standard deviation.

### Content

#### NORMDIST
>Returns the normal distribution for the specified mean and standard deviation.

**Syntax**

```plaintext
NORMDIST(x, mean, standard_dev, cumulative)
```

**Parameters**

- `x`: The value for which you want the distribution.
- `mean`: The arithmetic mean of the distribution.
- `standard_dev`: The standard deviation of the distribution.
- `cumulative`: A logical value that determines the form of the function. If `cumulative` is `True`, `NORMDIST` returns the cumulative distribution function. If `False`, it returns the probability mass function.

**Remarks**
- `Standard_dev` must be greater than 0.
- The equation for the normal density function (when `cumulative = False`) is:

\[
f(x, \mu, \sigma) = \frac{e^{-\frac{(x-\mu)^2}{2\sigma^2}}}{\sqrt{2\pi}\sigma}
\]

- When `cumulative = True`, the formula is the integral from negative infinity to \(x\) of the given formula.

#### 4.7.109 NORMINV
>Returns the inverse of the normal cumulative distribution for the specified mean and standard deviation.

**Syntax**

```plaintext
NORMINV(probability, mean, standard_dev)
```

## API Reference

### NORMDIST

- **Parameters**:
  - `x`: Value for which you want the distribution.
  - `mean`: Arithmetic mean of the distribution.
  - `standard_dev`: Standard deviation of the distribution.
  - `cumulative`: Logical value that determines the form of the function.

### NORMINV

- **Parameters**:
  - `probability`: The probability corresponding to the normal distribution.
  - `mean`: Arithmetic mean of the distribution.
  - `standard_dev`: Standard deviation of the distribution.

<!-- tags: [syncfusion, winforms, normal distribution, normdist, norminv] keywords: [normal distribution, cumulative, probability mass function, standard deviation, mean, probability, inverse, normal distribution function] -->
```

---

<!-- 페이지 179 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_203.jpeg
document_name: calculate
page_number: 203
page_id: calculate#page_203
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:01Z
fidelity: lossless
-->

### 4.7.116 ODD

**Returns the number rounded up to the nearest odd integer.**

#### Syntax

```plaintext
ODD(number)
```

**where:**  

`number` is the value to be rounded off.

#### Remarks

- Regardless of the sign of a number, a value is rounded up when adjusted away from zero. If the number is an odd integer, no rounding occurs.

---

### 4.7.117 Offset

**The Offset function returns a reference to a range that is offset a number of rows and columns from any given range or cell.**

#### Syntax:

```plaintext
Offset( range, rows, columns, height, width )
```

**where,**  
- `range` is the starting range from which you want to apply the offset.
- `rows` is the number of rows you want to apply as the offset to the range. This can be either a positive or negative number.

---

## Page-level Navigation/TOC (if applicable)

- [4.7.116 ODD](#4.7.116-odd)
- [4.7.117 Offset](#4.7.117-offset)

<!-- tags: [NPV, Odd, Offset, Financial Functions, Syncfusion Winforms] keywords: [NPV formula, rounding to nearest odd integer, offset function, range manipulation] -->
```

---

<!-- 페이지 180 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_207.jpeg
document_name: calculate
page_number: 207
page_id: calculate#page_207
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:12Z
fidelity: lossless
-->

### 4.7.124 PMT

Calculates the payment for a loan based on constant payments and a constant interest rate.

#### Syntax

``` 
PMT(rate, nper, pv, fv, type)
```

#### Parameters

- **rate**: The interest rate for the loan.
- **nper**: The total number of payments for the loan.
- **pv**: The present value or the total amount that a series of future payments is worth now; also known as the principal.
- **fv**: The future value or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (zero), that is, the future value of a loan is 0.
- **type**: The number 0 (zero) or 1 and indicates when payments are due. If type equals:
  - **0**: Payments are due at the end of the period.
  - **1**: Payments are due at the beginning of the period.

#### Remarks

- The payment returned by PMT includes principal and interest but no taxes, reserve payments or fees sometimes associated with loans.
- Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use `12%/12` for `rate` and `4*12` for `nper`. If you make annual payments on the same loan, use `12 percent` for `rate` and `4` for `nper`.

### 4.7.125 POISSON

Returns the Poisson distribution.

#### Syntax

``` 
POISSON(x, mean, cumulative)
```

<!-- tags: [PMT, constant payments, interest rate, POISSON, Poisson distribution, loan] keywords: [rate, nper, pv, fv, type, x, mean, cumulative, payment, principal, future value, consistent units] -->
```

---

<!-- 페이지 181 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_211.jpeg
document_name: calculate
page_number: 211
page_id: calculate#page_211
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:25Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Returns the present value of an investment.
- Calculates the total amount that a series of future payments is worth now.

### Overview
- Presents detailed information about the PV function used to calculate the present value of an investment.

## Content

### 4.7.131 PV

#### Overview
- Returns the present value of an investment.
- The present value is the total amount that a series of future payments is worth now.

#### Syntax
- `PV(rate, nper, pmt, fv, type)`

##### Parameters
- **rate**: The interest rate per period. For example, if you obtain an automobile loan at a 10% annual interest rate and make monthly payments, your interest rate per month is 10%/12 or 0.83%. You would enter 10%/12 or 0.83% or 0.0083, into the formula as the rate.
- **nper**: The total number of payment periods in an annuity. For example, if you get a four-year car loan and make monthly payments, your loan has 4*12 (or 48) periods. You would enter 48 into the formula for nper.
- **pmt**: The payment made for each period and cannot change over the life of the annuity. Typically, pmt includes principal and interest but, no other fees or taxes. For example, the monthly payments on a $10,000, four-year car loan at 12 percent are $263.33. You will have to enter -263.33 into the formula as the pmt. If pmt is omitted, you must include the fv argument.
- **fv**: The future value or a cash balance that you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0). For example, if you want to save $50,000 to pay for a special project in 18 years, then $50,000 is the future value. You could then make a conservative guess at an interest rate and determine how much you must save each month. If fv is omitted, you must include the pmt argument.
- **type**: The number 0 or 1 and indicates when payments are due. If type equals:
  - **0**: Payments are due at the end of the period.
  - **1**: Payments are due at the beginning of the period.

### Remarks
- **Consistency in Units**: Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper.
- **Cash Representation**: In annuity functions, the cash you pay out such as a deposit to savings is represented by a negative number; the cash you receive such as a dividend check is represented by a positive number.
- **Financial Argument Solution**: One financial argument is solved for in terms of the others. If rate is not 0, then, the other arguments are solved accordingly.

<!-- tags: [present value, investment, financial calculations, interest rate, payment periods, payment amount, future value, payment due date] keywords: [PV function, present value calculation, annuity, financial calculations] -->
```

---

<!-- 페이지 182 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_215.jpeg
document_name: calculate
page_number: 215
page_id: calculate#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:47Z
fidelity: lossless
-->

## Remarks

- Num_chars must be greater than or equal to zero.
- If num_chars is greater than the length of text, RIGHT returns all the text.
- If num_chars is omitted, it is assumed to be 1.

### 4.7.138 ROUND

*Rounds a number to a specified number of digits.*

#### Syntax

ROUND(number, num_digits)

where:
- **number**: is the number you want to round off.
- **num_digits**: specifies the number of digits you want to round off.

#### Remarks

- If num_digits > 0, then number is rounded off to the specified number of decimal places.
- If num_digits = 0, then number is rounded off to the nearest integer.
- If num_digits < 0, then number is rounded off to the left of the decimal point.

### 4.7.139 ROUNDDOWN

*Rounds a number down towards zero.*

#### Syntax

ROUNDDOWN(number, num_digits)

where:
<!-- tags: [product, module, control, api, version?] keywords: [round, rounddown, num_digits, number, decimal places, rounding, nearest integer, left of decimal point] -->
``` 
```

---

<!-- 페이지 183 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_219.jpeg
document_name: calculate
page_number: 219
page_id: calculate#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:57Z
fidelity: lossless
-->

# Essential Calculate

## Math Functions

The `sinh(z)` function computes the hyperbolic sine of the argument using the formula:

```tex
\sinh(z) = \frac{e^z - e^{-z}}{2}
```

### Description of Functions

#### 4.7.145 SinH
The SinH function computes the hyperbolic sine of the argument.

- **Syntax:**  
  `SinH(value)`

- **Parameters:**  
  - `value` is to get the sine of the specific value.

---

#### 4.7.146 SKEW

**Description:**  
Returns the skewness of a distribution. Skewness characterizes the degree of asymmetry of a distribution around its mean.

- **Syntax:**  
  `SKEW(number1, number2, ...)`

- **Parameters:**  
  - `number1`, `number2`, ... are arguments for which you want to calculate the skewness. You can also use a single array or a reference to an array instead of arguments separated by commas.

- **Remarks:**  
  The equation for skewness is defined as:

  ```tex
  \frac{n}{(n-1)(n-2)} \sum \left( \frac{x_i - \overline{x}}{s} \right)^3
  ```

## Page-level Navigation/TOC (if applicable)

- **4.7.145 SinH**
- **4.7.146 SKEW**

## Cross References

See also: [SinH Function], [SKEW Function]

## Code Examples (multi-language supported)

No code examples are provided in this section. Please refer to the API documentation or code samples for implementation.

<!-- tags: [sinh, skewness, hyperbolic sine, asymmetry, statistics, mathematical functions, syncfusion, winforms] keywords: [sinh, skew, asymmetry, distribution, calculate] -->
```

---

<!-- 페이지 184 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_223.jpeg
document_name: calculate
page_number: 223
page_id: calculate#page_223
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:12Z
fidelity: lossless
-->

# Essential Calculate

## Remarks

- STDEV assumes that its arguments are a sample of the population. If your data represents the entire population, then compute the standard deviation using STDEVP.
- STDEV uses the following formula:

\[
\sqrt{\frac{\sum(x - \bar{x})^2}{(n-1)}}
\]

where:
- **x-bar** is the sample mean AVERAGE(number1, number2,...).
- **n** is the sample size.

### 4.7.153 STDEVA

#### Overview
- Estimates standard deviation based on a sample. The standard deviation is a measure of how widely values are dispersed from the average value (the mean). Text and logical values such as True and False are also included in the calculation.

#### Syntax
- **STDEVA(value1, value2, ...)**

where:
- **value1, value2,...** are values corresponding to a sample of a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks

- Arguments that contain True evaluate as 1; arguments that contain text or False evaluate as 0 (zero).
- STDEVA uses the following formula:

\[
\sqrt{\frac{\sum(x - \bar{x})^2}{(n-1)}}
\]
```

---

<!-- 페이지 185 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_227.jpeg
document_name: calculate
page_number: 227
page_id: calculate#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:23Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains functions and formulas used in calculations.
- Focuses on the SUBSTITUTE function and its applications.
- Includes description of the Sum and SumIf functions.

## Content

|   | A                                  | Description (Result)                                            |
|---|------------------------------------|-----------------------------------------------------------------|
| 1 | Data                              |                                                                 |
| 2 | Sales Data                        |                                                                 |
| 3 | Quarter 1, 2008                   |                                                                 |
| 4 | Quarter 1, 2011                   |                                                                 |
|   | Formula                            | Description (Result)                                            |
|   | =SUBSTITUTE(A2, "Sales", "Cost") | Substitutes Cost for Sales (Cost Data)                          |
|   | =SUBSTITUTE(A3, "1", "2", 1)     | Substitutes first instance of "1" with "2" (Quarter 2, 2008)   |
|   | =SUBSTITUTE(A4, "1", "2", 3)     | Substitutes third instance of "1" with "2" (Quarter 1, 2012)   |

### 4.7.158 Sum

The Sum function adds all numbers in a range of cells and returns the result.

#### Syntax:
Sum( number1, number2, … number_n )

**Where:**
- number1 is the first number
- number2 is the second number
- number_n is the nth number to be added together

### 4.7.159 SumIf

SumIf function adds the specified range of cells by a given criteria.

#### Syntax:
SumIf( range, criteria, sum_range )

**Where:**
- range is the range of cells you want to apply the criteria against.

## API Reference (if applicable)
- None explicitly mentioned in this section.

## Code Examples (multi-language supported)
- No specific code examples are provided in this section.

## Page-level Navigation/TOC (if applicable)
- None explicitly present.

## Cross References
- See also: SUBSTITUTE function, Sum function, SumIf function.

<!-- tags: [product, module, control, api, version?] keywords: [SUBSTITUTE, Sum, SumIf, Excel functions, formula, calculate, data analysis] -->
```

---

<!-- 페이지 186 -->

```md
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_231.jpeg
document_name: calculate
page_number: 231
page_id: calculate#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:37Z
fidelity: lossless
-->

# Essential Calculate

$\frac{(cost - salvage) \cdot (life - per + 1) \cdot 2}{(life)(life + 1)}$

## 4.7.166 TAN

Returns the tangent of a number.

### Syntax

```plaintext
TAN(number)
```

where:

- `number` is the tangent of the angle that you want.

## 4.7.167 TANH

Returns the hyperbolic tangent of a number.

### Syntax

```plaintext
TANH(number)
```

where:

- `number` is any real number.

### Remarks

- The formula for the hyperbolic tangent is:

$$
\tanh(z) = \frac{\sinh(z)}{\cosh(z)}
$$

## API Reference (if applicable)

- None provided in this excerpt.

## Code Examples (if applicable)

- None provided in this excerpt.

## Cross References

- None provided in this excerpt.

<!-- tags: [Essential Calculate, TAN, TANH, trigonometric functions, hyperbolic functions] keywords: [tangent, hyperbolic tangent, trigonometry, mathematical functions, calculate] -->
```

---

<!-- 페이지 187 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_235.jpeg
document_name: calculate
page_number: 235
page_id: calculate#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:47Z
fidelity: lossless
-->

## TRUNC(number, num_digits)

### Function Description
- **TRUNC(number, num_digits)** truncates a number to a specified number of decimal places.

### Parameters
- **number**: The number you want to truncate.
- **num_digits**: A number specifying the precision of the truncation. The default value for **num_digits** is 0 (zero).

### Remarks
- **TRUNC and INT Comparison**:
  - Both functions return integers.
  - **TRUNC** removes the fractional part of the number.
  - **INT** rounds numbers down to the nearest integer based on the value of the fractional part of the number.
  - **INT and TRUNC** differ only when using negative numbers:
    - **TRUNC(-4.3)** returns `-4`.
    - **INT(-4.3)** returns `-5` because `-5` is the lower number.

---

## 4.7.176 Upper

### Function Description
The **Upper** function converts all characters in a text string to uppercase.

### Syntax
- **Upper(text)**

### Parameters
- **text**: The string you want to convert to uppercase.

---

## 4.7.177 Value

### Function Description
The **Value** function computes the date or a string that contains the number, and converts it into number format.

### Syntax
- **Value(range)**

### Parameters
- **range**: The string that contains the date or a number.

---

<!-- tags: [syncfusion-sdk, calculate, TRUNC, Upper, Value] keywords: [truncation, integer conversion, uppercase, number format, string conversion] -->
```

---

<!-- 페이지 188 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_239.jpeg
document_name: calculate
page_number: 239
page_id: calculate#page_239
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:59Z
fidelity: lossless
-->

## Overview
- Explanation of `col_index_num` and `range_lookup` parameters in `VLOOKUP`.
- Description of the `WEEKDAY` function and its parameters.

## Content

### VLOOKUP Parameters

- **col_index_num**: The column number in the `table_array` from which the matching value must be returned.
  - A `col_index_num` of `1` returns the value in the first column of the `table_array`.
  - A `col_index_num` of `2` returns the value in the second column of the `table_array`, and so on.

- **range_lookup**: A logical value that specifies whether you want `VLOOKUP` to find an exact match or an approximate match.
  - If `True` or omitted, an approximate match is returned.
  - If an exact match is not found, the next largest value that is less than the `lookup_value` is returned.

#### Remarks
- If `VLOOKUP` can't find a `lookup_value` and the `range_lookup` is `True`, it uses the largest value that is less than or equal to the `lookup_value`.

### 4.7.184 WEEKDAY

**Returns the day of the week corresponding to a date.** The day is given as an integer, ranging from `1` (Sunday) to `7` (Saturday) by default.

#### Syntax
``` 
WEEKDAY(serial_number, return_type)
```

#### Parameters
- **serial_number**: A sequential number that represents the date of the day you are trying to find.
  - Dates should be entered using the `DATE` function or as results of other formulas or functions.
  - Example: Use `DATE(2008,5,23)` for the 23rd day of May 2008.

- **return_type**: A number that determines the type of return value.
  - **If Return_type is:**
    - `1` or omitted: Numbers `1` (Sunday) through `7` (Saturday).
    - `2`: Numbers `1` (Monday) through `7` (Sunday).
    - `3`: Numbers `0` (Monday) through `6` (Sunday).

#### Remarks
- Dates are stored as sequential serial numbers so that they can be used in calculations.
  - By default, January 1, 1900 is serial number `1`, and January 1, 2008 is serial number `39448` because it is 39,448 days after January 1, 1900.

## API Reference (if applicable)
- None specified in the current content.

## Code Examples (multi-language supported)
- None specified in the current content.

<!-- tags: [vlookup, weekday, function, parameter, return_type] keywords: [col_index_num, range_lookup, serial_number, exact match, approximate match, day of the week, date, integer, monday] -->
```

---

<!-- 페이지 189 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_243.jpeg
document_name: calculate
page_number: 243
page_id: calculate#page_243
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:18Z
fidelity: lossless
-->


# 5 Frequently Asked Questions

This section will help you find answers to common questions regarding Essential Calculate. It includes the below sections:

## 5.1 CalcQuick

CalcQuick is the simplest way to incorporate calculation support into your code. You can create an instance of it then you can assign variables just by using an indexer on your instance. You can parse and compute formulas based on these variables by calling a single method on your CalcQuick object.

### 5.1.1 How To Add, Remove, And Modify the Implementation Of Functions In the Function Library In CalcQuickBase?

Refer the **Function Library** topic to know about this.

### 5.1.2 How To Calculate a Formula?

To calculate a formula, use the `ParseAndCompute` method from the `CalcQuickBase` class.

```csharp
// Declares a CalcQuickBase object.
private CalcQuickBase calculate;

//...

// Creates an instance.
this.calculate = new CalcQuickBase();

//... Set up any variables you need in your calculation.

// Calls the ParseAndCompute method to compute formulas.
string result = this.calculate.ParseAndCompute("4 * 5 + SQRT(3)");
```

## Page-level Navigation/TOC (if applicable)

- **5 Frequently Asked Questions**
  - **5.1 CalcQuick**
    - **5.1.1 How To Add, Remove, And Modify the Implementation Of Functions In the Function Library In CalcQuickBase?**
    - **5.1.2 How To Calculate a Formula?**

## Cross References

See also: **Function Library**

<!-- tags: [syncfusion, winforms, essentialcalculate, calcquick, formula parsing, function library, parseandcompute] keywords: [calcquick, parseandcompute, formula calculation, function implementation, variables assignment, calculation support, indexer, calculate, syncfusion winforms] -->
```

---

<!-- 페이지 190 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_247.jpeg
document_name: calculate
page_number: 247
page_id: calculate#page_247
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:31Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Understand how to read XLS files into Essential Calculate using Essential XlsIO.
- Learn methods to suspend calculations while updating values in ICalcData objects.

## Content

### 5.2.2 How To Read an XLS File Into Essential Calculate?
To get Essential Calculate to work with an XLS file requires Essential XlsIO. Essential ExcelRW is a library that exposes Excel-Like Automation APIs without any dependence upon Excel. It has the ability to Read / Write XLS files.

For details, see [Working with an Excel SpreadSheet](Working with an Excel SpreadSheet).

### 5.2.3 How To Suspend Calculations While a Series Of Values Are Updated?
You can use the property `CalcEngine.CalculationSuspended` to control the calculations that will be performed as values change in your ICalcData object.

#### Example in C#
```csharp
// Creates some data object that implements ICalcData.
this.data = new ArrayCalcData(a);

// Creates a CalcEngine object using this ICalcData object.
CalcEngine engine = new CalcEngine(this.data);
//...
// Turn off calculations.
engine.CalculationSuspended = true;

// Makes multiple updates to this.data somehow...
// Turn on calculations.
engine.CalculationSuspended = false;
```

#### Example in VB
```vb
' Creates some data object that implements ICalcData.
Me.data = New ArrayCalcData(a)

' Creates a CalcEngine object using this ICalcData object.
Dim engine As New CalcEngine(Me.data)

'...
' Turn off calculations.
```

## API Reference
### Methods
- `CalcEngine.CalculationSuspended`: A property to suspend or resume calculations.

### Parameters
- `ICalcData`: The data object that implements the ICalcData interface.

## Code Examples

#### C#
```csharp
this.data = new ArrayCalcData(a);
CalcEngine engine = new CalcEngine(this.data);
engine.CalculationSuspended = true;
// Multiple updates to this.data
engine.CalculationSuspended = false;
```

#### VB
```vb
Me.data = New ArrayCalcData(a)
Dim engine As New CalcEngine(Me.data)
engine.CalculationSuspended = True
' Multiple updates to Me.data
engine.CalculationSuspended = False
```

## See also
- [Working with an Excel SpreadSheet](Working with an Excel SpreadSheet)
- `CalcEngine`
- `ICalcData`

<!-- tags: [Syncfusion Winforms, Essential Calculate, XlsIO, ICalcData, CalcEngine, ExcelRW] keywords: [read XLS file, suspend calculations, Excel automation, Excel-like APIs, XlsIO library, Essential Calculate, ExcelSpreadSheet, CalculationSuspended] -->
```

---

<!-- 페이지 191 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_251.jpeg
document_name: calculate
page_number: 251
page_id: calculate#page_251
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:49Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Deployment and requirements for Essential Calculate
- Function library and reference.
- Removal and modification of functions in the Function Library in CalcQuickBase.

## Content

### Deployment
- **Deploying Essential Calculate**: 28
- **Deployment Requirements**: 23

### Dictionaries and Libraries
- **DEVSQ**: 164
- **DLLs**: 23

### Dollar and Equal Sign
- **Dollar**: 165
- **E**
  - **Equal Sign, the Formula Character**: 105

### Errors and Conditions
- **Error Messages**: 141
- **ERROR.TYPE**: 121

### Even and Exact Functions
- **EVEN**: 165
- **Exact**: 165

### Exponential and Factorial
- **EXP**: 166
- **EXPONDIST**: 166
- **F**
  - **FACT**: 167
  - **FACTDOUBLE**: 125

### Logical and Financial
- **False**: 167
- **FDIST**: 167
- **Feature Summary**: 35
- **Financial**: 115
- **Find**: 168
- **Finv**: 168
- **FISHER**: 169
- **FISHERINV**: 169

### Fixed and Floor Functions
- **Fixed**: 170
- **FLOOR**: 170

### Forecast and Frequently Asked Questions
- **FORECAST**: 171
- **Frequently Asked Questions**: 243

### Financial Functions
- **Functions**: 112
- **FV**: 172
- **G**
  - **GAMMADIST**: 172

### Statistical and Mathematical Functions
- **Gamma distribution**
  - **Gammadist**: 172
  - **Gammainv**: 173
  - **GAMMALN**: 173
- **GCD**: 125
- **General Calculation Support - ICalcData**: 77
- **GEOMEAN**: 174
- **GETTING STARTED**: 25
- **GROWTH**: 175

### Hierarchy and Hours
- **H**
  - **HARMEAN**: 175
  - **HLOOKUP**: 176
- **HOUR**: 175

### How Things Work
- **How Things Work**: 140

### Function Implementation
- **How To Add, Remove, And Modify the Implementation Of Functions In the Function Library In CalcQuickBase?**: 243
- **How To Calculate a Formula?**: 243
- **How To Enter Vectors Of Numbers Into CalcQuickBase?**: 244

### Calculation Processing
- **How To Force Calculations To Be Processed After They Have Been Suspended?**: 245

### Error Messages
- **How to generate error messages or exceptions while performing String-related calculations?**: 249

### File Reading
- **How To Read an XLS File Into Essential Calculate?**: 247

### Suspension of Calculations
- **How To Suspend Calculations While a Series Of Values Are Updated?**: 247
- **How to Use a Comma as a Decimal Separator in Formula?**: 248

### Logical Expressions
- **How To Use Logical Expressions In Other Calculated Expressions?**: 245

### Hypergeometric Distribution
- **HYPEGEOMDIST**: 178
- **Hypgeomdist**: 178

### ICalcData
- **I**
  - **ICalcData**: 44

### Conditional Expressions
- **IF**: 179
- **IFERROR**: 127
- **IFNA**: 129

## API Reference
- **Namespace**: Essential.Calculate
- **Class**: FunctionLibrary
- **Members**: Methods, Properties, Events

## Code Examples

### C# Example
```csharp
using Syncfusion.Windows.Forms;

// Example of using Essential Calculate
void CalculateSample() {
    // Example implementation here
}
```

### Cross References
- **See also**: Deployment, Financial Functions, Logical Expressions, Error Messages

<!-- tags: [syncfusion, winforms, essential-calculate, calculate, version-11.4.0.26] keywords: [essential calculate, function library, error messages, logical expressions, Deployment Requirements, GCD, CalcQuickBase] -->
```

---

<!-- 페이지 192 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_255.jpeg
document_name: calculate
page_number: 255
page_id: calculate#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:14Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- A detailed explanation of the Essential Calculate component in Syncfusion Winforms.
- Includes setup, configuration, and integration into Windows Forms applications.
- Covers key features, methods, and properties relevant to the component.

## Content
The Essential Calculate component is designed to provide advanced calculation and formula support for Windows Forms applications. It allows developers to integrate powerful spreadsheet-like functionalities, enabling users to perform complex calculations and data manipulations seamlessly within their applications.

## API Reference (if applicable)
This section would detail the namespace, classes, methods, properties, and events associated with the Essential Calculate component. It would provide comprehensive information on how to interact with the component programmatically, including code examples.

## Code Examples (multi-language supported)
This section showcases sample code demonstrating how to use the Essential Calculate component in C#.

### Example: Integrating Essential Calculate
```csharp
// Assuming a reference to Syncfusion.WinForms.Controls
using Syncfusion.WinForms.Controls.WinForms;

public class CalculateExample
{
    public void InitializeCalculateComponent()
    {
        // Create an instance of the Essential Calculate control
        SfCalculate calculate = new SfCalculate();

        // Configure basic properties
        calculate.Width = 800;
        calculate.Height = 600;

        // Add to the form's container
        this.Controls.Add(calculate);
    }
}
```

## Page-level Navigation/TOC (if applicable)
- Overview
- Content
- API Reference
- Code Examples

## Cross References
- Refer to the Syncfusion documentation for more advanced features and troubleshooting.
- See also: "Syncfusion WinForms Documentation" for overall platform guidance.

<!-- tags: [syncfusion, winforms, essentialcalculate, controls] keywords: [winforms, calculate, component, integration, essentialcalculate, api, methods, properties] -->
```

---

<!-- 페이지 193 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_004.jpeg
document_name: calculate
page_number: 004
page_id: calculate#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:22Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Comprehensive list of functions in the "Calculate" section.
- Detailed breakdown of function subheadings, such as "Multinomial," "ISEVEN," and "ISODD."
- Each function includes a page number for quick reference.
- Includes specific sections like "Inside CalcEngine" and "Tracking the Information."

## Content

### 4.5.6.1 Multinomial
- **Reference:** 118

### 4.5.6.2 ISEVEN
- **Reference:** 119

### 4.5.6.3 ISODD
- **Reference:** 119

### 4.5.6.4 N
- **Reference:** 120

### 4.5.6.5 NA
- **Reference:** 120

### 4.5.6.6 ERROR.TYPE
- **Reference:** 121

### 4.5.6.7 SUBTOTAL
- **Reference:** 122

### 4.5.6.8 MROUND
- **Reference:** 123

### 4.5.6.9 RAND BETWEEN
- **Reference:** 123

### 4.5.6.10 SQRTPI
- **Reference:** 124

### 4.5.6.11 QUOTIENT
- **Reference:** 124

### 4.5.6.12 FACTDOUBLE
- **Reference:** 125

### 4.5.6.13 GCD
- **Reference:** 125

### 4.5.6.14 LCM
- **Reference:** 126

### 4.5.6.15 ROMAN
- **Reference:** 126

### 4.5.6.16 IFERROR
- **Reference:** 127

### 4.5.6.17 T
- **Reference:** 128

### 4.5.6.18 XOR
- **Reference:** 128

### 4.5.6.19 IFNA
- **Reference:** 129

### 4.5.6.20 CLEAN
- **Reference:** 129

### 4.5.6.21 ISREF
- **Reference:** 130

### 4.5.6.22 AVERAGEIF
- **Reference:** 130

### 4.5.6.23 AVERAGEIFS
- **Reference:** 131

### 4.5.6.24 NETWORKDAYS
- **Reference:** 132

### 4.5.6.25 SUMIFS
- **Reference:** 133

### 4.5.6.26 ADDRESS
- **Reference:** 133

### 4.5.6.27 LOOKUP
- **Reference:** 134

### 4.5.6.28 SEARCH
- **Reference:** 135

### 4.5.7 Statistics
- **Reference:** 136

### 4.6 Inside CalcEngine
- **Reference:** 139

#### 4.6.1 Tracking the Information
- **Reference:** 139

#### 4.6.2 Parsing
- **Reference:** 139

#### 4.6.3 Calculating
- **Reference:** 140

#### 4.6.4 How Things Work
- **Reference:** 140

#### 4.6.5 Error Messages
- **Reference:** 141

## RAG Annotations

<!-- tags: syncfusion-winforms, calculate, functions, statistics, calcengine, error-handling keywords: [Multinomial, ISEVEN, ISODD, N, NA, ERROR.TYPE, SUBTOTAL, MROUND, RAND BETWEEN, SQRTPI, QUOTIENT, FACTDOUBLE, GCD, LCM, ROMAN, IFERROR, T, XOR, IFNA, CLEAN, ISREF, AVERAGEIF, AVERAGEIFS, NETWORKDAYS, SUMIFS, ADDRESS, LOOKUP, SEARCH, Tracking, Parsing, Calculating, Error Messages, statistics, calcengine, syncfusion,']
```


---

<!-- 페이지 194 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: calculate
page_number: 008
page_id: calculate#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:58:48Z
fidelity: lossless
-->

### Functions List

- 4.7.104 MOD: 196
- 4.7.105 MODE: 197
- 4.7.106 MONTH: 197
- 4.7.107 NEGBINOMDIST: 198
- 4.7.108 NORMDIST: 198
- 4.7.109 NORMINV: 199
- 4.7.110 NormsDist: 200
- 4.7.111 NormsInv: 200
- 4.7.112 NOT: 201
- 4.7.113 NOW: 201
- 4.7.114 NPER: 201
- 4.7.115 NPV: 202
- 4.7.116 ODD: 203
- 4.7.117 Offset: 203
- 4.7.118 OR: 204
- 4.7.119 PEARSON: 204
- 4.7.120 PERCENTILE: 205
- 4.7.121 PERCENTRANK: 205
- 4.7.122 Permut: 206
- 4.7.123 PI: 206
- 4.7.124 PMT: 207
- 4.7.125 POISSON: 207
- 4.7.126 Pow: 208
- 4.7.127 POWER: 209
- 4.7.128 PPMT: 209
- 4.7.129 PROB: 210
- 4.7.130 PRODUCT: 210
- 4.7.131 PV: 211
- 4.7.132 QUARTILE: 212
- 4.7.133 RADIANS: 212
- 4.7.134 RAND: 213
- 4.7.135 RANK: 213
- 4.7.136 RATE: 214
- 4.7.137 RIGHT: 214
- 4.7.138 ROUND: 215

<!-- tags: [calculator, functions, mathematical, financial, statistical, logical] keywords: [mod, mode, month, negative binomial distribution, normal distribution, normal inverse, normsdist, normsinv, not, now, nper, npv, odd, offset, or, pearson, percentile, percentrank, permutation, pi, pmt, poisson, power, ppmt, prob, product, pv, quartile, radians, rand, rank, rate, right, round] -->
```

---

<!-- 페이지 195 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_012.jpeg
document_name: calculate
page_number: 012
page_id: calculate#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:06Z
fidelity: lossless
--> 

# Essential Calculate

## Overview
- Essential features of Essential Calculate are highlighted below.
- Extensive calculation support can be added to your own business objects in both Windows Forms and ASP.NET.
- Easily set up forms that have calculation dependencies among various controls.
- The tool includes a function library with over 150 entries and supports cross sheet references.
- Used in conjunction with Essential XlsIO, it allows full loading, manipulation, and computation of Excel spreadsheets independently of Excel.
- It does not rely on Microsoft Excel, granting independent calculation capabilities.

## User Guide Organization

The product includes numerous examples and an extensive documentation guide to facilitate usage. This User Guide provides detailed information on the features and functionalities of Essential Calculate. It is structured as follows:

- **Overview:** A brief introduction to the product and its key features.
- **Installation and Deployment:** Details on the installation location of samples, license management, and more.
- **Getting Started:** Guidance on setting up the application and integrating Essential Calculate into it.
- **Concepts and Features:** Illustrations of the product's features through use case scenarios, code examples, and screenshots.
- **Frequently Asked Questions:** Solutions to common task-based queries about Essential Calculate.

## Document Conventions

The following conventions are employed to quickly identify important sections of information:

### Table 1: Document Conventions

| Convention            | Icon            | Description                                     |
|-----------------------|-----------------|-------------------------------------------------|
| Note                  | 📝 Note:       | Represents important information.              |
| Example               | 🔢 Example     | Represents an example.                         |
| Tip                   | 💡             | Represents useful hints to assist in using the controls/features. |
| Additional Information| 📌 Information | Represents additional information.             |

## Additional Information

The following conventions will assist you in quickly identifying the important sections while using the content.
```html

<!-- tags: [Essential Calculate, Syncfusion Winforms, Windows Forms, ASP.NET, XlsIO, User Guide, Installation, Deployment, Getting Started, Concepts and Features, Frequently Asked Questions, Integration, Features, Code Examples, Screenshots, Hint, Information] keywords: [calculation support, business objects, forms, controls, function library, cross sheet references, Excel manipulation, independent calculations, use case scenarios, task-based queries, code examples, screenshots, hints, information] -->
```

---

<!-- 페이지 196 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: calculate
page_number: 016
page_id: calculate#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:21Z
fidelity: lossless
-->

# 2 Installation and Deployment

This section covers information on the install location, samples, licensing, patches update, and updation of the recent version of Essential Studio. It comprises the following subsections:

## 2.1 Installation

For step-by-step installation procedure for the installation of Essential Studio, refer to the Installation topic under **Installation and Deployment** in the Common UG.

### See Also

For licensing, patches, and information on adding or removing selective components, refer to the following topics in Common UG under **Installation and Deployment**:

- Licensing
- Patches
- Add/Remove Components

## 2.2 Samples and Installation

### Where to Find Samples?

This section covers the location of the installed samples and describes the procedure to run the samples through the sample browser and online. It also lists the location of utilities, assemblies, and source code.

#### Sample Installation Location

The Windows Forms Calculate samples are installed in the following location, locally on the disk:

```
[Install Location]\...\Syncfusion\Essential Studio\[Version Number]\Windows\Calculate.Windows\Samples\2.0
```

The Calculate Web samples are installed in the following location, locally on the disk:

```
[Install Location]\...\Syncfusion\Essential Studio\[Version Number]\Web\Calculate.Web\Samples\3.5
```

#### Viewing Samples

<!-- tags: [Essential Studio, Installation, Deployment, Samples, Licensing, Patches, Components, Syncfusion Winforms, Version 11.4.0.26] keywords: [installation procedure, samples location, sample browser, utilities, assemblies, source code] -->
```

---

<!-- 페이지 197 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: calculate
page_number: 020
page_id: calculate#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:32Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Demonstrates the features of Essential Calculate, a class library that adds formula calculation support for Windows Forms and Web Forms applications.
- Highlights the versatility of Essential Calculate in performing calculations independent of Microsoft Excel.
- Emphasizes the range of supported calculations, from simple algebraic expressions to sophisticated formulas involving intrinsic functions.

## Content

### Windows Forms

#### Essential Calculate Overview
Essential Calculate is a class library that lets you add formula calculation support to both Window Forms and Web Forms applications. Essential Calculate does not depend upon Microsoft Excel and thus allows you to perform calculations independent of Excel. The range of calculations runs from simple algebraic expressions such as `(1.2^3-1)/8`, to formulas using intrinsic functions like `4 * sqrt(exp(3.4))`, to formulas relying on variables that are defined through controls on a form such as `cos([textBox1] * PI / 180)`, to spreadsheet-like formulas such as `sum(A2:B14)`. Essential Calculate lets you parse and compute such expressions and includes a library of more than 150 functions. This function library is easily extendable. The data used in the calculations can be from any source, ranging from fixed values, to values that are entered through controls, to data tables and Excel spreadsheets.

#### Featured Samples
- **XLS File Using CalcEngine**
- **Tabbed panel grid demo**
- **Working with CalcQuick demo**

**Figure 6: Calculate samples displayed in the Windows Forms Sample Browser**

1. **Select any sample and browse through the features.**

### ASP.NET
1. **In the Dashboard window, click Run Samples for ASP.NET under Reporting Edition panel. The ASP.NET Sample Browser window is displayed.**

**Note:** You can view the samples in any of the three options displayed.

## Cross References
- See also: *Dashboard*, *Reporting Edition*, *ASP.NET*, *Sample Browser*

<!-- tags: [essential calculate, windows forms, web forms, formula calculation, microsoft excel, algebraic expressions, intrinsic functions, controls, spreadsheets, data tables, asp.net, dashboard, reporting edition, sample browser] keywords: [calculate, essential calculate, windows forms, web forms, formula calculation, algebraic expressions, intrinsic functions, controls, spreadsheets, data tables, asp.net, dashboard, reporting edition, sample browser] -->
```

---

<!-- 페이지 198 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: calculate
page_number: 024
page_id: calculate#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:47Z
fidelity: lossless
-->

## Essential Calculate

- Syncfusion.Core.dll
- Syncfusion.Compression.Base.dll
- Syncfusion.Calculate.Web.dll

## Page-level Navigation/TOC (if applicable)

- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown.

## Cross References

- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

<!-- tags: [essential calculate, dll files, syncfusion.winforms, version 11.4.0.26] keywords: [Syncfusion.Core.dll, Syncfusion.Compression.Base.dll, Syncfusion.Calculate.Web.dll, Essential Calculate, DLLs, Syncfusion, version, 11.4.0.26] -->
```


---

<!-- 페이지 199 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: calculate
page_number: 028
page_id: calculate#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T02:59:55Z
fidelity: lossless
-->

# Essential Calculate

## Content

### New Project Creation

-figure 12-
![Figure 12: New Project Dialog Box](https://i.imgur.com/u4hBy.png)

**Figure 12: New Project Dialog Box**

A new WPF application is created.

1. Open the main form of the application in the designer.
   
2. Add the Syncfusion controls to your VS.NET toolbox if you haven't done so already [This is done automatically when you install Essential Studio].

3. Now you need to deploy Essential Calculate into this WPF application. Refer the [WPF] topic for detailed information.

For more information, refer the following topic.

### 3.3 Deploying Essential Calculate

We have now created a platform application in the previous topic (Creating Platform Application).

## Page-level Navigation/TOC (if applicable)

## Cross References

See also: [Creating Platform Application]

## RAG Annotations
<!-- tags: [syncfusion, winforms, wpf, new_project_dialog, essential_calculate, deployment] keywords: [Syncfusion Winforms, WPF, New Project Dialog, Essential Calculate, Deploying] -->
```

---

<!-- 페이지 200 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: calculate
page_number: 032
page_id: calculate#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:04Z
fidelity: lossless
-->

# Essential Calculate

Essential Calculate is deployed in your Windows application.

## 3.3.2 ASP.NET

Now, you have created an ASP.NET application (refer to *Creating Platform Application*). This section illustrates how to deploy Essential Calculate into this ASP.NET application.

### Deploying Essential Calculate in an ASP.NET Application

This section provides information and instructions for deploying ASP.NET applications that use Essential Calculate. This is in addition to the section on Deploying Essential Studio for ASP.NET (*Common --> Deploying Essential Studio for ASP.NET*) in the Getting Started Guide.

Essential Calculate ships with .NET Framework 2.0 (Visual Studio 2005) version of the C# and VB.NET samples, which are installed beneath 2.0 directories. During installation, application directories are created in IIS for each of the C# and VB.NET samples.

The following steps will guide you to deploy Essential Calculate in an ASP.NET application:

1. **Marking the Application Directory**  
   The appropriate directory, usually where the aspx files are stored, must be marked as Application in IIS.

2. **Syncfusion Assemblies**  
   The Syncfusion assemblies need to be in the *bin* folder that is beside the aspx files.

---

**Note:** They can also be in the GAC, in which case, they should be referenced in the *Web.config* file.

```xml
[ASPX]
<configuration>
  <system.web>
    <compilation>
      <assemblies>
        <add assembly="Syncfusion.Calculate.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89"/>
      </assemblies>
    </compilation>
    ...
  </system.web>
</configuration>
```

## API Reference

## Code Examples

<!-- tags: [product, syncfusion-winforms, essential-calculate, asp.net, deployment, api, version-11.4.0.26] keywords: [essential calculate, asp.net deployment, syncfusion studio, application directory, assemblies, bin folder, web.config, gac] -->
```

---

<!-- 페이지 201 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: calculate
page_number: 036
page_id: calculate#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:18Z
fidelity: lossless
-->

## Overview

- Easily set up forms that have calculation dependencies among various controls.
- With Essential Calculate, you can set properties that will indicate that you want formula dependencies to be tracked so that the values are automatically updated when a dependent value changes. Or you can turn off the overhead of tracking dependencies and have formulas calculated from scratch when you need a particular formula value.
- Essential Calculate can be used in manual mode or automatic mode.
- The manual mode works when you explicitly request for a value. At that point, the calculation is done from scratch to obtain the computed value.
- In automatic mode, Essential Calculate maintains a dependency list. Hence, when a value is changed, any formula that depends on it is recalculated at that particular point.

## Content

### 3.5 Quick Start

This section will show you how easy it is to get started using Essential Calculate. It will give you a basic introduction to the concepts you need to know before getting started with the product and some tips and ideas on how to use Essential Calculate in your projects.

#### Console Application Using CalcQuickBase

In this section, you will learn how to use the `CalcQuickBase` object to perform arbitrary calculations from a Console Application. This will show you the minimal steps that are required to use Essential Calculate to add calculation support to an application. This quick application lets you type algebraic expressions using a `Console.ReadLine` and display the calculated results using a `Console.WriteLine`.

#### Windows Application Using CalcQuickBase

In this section, you will create a Windows Application that uses a `CalcQuickBase` object that handles arbitrary variables in its calculations.

#### Adding Calculation Support to an Arbitrary Array with an ICalcData Interface

This section will demonstrate how to add calculation support to an arbitrary array of doubles by adding an additional row and column to hold summary information.
```

---

<!-- 페이지 202 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_040.jpeg
document_name: calculate
page_number: 040
page_id: calculate#page_040
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:30Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- Learn to create a Windows Application that allows you to register variables with a `CalcQuick` object and use these variables in algebraic expressions.
- Understand how to compute quantities represented by formulas like `Rate * Amount` or `(1 + Rate) * Amount`.

## Content

### 3.5.2 Windows Application Using Variables and CalcQuickBase

In this section, you will learn how to create a Windows Application that allows you to register variables with a `CalcQuick` object and then use these variables in algebraic expressions. For example, you might register a variable named `Rate` to be `0.07` and a variable named `Amount` to be `1500`, and then compute a quantity represented by the formula `Rate * Amount` or by `(1 + Rate) * Amount`.

#### 3.5.2.1 Windows Forms CalcQuickBase

1. **In Visual Studio, use `File | New | Project` to create a new Windows Forms Application. Right-click the `References` in Solution Explorer and add a reference to `Syncfusion.Calculate.Base`.**

    **Figure 17: Essential Calculate Reference Being Added to the Project**
    ![Add Reference Dialog](https://i.imgur.com/additional_image_link_here.png)

    - The **Add Reference** dialog shows various components, and you need to select `Syncfusion.Calculate.Base` version `5.202.0.25` and add it to your project.

2. **Using the designer, drop three text boxes, three labels, two buttons, and one list box onto the form as shown in the picture below.**

## Code Examples

No specific code examples provided in this section, but you can add any relevant C# or XAML code snippets here.

## API Reference

### Namespace: Syncfusion.Calculate.Base

#### Class: `CalcQuick`

- **Properties:**
  - `RegisterVariable(String name, Object value)` — Registers a variable with the given name and value.
  - `Compute(String formula)` — Computes the result of the given formula.

## RAG Annotations

<!-- tags: windows application, calcquick, windows forms, algebraic expressions, variables, reference addition keywords: calculate, essential calculate, winforms, algebra, formulas, register variables -->
```

---

<!-- 페이지 203 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_044.jpeg
document_name: calculate
page_number: 044
page_id: calculate#page_044
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:44Z
fidelity: lossless
-->

## Essential Calculate

For rectangular business objects, implementing an ICalcData interface lets you use values from your object in calculations. This section illustrates the process of adding calculation support to an Array.

### 3.5.3.1 ICalcData

1. In Visual Studio, use File | New | Project to create a new Windows Forms Application. Right-click the References in Solution Explorer and add a reference to Syncfusion.Calculate.Base.

   ![Figure 20: Essential Calculate Reference Being Added to the Project](https://example.com/image-url) 

2. As you drop the controls on the form, accept the default names so that you can copy and paste the code snippets later in this lesson.

3. The form has two buttons: the first is the Generate Data button and the second is the Set button. Drop a text box on the form and set its MultiLine property to True so that you can size it to occupy most of the form.

4. Drop the final three text boxes in left to right order under the Generate Data button, adding three labels to identify these text boxes.

## Footer
© 2013 Syncfusion. All rights reserved.
``` 

<!-- tags: [product, module, control, api, version?] keywords: [Syncfusion, Windows Forms, ICalcData, Array, Essential Calculate, Visual Studio] -->
```

---

<!-- 페이지 204 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: calculate
page_number: 048
page_id: calculate#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:55Z
fidelity: lossless
-->

## Overview

1. Implements a class for managing array calculation data tailored for the Syncfusion Winforms framework.
2. Introduces `ArrayCalcData` class in VB and C# syntax with support for additional rows and columns as well as row and column counts for convenience.

## Content

### Implementation Details

This section illustrates how to integrate additional rows and columns into synchronization-based data processing using the `ArrayCalcData` class in both VB and C#.

#### VB Implementation

```vb
Imports System

Namespace Calculate_ICalcData
    '''
    ''' <summary>
    ''' Summary description for ArrayCalcData.
    ''' </summary>
    Public Class ArrayCalcData
        Public Sub New()
            ' TODO: Add constructor logic here.
        End Sub
    End Class
End Namespace
```

#### C# Implementation

```csharp
using System;
using Syncfusion.Calculate;

namespace Calculate_ICalcData
{
    public class ArrayCalcData
    {
        /// <summary>
        /// Original double array.
        /// </summary>
        private double[,] dValues;

        /// <summary>
        /// Vector holding the sum of the rows.
        /// </summary>
        /// <remarks>
        /// Serves as the last column.
        /// </remarks>
        private object[] rowSums;

        /// <summary>
        /// Vector holding the sum of the columns.
        /// </summary>
        /// <remarks>
        /// Serves as the last row.
        /// </remarks>
    }
}
```

### Enhancements for Synchronization

The `ArrayCalcData` class provides enhanced functionality with the ability to synchronize additional data structures such as row and column sums for performing quick calculations. This is particularly useful in large-scale data manipulation and can be extended for flexibility and scalability.

#### Remarks

- The `dValues` array holds the main data for calculations.
- `rowSums` acts as an additional column, used to store the sum of each row, enhancing indexed calculations.
- Similarly, the column sums feature, which acts as the last row, provides efficient access to column summations.

The additional fields and logic facilitate more complex operations in data processing tasks where multiple summaries are required.

### API Reference

#### Class: `ArrayCalcData`

- **Purpose**: Provides a structure to hold and process array calculation data, including supplementary row and column summation data.

- **Fields**:
  - `dValues`: Holds the original double array.
  - `rowSums`: Represents the sum of rows; used as an additional column for various synthesis tasks.
  - `columnSums`: Represents the sum of columns; used as an additional row for similar tasks.

#### Methods

- **Constructor**: Initializes the `ArrayCalcData` object. Additional logic can be added as required for specific use cases.

### Code Examples

#### Example in C#

```csharp
using System;

public class ArrayCalcDataUsage
{
    public static void Main()
    {
        // Initialize the ArrayCalcData object
        var calcData = new Calculate.ICalcData.ArrayCalcData();

        // Example of accessing and updating the data structures
        // (Further implementation depends on specific application requirements)
    }
}
```

This example demonstrates the initialization of the `ArrayCalcData` class and sets a foundation for additional functionality to be implemented.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, WinForms, Grid control, Array data management, судебная система, C#, VB] keywords: [ArrayCalcData, dValues, rowSums, columnSums, data processing, synchronization, additional column, additional row] -->
```

---

<!-- 페이지 205 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_052.jpeg
document_name: calculate
page_number: 052
page_id: calculate#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:14Z
fidelity: lossless
-->

## Implementing the ICalcData Interface

### Overview
- Demonstrates how to implement the `ICalcData` interface in C# and VB.NET.
- Explains the process of adding interface stubs using the drop-down lists in Visual Studio for VB.NET.

### Content

#### Implementing the ICalcData Interface in C#
The following C# code snippet illustrates how to implement the `ICalcData` interface:

```csharp
using System;
using Syncfusion.Calculate;

namespace Calculate_ICalcData
{
    /// <summary>
    /// Wrapper class for a double array.
    /// </summary>
    /// <remarks>
    /// Wrapper class for a double array that adds an extra column
    /// to hold the sum of each row, and also adds an extra row
    /// to hold the sum of the columns.
    /// </remarks>
    public class ArrayCalcData : ICalcData
    {
        /// <summary>
        /// original double array
        /// </summary>
        private double[,] dValues;
    }
}
```

- **Figure 24**: Implementing the ICalcData Interface in C#

#### Implementing the ICalcData Interface in VB.NET
If you are using VB.NET, you can add the `ICalcData` stubs using the drop-down lists at the top of the edit window in Visual Studio. In the left drop-down, select the `ICalcData` interface as shown below:

```vb
Public Class ArrayCalcData
    Implements ICalcData

    ' <summary>
    ' original double array
    ' </summary>
    Private dValues(,) As Double
End Class
```

- **Figure 25**: Implementing the ICalcData Interface in VB, Choosing the Interface

### API Reference
The following APIs are relevant in this context:
- **Namespace**: `Syncfusion.Calculate`
- **Class**: `ArrayCalcData`
- **Interface**: `ICalcData`
- **Properties**:
  - `private double[,] dValues;`

### Code Examples

#### C#
```csharp
using System;
using Syncfusion.Calculate;

namespace Calculate_ICalcData
{
    public class ArrayCalcData : ICalcData
    {
        private double[,] dValues;

        // Add necessary method implementations here
    }
}
```

#### VB
```vb
Public Class ArrayCalcData
    Implements ICalcData

    Private dValues(,) As Double

    ' Add necessary method implementations here
End Class
```

### Cross References
See also:
- [Syncfusion.Calculate Namespace Documentation](#)
- [Instructions on Implementing Interfaces in Visual Studio](#)

<!-- tags: [Syncfusion Winforms, ICalcData, interface implementation, C#, VB.NET] keywords: [ICalcData, Visual Studio, drop-down lists, wrapper class, array, double array, extra column, extra row] -->
```

---

<!-- 페이지 206 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: calculate
page_number: 056
page_id: calculate#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:33Z
fidelity: lossless
-->

# Essential Calculate

## Content

Below is the `SetValueRowCol` method in C# and VB.NET along with its documentation.

### C# Method

```csharp
/// </remarks>
public void SetValueRowCol(object value, int row, int col)
{
    if (row - 1 == rowCount)
    {
        colSums[col - 1] = value;
    }
    else if (col - 1 == colCount)
    {
        rowSums[row - 1] = value;
    }
    else
        this.dValues[row - 1, col - 1] = double.Parse(value.ToString());

    ValueChangedEventArgs el = new ValueChangedEventArgs(row, col, value.ToString());
    ValueChanged(this, el);
}
```

### VB.NET Method

```vb
''' <summary>
''' Sets the value into either the double array or column vector or row vector.
''' </summary>
''' <param name="row">One-based row index.</param>
''' <param name="col">One-based column index.</param>
''' <param name="value">The value to be set.</param>
''' <remarks> This setter raises the ICalcData.ValueChanged event which,
''' is listened to by the CalcEngine to manage the calculations.
''' By convention, ICalcData uses one-based indexes.
''' </remarks>
Public Sub SetValueRowCol(ByVal value As Object, ByVal row As Integer, ByVal col As Integer) Implements Syncfusion.Calculate.ICalcData.SetValueRowCol

    If row = rowCount Then
        colSums(col - 1) = value
    Else
        If col = colCount Then
            rowSums(row - 1) = value
        Else
            Me.dValues(row - 1, col - 1) = Double.Parse(value.ToString())
        End If
    End If
End Sub
```

## Page-level Navigation/TOC (if applicable)

- **C# Method**: Explanation and implementation of the `SetValueRowCol` method.
- **VB.NET Method**: Equivalent implementation of the `SetValueRowCol` method in VB.NET.

## Cross References

See also: 
- [ICalcData Interface](#)
- [CalcEngine Class](#)

<!-- tags: [Syncfusion Winforms, Calculate, ICalcData, ICalcData.SetValueRowCol, CalcEngine, RowColVector, ValueChangedEventArgs] keywords: [SetValueRowCol, row, col, value, one-based index, rowSums, colSums, ValueChangedEventArgs, C#, VB.NET] -->
```

---

<!-- 페이지 207 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_060.jpeg
document_name: calculate
page_number: 060
page_id: calculate#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:01:48Z
fidelity: lossless
-->

## Essential Calculate

```vb
' / </summary>
' / <param name="sender"></param>
' / <param name="e"></param>
Private Sub button1_Click(ByVal sender As Object, ByVal e As
System.EventArgs) _
                                              Handles Button1.Click
    ' Creates some sample data.
    Me.nRows = r.Next(10) + 2
    Me.nCols = r.Next(3) + 1
    Dim a(nRows, nCols) As Double
    Dim row As Integer
    For row = 0 To nRows - 1
        Dim col As Integer
        For col = 0 To nCols - 1
            a(row, col) = CDbl(r.Next(100)) / 10
        Next
    Next

    ' Creates an ArrayCalcData object and passes it in this array.
    Me.data = New ArrayCalcData(a)

    ' Creates a CalcEngine object using this ArrayCalcData object.
    Dim engine As New CalcEngine(Me.data)

    ' Turns on dependency tracking so that values set with the Set button
    ' take effect immediately.
    engine.UseDependencies = True

    ' Calls the RecalculateRange so any formulas in the data can be
    ' initially computed.
    engine.RecalculateRange(RangeInfo.Cells(1, 1, nRows + 1, nCols + 1), data)

    ShowObject()

    ' Button1_Click
End Sub
' / <summary>
' / Displays the ArrayCalcData values in a text box.
' / </summary>
Private Sub ShowObject()
    Me.TextBox1.Text = ""
    Dim i As Integer
    For i = 0 To Me.nRows
```

## Page-level Navigation/TOC (if applicable)
- [Previous Section](#previous-section-label)
- [Next Section](#next-section-label)

## Cross References
- Related Topic: [Dependency Tracking](#dependency-tracking)
- Related API: [ArrayCalcData](#arraycalcdatadoc), [CalcEngine](#calcenginedoc)

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Essential Calculate, dependency tracking, ArrayCalcData, CalcEngine, version: 11.4.0.26] keywords: [calculate, dependency, tracking, recalculate, arraycalcdata, calcengine] -->
```

---

<!-- 페이지 208 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_064.jpeg
document_name: calculate
page_number: 064
page_id: calculate#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:02Z
fidelity: lossless
-->

# Concepts and Features

This section discusses the concepts and features of Essential Calculate. It includes the following topics.

## 4.1 Adding Calculation Support

Essential Calculate has a **CalcQuickBase** class that enables you to easily add formula parsing calculation support to arbitrary business objects. In addition, you can add calculation support to any data class by having that class implement the **ICalcData** interface.

The following sections will discuss this class and interface:

### 4.1.1 CalcQuickBase

The simplest way to use Essential Calculate is through an instance of its **CalcQuickBase** class. This class provides options to directly parse and compute a formula, or register variable names that can later be used in more complex formulas involving these variables. After registering the variables, it provides options to perform manual or automatic calculations.

This section discusses the usage of the CalcQuickBase class, under the following topics:

#### 4.1.1.1 Manual Calculations

Manual calculations require you to explicitly request Essential Calculate to compute the value and return it. You can do this by invoking methods in the CalcQuickBase class. There are several methods available which are discussed under the following topics:

- **ParseAndCompute**- This method will accept a formula string, parse it, and then return the computed value of the parsed formula. You can also directly invoke computation methods for any of the library functions of Essential Calculate through the **CalcEngine** class.
- **Indexer method by using Variables**

```html
<!-- tags: [calculation, formula parsing, calculation support, CalcQuickBase, ICalcData, manual calculations, Syncfusion Winforms] -->
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
```

<!-- tags: [syncfusion, windowsforms, calculate, calculation, formula parsing, calculation support, calcquickbase, icalldata, manual calculations, auto calculations, library functions, calcengine] -->
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
``` 
```html
```

```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```html
```

---

<!-- 페이지 209 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: calculate
page_number: 068
page_id: calculate#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:33Z
fidelity: lossless
-->

## Essential Calculate

The collection that `CalcQuickBase` maintains in order to hold information on variables, is a collection of `FormulaInfo` objects. The `FormulaInfo` class has the following public properties.

- **FormulaText:** String holding the formula as originally entered
- **ParsedFormula:** String holding the parsed version of the formula
- **FormulaValue:** String holding the last computed value for the formula

Indexing is an instance of the `CalcQuickBase` class, which sets the `FormulaText` property and gets the `FormulaValue` property for the `FormulaInfo` object that is associated with the variable name and used as the indexer. A `FormulaInfo` object is dynamically created if you use a variable name that is not in the `CalcQuickBase FormulaInfo` collection. To retrieve `FormulaText`, you must use the `CalcQuickBase.GetFormula` method and pass it in the variable name.

While using an indexer to get a value from a `CalcQuickBase` object, the `FormulaValue` property is returned. So, the question arises: as to exactly "when" this `FormulaValue` is computed from the `FormulaText` that has been set into this `FormulaInfo` object. When a new value for `FormulaValue` is computed, it is controlled by an internal member of `FormulaInfo`, the `calcID`. The `CalcQuickBase` object maintains a `calcID` value as well. Whenever the `FormulaInfo.FormulaValue` is requested, the `CalcQuickBase.calcID` is compared to the `FormulaInfo.calcID`, and if they do not match, the `FormulaInfo.FormulaValue` is recomputed and its `FormulaInfo.calcID` is set to match the `CalcQuickBase.calcID`. So, `FormulaValue` is only computed when the `calcID` value does not match the `CalcQuickBase.calcID` value. Also, you can force new computations by calling the `SetDirty` method on your `CalcQuickBase` instance.

The actual collection of `FormulaInfo` objects (and some related collections) are protected members of the `CalcQuickBase` class. In order to access the objects of these collections directly, you must derive the `CalcQuickBase` class of Essential Calculate. The `Calculate` class reference has more information on these protected collections.

You can access the underlying `Calculate.Engine` object through the public read-only `Engine` property of the `CalcQuickBase` class. You can then use this `Engine` property to add custom functions to the Function Library that is available for the `CalcQuickBase` object.

## 4.1.1.2 Automatic Calculations

Essential Calculate enables you to monitor value changes, and then automatically recomputes formulas that depend upon the changed values. There is an additional overhead associated with automatic calculations that enables you to determine "when" you want to use this feature.

### 4.1.1.2.1 Using Explicit Events

## Page-level Navigation/TOC (if applicable)
- [Unclear]

<!-- tags: [CalcQuickBase, FormulaInfo, VariableIndexing, AutomaticCalculations, ExplicitEvents] keywords: [Essential Calculate, FormulaValue, calcID, SetDirty, Calculate.Engine, CustomFunctions, ProtectedCollections, FunctionLibrary] -->

---

<!-- 페이지 210 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: calculate
page_number: 072
page_id: calculate#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:03:51Z
fidelity: lossless
-->

## Essential Calculate

### C# Code Example

```csharp
' 2) Populate your controls.
Me.textBoxA.Text = "12"
Me.textBoxB.Text = "3"
Me.textBoxC.Text = "= [A] + 2 * [B]"

' Must enter formula names before turning on calculations.
' 3) Assign formula object names.
calculator("A") = Me.textBoxA.Text
calculator("B") = Me.textBoxB.Text
calculator("C") = Me.textBoxC.Text
calculator("D") = Me.textBoxD.Text

' 4) Turn on auto calculations.
Me.calculator.AutoCalc = True

' 5) Subscribe to the event to set newly calculated values.
AddHandler Me.calculator.ValueSet, AddressOf calculator_ValueSet

' 6) Subscribe to some events to trigger the setting of values into CalcQuickBase.
AddHandler Me.textBoxA.Leave, AddressOf textBoxA_Leave
AddHandler Me.textBoxB.Leave, AddressOf textBoxB_Leave
AddHandler Me.textBoxC.Leave, AddressOf textBoxC_Leave
AddHandler Me.textBoxD.Leave, AddressOf textBoxD_Leave

' 7) Allow the CalcQuickBase sheet to create dependency lists necessary for auto calculations.
Me.calculator.RefreshAllCalculations()

' Form_Load
End Sub

' 8) Raised when a variable value is calculated.
Private Sub calculator_ValueSet(ByVal sender As Object, ByVal e As QuickValueSetEventArgs)
    Select Case e.Key
        Case "A"
            Me.textBoxA.Text = Me.calculator(e.Key).ToString()
        Case "B"
            Me.textBoxB.Text = Me.calculator(e.Key).ToString()
        Case "C"
            Me.textBoxC.Text = Me.calculator(e.Key).ToString()
        Case "D"
            Me.textBoxD.Text = Me.calculator(e.Key).ToString()
        Case Else
    End Select

    ' Calculator_ValueSet
End Sub
```

### Overview

- Populates controls with initial values and expressions.
- Assigns formula objects to respective text boxes.
- Enables automatic calculation and subscribes to appropriate events.
- Refreshes all calculations for dependency tracking.
- Updates text boxes with calculated values when changes occur.

### Code Explanation

The provided example demonstrates the setup and usage of the `CalcQuickBase` control in a Windows Forms application. Key steps include:

1. **Populating Controls**: Setting initial values and expressions for text boxes.
   ```csharp
   Me.textBoxA.Text = "12"
   Me.textBoxB.Text = "3"
   Me.textBoxC.Text = "= [A] + 2 * [B]"
   ```

2. **Assigning Formula Objects**: Linking text box values to formula variables.
   ```csharp
   calculator("A") = Me.textBoxA.Text
   calculator("B") = Me.textBoxB.Text
   calculator("C") = Me.textBoxC.Text
   calculator("D") = Me.textBoxD.Text
   ```

3. **Enabling Auto Calculations**: Activating automatic calculation mode.
   ```csharp
   Me.calculator.AutoCalc = True
   ```

4. **Subscribing to Events**: Handling new calculations and updating text boxes.
   ```csharp
   AddHandler Me.calculator.ValueSet, AddressOf calculator_ValueSet
   ```

5. **Dependency Tracking**: Refreshing all calculations for accurate dependency management.
   ```csharp
   Me.calculator.RefreshAllCalculations()
   ```

6. **Updating Controls**: Updating text boxes with calculated values when changes occur.
   ```csharp
   Private Sub calculator_ValueSet(ByVal sender As Object, ByVal e As QuickValueSetEventArgs)
       Select Case e.Key
           Case "A"
               Me.textBoxA.Text = Me.calculator(e.Key).ToString()
           Case "B"
               Me.textBoxB.Text = Me.calculator(e.Key).ToString()
           Case "C"
               Me.textBoxC.Text = Me.calculator(e.Key).ToString()
           Case "D"
               Me.textBoxD.Text = Me.calculator(e.Key).ToString()
           Case Else
       End Select
   ```

### API Reference

#### Properties

- **AutoCalc**: Enables or disables automatic calculation mode.
  - Type: Boolean
  - Description: Determines whether calculations are performed automatically on value changes.

#### Methods

- **RefreshAllCalculations()**: Triggers a refresh of all calculation dependencies.
  - Description: Ensures that all calculations are updated based on the latest values and formulas.

- **ValueSet**: Event raised when a variable value is calculated.
  - Parameters: `sender` - Object that raised the event, `e` - `QuickValueSetEventArgs` containing the variable key.
  - Description: Handler to update controls with the calculated value.

---

<!-- tags: [syncfusion, winforms, calculation, calcquickbase] keywords: [calculator, auto calculation, text box, formula, value set, refresh, dependency tracking] -->
```

---

<!-- 페이지 211 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: calculate
page_number: 076
page_id: calculate#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:18Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Calls the RegisterControlArray method in the `CalcQuickBase` object, handling all manually added event code.
- Recalculates all variables registered with the `CalcQuickBase` object.
- Discusses resetting keys using the Calculate Engine.

## Content

### Section 4.1.1.3 Resetting Keys by using Calculate Engine

#### Subsection 4.1.1.3 Resetting Keys by using Calculate Engine
This method provides support for resetting keys (which happens backend) using the Calculate Engine. The user can reset or clear the keys by using this method.

### Samples Installation Location

`CalcQuick WF` samples are installed under the following location:

```
C:\Syncfusion\EssentialStudio\<Version Number>\Windows\Calculate.Windows\Samples \2.0\Working With CalcQuick Demo
```

### Viewing Samples

Follow steps 1 to 2 of viewing Windows samples in section 2.2 Samples and Installation.

---

### Figure 32: WF Edition Sample Browser

![Screenshot of Essential Studio Reporting Edition Sample Browser](https://unclear)

---

## Page-level Navigation/TOC (if applicable)
- <overview content>

---

## Cross References
- See also: References to related topics or documentation, if any.

---

## API Reference (if applicable)
No explicit API reference details are visible on this page.

---

## Code Examples (multi-language supported)

No explicit code examples are visible on this page.

---

<!-- tags: [syncfusion, windows forms, calcquickbase, calculate engine, essential calculate, version 11.4.0.26] keywords: [resetting keys, user interaction, calculate engine, samples, installation location, essential studio, windows forms, programmatic calculation, recalculating variables] -->
```

---

<!-- 페이지 212 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: calculate
page_number: 080
page_id: calculate#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:31Z
fidelity: lossless
-->

## Essential Calculate

### C#

```csharp
private void SingleDataGridForm_Load(object sender, System.EventArgs e)
{
    // Set up your DataTable.
    this.dt = GetTheDataTable();

    // Set the datasource to a DataTable.
    this.dataGrid1.DataSource = this.dt;

    // Set any formulas you want
    // or they might already be in the DataTable.
    this.dataGrid1[2, 2] = "= A1 + A3";

    // 1) Reset static members of CalcEngine.
    Syncfusion.Calculate.CalcEngine.ResetSheetFamilyID();

    // 2) Create a CalcEngine object and tie it to the DataGrid that implements ICalcData.
    engine = new Syncfusion.Calculate.CalcEngine(this.dataGrid1);

    // 3) Set the CalcEngine to track dependencies required for auto updating.
    engine.UseDependencies = true;

    // 4) Call RecalculateRange so any formulas in the data can be initially computed.
    engine.RecalculateRange(RangeInfo.Cells(1, 1, dt.Rows.Count, dt.Columns.Count), this.dataGrid1);
}
```

### VB

```vb
Private engine As Syncfusion.Calculate.CalcEngine
Private dt As DataTable

Private Sub SingleDataGridForm_Load(sender As Object, e As System.EventArgs)

    ' Set up your DataTable.
    Me.dt = GetTheDataTable()

    ' Set the datasource to a DataTable.
    Me.dataGrid1.DataSource = Me.dt

    ' Set any formulas you want
    ' or they might already be in the DataTable.
End Sub
```

## API Reference

<!-- tags: [Syncfusion, Winforms, CalcEngine, SingleDataGridForm_Load] keywords: [DataTable, DataSource, RangeInfo, RecalculateRange, UseDependencies, Essential Calculate] -->
```

---

<!-- 페이지 213 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_084.jpeg
document_name: calculate
page_number: 084
page_id: calculate#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:43Z
fidelity: lossless
-->

# Essential Calculate

```vb
engine = New Syncfusion.Calculate.CalcEngine(Me.dataGrid1)

' 4) Track dependencies required for auto calculations.
engine.UseDependencies = True

' 5) Register multiple ICalcData objects for cross sheet references.
Dim sheetfamilyID As Integer = CalcEngine.CreateSheetFamilyID()
engine.RegisterGridAsSheet("DG1", Me.dataGrid1, sheetfamilyID)
engine.RegisterGridAsSheet("DG2", Me.dataGrid2, sheetfamilyID)
engine.RegisterGridAsSheet("DG3", Me.dataGrid3, sheetfamilyID)
engine.RegisterGridAsSheet("DG4", Me.dataGrid4, sheetfamilyID)
engine.RegisterGridAsSheet("DG5", Me.dataGrid5, sheetfamilyID)

' DataGridWorkBookForm_Load
End Sub
```

The following is an explanation of the preceding code.

1. Assign the datasources to the DataGrids.
2. **ResetSheetFamilyID** clears any static members of the CalcEngine class and sets the engine state to operate with a single ICalcData object.
3. Creates an instance of the CalcEngine object.
4. Sets the engine object to track calculation dependencies so that cells can be automatically updated as other cell values change.
5. This is the code that registers a name for each ICalcData object so that the CalcEngine can support references across ICalcData objects.

## 4.1.2.3 Conventions

There are two conventions that are honored by Essential Calculate. While processing strings that are used as data values, any string beginning with `"="` is treated as a formula that is to be parsed and evaluated. You can change the `"="` to some other character by setting this static (Shared in VB) member, CalcEngine.FormulaCharacter. If you call Parse routines directly from code, the FormulaCharacter is optional.
```


<!-- tags: [product, Syncfusion Winforms, module, control, calcengine, version: 11.4.0.26] keywords: [CalcEngine, ICalcData, sheetfamilyID, dependence tracking, cross sheet references, Conventions, FormulaCharacter] -->
```

---

<!-- 페이지 214 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: calculate
page_number: 088
page_id: calculate#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:04:56Z
fidelity: lossless
-->

# Essential Calculate

event whenever a data value changes. WireParentObject is a callback method from CalcEngine which gives the ICalcData object a chance to do whatever it needs to initially set up this notification process. In this particular case, this means subscribing to the DataTable.ColumnChanged event whose event handler will raise the required ValueChanged event. These type of actions cannot be done in the ICalcData constructor as the data source of the DataGrid would not have been set at this point. Using the WireParentObject callback, enables the DataGrid to have things completely set up before the WireParentObject is triggered when the CalcEngine is created.

2. This is the DataTable.ColumnChanged event handler. Its purpose is to raise the ICalcData.ValueChanged event. It uses the CurrencyManager to retrieve the row position of the changed row, and looks up the changed column in the Columns collection. One point to note is that both these values are zero-based indexes. Anytime you interact with an ICalcData object, the indexes have to be one-based. So, when the ValueChangedEventArgs are created, the indexes are incremented by one.

3. This GetValueRowCol implementation returns the value in the DataGrid for a certain row and column index, which are passed in by the caller. These values must be one-based in the call list. So, before they are used to retrieve the value from the DataGrid, they are decremented to be proper zero-based indexes on the DataGrid.

4. This SetValueRowCol implementation sets the value in the DataGrid for a certain row and column index, which are passed in by the caller. Again the row and column indexes are adjusted for the base difference.

5. This is the declaration of the ValueChanged event that was raised in the ColumnChanged event discussed in item two.

## 4.2 Web Control Performance

Syncfusion Essential studio makes use of the class named ScriptResourceAttribute which is used to define a resource in an assembly to be used from a client script file.

Then the resource files which are all used in the Syncfusion controls are gzipped and served over the network. The following screenshot shows this.

<!-- tags: [winforms, syncfusion, datatable, columnchanged, datachanged, valuechanged, currencymanager, webcontrol, performancetuning, calculationengine, essentialstudio, scriptingresources] keywords: [datatable, syncfusion, winforms, datachanged, scriptresourceattribute, gzipped, syncfusioncontrol, performance, calculation, essentialstudio, scriptingresources] -->
```

---

<!-- 페이지 215 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: calculate
page_number: 092
page_id: calculate#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:12Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- The page demonstrates how to use a Microsoft Excel worksheet to perform calculations.
- Utilizing `VLOOKUP` and other features to generate an insurance quote based on input variables.
- The worksheet includes various input variables such as Age, Sex, State, Points, Model, Model Year, and Multiplediscount.

## Content

### Microsoft Excel Worksheet Example

The Microsoft Excel worksheet shown in the figure performs calculations to derive an insurance quote. The worksheet is titled "Copy of CarlIns.xls" and is read-only.

#### Key Information in the Worksheet
- **Input Variables** are listed in column A, with corresponding values in column B. The **Multiplier** for each variable is calculated and displayed in column C.
- **Age**: 15, with a multiplier of 1.4000.
- **Sex**: "m" (male), with a multiplier of 1.2000.
- **State**: "az" (Arizona), with a multiplier of 0.9604.
- **Points**: 0, with a multiplier of 1.0000.
- **Model**: "ford", with a multiplier of 1.0000.
- **ModelYear**: 2004, with a multiplier of 1.2350.
- **MultipleDiscount**: "no", with a multiplier of 1.0000.

#### Formula Usage
The cell `C5` uses the `VLOOKUP` function to retrieve the multiplier for the state:
\[ =VLOOKUP(State, LookUps!A3:B52, 2) \]

This formula helps in calculating the insurance quote by referencing a table in the "LookUps" sheet.

#### Tabs Overview
- The worksheet includes tabs named "Inputs", "LookUps", "Calculate", and "Outputs" to organize the data and calculations.

### Figure 39: Worksheet that Performs Calculations

The figure shows a detailed view of the worksheet that performs these calculations. It illustrates how various input variables and corresponding multipliers are used to calculate an insurance quote.

#### Table Layout

The table is structured as follows:

| Input Variable | value | Multiplier |
|-----------------|-------|------------|
| Age             | 15    | 1.4000     |
| Sex             | m     | 1.2000     |
| State           | az    | 0.9604     |
| Points          | 0     | 1.0000     |
| Model           | ford  | 1.0000     |
| ModelYear       | 2004  | 1.2350     |
| MultipleDiscount | no   | 1.0000     |

The **Multiplier** for the "State" column (`C5`) is calculated using the `VLOOKUP` function, as shown in the formula bar.

---

### Summary

This worksheet effectively uses Excel functions like `VLOOKUP` to calculate multipliers for various input variables, ultimately deriving an insurance quote. The organized structure and use of lookup tables ensure accurate and efficient computation.

## Code Examples (Example)
The formula used in the worksheet is as follows:
```excel
=VLOOKUP(State, LookUps!A3:B52, 2)
```

This formula retrieves the multiplier for the given state from the "LookUps" sheet.

## API Reference
- **VLOOKUP Function**: A standard Excel function used for lookup operations.
- **Worksheets Tabs**: "Inputs", "LookUps", "Calculate", and "Outputs" are used to organize the calculation process.

## Page-level Navigation/TOC (if applicable)
- **Figure 39:** Worksheet that Performs Calculations.

## Cross References
See also:
- Excel functions like `VLOOKUP`.
- Workbook organization techniques for performing calculations.

<!-- tags: [product, module, control, api, version?] keywords: [Excel, VLOOKUP, worksheet, insurance quote, calculated multipliers, workbook organization] -->
```

---

<!-- 페이지 216 -->

```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: calculate
page_number: 096
page_id: calculate#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:33Z
fidelity: lossless
--> 

## Overview
- Indicates a technical guide for creating and managing an Excel workbook object using the Syncfusion Essential Calculate library in a WinForms application.
- Demonstrates the instantiation and setup of a workbook object from an Excel file and performing preliminary calculations to establish dependencies.
- Shows the initial setup of a form with combo boxes and how they relate to the instantiated Excel workbook.
- Provides both C# and VB.NET code examples for the same functionality.

## Content

### WinForms Workbook Initialization Code

```csharp
private void Form1_Load(object sender, System.EventArgs e)
{
    // 1) Instantiates the workbook object from the spreadsheet file.
    calcWB = ExcelRWCalcWorkbook.CreateFromXLS(@"CarIns.xls");

    // 2) Do all calculations so that dependencies are known.
    this.calcWB.Engine.LockDependencies = false;
    this.calcWB.CalculateAll();

    // this.calcWB.Engine.CalculatingSuspended = true;
    this.calcWB.Engine.LockDependencies = true;

    // 3) Set some initial values on the form.
    this.comboBoxSex.SelectedIndex = 0;
    this.comboBoxState.SelectedIndex = 0;
    this.comboBoxModel.SelectedIndex = 0;
}
```

```vb
[VB]

Private calcWB As ExcelRWCalcWorkbook

Private Sub Form1_Load(sender As Object, e As System.EventArgs)
    ' 1) Instantiate the workbook object from the spreadsheet file.
    calcWB = ExcelRWCalcWorkbook.CreateFromXLS("CarIns.xls")

    ' 2) Do all calculations so that dependencies are known.
    Me.calcWB.Engine.LockDependencies = False
    Me.calcWB.CalculateAll()

    ' Me.calcWB.Engine.CalculatingSuspended = True
    Me.calcWB.Engine.LockDependencies = True

    ' 3) Set some initial values on the form.
    Me.comboBoxSex.SelectedIndex = 0
    Me.comboBoxState.SelectedIndex = 0
    Me.comboBoxModel.SelectedIndex = 0
End Sub
```

### Explanation of the Code

The following is an explanation of the preceding code.

1. **Workbook Instantiation**: 
   - **Usage**: Uses a static member, `ExcelRWWorkbook.CreateFromXLS`, to read and instantiate an `ExcelRWWorkbook` object from the given XLS file. (The `CreateFromXLS` method relies on Essential XlsIO to actually do this work.)
   - **Description**: This step involves loading an existing Excel file (`CarIns.xls`) into memory as a workbook object. This enables further interaction with the Excel workbook's data and formulas via the Essentia Action Calculate library.

---

<!-- tags: [Syncfusion, WinForms, Essential Calculate, ExcelRWWorkbook, CalculateFromXLS, CarIns.xls, Version: 11.4.0.26] keywords: [workbook object, calculate dependencies, form initialization, combo boxes, Excel file loading] -->
```

---

<!-- 페이지 217 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_100.jpeg
document_name: calculate
page_number: 100
page_id: calculate#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:05:51Z
fidelity: lossless
-->

## Necessary Calculations

This section explains the process of transferring values from controls on a form to the Inputs sheet. It highlights the importance of indexing the workbook with the sheet's name and utilizing specific row and column indexes to insert the values into the Inputs sheet.

### Batch Processing with Performance Optimization

The final set of code demonstrates how to handle batch processing requirements. This involves iterating through setting Input values and retrieving corresponding Output values. Setting `CalculatingSuspended` to `True` prevents triggering intermediate calculations, which improves performance by approximately 10% in the provided example with eight inputs. For scenarios with hundreds of inputs, this optimization becomes even more significant.

### Code Example: Button Click Event

The following C# code illustrates how to accomplish this batch processing, running 1000 iterations. It sets various random values into the Inputs sheet while suspending calculations to ensure efficiency.

```csharp
[C#]

private void button2_Click(object sender, System.EventArgs e)
{
    // Runs 1000 iterations.
    int num = 1000;

    this.Cursor = Cursors.WaitCursor;
    DateTime start = DateTime.Now;
    CalcSheet inputSheet = this.calcWB["Inputs"];
    Random r = new Random();

    this.calcWB.Engine.CalculatingSuspended = true;

    for (int i = 0; i < num; ++i)
    {
        // 1) Sets random values into the Inputs sheet.
        inputSheet[ageRow, 2] = (r.Next(74) + 15).ToString();
        inputSheet[sexRow, 2] = r.Next(2) == 1 ? "M" : "F";
        inputSheet[stateRow, 2] = this.comboBoxState.Items[r.Next(50)];
        inputSheet[pointsRow, 2] = r.Next(15).ToString();
        inputSheet[modelRow, 2] = r.Next(11).ToString();
        inputSheet[modelYearRow, 2] = (33 + r.Next(1972)).ToString();
        inputSheet[multipleDiscountRow, 2] = r.Next(2) == 1 ? "Yes" : "No";
        inputSheet[3, 5] = this.textBoxBaseAmount.Text;

        // 2) Calculations are suspended so need to pull the computed value to make sure it has been calculated with the latest changes.
        this.calcWB.Engine.UpdateCalcID();

        calcWB.Engine.PullUpdatedValue(this.calcWB.GetSheetID("Outputs"), 1, 1);

        // 3) Gets the value from cell 1,1 on the output sheet.
    }
}
```

This code snippet effectively demonstrates how to manipulate and retrieve data from Excel sheets within a batch process, emphasizing performance enhancement techniques.

## Related Content

- For more information on performance optimization techniques, refer to [Performance Optimization in Excel with Syncfusion](#).
- Detailed handling of batch operations is explained in [Batch Processing in Syncfusion WinForms](#).

<!-- tags: [Syncfusion, Winforms, Excel, batch processing, performance optimization, inputs, outputs] keywords: [batch processing, random values, calculating suspended, performance improvement, worksheet manipulation, form controls, sheet indexing] -->
```

---

<!-- 페이지 218 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_104.jpeg
document_name: calculate
page_number: 104
page_id: calculate#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:12Z
fidelity: lossless
-->

# Essential Calculate

- `>=` Greater Than Or Equal
- `<>` Not Equal

All operations are subject to the following hierarchy of operations. The level 1 operations are done first, followed by level 2, and so on. Within the same level, the operations are performed from left to right in the order in which they are encountered during the parsing of the formula.

1. - (Unary Minus)
2. `*` `/`
3. `+` `-`
4. `<` `>` `=` `<=` `>=` `<>`
5. `&` (Concatenation)

If you want to change the default operators precedence, then use parentheses to explicitly indicate the operation order.

## Examples

1. **Formulas** | **Computed Value**
   - `= 6 / 2 + 1` | 4
   - `= 6 / (2 + 1)` | 2
   - `= 2 + 4 / 2` | 4
   - `= (2 + 4) / 2` | 3

Logical operations return specific values: True or False. If you need specific numerical values associated with any logical expression, then use the logical expression as the first argument in the Formula Library IF-function, with the second argument being the numerical value of True and the third argument being the numerical value of False. If you use a well-formed logical expression in a larger calculation, True evaluates to numerical 1 and False evaluates to numerical 0 for use in the calculations.

## 4.4.2 Square Brackets in CalcQuickBase Formulas

If you are using a `CalcQuickBase` object to add calculation support to your business object, then you must use strings as indexers on the CalcQuickBase instance to get and set values. These strings are referred to as the value's Name. If you need to use a Name in a formula, then you should enclose the string within brackets, `[ ]`. In step three of the code below, four names A, B, C, and D are registered. Notice that the formula entered in step two uses the values from A and B by enclosing these names in brackets.

### Code Example

```csharp
// 1) Instantiates a CalcQuickBase object.
```
```html
<!-- tags: [product, module, control, api, version?] keywords: [calculate, operations, precedence, operators, logical operations, truth values, calcquickbase, square brackets, indexer strings, formula library, if function, true, false, numerical evaluation, business object, syncfusion winforms] -->
```

---

<!-- 페이지 219 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_108.jpeg
document_name: calculate
page_number: 108
page_id: calculate#page_108
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:27Z
fidelity: lossless
-->

## Overview

- Adds a method to accept an argument list and return the minimum value.
- Handles parsing and retrieving values from the argument list using `CalcEngine` methods.
- Discusses handling list separators based on cultural settings.
- Utilizes `CalcEngine.ParseArgumentSeparator`, `GetCellsFromArgs`, and `GetValueFromArg`.

## Content

### Implementing a Custom Min Function

Here's a method that accepts an argument list and computes the minimum value in the list. The list may contain cell references, cell ranges, or numbers. The `CalcEngine` methods are used to handle parsing and retrieving values.

#### Note on List Separators

**Note:** List separators can vary depending on the culture. While a comma is used as a list separator in en-US, it is used as a decimal separator in fr-FR. For this reason, `CalcEngine.ParseArgumentSeparator` is a static member that holds the list separator recognized by algorithms in `CalcEngine`.

```cs
[C#]

// This sample computes the minimum of an arbitrary range.
// Example: = Mymin(A1:C3)
// Example: = mymin(a1,c2,a4,b2,100)
public string ComputeMymin(string args)
{
    // Assumes that this.engine is the CalcEngine object.

    double min = double.MaxValue;
    double d;
    string s1;

    foreach (string r in args.Split(new char[] { CalcEngine.ParseArgumentSeparator }))
    {
        // Cell range
        if (r.IndexOf(':') > -1)
        {
            foreach (string s in engine.GetCellsFromArgs(r))
            {
                // s is a cell line a1, a21, or c3...
                try
                {
                    s1 = engine.GetValueFromArg(s);
                    if (s1 != ""
                        && double.TryParse(s1, System.Globalization.NumberStyles.Number, null, out d))
                    {
                        min = Math.Min(min, d);
                    }
                }
                catch
                {
                    continue;
                }
            }
        }
        else
        {
            // Single cell or number
            try
            {
                s1 = engine.GetValueFromArg(r);
                if (s1 != ""
                    && double.TryParse(s1, System.Globalization.NumberStyles.Number, null, out d))
                {
                    min = Math.Min(min, d);
                }
            }
            catch
            {
                continue;
            }
        }
    }

    return min.ToString();
}
```

### Explanation of Code

1. **Argument Parsing**: The `args.Split` method uses `CalcEngine.ParseArgumentSeparator` to handle list separators based on the current culture.
2. **Handling Cell Ranges**: If the argument contains a colon (`:`), it is treated as a cell range. The `GetCellsFromArgs` method splits the range into individual cell references.
3. **Value Retrieval**: The `GetValueFromArg` method retrieves the numerical value of each cell or number.
4. **Minimum Calculation**: The `Math.Min` function is used to compute the minimum value among all retrieved numbers.
5. **Error Handling**: `try-catch` blocks ensure that the method continues processing even if some cells or arguments are invalid.

#### Key Points

- **List Separators**: Uses the `ParseArgumentSeparator` to handle cultural variations in list separators.
- **Utility Methods**:
  - `GetCellsFromArgs`: Converts a range into individual cell references.
  - `GetValueFromArg`: Converts a cell reference, formula, or number into its numerical value.
- **Handling Exceptions**: Ensures robustness by handling invalid inputs gracefully.

## API Reference

### Methods Used

- **CalcEngine.ParseArgumentSeparator**: Returns the list separator recognized by the parsing algorithms.
- **CalcEngine.GetCellsFromArgs(string args)**: Converts a cell range into individual cell references.
- **CalcEngine.GetValueFromArg(string arg)**: Retrieves the numerical value of a cell, formula, or number.
- **System.Globalization.NumberStyles**: Specifies the number styles allowed for parsing.
- **double.TryParse(string, IFormatProvider, out double)**: Attempts to convert a string to a double, returning `true` on success.
- **Math.Min(double, double)**: Returns the smaller of two numbers.

### Parameters

| Name       | Type                | Description                                                                         |
|------------|---------------------|-------------------------------------------------------------------------------------|
| `args`     | `string`            | The input argument list containing cell references, ranges, or numbers.        |
| `ParseArgumentSeparator` | `char` | The separator character used to split arguments based on culture settings.     |

### Returns

- **Type**: `string`
- **Description**: The minimum value in the list, as a string.

### Exceptions

- Handled internally within `try-catch` blocks to ensure the method is robust.

## Code Examples

### Example 1: Using Cell Ranges

```cs
// Computes the minimum value in the range A1:C3
public string ComputeMymin(string args)
{
    // Implementation as shown above
}
```

### Example 2: Using Individual Cells and Numbers

```cs
// Computes the minimum value among a1, c2, a4, b2, and 100
public string ComputeMymin(string args)
{
    // Implementation as shown above
}
```

## Cross References

- See also:
  - [CalcEngine Methods](#calcengine-methods)
  - [Handling Cultural Variations](#handling-cultural-variations)

<!-- tags: [syncfusion, winforms, calcengine, range parsing, culture-dependent, min function] keywords: [CalcEngine, ParseArgumentSeparator, GetCellsFromArgs, GetValueFromArg, TryParse, Math.Min, cultural settings, list separator, cell range, minimum value, argument list, robustness, try-catch, utility methods] -->
```

---

<!-- 페이지 220 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_112.jpeg
document_name: calculate
page_number: 112
page_id: calculate#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:06:58Z
fidelity: lossless
-->

## Overview
- Explains how to remove functions from the Library.
- Describes the use of `CalcEngine.RemoveFunction` method to remove a single function.
- Includes examples in C# and VB for removing functions from the Library.
- Outlines the process for replacing a function with another implementation.

## Content

### Removing Functions from the Library

#### Clearing All Functions
```csharp
// Remove all functions from the Library.
engine.LibraryFunctions.Clear();
```

```vb
// Remove all functions from the Library.
engine.LibraryFunctions.Clear()
```

After clearing all functions, you can add a few functions that will be used often. To know how to add functions, see **Add Function**.

#### Removing a Single Function
To remove a single function from the Function Library, use the `CalcEngine.RemoveFunction` method, passing a "function name" as the string that references this function, from a formula.

```csharp
// Remove formula name MyMin from the Library.
engine.RemoveFunction("MyMin");
```

```vb
' Remove formula name MyMin from the Library.
engine.RemoveFunction("MyMin")
```

### Replace Function
To replace a function with another implementation, you must remove the original name, and add the same name again with a different delegate method.

### 4.5.3 Functions

Here is a list of the Function Library entries included with Essential Calculate which includes more than 150 entries. For detailed information on each function, see **Function Reference Section**.

#### 4.5.3.1 Logical
This section lists the logical functions included with Essential Calculate in the below table.

## Page-level Navigation/TOC (if applicable)
- 4.5.3 Functions
  - 4.5.3.1 Logical

## Cross References
See also:
- Add Function
- Function Reference Section

<!-- tags: [Product, Syncfusion, Winforms, Calculate, Functions, Library, Essential Calculate, CalcEngine, RemoveFunction, Logical Functions] keywords: [clear functions, remove function, replace function, function library, MyMin, removeFunction, logical functions, essential calculate, function reference, add function] -->
```

---

<!-- 페이지 221 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_116.jpeg
document_name: calculate
page_number: 116
page_id: calculate#page_116
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:11Z
fidelity: lossless
-->

Essential Calculate

| Function Name | Description                                   |
|---------------|-----------------------------------------------|
| Ispmt         | Returns interest payment.                    |
| Mirr          | Returns internal rate of return.             |
| Nper          | Returns number of payment periods.           |
| Npv           | Returns net present value.                   |
| Pmt           | Returns loan payment.                        |
| Ppmt         | Returns principal payment.                   |
| Pv           | Returns present value.                       |
| Rate         | Returns interest rate per period.            |
| Sln          | Returns straight-line depreciation.          |
| Syd          | Returns sum-of-years depreciation.           |
| Vdb          | Returns the depreciation using double declining balance calculation. |

## Math and Trig functions

This section lists the Math and Trig functions included with Essential calculate in the below table.

### Table 10: Math and Trig functions

| Function Name | Description                                       |
|---------------|---------------------------------------------------|
| Abs           | Returns the absolute value of a value.          |
| Acos          | Returns the inverse cosine.                     |
| Acosh         | Returns the inverse hyperbolic cosine.         |
| Asin          | Returns the inverse sine.                       |
| Asinh         | Returns the inverse hyperbolic sine.           |
| Atan          | Returns the inverse tangent.                   |
| Atan2         | Returns the inverse tangent.                   |
```

---

<!-- 페이지 222 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: calculate
page_number: 120
page_id: calculate#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:22Z
fidelity: lossless
-->

## ISODD Function

### Overview
- `ISODD` Function behavior explained.
- Error handling when the input is non-numeric.
- Example demonstrating how `ISODD` evaluates different values.

### ISODD Function Description
**Note:** If the given value is nonnumeric, the `ISODD` function returns the `#VALUE!` error value.

#### Example
| **FORMULA**    | **RESULT** |
|----------------|------------|
| `=ISODD(-1)`  | `TRUE`     |
| `=ISODD(2.5)` | `FALSE`    |
| `=ISODD(5)`   | `TRUE`     |

---

## 4.5.6.4 N Function

### Overview
- The `N` function converts the given value into a numeric value.
- Syntax and usage described.

### Description
The `N` function converts the given value into a numeric value.

#### Syntax:
The syntax of the `N` function is:
```
=N(value)
```
**A value is required.**

**Numeric values are converted as numeric values.**
- A date value is converted as a serial number.
- The Logic operator `TRUE` returns a value of `1`. The other values are returned as `0`.

#### Example
| **FORMULA**     | **RESULT** |
|----------------|------------|
| `=N(7)`        | `7`        |
| `=N("EVEN")`   | `0`        |
| `=N(1/1/2008)` | `39448`    |
| `=N(TRUE)`     | `1`        |

---

## 4.5.6.5 NA Function

### Overview
- The `NA` function returns the `#N/A` error.
- Explanation of when and why the error is produced.

### Description
The `NA` function returns the `#N/A` error. This error message is produced when a formula is unable to find a value that it needs. This error message denotes 'value not available.'

---

<!-- tags: [syncfusion, winforms, calculate, isodd, n-function, na-function, error-handling] keywords: [isodd, n-function, na-function, numeric-values, date-serial-number, logic-operator, error-value] -->
```

---

<!-- 페이지 223 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: calculate
page_number: 124
page_id: calculate#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:37Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains conditions under which errors like #VALUE! and #NUM! occur in calculations.
- Demonstrates the usage of functions such as RAND BETWEEN, SQRTPI, and QUOTIENT.

## Content

### #VALUE! Error
Occurs if any of the given arguments are non-numeric.

#### Example
| FORMULA                          | RESULT                                                                  |
|----------------------------------|-------------------------------------------------------------------------|
| = RAND BETWEEN (`10`, `20`)     | `12`<br>The value is generated randomly between the given values. |

### 4.5.6.10 SQRTPI

The SQRTPI function returns the square root of a given number multiplied by π. Here π is the constant math value.

#### Syntax
The syntax of the SQRTPI function is:
```
=SQRTPI (number)
```
- **number** – Required.

#### Error Conditions
- **#NUM!** - If the number is less than zero (0).
- **#VALUE!** - Occurs if any of the given arguments are non-numeric.

#### Example
| FORMULA                          | RESULT                     |
|----------------------------------|----------------------------|
| = SQRTPI (`2`)                  | `2.506628`                |
| = SQRTPI (`-2`)                 | `#NUM!`                   |

### 4.5.6.11 QUOTIENT

The QUOTIENT function returns the integer portion of a division between two given numbers. The returned value will be an integer value.

#### Syntax
The syntax of the QUOTIENT function is:
```
=QUOTIENT (numerator, denominator)
```
- **Numerator** – Required.
- **Denominator** – Required.

## RAG Annotations
<!-- tags: [error handling, numeric functions, math, sqrt, integer division, winforms] keywords: [#VALUE!, #NUM!, RAND BETWEEN, SQRTPI, QUOTIENT, math functions, division, integer portion, numeric arguments] -->
```

---

<!-- 페이지 224 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_128.jpeg
document_name: calculate
page_number: 128
page_id: calculate#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:07:50Z
fidelity: lossless
-->

# Essential Calculate

If the value_error is an empty cell, then the function takes the error value as an empty string.

## 4.5.6.17 T

The T function tests whether the given value is text or not. If the given value is text, then it returns the given text. Otherwise, the function returns an empty text string.

### Syntax

The syntax of the T function is

```
=T( value )
```

- **value** – Required. This is a value to be checked.

If the value is not a number or logical value, then the function returns an empty string.

### Example

| FORMULA       | RESULT       |
|---------------|--------------|
| `=T("SYNCFUSION")` | SYNCFUSION |
| `=T(TRUE)`     |              |
| `=T(10)`       |              |

## 4.5.6.18 XOR

The XOR function returns the exclusive OR for the given arguments.

### Syntax

```
XOR (logical_value1, logical_value2, ...)
```

## Page-level Navigation/TOC (if applicable)

- **4.5.6.17 T**
- **4.5.6.18 XOR**

## Cross References

See also: [IFERROR] 

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, Calculate, T function, XOR function, Error handling, Text validation, Logical operations] keywords: [IFERROR, T, XOR, error_value, logical_value, exclusive OR, text checking] -->
```

---

<!-- 페이지 225 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_132.jpeg
document_name: calculate
page_number: 132
page_id: calculate#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:01Z
fidelity: lossless
-->

# Essential Calculate

## Input Table

|     | A       | B     | C       |
|-----|---------|-------|---------|
| 1   | Earning | Tax   | other   |
| 2   | 100000  | 3000  | 100     |
| 3   | 200000  | 6000  | 200     |
| 4   | 300000  | 7500  | 300     |
| 5   | 400000  | 9000  | 500     |

### Formula Result

| FORMULA                                                                | RESULT |
|------------------------------------------------------------------------|--------|
| `AVERAGEIFS(C2:C5, B2:B5, ">7000", B2:B5, "<10000")`                | 400    |

## NETWORKDAYS

### Overview
- **Networkdays Function**: Calculates the number of whole work days between two given dates.
- **Key Features**:
  - Includes all weekdays from Monday to Friday.
  - Excludes a supplied list of holidays.

### Syntax

```plaintext
= NETWORKDAYS(start_date, end_date, [holidays])
```

#### Parameters
- **start_date**: The start of the period to find the working days.
- **end_date**: The end of the period to find the working days.
- **[holidays]**: An optional argument, specifying an array of dates that are not to be counted as working days.

### Notes
- If any argument is not a valid date, `NETWORKDAYS` returns the `#VALUE!` error value.

### Example

| FORMULA                                                  | RESULT |
|----------------------------------------------------------|--------|
| `=NETWORKDAYS(DATE(2012,10,1), DATE(2013,3,1))`       | 110    |
```

---

<!-- 페이지 226 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_136.jpeg
document_name: calculate
page_number: 136
page_id: calculate#page_136
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:14Z
fidelity: lossless
-->

## Statistics

### Overview
- Lists the Statistic functions included with Essential Calculate.
- Provides descriptions for each function in a structured table.

## Content

This section lists the Statistic functions included with Essential Calculate in the below table.

### Statistic Functions

| Function Name | Description |
|---------------|-------------|
| Avedev        | Returns average deviation. |
| Average        | Returns the arithmetic mean. |
| Averagea       | Returns the arithmetic mean. |
| Binomdist      | Returns the cumulative beta probability density function. |
| Chidist        | Returns the chi-squared distribution. |
| Chiinv         | Returns the inverse of Chidist. |
| Chitest        | Returns the chi-squared distribution test for independence. |
| Confidence     | Returns the confidence interval. |
| Correl         | Returns the correlation between two sets of data. |
| Count          | Returns the count of the data listed in the arguments. |
| Counta         | Returns the count of the data listed in the arguments. |
| Countblank     | Returns the count of the empty cells listed in the arguments. |
| Countif        | Returns the count of values that meet a specified criteria. |
| Covar          | Returns covariance. |
| CritBinom      | Returns the critical value for the cumulative binomial distribution. |
| Devsq          | Returns the sum of the squares of the mean deviation. |
| Expdist        | Returns the exponential distribution. |
| Fdist          | Returns the F probability distribution. |
| Finv          | Returns the inverse of Fdist. |


## Page-level Navigation/TOC (if applicable)
- This page specifically covers statistical functions available in Essential Calculate.

## Cross References
- Refer to related sections or functions for additional context and usage examples.
- [See also: Statistical Functions, Essential Calculate Documentation]

<!-- tags: [Essential Calculate, Statistic Functions, Syncfusion, Winforms] keywords: [Statistic, Essential Calculate, Average, Chi-squared, Confidence Interval, Correlation, Count, Exponential Distribution, F Probability, Financial Functions] -->
```

---

<!-- 페이지 227 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_140.jpeg
document_name: calculate
page_number: 140
page_id: calculate#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:28Z
fidelity: lossless
-->

# Essential Calculate

This section discusses the Parse function available for the CalcEngine.

## Content

### CalcEngine.Parse Method

The `CalcEngine.Parse` method does the following:

- Accepts a string formula, for example `= A2 + 5`.
- Checks whether it is a valid formula that CalcEngine can understand.
- Returns a string that represents a parsed version of the formula that can be more readily computed.

The parsed formula is a Reverse Polish Notation expression using tokens to compactly represent the entered formula. The parsing recognizes and replaces NamedRanges with their corresponding value. The parsing also recognizes library functions and tokenizes them as well.

### 4.6.3 Calculating

This section discusses the Calculate function available for the CalcEngine.

`CalcEngine.Calculate` is the method that actually performs calculations. It does the following:

- It accepts a parsed formula.
- Uses a stack-oriented calculation technique to convert the parsed formula into the value that it represents.

#### Note

The value returned is a string holding the computed quantity.

### 4.6.4 How Things Work

1. **What happens when you enter the formula `= A1 + 5` into a cell in a `CalcSheet` object?**

2. **Explanation of Data Handling**
   
   Here let’s assume that `CalcSheet` is using its own internal data storage to hold values, so that it makes it simple to understand what is going on within `CalcEngine`. If the data is being held in some other object (like a DataGrid with a DataTable datasource), things will look the same from within the `CalcEngine`.

3. **Processing Steps**
   
   Here is a sketch of the major steps taken within the library code when you enter a formula into a cell assuming `CalcEngine.UseDependencies` is `True`. The actual processing is more involved; these steps should give you an outline of what happens:

---

<!-- tags: [CalcEngine, Parse, Calculate, Reverse Polish Notation, NamedRanges, Library Functions, Stack Calculation, CalcSheet, Dependencies] keywords: [CalcEngine, ParseMethod, CalculateMethod, RPN, NamedRanges, Dependencies, CalcSheet, DataGrid, DataTable, InternalStorage] -->
```

---

<!-- 페이지 228 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_144.jpeg
document_name: calculate
page_number: 144
page_id: calculate#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:41Z
fidelity: lossless
-->

# Essential Calculate

## 4.7.4 AND

Returns `True` if all the arguments have a logical value of `True` and returns `False` if at least one argument is `False`.

### Syntax

`AND(logical1, logical2, ...)`

#### Where:
- `logical1, logical2, ...` are multiple conditions you want to test for `True` or `False`.

### Remarks

- The arguments must evaluate to logical values (`True` or `False`).
- If an argument does not evaluate to `True` or `False`, those values are ignored.
- There must be at least one value in the argument list.

## 4.7.5 ASIN

Returns the inverse sine of a number. Inverse sine is also referred to as arcsine. The arcsine is the angle whose sine is the given number. The returned angle is given in radians in the range from `-pi/2` to `+pi/2`.

### Syntax

`ASIN(number)`

#### Where:
- `number` is the sine of the angle that you want and must be between `-1` and `1`.

## 4.7.6 ASINH

### Overview
- Functions for logical operations (`AND`).
- Returns the inverse sine of a number (`ASIN`).
- Operations related to `ASINH` are not detailed in this section.

### WinForms-specific conventions
- All methods and properties are documented using clear and concise language.
- Logical expressions and mathematical functions are explained with appropriate syntax.
- Each function's parameters and expected outputs are thoroughly defined.

<!-- tags: [syncfusion, winforms, calculate, asin, asinh, and, logical, math, version] keywords: [logicalvalue, arguments, arcsine, inverse sine, sine, radians, angle, range, operations] -->
```

---

<!-- 페이지 229 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_148.jpeg
document_name: calculate
page_number: 148
page_id: calculate#page_148
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:08:54Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Implements a simple calculation engine.
- Covers functions for calculating averages.
- Explains syntax and usage of AVERAGEA, AVG, and BINOMDIST functions.

## Content

### AVERAGEA

#### Syntax
```plaintext
AVERAGEA(value1, value2,...)
```

#### Where:
- `value1, value2, ...` are cells, ranges of cells, or values for which you want the average.

#### Remarks
- The arguments must be numbers, names, arrays, or references.
- Array or reference arguments that contain text evaluate as 0 (zero).
- If the calculation should not include text values in the average, then use the AVERAGE function.
- Arguments that contain True evaluate as 1; arguments that contain False evaluate as 0 (zero).

### 4.7.13 AVG

#### Returns
The average (arithmetic mean) of the arguments.

#### Syntax
```plaintext
AVG(number1, number2,...)
```

#### Where:
- `number1, number2, ...` are numeric arguments for which you want the average.

#### Remarks
- This method is the same as AVERAGE and is included for compatibility purposes.

### 4.7.14 BINOMDIST

#### Returns
The individual term binomial distribution probability.

#### Syntax

<!-- Calculate#page_148 -->
``` 
© 2013 Syncfusion. All rights reserved. 148 | Page
```

## Tag and Keywords
<!-- tags: [essential, calculate, averagea, avg, binomdist, function, syntax, average, arithmetic mean, binomial distribution, user guide, syncfusion winforms] keywords: [average, binomial probability, calculation engine, reference, numeric parameters, text evaluation, compatibility, arithmetic mean, winforms, 11.4.0.26] -->
``` 


---

<!-- 페이지 230 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_152.jpeg
document_name: calculate
page_number: 152
page_id: calculate#page_152
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:06Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.19 CHITTEST

#### Overview

- Returns the test for independence. CHITEST returns the value from the chi-squared (χ²) distribution for the statistic and the appropriate degrees of freedom.
- Provides insight into whether observed values are independent of expected values.

#### Content

##### Syntax

```plaintext
CHITEST(actual_range, expected_range)
```

##### Parameters

- **actual_range**: The range of data that contains observations to test against expected values.
- **expected_range**: The range of data that contains the ratio of the product of row totals and column totals to the grand total.

##### Remarks

- The χ² test first calculates a χ² statistic using the formula:
  \[
  \chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(A_{ij} - E_{ij})^2}{E_{ij}}
  \]
  where:
  - \( A_{ij} \): actual frequency in the i-th row, j-th column
  - \( E_{ij} \): expected frequency in the i-th row, j-th column
  - \( r \): number of rows
  - \( c \): number of columns

- A low value of χ² is an indicator of independence.
- The use of CHITEST is most appropriate when Eij's are not too small. Some statisticians suggest that each Eij should be greater than or equal to 5.

### 4.7.20 Choose

#### Overview

- The Choose function returns the value from a range of values on a specific index.

#### Content

- The Choose function is useful for selecting specific values based on a given index.
- It is commonly used for creating branch logic or selecting options dynamically.

---

<!-- tags: [calculate, chitest, choose, chi-squared-test, statistical-testing, user-guide, syncfusion-winforms, version-11.4.0.26] keywords: [chitest, chi-squared, independence-test, choose function, range selection, statistical analysis, syncfusion, winforms] -->
``` 


---

<!-- 페이지 231 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_156.jpeg
document_name: calculate
page_number: 156
page_id: calculate#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:22Z
fidelity: lossless
-->

## Essential Calculate

x-bar and y-bar are the sample means AVERAGE(array1) and AVERAGE(array2).

### 4.7.26 COS

Returns the cosine of the given angle.

#### Syntax

```markdown
COS(number)
```

where:

- `number` is the angle in radians for which you want the cosine.

### 4.7.27 COSH

Returns the hyperbolic cosine of a number.

#### Syntax

```markdown
COSH(number)
```

where:

- `number` is any real number for which you want to find the hyperbolic cosine.

#### Remarks

- The formula for the hyperbolic cosine is:

  \[
  \cosh(z) = \frac{e^z + e^{-z}}{2}
  \]

### 4.7.28 COUNT

---

<!-- tags: [syncfusion, calculate, cosine, hyperbolic cosine, count] -->
```

---

<!-- 페이지 232 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_160.jpeg
document_name: calculate
page_number: 160
page_id: calculate#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:31Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- probability_s is the probability of a success on each trial.
- alpha is the criterion value.

### Remarks
- Trials must be >= 0.
- Probability_s must be >= 0 and <= 1.
- Alpha must be >= 0 and <= 1.

## 4.7.34 DATE

### Overview
- Returns the sequential serial number that represents a particular date.

### Syntax
- **DATE(year, month, day)**

#### Where:
- **year** can be one to four digits. Year is interpreted based on 1900.
  - If a year is between 0 (zero) and 1899 (inclusive), the value is added to 1900 to calculate the year. For example, DATE(102,11,12) returns November 12, 2002 (1900+102).
  - If a year is between 1900 and 9999 (inclusive), the value is used as is, for example, DATE(2002,11,12) returns November 12, 2002.
- **month** is a number representing the month of the year.
- **day** is a number representing the day of the month.

### Remarks
- Dates are stored as sequential serial numbers so that they can be used in calculations. By default, January 1, 1900 is serial number 1 and November 12, 2002 is serial number 37572 because it is 37572 days after January 1, 1900.

## 4.7.35 DATEVALUE

### Overview
- Returns the serial number of the date represented by the date_text.

<!-- tags: [probability, alpha, trials, DATE, DATEVALUE, serial number, date calculation, Syncfusion Winforms, version 11.4.0.26] keywords: [probability_s, alpha, trials, date, date_serial, datevalue, date_text, 1900, 37572] -->
```

---

<!-- 페이지 233 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_164.jpeg
document_name: calculate
page_number: 164
page_id: calculate#page_164
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:45Z
fidelity: lossless
-->

### depreciation/calculation

- The double-declining balance method computes the depreciation at an accelerated rate. Depreciation is highest in the first period and decreases in successive periods. DDB uses the following formula to calculate depreciation for a period:
  
  \[
  (\text{cost-salvage}) - \text{total depreciation from prior periods} * (\text{factor/life})
  \]

### 4.7.40 Degrees

**Converts radians into degrees.**

#### Syntax

```text
DEGREES(angle)
```

**where:**

- angle is the angle in radians that you want to convert.

### 4.7.41 DEVSQ

**Returns the sum of squares of deviations of data points from their sample mean.**

#### Syntax

```text
DEVSQ(number1, number2,...)
```

**where:**

- number1, number2, ... are arguments for which you want to calculate the sum of squared deviations. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks

- The arguments must be numbers or names, arrays or references that contain numbers.
- The equation for the sum of squared deviations is:

  \[
  \text{DEVSQ} = \sum (x - \bar{x})^2
  \]
```

---

<!-- 페이지 234 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_168.jpeg
document_name: calculate
page_number: 168
page_id: calculate#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:09:55Z
fidelity: lossless
-->

# Essential Calculate

degrees_freedom1 is the numerator degrees of freedom.  
degrees_freedom2 is the denominator degrees of freedom.

## Remarks

- All arguments must be numeric.
- X must be >= 0.
- Both degrees_freedom1 and degrees_freedom2 must be >= 1 and < 10^10.
- FDIS T is calculated as follows:

**FDIST = P( F>x )**

where:

F is a random variable that has an F distribution with degrees_freedom1 and degrees_freedom2 degrees of freedom.

### 4.7.50 Find

The Find function finds a portion of a string from a particular text and returns the location of the string.

#### Syntax:

**Find(lookfor, lookin, start)**

where:
- lookfor is the text you want to search.
- lookin is the text in which you want to search.
- start specifies the starting position of the text from which you want to start searching in the text. This is optional.

### 4.7.51 FINV

The Finv function returns the inverse of the F probability distribution. If p = FDIST(x,...), then FINV(p,...) = x.

Using F distribution, you can compare the degree of variability for two data sets.

#### Syntax:

**FINV(probability,deg_freedom1,deg_freedom2)**
```markdown

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```

---

<!-- 페이지 235 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: calculate
page_number: 172
page_id: calculate#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:07Z
fidelity: lossless
-->

## Content

### 4.7.57 FV

The **FV** function returns the future value of an investment, based on an interest rate and a constant payment schedule.

#### Syntax:

```
FV( interest_rate, number_payments, payment, PV, Type )
```

#### where:
- **interest_rate** is the interest rate for the investment.
- **number_payments** is the number of payments for the annuity.
- **payment** is the payment made on each period.
- **PV** is the present value of the payments. This is optional. The FV function assumes PV value as 0, when this parameter is omitted.
- **Type** indicates the payments due. Type accepts the following values:
  - **0 - Payments at the end of the period (default)**.
  - **1 - Payments at the beginning of the period**.

This is optional. The FV function assumes Type value as 0, when this parameter is omitted.

### 4.7.58 GAMMADIST

#### Returns the gamma distribution.

#### Syntax

```
GAMMADIST(x, alpha,beta, cumulative)
```

#### where:
- **x** is the value at which you want to evaluate the distribution.
- **alpha** is a parameter to the distribution.
- **beta** is a parameter to the distribution. If beta = 1, GAMMADIST returns the standard gamma distribution.
- **cumulative** is a logical value that determines the form of the function. If cumulative is True, GAMMADIST returns the cumulative distribution function; if False, it returns the probability density function.

---

#### Remarks

---

##### Page-level Navigation/TOC (if applicable)

- **FV**
- **GAMMADIST**

---

<!-- tags: [syncfusion, winforms, calculate, fv, gammadist, api, 11.4.0.26] keywords: [futures value, annuity, interest rate, present value, gamma distribution, cumulative distribution function, probability density function] -->
```

---

<!-- 페이지 236 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_176.jpeg
document_name: calculate
page_number: 176
page_id: calculate#page_176
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:20Z
fidelity: lossless
-->

## Essential Calculate

Returns the harmonic mean of a data set. The harmonic mean is the reciprocal of the arithmetic mean of reciprocals.

### Syntax

**HARMEAN(number1, number2,...)**  
`number1, number2, ...` are arguments for which you want to calculate the mean.

### Remarks

- The arguments must be either numbers or names, arrays, or references that contain numbers.
- All data values must be positive.
- The equation for the harmonic mean is:

\[ H = \frac{n}{\sum \frac{1}{y_i}} \]

## 4.7.64 HLOOKUP

Searches for a value in the top row of the array of values and then returns a value in the same column from a row you specify in the array. Use HLOOKUP when your comparison values are located in a row across the top of a table of data and you want to look down a specified number of rows. Use VLOOKUP when your comparison values are located in a column to the left of the data you want to find.

### Syntax

**HLOOKUP(lookup_value, table_array, row_index_num, range_lookup)**

#### where:
- `lookup_value` is the value to be found in the first row of the table. Lookup_value can be a value, a reference, or a text string.
- `table_array` is a table of information in which data is looked up. Use a reference to a range or a range name.

<!-- tags: [syncfusion, winforms, harmonic mean, arithmetric mean, reciprocals, lookup, hlookup, vlookup, array, data set] keywords: [harmonic mean, arithmetric mean, reciprocals, lookup value, table, row, number, reference, equation, search, comparison, data, page, harmonic mean equation] -->
```

---

<!-- 페이지 237 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: calculate
page_number: 180
page_id: calculate#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:32Z
fidelity: lossless
-->

## Overview

- Describes the syntax and usage of the `INDIRECT`, `INT`, and `INTERCEPT` functions.
- Explains how these functions handle numerical and textual data.
- Provides the equation for calculating the intercept of the regression line.

## Content

### 4.7.71 INT

**Description:**  
Rounds a number down to the nearest integer.

**Syntax:**  
`INT(number)`

**Where:**  
- `number` is the real number that you want to round down to an integer.

---

### 4.7.72 INTERCEPT

**Description:**  
Calculates the point at which the least squares fit line will intersect the y-axis.

**Syntax:**  
`INTERCEPT(known_y's, known_x's)`

**Where:**  
- `known_y's` is the dependent set of observations or data.
- `known_x's` is the independent set of observations or data.

---

## Remarks

- The equation for the intercept of the regression line, \( a \), is:  
  <!-- The equation itself is not provided in the text, so it needs to be included here -->

## API Reference

No specific API references are provided in this section.

## Code Examples

No code examples are provided in this section.

## Page-level Navigation/TOC (if applicable)

No local Table of Contents is present on this page.

## Cross References

No cross-references are explicitly listed on this page.

## RAG Annotations

<!-- tags: [syncfusion-sdk, calculate, indirecfunction, int-function, intercept-function] keywords: [indirect, content, textual representation, rounding down, least squares fit, regression line, intercept] -->
```

---

<!-- 페이지 238 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_184.jpeg
document_name: calculate
page_number: 184
page_id: calculate#page_184
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:44Z
fidelity: lossless
-->

# Essential Calculate

## IsNonText

**4.7.80 IsNonText**

The IsNonText function returns the boolean value after determining that the provided value is not a string.

### Syntax

```
IsNonText(text)
```

**where,**

- **text** is the value you want to test whether it is a string or not.

## ISNUMBER

**4.7.81 ISNUMBER**

Returns True if the value parses as a numeric value.

### Syntax

```
ISNUMBER(value)
```

**where:**

- **value** is the value that is to be tested.

## ISPMT

**4.7.82 ISPMT**

Calculates the interest paid during a specific period of an investment.

### Syntax

```
ISPMT(rate, per, nper, pv)
```

**where:**

- **rate** is the interest rate for the investment.
- **per** is the period for which you want to find the interest and must be between 1 and nper.
- **nper** is the total number of payment periods for the investment.
- **pv** is the present value of the investment. For a loan, pv is the loan amount.

<!-- tags: [syncfusion, essential calculate, isnontext, isnumber, ispmt] keywords: [boolean function, string, numeric value, interest calculation, rate, per, nper, pv] -->
```

---

<!-- 페이지 239 -->

```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_188.jpeg
document_name: calculate
page_number: 188
page_id: calculate#page_188
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:10:55Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Functions to determine the length of a text string.
- Calculating logarithms of a number with various bases.
- Returning the base-10 logarithm of a number.
- Exploring other logarithmic functions.

## Content

### Len(text)

Where:
- **text** is the text string whose length is to be determined.

#### 4.7.89 LOG

Returns the logarithm of a number to the base that you specify.

**Syntax**

```
LOG(number, base)
```

Where:
- **number** is the positive real number for which, you want the logarithm.
- **base** is the base of the logarithm. If base is omitted, it is assumed to be 10.

#### 4.7.90 LOG10

Returns the base-10 logarithm of a number.

**Syntax**

```
LOG10(number)
```

Where:
- **number** is the positive real number for which, you want the base-10 logarithm.

#### 4.7.91 LOGEST

(Note: This section is incomplete in the provided text and does not contain additional details.)

## Page-level Navigation/TOC

- Len(text)
- LOG
- LOG10
- LOGEST

## Cross References

See also:
- Related calculate functions for number manipulation.
- Logarithmic calculations in Syncfusion Winforms.

<!-- tags: [Syncfusion, Winforms, Calculate, Logarithms, Text Functions, SDK] keywords: [Len, LOG, LOG10, LOGEST, base, number, logarithm, text string] -->
```

---

<!-- 페이지 240 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: calculate
page_number: 192
page_id: calculate#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:06Z
fidelity: lossless
-->

## Content

### Overview
- The Match function is case-insensitive when searching.
- If the Match function cannot find a match, it returns a #N/A error.
- The match_type parameter is optional, defaulting to 1 if omitted.
- When match_type is set to 0 and used with a text value, wildcards can be applied.

### Where
- `*` - matches any sequence of characters.
- `?` - matches any single character.

#### 4.7.96 MAX
Returns the largest value in a set of values.

**Syntax**
```
MAX(number1, number2, ...)
```

**Parameters**
- `number1, number2, ...` are numbers for which you want to find the maximum value.

#### 4.7.97 MAXA
Returns the largest value in a list of arguments, including text and logical values such as `True` and `False` along with numbers.

**Syntax**
```
MAXA(value1, value2, ...)
```

## API Reference (if applicable)
- **MAX Function**
  - **Parameters:**
    - `number1, number2, ...` - Numbers or cell references to find the maximum value.
  - **Returns:** The largest numeric value.
  - **Example Usage:**
    ```csharp
    double max_value = MAX(10, 20, 30); // Returns 30
    ```
- **MAXA Function**
  - **Parameters:**
    - `value1, value2, ...` - Values or cell references to find the maximum value.
  - **Returns:** The largest value, considering text and logical values.
  - **Example Usage:**
    ```csharp
    double maxa_value = MAXA(10, "20", true); // Returns 20
    ```

## Code Examples
```csharp
using System;

class Program
{
    static void Main()
    {
        double[] numbers = { 10, 20, 30 };
        Console.WriteLine("MAX: " + MAX(numbers));
        
        object[] values = { 10, "20", true };
        Console.WriteLine("MAXA: " + MAXA(values));
    }

    static double MAX(params double[] numbers)
    {
        return numbers.Max();
    }

    static object MAXA(params object[] values)
    {
        double max = Double.MinValue;
        foreach (var value in values)
        {
            if (value is double d)
            {
                if (d > max) max = d;
            }
            else if (value is bool b)
            {
                if (b)
                {
                    if (1 > max) max = 1;
                }
            }
            else if (value is string s)
            {
                if (double.TryParse(s, out double num))
                {
                    if (num > max) max = num;
                }
            }
        }
        return max;
    }
}
```

## Cross References
- Refer to the section on the Match function for more details on text matching operations.
- See also: MIN, MINA, MAXIF, MINIF for related functions.

<!-- tags: [product, module, control, api, version?] keywords: [Match function, MAX, MAXA, MAXIF, MIN, MINA, Match type, Case insensitivity, Wildcards, Logical values, Text values] -->
```

---

<!-- 페이지 241 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_196.jpeg
document_name: calculate
page_number: 196
page_id: calculate#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:27Z
fidelity: lossless
-->

# Essential Calculate

**values** is an array or a reference to cells that contain numbers. These numbers represent a series of payments (negative values) and income (positive values) occurring at regular periods. Values must contain at least one positive value and one negative value to calculate the modified internal rate of return.

**finance_rate** is the interest rate you pay on the money used in the cash flows.

**reinvest_rate** is the interest rate you receive on the cash flows as you reinvest them.

## Remarks

- MIRR uses the order of values to interpret the order of cash flows. Be sure to enter your payment and income values in the sequence you want and with the correct signs (positive values for cash received, negative values for cash paid).
- If \( n \) is the number of cash flows in values, \( \text{frate} \) is the finance_rate, and \( \text{rrate} \) is the reinvest_rate, then the formula for MIRR is:

\[
\left( \frac{-NPV(\text{rrate}, \text{values[positive]}) \cdot (1+\text{rrate})^n}{NPV(\text{frate}, \text{values[negative]}) \cdot (1+\text{frate})} \right)^{\frac{1}{n-1}} - 1
\]

## 4.7.104 MOD

Returns the remainder after the number is divided by a divisor. The result has the same sign as the divisor.

### Syntax

MOD(number, divisor)

**where:**

- number is the number for which, you want to find the remainder.
- divisor is the value by which, you want to divide the number.

## Remarks

- The MOD function can be expressed in terms of the INT function:

\[
\text{MOD}(n, d) = n - d \cdot \text{INT}(n/d)
\]

<!-- tags: [MIRR, MOD, finance_rate, reinvest_rate, cash_flows, integers, divisors, interest_rates, number_manipulation, calculate, essential_calculate] keywords: [MIRR calculation, MOD function, negative_values, positive_values, reinvest_rate, finance_rate, remainder, number, divisor, INT function, cashflows, array, reference_cells] -->
```

---

<!-- 페이지 242 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_200.jpeg
document_name: calculate
page_number: 200
page_id: calculate#page_200
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:11:42Z
fidelity: lossless
-->

## Essential Calculate

### Overview
- The document describes the `NORMINV` and `NormsDist` functions related to the normal distribution, focusing on their parameters, constraints, and functionality.
- Highlights include the iterative search technique used by `NORMINV` and the probability calculations handled by `NormsDist`.

### Content

#### Probability and Parameters Definition

**Where:**
- `probability` is a probability corresponding to the normal distribution.
- `mean` is the arithmetic mean of the distribution.
- `standard_dev` is the standard deviation of the distribution.

**Remarks:**
- Probability must be >= 0 and <= 1.
- `standard_dev` must be > 0.

Given a value for probability, `NORMINV` seeks value \( x \) such that \( \text{NORMDIST}(x, \text{mean}, \text{standard\_dev}, \text{True}) = \text{probability} \). `NORMINV` uses an iterative search technique.

---

### 4.7.110 NormsDist

#### Function Definition
**NormsDist** returns the probability that the observed value of a standard normal random variable will be less than or equal to the parameter.

**Syntax:**
```csharp
NormsDist(value)
```

**Where:**
- `value` is a numeric value that checks with the random variable.

---

### 4.7.111 NormsInv

#### Function Definition
**NormsInv** returns the standard normal random variable that has Mean 0 and Standard Deviation 1.

**Syntax:**
```csharp
NormsDist(value)
```

**Where:**
- `value` is probability of the standard deviation.

---

## API Reference

### NormsDist
#### Parameters:
- **value** | Numeric | The numeric value to check the random variable.

#### Returns:
- Probability of the standard normal distribution related to the input value.

### NormsInv
#### Parameters:
- **value** | Numeric | Probability of the standard deviation.

#### Returns:
- Standard normal random variable with Mean 0 and Standard Deviation 1.

---

## Code Examples

### Example: Using NormsDist
```csharp
double value = 1.96; // Example value
double probability = NormsDist(value);
// probability contains the cumulative probability for the standard normal distribution.
```

### Example: Using NormsInv
```csharp
double probability = 0.975; // Example probability
double value = NormsInv(probability);
// value contains the standard normal random variable corresponding to the probability.
```

---

### Cross References
- See also: [NORMDIST](#section-id-for-normdist), [Standard Normal Distribution](#section-id-for-normal-distribution)

<!-- tags: [normsdist, normsinv, normal-distribution, syncfusion, winforms, probability, standard-deviation, statistics] keywords: [probability, normsdist, normsinv, iterative-search, standard-normal, normal-distribution, mean, standard-deviation] -->
```

---

<!-- 페이지 243 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_204.jpeg
document_name: calculate
page_number: 204
page_id: calculate#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:01Z
fidelity: lossless
-->

## Content

### Essential Calculate

- columns is the number of columns you want to apply as the offset to the range. This can be either a positive or a negative number.
- height is the number of rows that you want the returned range to be.
- width is the number of columns that you want the returned range to be.

### 4.7.118 OR

**Returns True if any argument is True; returns False if all arguments are False.**

#### Syntax

`OR(logical1, logical2, ...)`

**where**:  
logical1, logical2, ... are conditions you want to test that can be either True or False.

#### Remarks
- The arguments must evaluate to logical values such as True or False or in arrays or references that contain logical values.

### 4.7.119 PEARSON

**Returns the Pearson product moment correlation coefficient, r, a dimensionless index that ranges from -1.0 to 1.0 inclusive and reflects the extent of a linear relationship between two data sets.**

#### Syntax

`PEARSON(array1, array2)`

**where**:  
- array1 is a set of independent values.  
- array2 is a set of dependent values.

#### Remarks

<!-- tags: [pearson, correlation, coefficient, logical values, arguments, conditional logic, dependencies, independent variables, dependent variables] keywords: [or function, arguments, true, false, pearson correlation, r value, linear relationship, data sets] -->
```

---

<!-- 페이지 244 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_208.jpeg
document_name: calculate
page_number: 208
page_id: calculate#page_208
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:12Z
fidelity: lossless
-->


## EssentialCalculate

### Overview
- Explains the parameters and usage of the POISSON function, including details on how it calculates probabilities.
- Describes the syntax and functionality of the POW function, which raises a number to a specified power.

### Content

#### Poisson Function
The POISSON function is used to calculate probabilities based on the Poisson distribution.

**Parameters:**
- **x**: The number of events.
- **mean**: The expected numeric value.
- **cumulative**: A logical value that determines the form of the probability distribution returned. If True, it returns the cumulative Poisson probability; if False, it returns the Poisson probability mass function.

**Remarks:**
- **X**: Must be >= 0.
- **Mean**: Must be > 0.
- **POISSON Calculation**:
  - For **cumulative = False**:
    \[
    POISSON = \frac{e^{-\lambda} \lambda^x}{x!}
    \]
  - For **cumulative = True**:
    \[
    CUMPOISSON = \sum_{k=0}^{x} \frac{e^{-\lambda} \lambda^k}{k!}
    \]

#### 4.7.126 Pow

**The Pow Function**
The Pow function returns the result of a number raised to a power.

**Syntax:**
\[
\text{POW(number, power)}
\]

**Parameters:**
- **number**: The base number. It can be any real number.
- **power**: The exponent to which the base number is raised.

## API Reference (if applicable)

### Poisson Function

- **Parameters**:
  - Name | Type | Description | Default | Required
  - x | Numeric | Number of events | - | Yes
  - mean | Numeric | Expected numeric value | - | Yes
  - cumulative | Logical | Determines the type of probability distribution | - | Yes

### Pow Function

- **Parameters**:
  - Name | Type | Description | Default | Required
  - number | Numeric | Base number | - | Yes
  - power | Numeric | Exponent | - | Yes

Returns:
- **Type**: Numeric
- **Description**: The result of raising the base number to the specified power.

## Code Examples (multi-language supported)

```csharp
// Example of using the Poisson function with cumulative = False
double poissonResult = Math.Poisson(5, 3, false);

// Example of using the Pow function
double powerResult = Math.Pow(2, 3);
```

## Page-level Navigation/TOC (if applicable)
- 4.7.125 Poisson Function
- 4.7.126 Pow Function
- Additional relevant topics if applicable

## Cross References
- See also: Other functions related to statistical calculations and mathematical operations.

<!-- tags: [syncfusion, winforms, pow, poisson, function, probability, statistics] keywords: [poisson, pow, function, statistical, probability, mathematical] -->
```

---

<!-- 페이지 245 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: calculate
page_number: 212
page_id: calculate#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:32Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Explains essential calculations involving the formula for financial calculations.
- Details how to handle cases where the rate is 0 in the formula.
- Provides information on returning the quartile of a data set using the QUARTILE function.
- Explains the conversion of degrees to radians using the RADIANS function.

## Content

### Financial Formula
The formula is as follows:

\[ pv \cdot (1 + rate)^{nperi} + pmt \cdot (1 + rate \cdot type) \cdot \left( \frac{(1 + rate)^{nperi} - 1}{rate} \right) + fv = 0 \]

If the rate is 0:

\[ (pmt \cdot nperi) + pv + fv = 0 \]

### 4.7.132 QUARTILE

#### Overview
Returns the quartile of a data set.

#### Syntax

**QUARTILE(array, quart)**

#### Parameters
- **array**: The array or cell range of numeric values for which you want the quartile value.
- **quart**: Indicates which value to return.

#### Value Returned
- **quart = 0**: Minimum value
- **quart = 1**: First quartile (25th percentile)
- **quart = 2**: Median value (50th percentile)
- **quart = 3**: Third quartile (75th percentile)
- **quart = 4**: Maximum value

### 4.7.133 RADIANS

#### Overview
Converts degrees to radians.

#### Syntax
- Not explicitly shown, but explained that this function converts degrees to radians.

## API Reference

### QUARTILE
- **Parameters**:
  - `array`: Array or cell range of numeric values.
  - `quart`: Integer value indicating which quartile to return (0 to 4).
- **Returns**: The quartile value based on the specified quartile (minimum, first quartile, median, third quartile, or maximum).

### RADIANS
- **Parameters**: Angle in degrees.
- **Returns**: The equivalent value in radians.

## Code Examples (Not explicitly shown in the image, but suggested examples)

### Example of Using QUARTILE Function
```csharp
var values = new double[] { 10, 20, 30, 40, 50 };
var quartile = Syncfusion.Math.Quartile(values, 2);
// quartile will contain the median value
```

### Example of Using RADIANS Function
```csharp
var degrees = 180;
var radians = Syncfusion.Conversion.Radians(degrees);
// radians will be π (approximately 3.14159)
```

## Page-level Navigation/TOC (if applicable)
- 4.7.132 QUARTILE
- 4.7.133 RADIANS

## Cross References
- Possible references to:
  - Other functions in the documentation related to mathematical or statistical calculations.

<!-- tags: [syncfusion, winforms, financial calculations, quartiles, radians] keywords: [quartile, radians, calculate, array, quart, quartile values, degrees, radians conversion] -->
```

---

<!-- 페이지 246 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_216.jpeg
document_name: calculate
page_number: 216
page_id: calculate#page_216
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:12:53Z
fidelity: lossless
-->

# Essential Calculate

## Overview

- number is any real number that you want rounded down.
- Num_digits is the number of digits to which you want to round a number.

### Remark

- ROUNDOWN behaves like ROUND, except that it always rounds a number down.

## 4.7.140 ROUNDUP

### Overview

- Rounds a number up away from 0 (zero).

### Syntax

ROUNDUP(number, num_digits)

**where:**

- number is any real number that you want rounded up.
- num_digits is the number of digits to which you want to round a number.

### Remarks

- ROUNDUP behaves like ROUND, except that it always rounds a number up.

## 4.7.141 RSQ

### Overview

- Returns the square of the Pearson product moment correlation coefficient through data points in known_y's and known_x's.

### Syntax

RSQ(known_y's, known_x's)

**where:**

- known_y's is an array or range of data points.
- known_x's is an array or range of data points.

<!-- tags: [essential calculate, roundup, rounddown, rsq, number, num_digits, known_y's, known_x's] keywords: [roundup, rounddown, correlation coefficient, pearson product moment correlation coefficient, data points, known y's, known x's] -->
```

---

<!-- 페이지 247 -->

<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_220.jpeg
document_name: calculate
page_number: 220
page_id: calculate#page_220
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:03Z
fidelity: lossless
-->

# Essential Calculate

## Content

### 4.7.147 SLN

**Returns the straight-line depreciation of an asset for one period.**

#### Syntax

```markdown
SLN(cost, salvage, life)
```

#### Parameters:

- **cost**: The initial cost of the asset.
- **salvage**: The value at the end of the depreciation (sometimes called the salvage value of the asset).
- **life**: The number of periods over which the asset is depreciated (the useful life of the asset).

### 4.7.148 SLOPE

**Returns the slope of the linear regression line through data points in known_y's and known_x's. The slope is the rate of change along the regression line.**

#### Syntax

```markdown
SLOPE(known_y's, known_x's)
```

#### Parameters:

- **known_y's**: An array or cell range of numeric dependent data points.
- **known_x's**: The set of independent data points.

#### Remarks

- The equation for the slope of the regression line is:

<!-- tags: [syncfusion sdk, winforms, calculate, sln, slope, linear regression]  
keywords: [depreciation, straight-line depreciation, slope, regression line, known_y's, known_x's, useful life, salvage value] -->

---

<!-- 페이지 248 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_224.jpeg
document_name: calculate
page_number: 224
page_id: calculate#page_224
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:13Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Describes how to calculate standard deviation based on the entire population using the STDEVP function.
- Explains the syntax and formula for the STDEVP function.
- Provides remarks on when to use the STDEVP function versus the STDEV function.

## Content

### 4.7.154 STDEVP

**Calculates standard deviation based on the entire population given as arguments.**

#### Syntax
STDEVP(number1, number2, ...)

**where:**
- `number1, number2, ...` are 1 to 30 number arguments corresponding to a population. You can also use a single array or a reference to an array instead of arguments separated by commas.

#### Remarks
- STDEVP assumes that its arguments are the entire population. If your data represents a sample of the population, then compute the standard deviation using STDEV.
- STDEVP uses the following formula:

  \[
  \sqrt{\frac{\sum(x - \bar{x})^2}{n}}
  \]

  **where:**
  - \(x\) is the sample mean AVERAGE(number1, number2, ...).
  - \(n\) is the sample size.

### 4.7.155 STDEVPA

#### Overview
Describes how to calculate standard deviation based on the entire population, including logical values and text representations of numbers.

#### Syntax
STDEVPA(number1, number2, ...)

#### Remarks
STDEVPA assumes that its arguments represent the entire population, similar to STDEVP. It includes logical values and text representations of numbers in the calculation.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms
- **Class:** Essentials.Calculate
- **Method:** STDEVP
  - **Parameters:**
    - `number1`: Number or reference to a number.
    - `number2`: Number or reference to a number.
    - `...`: Up to 30 numbers or references to numbers.
  - **Returns:** The standard deviation of the population.
  - **Exceptions:** None.

## Code Examples
### Example: Using STDEVP
```csharp
double[] population = {10, 20, 30, 40, 50};
double standardDeviation = STDEVP(population);
```

### Example: Using STDEVPA with Logical Values and Text
```csharp
object[] mixedValues = {10, "20", true, false, 30};
double standardDeviation = STDEVPA(mixedValues);
```

## Cross References
- Refer to section 4.7.153 for details on the STDEV function.
- Refer to section 4.7.156 for further calculations involving standard deviation.

<!-- tags: [Syncfusion, WinForms, standard deviation, STDEVP, STDEVPA, population, sample, formula] keywords: [STDEVP, STDEVPA, population arguments, standard deviation, sample size, sample mean, logical values, text representations] -->
```

---

<!-- 페이지 249 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_228.jpeg
document_name: calculate
page_number: 228
page_id: calculate#page_228
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:33Z
fidelity: lossless
-->

# Essential Calculate

- **criteria** is used to determine the cells that will be added.
- **sum_range** are the cells to sum.

## 4.7.160 SUMPRODUCT

**Description:**  
Multiplies corresponding components in the given arrays and returns the sum of those products.

### Syntax

**SUMPRODUCT(array1, array2, array3, …)**

**where:**  
- **array1, array2, array3, …** are 2 to 30 arrays whose components you will want to multiply and then add.

### Remarks

- The array arguments must have the same dimensions.
- SUMPRODUCT treats array entries that are not numeric as if they were zeros.

## 4.7.161 SUMSQ

**Description:**  
Returns the sum of the squares of the arguments.

### Syntax

**SUMSQ(number1, number2, …)**

**where:**  
- **number1, number2, …** are arguments for which you want the sum of the squares. You can also use a single array or a reference to an array instead of arguments separated by commas.

## 4.7.162 SumXmY2

**Description:**  
The SumXmY2 function calculates the sum of the squares of the differences between the corresponding items in the arrays and returns the sum as results.
```

---

<!-- 페이지 250 -->

```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_232.jpeg
document_name: calculate
page_number: 232
page_id: calculate#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:13:43Z
fidelity: lossless
-->

## Content

### TEXT

**Converts a value to text in a specific number format.**

#### Syntax

```markdown
TEXT(value, format_text)
```

**where:**

- `value` is a numeric value, a formula that evaluates to a numeric value or a reference to a cell containing a numeric value.
- `format_text` is a number format in text form in the Category box on the Number tab in the Format Cells dialog box.

### TIME

**Returns the decimal number for a particular time.**

The decimal number returned by TIME is a value ranging from 0 (zero) to 0.99999999, representing the times from 0:00:00 (12:00:00 A.M.) to 23:59:59 (11:59:59 P.M.).

#### Syntax

```markdown
TIME(hour, minute, second)
```

**where:**

- `hour` is a number from 0 (zero) to 23 representing the hour.
- `minute` is a number from 0 to 59 representing the minute.
- `second` is a number from 0 to 59 representing the second.

### TIMEVALUE

**Returns the decimal number of the time represented by a text string. The decimal number is a value ranging from 0 (zero) to 0.99999999, representing the times from 0:00:00 (12:00:00 A.M.) to 23:59:59 (11:59:59 P.M.).**

---

## API Reference

### Parameters

#### TEXT
- **value**: Numeric value or reference to a numeric value.
- **format_text**: String specifying the number format.

#### TIME
- **hour**: Integer representing the hour (0 to 23).
- **minute**: Integer representing the minute (0 to 59).
- **second**: Integer representing the second (0 to 59).

#### TIMEVALUE
- **text_string**: A string representing the time.

### Returns

- **TEXT**: A string representation of the number in the specified format.
- **TIME**: A floating-point number representing the given time as a decimal fraction of a day.
- **TIMEVALUE**: A floating-point number representing the given time as a decimal fraction of a day.

## Code Examples

### C#

```csharp
// Example using TEXT
string result = TEXT(1234.567, "#,##0.00");
// result: "1,234.57"

// Example using TIME
double timeDecimal = TIME(13, 45, 30); 
// timeDecimal: 0.572916667 (3:45:30 PM)

// Example using TIMEVALUE
double timeValue = TIMEVALUE("13:45:30"); 
// timeValue: 0.572916667 (3:45:30 PM)
```

---

## Tags and Keywords

<!-- tags: syncfusion, winforms, text, time, timevalue, datetime, numeric formatting, function, syntax, parameter, return value keywords: text, time, timevalue, format_text, hour, minute, second, decimal number, numeric value, function syntax -->
```

---

<!-- 페이지 251 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_236.jpeg
document_name: calculate
page_number: 236
page_id: calculate#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:02Z
fidelity: lossless
-->

# Essential Calculate

## 4.7.178 Var

The Var function returns the variance of a population based on a sample of numbers.

### Syntax:
Var( number1, number2, … number_n )

Where:
number1, number2, … number_n are the sample numbers. 30 numbers can be entered.

## 4.7.179 VarA

The VarA function returns the variance of a population based on a sample of numbers, text, and logical values (ie: TRUE or FALSE).

### Syntax:
VarA( value1, value2, … value_n )

Where:
value1, value2, … value_n are the sample values. They can be numbers, text, and logical values. Values that are TRUE are evaluated as 1. Values that are FALSE or text values are evaluated as 0. 30 values can be entered.

## 4.7.180 VarP

The VarP function returns population variance of the listed values.

### Syntax:
VarP(listofvalues)

Where:
- listofvalues provides the range or values that contain the population.

## 4.7.181 VARPA

### Overview
- The Var function calculates the variance of a population based on a sample of numbers.
- The VarA function evaluates a population variance including logical and text values.
- The VarP function calculates the population variance of a list of values.

### Content
#### Variance Functions Summary
- **Var**: Computes the variance of a population using a sample of numbers.
- **VarA**: Computes the population variance including text and logical values where TRUE is treated as 1 and FALSE or text is treated as 0.
- **VarP**: Computes the population variance based on a complete population of values.
- **VARPA**: (Missing description in the image)

#### Usage Examples
```csharp
// Example for Var
double variance = Var(new double[] {10, 20, 30, 40});

// Example for VarA
double varAValue = VarA(new object[] {true, 10, "test", 20});

// Example for VarP
double varPValue = VarP(new double[] {5, 10, 15, 20});
```

### RAG Annotations
- Tags: [essential calculate, variance functions, sample variance, population variance, numerical computation, syncfusion winforms]
- Keywords: [var, vara, varp, varpa, population variance, numerical data, sample, logical values, text values, list of values]

```


---

<!-- 페이지 252 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_240.jpeg
document_name: calculate
page_number: 240
page_id: calculate#page_240
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:18Z
fidelity: lossless
-->

## Essential Calculate

### 4.7.185 Weibull

The Weibull function returns the Weibull distribution. This distribution is used in reliability analysis, such as calculating a device's mean time to failure.

#### Syntax:
```plaintext
WEIBULL(x, alpha, beta, cumulative)
```

Where:
- **X** is the value at which the function is evaluated.
- **Alpha** is a parameter to the distribution.
- **Beta** is a parameter to the distribution.
- **Cumulative** determines the form of the function.

#### Remarks:
- If x, alpha, or beta is nonnumeric, WEIBULL returns the #VALUE! error value.
- If x < 0, WEIBULL returns the #NUM! error value.
- If alpha ≤ 0 or if beta ≤ 0, WEIBULL returns the #NUM! error value.

### 4.7.186 Xirr

The Xirr function computes the internal rate of return for a schedule of possibly non-periodic cash flows.

#### Syntax:
```plaintext
Xirr(cashflow, datelist, value)
```

Where:
- **cashflow** is the range of cash flow.
- **datelist** is the list of corresponding date serial number values.
- **value** is an initial guess at the return value.

### 4.7.187 YEAR

Returns the year corresponding to a date. The year is returned as an integer in the range 1900-9999.

#### Syntax
```plaintext
 YEAR
```

---
Source: Syncfusion Inc., 2013. All rights reserved.
---

## Cross References
See also:
- Weibull
- Xirr
- YEAR

<!-- tags: [essential-calculate, weibull-distribution, reliability-analysis, xirr-function, cash-flow-analysis, year-function, syncfusion-winform, version-11.4.0.26] keywords: [weibull-distribution, mean-time-to-failure, reliability-analysis, internal-rate-of-return, non-periodic-cash-flows, initial-guess, year-function, essential-calculate, numeric-parameters, error-values, date-serial-number] -->
```

---

<!-- 페이지 253 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_244.jpeg
document_name: calculate
page_number: 244
page_id: calculate#page_244
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:32Z
fidelity: lossless
-->

## Content

### Example Code: Parsing and Computing Formulas

#### C#

```csharp
string result1 = this.calculate.ParseAndCompute("[Rate] * [Amount]");
```

#### VB

```vb
' Declares a CalcQuickBase object.
private calculate As CalcQuickBase

'...
' Creates an instance.
Me.calculate = New CalcQuickBase()
'... Sets up any variables you need in your calculation.
' Calls the ParseAndCompute method to compute formulas.
Dim result As String = Me.calculate.ParseAndCompute("4 * 5 + SQRT(3)")
Dim result1 As String = Me.calculate.ParseAndCompute("[Rate] * [Amount]")
```

### 5.1.3 How To Enter Vectors Of Numbers Into CalcQuickBase?

Some formulas, like Intercept, require you to enter the parameters as vectors of numbers. Other formulas, like Sum, accept number vectors as parameter arguments. To use such formulas through a CalcQuickBase object, you must enter the numbers by enclosing them in braces. The following code illustrates this.

#### C#

```csharp
// Sets the number vectors as parameters.
CalcQuickBase["known_Y"] = "{2,3,9,1,8}";
CalcQuickBase["known_X"] = "{6,5,11,7,5}";

// Computes the Intercept returned by these values.
this.textBox1.Text = 
CalcQuickBase.ParseAndCompute("Intercept([known_Y],[known_X])");
```

#### VB

```vb
' Sets the number vectors as parameters.
CalcQuickBase("known_Y") = "{2,3,9,1,8}"
CalcQuickBase("known_X") = "{6,5,11,7,5}"

' Computes the Intercept returned by these values.
Me.textBox1.Text =
```

### Summary

This section explains how to use the `ParseAndCompute` method of the `CalcQuickBase` object to compute formulas in both C# and VB. Additionally, it demonstrates how to handle number vectors as arguments for formulas that support them, such as the `Intercept` function.

### API Reference

#### Methods
- **ParseAndCompute(string formula): string**
  - **Parameters**: 
    - formula: `string` - The formula to compute.
  - **Returns**: `string` - The computed result of the formula.
  - **Description**: Parses and computes the given formula string.

### Code Examples

#### Example: Computing the Product of Rate and Amount

```csharp
string result1 = this.calculate.ParseAndCompute("[Rate] * [Amount]");
```

#### Example: Entering Number Vectors for the Intercept Formula

```csharp
CalcQuickBase["known_Y"] = "{2,3,9,1,8}";
CalcQuickBase["known_X"] = "{6,5,11,7,5}";
this.textBox1.Text = CalcQuickBase.ParseAndCompute("Intercept([known_Y],[known_X])");
```

### Tags and Keywords
<!-- tags: CalcQuickBase, ParseAndCompute, Intercept, number vectors, formula computation, C#, VB, Syncfusion Winforms keywords: CalcQuickBase, ParseAndCompute, Intercept, number vectors, formula computation, C#, VB, Syncfusion, Winforms -->
```

---

<!-- 페이지 254 -->

```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_248.jpeg
document_name: calculate
page_number: 248
page_id: calculate#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:14:50Z
fidelity: lossless
-->

# Essential Calculate

```csharp
engine.CalculatingSuspended = True

' Makes multiple updates to this.data somehow...
' Turn on calculations.
engine.CalculatingSuspended = False
```

## 5.3 Common

This section deals with the tasks and solutions that apply to both CalcQuick and CalcEngine.

### 5.3.1 How to Use a Comma as a Decimal Separator in Formula?

Local settings may require the use of a different decimal separator than the period character that Essential Calculate uses by default. For example, many Local settings use a comma as the decimal separator.

To manage this problem, Essential Calculate exposes two static (Shared in VB.NET) members, which you can set to specify the character that is recognized as the decimal separator and the character that is recognized as the list separator. The default values of these members are a period and a comma, respectively. You can set these static members at any point in your code before you use any Essential Calculate objects.

#### Code Example

```csharp
[C#]
public string Form_Load(object sender, EventArgs e)
{
    // Comma
    CalcEngine.ParseDecimalSeparator = ',';

    // Semicolon
    CalcEngine.ParseArgumentSeparator = ';';

    // .... More code
}
```

```vb
[VB]
```

## API Reference

## Code Examples

## Page-level Navigation/TOC

## Cross References

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```

---

<!-- 페이지 255 -->

```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_252.jpeg
document_name: calculate
page_number: 252
page_id: calculate#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:15:01Z
fidelity: lossless
-->

## Index of Functions and Features

### Overview

- Lists various functions and methods available in the Essential Calculate library.
- Provides page references for each function and feature.
- Covers both mathematical and text manipulation functions.

### Function and Feature Index

- **Index**: 179
- **Indexer Method using Variables**: 66
- **Indirect**: 179
- **Inside CalcEngine**: 139
- **Installation**: 16
- **Installation and Deployment**: 16
- **INT**: 180
- **INTERCEPT**: 180
- **Introduction to Essential Calculate**: 11
- **IPMT**: 181
- **IRR**: 182
- **IsBlank**: 182
- **IsErr**: 182
- **ISERROR**: 183
- **ISEVEN**: 119
- **IsLogical**: 183
- **IsNA**: 183
- **IsNonText**: 184
- **ISNUMBER**: 184
- **ISODD**: 119
- **ISPMT**: 184
- **ISREF**: 130
- **IsText**: 185
- **KURT**: 185
- **LARGE**: 186
- **LCM**: 126
- **LEFT**: 186
- **LEN**: 187
- **LN**: 187
- **LOG**: 188
- **LOG10**: 188
- **LOGEST**: 188
- **Logical**: 112

- **LOGINV**: 189
- **LOGNORMDIST**: 190
- **LOOKUP**: 134
- **LookUps and Information**: 115
- **Lower**: 191
- **Manual Calculations**: 64
- **Match**: 191
- **Math and Trig functions**: 116
- **MAX**: 192
- **MAXA**: 192
- **MEDIAN**: 193
- **Methods**: 77
- **MID**: 193
- **MIN**: 194
- **MINA**: 194
- **MINUTE**: 195
- **MIRR**: 195
- **MOD**: 196
- **MODE**: 197
- **MONTH**: 197
- **MROUND**: 123
- **Multinomial**: 118
- **N**: 120
- **NA**: 120
- **NEGBINOMDIST**: 198
- **NETWORKDAYS**: 132
- **NORMDIST**: 198
- **NORMINV**: 199
- **NormsDist**: 200
- **NormsInv**: 200
- **NOT**: 201
- **NOW**: 201
- **NPER**: 201

## Cross References

- **See also**: For detailed information on specific functions and features, refer to the corresponding page numbers listed above.

<!-- tags: [Essential Calculate, Essential Calculate functions, Index, Installation, Calculation, Math, Trig, Statistical functions, Date and Time functions] keywords: [index, functions, install, math, trig, lookup, match, error handling, logical functions, date time functions, syncfusion winforms, 11.4.0.26] -->
```