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