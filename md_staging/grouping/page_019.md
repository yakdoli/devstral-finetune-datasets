```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_019.jpeg
document_name: grouping
page_number: 019
page_id: grouping#page_019
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:42Z
fidelity: lossless
-->

# Essential Grouping

We have now created a platform application in the previous topic ([Creating Platform Application](Creating_Platform_Application)). This section will guide you to deploy Essential Grouping in those applications under the following topics:

- Windows / WPF-Step-by-step procedure to deploy Grouping in Windows / WPF applications
- ASP.NET-Step-by-step procedure to deploy Grouping in web applications

## 3.2.1 Windows / WPF

Now, you have created a Windows / WPF application ([refer Creating Platform Application](Creating_Platform_Application)). This section will guide you to deploy Essential Grouping in a Windows/WPF applications.

### Deploying Essential Grouping in a Windows / WPF Application

The following steps will guide you to deploy Essential Grouping:

1. In order to deploy an application that uses the Syncfusion assemblies, the referenced Syncfusion assemblies should reside in the application folder where the exe exists, in the target machine.
2. In order to do that, go to the References folder in the Solution Explorer. Select all the Syncfusion assemblies, right-click and go to Properties. Change the Copy Local property of the Syncfusion assemblies to **true** and compile the project.
3. Check whether the licenses.licx file listed in the project has its Build Action property to be **Embedded Resource**.
4. Now you may see that the Syncfusion assemblies referenced in the project are copied to the output directory along with the application executable `(bin/debug/)`.
5. Deploy the exe along with the Syncfusion assemblies in that location to the target machine. Be sure that these Syncfusion assemblies reside in the same location as the application exe in the target machine.

**Note**: For Windows Forms applications, placing these referenced Syncfusion assemblies in the GAC alone, in the target machine, will also work.

### DLLs needed for deployment

- Syncfusion.Core.dll
- Syncfusion.Grouping.Base.dll
- Syncfusion.Grouping.Windows.dll

<!-- tags: [product, module, control, api, version?] keywords: [Essential Grouping, Windows, WPF, ASP.NET, Syncfusion assemblies, Deployment, Solution Explorer, Build Action, Embedded Resource, licenses.licx, DLLs, Syncfusion.Core.dll, Syncfusion.Grouping.Base.dll, Syncfusion.Grouping.Windows.dll, GAC] -->
```