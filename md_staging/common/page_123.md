```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: common
page_number: 123
page_id: common#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:37Z
fidelity: lossless
-->

## Overview
- Steps to remove folders, ensure assembly versions, and embed a license file in a Syncfusion WinForms project.

## Content

### Steps for Embedding a License

1. Reload the application and then remove the `bin` and `obj` folders.
2. Ensure that the assemblies referred in the project belong to the same version.
3. Recompile your project and run it.
4. In the Solution Explorer, click **Show All Files**.
5. A file called **licenses.licx** with the following entry will be available in the project tree:
   - Syncfusion.Core.Licensing.LicensedComponent
   - Syncfusion.Core.
6. Add the file to the project.
7. Open the properties of this file.
8. Set the **BuildAction** property to **Embedded Resource**.
9. Run the project.

### Embedding the License.licx File

The following are the steps to embed the **License.licx** file as an embedded resource in the project:

1. Open the project.
2. In the **Solution Explorer**, right-click on the project node and then select **Add New Item**.
3. Choose the **licenses.licx** file from the following location:
   ```
   (Installed Drive):\Program Files\Syncfusion\Essential
   Studio\<version>\Templates\licenses.licx file.
   ```
4. The file will be added.
5. In the **Solution Explorer**, click the license file node and then open the **Properties** window.
6. Set the **Build Action** property to **Embedded Resource**.

## Page-level Navigation/TOC (if applicable)
- Steps for Embedding a License
- Embedding the License.licx File

## Cross References
- Refer to the Syncfusion documentation for detailed instructions on version compatibility and assembly management.

<!-- tags: [Syncfusion, WinForms, License Management, Embedding, Version Compatibility] keywords: [licenses.licx, BuildAction, Embedded Resource, Syncfusion.Core.Licensing.LicensedComponent, Solution Explorer] -->
```