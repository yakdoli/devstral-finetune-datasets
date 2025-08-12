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