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