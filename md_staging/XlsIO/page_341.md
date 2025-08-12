```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_341.jpeg
document_name: XlsIO
page_number: 341
page_id: XlsIO#page_341
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:44Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to use the XlsIO CalcEngine to perform calculations in Excel spreadsheets.
- Highlights the debugging information displayed in Visual Studio's Output window.
- Explores the integration of XlsIO with the Syncfusion XlsIO library for handling Excel file operations.

## Output Box in Visual Studio

### Description
The Output box in Visual Studio provides detailed information about the assemblies loaded during the execution of the application. The listed assemblies include essential components of the Syncfusion XlsIO library and related .NET Framework assemblies.

### Output
```
'XlsIOCalcEngine.vhost.exe' (Managed): Loaded 'C:\Windows\assembly\GAC_MSIL\Syncfusion.Calculate.Wi...
'XlsIOCalcEngine.vhost.exe' (Managed): Loaded 'C:\Windows\assembly\GAC_MSIL\Syncfusion.Core\5.102....
'XlsIOCalcEngine.vhost.exe' (Managed): Loaded 'C:\Windows\assembly\GAC_MSIL\Syncfusion.XlsIO.Base!...
'XlsIOCalcEngine.vhost.exe' (Managed): Loaded 'C:\Windows\assembly\GAC_MSIL\Syncfusion.XlsIO.Windo...
'XlsIOCalcEngine.vhost.exe' (Managed): Loaded 'C:\Windows\assembly\GAC_32\System.Data\2.0.0.0_b777...
'XlsIOCalcEngine.vhost.exe' (Managed): Loaded 'C:\Windows\assembly\GAC_MSIL\System.Xml\2.0.0.0_b77...
The thread 0xe08 has exited with code 0 (0x0).
The thread 0xfe8 has exited with code 0 (0x0).
'XlsIOCalcEngine.vhost.exe' (Managed): Loaded 'C:\Users\Administrator\Documents\Syncfusion\Essentia...
'XlsIOCalcEngine.vhost.exe' (Managed): Loaded 'C:\Windows\assembly\GAC_MSIL\System.Configuration\2...
20.99
10.495
22.99
```

## XlsIO with XlsIO CalcEngine

### Description
The figure illustrates an Excel spreadsheet where the XlsIO CalcEngine is used to perform calculations. The cells display the results of the calculations involving numerical values.

### Excel Sheet
| Column A | Column B | Column C | Column D | Column E | Column F |
|----------|----------|----------|----------|----------|----------|
| 10.99    | 10       | 20.99    | 10.495   |          |          |
| 11.99    | 11       | 22.99    | 11.495   |          |          |

## API Reference

### Namespace: Syncfusion.XlsIO

#### Members
- **CalcEngine**: Provides functionalities to perform Excel-like calculations programmatically.
- **Load**: Method for loading the necessary assemblies to use the CalcEngine.
- **Calculate**: Method to compute the results based on the provided formulas or numerical values.

## Code Examples (C#)

```csharp
using Syncfusion.XlsIO;
using System;

public class XlsIOExample
{
    public static void Main()
    {
        // Create a new instance of XlsIO CalcEngine
        CalcEngine engine = new CalcEngine();

        // Perform calculations
        double result1 = engine.Calculate(10.99 + 10);
        double result2 = engine.Calculate(20.99 + 10.495);

        Console.WriteLine(result1); // 20.99
        Console.WriteLine(result2); // 31.485

        // Clean up
        engine.Dispose();
    }
}
```

## Page-level Navigation/TOC
- Output Box in Visual Studio
- XlsIO with XlsIO CalcEngine
- API Reference
- Code Examples

## RAG Annotations
<!-- tags: [XlsIO, CalcEngine, Excel, calculations, Visual Studio] keywords: [Syncfusion, XlsIO, CalcEngine, Output Box, Excel Spreadsheet, Calculations, Visual Studio Debugging] -->
```