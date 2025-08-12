```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_237.jpeg
document_name: edit
page_number: 237
page_id: edit#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:54Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Replacing strings in English to German using the WinRes Utility.
- Steps for localizing resources in Visual Studio.NET 2005.

## Content

### Figure 80: Replacing strings in English to German by using the WinRes Utility

![Figure 80: Replacing strings in English to German by using the WinRes Utility](#)

**Steps for Localization:**

1. Click **File -> SaveAs**, and select the **Culture** to be localized (in this case, German - German). Now, a new resource file with the name `Syncfusion.Windows.Forms.Edit.Dialogs.frmFindDialog.de-DE.resources` will be added to the source path.

2. Similarly, repeat the process for other resources and save them.

3. Now, in the **Visual Studio.NET 2005 Command Prompt**, type the following command, and then press ENTER. Make sure that you have the `sf.publicsnk` file from the Localization folder.

   ```plaintext
   al /t:lib /culture:de-DE /out:Syncfusion.Edit.Windows.resources.dll
   /v:1.0.0.0 /delay+ /keyf:sf.publicsnk /embed:
   Syncfusion.Windows.Forms.Edit.Dialogs.frmFindDialog.de-DE.resources
   ```

4. Press ENTER. Make sure that you have the `sf.publicsnk` file from the Localization folder.

5. The version (1.0.0.0) that you specify for these DLLs in the above `al` command, should be based on the `SatelliteContractVersionAttribute` setting in the product `AssemblyInfo.cs` file in Edit source. Note that the incorrect version won't localize the assembly properly.

6. On successful execution, an Assembly file named `Syncfusion.Edit.Windows.resources.dll` will be created.

7. Finally, mark this satellite DLL for verification skipping (since it has not been signed with the same strong-name as the product assembly), as follows.

   ```plaintext
   sn -Vr Syncfusion.Edit.Windows.resources.dll
   ```

8. Now, drop this DLL into an appropriate subdirectory under your EXE's directory (`bin\Debug\`), based on the naming conventions that are enforced in .NET. You should create a folder named "de-DE" under `bin\Debug` if this DLL contains resources from the German (Germany) culture.

## RAG Annotations
<!-- tags: localization, WinForms, WinRes Utility, Visual Studio.NET 2005, satellite DLL, AssemblyInfo.cs, strong-name, resource file keywords: localization, German, resource management, WinForms controls, culture settings, DLL embedding, assembly versioning -->
```