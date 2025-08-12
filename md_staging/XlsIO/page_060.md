```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: XlsIO
page_number: 060
page_id: XlsIO#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:32Z
fidelity: lossless
-->

## Overview
- Discusses scenarios where Syncfusion Assemblies are used in XlsIO under different trust levels.
- Highlights the usage of specific assemblies for XlsIO in medium trust environments.
- Provides a summary of key features of Essential XlsIO.

## Content

### Trust Scenarios with Syncfusion Assemblies

#### Example 1
If the Syncfusion Assemblies are in the **GAC (Global Assembly Cache)**, and the **Web Application** is running in **medium trust**, then the Syncfusion assemblies actually run in **full trust**. Hence, this scenario is fully supported and there are no additional steps necessary for deployment.

#### Example 2
Say, the Syncfusion Assemblies are present in the application's **bin** folder and the **Web Application** is running in **medium trust**, then the Syncfusion assemblies will run in **medium trust**.

You have to use the following assemblies instead of **XlsIO.Base** to work with XlsIO in medium trust level:

- **Syncfusion.Core.dll**
- **Syncfusion.Compression.Base.dll**
- **Syncfusion.XlsIO.Web.dll**

No additional changes are required, except the assembly references.

---

```markdown
### Note
There will be reasonable performance lag while using XlsIO in medium trust, for large files.
```

### 3.5 Feature Summary

This section provides a list of important features of **Essential XlsIO** with their definition and usage.

#### Formatting
Essential XlsIO provides various formatting options like setting fonts, alignment of content, number formatting, border settings, and color-fill settings. It also supports various styles for cells and conditional formatting options.

The following screenshot shows various formatting options provided in Essential XlsIO.

---

## Cross References
See also:
- Trust Levels and Assembly Deployment
- Performance Considerations in Medium Trust

## Code Examples
<!-- No code examples are provided in this section. -->

<!-- tags: [XlsIO, trust level, medium trust, GAC, Web Application, Syncfusion.Core, formatting, fonts, alignment, number formatting, border settings, color-fill] keywords: [medium trust, full trust, performance lag, XlsIO.Base, Syncfusion.Core.dll, Syncfusion.Compression.Base.dll, Syncfusion.XlsIO.Web.dll] -->
```