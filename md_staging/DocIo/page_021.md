```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: DocIo
page_number: 021
page_id: DocIo#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:29:46Z
fidelity: lossless
-->

## Overview
- This page outlines the deployment requirements for using Essential DocIO, focusing on the necessary DLL references for different trust modes across various platforms such as Windows Forms, ASP.NET, WPF, ASP.NET MVC, and Silverlight.
- Key assemblies are listed for both Full Trust Mode and Medium/Partial Trust Mode, ensuring comprehensive guidance for integrating DocIO into different application environments.

## Content

### 2.3 Deployment Requirements

The various deployment requirements are illustrated under the following sections:

#### 2.3.1 DLLs

The following assemblies need to be referenced in your application for the usage of Essential DocIO.

##### Full Trust Mode

In full trust mode, add references to the following assemblies corresponding to the platform:

**DocIO (Full-Trust) – Windows Forms, ASP.NET, WPF, ASP.NET MVC**
- Syncfusion.Core.dll
- Syncfusion.Compression.dll
- Syncfusion.DocIO.Base.dll

**DocIO – Silverlight**
- Syncfusion.Compression.Silverlight.dll
- Syncfusion.DocIO.Silverlight.dll

##### Medium/Partial Trust Mode

In medium/partial trust mode, add references to the following assemblies corresponding to the platform:

**DocIO (Partial-Trust) - ASP.NET**
- Syncfusion.Core.dll
- Syncfusion.Compression.dll
- Syncfusion.DocIO.Web.dll

**DocIO (Partial-Trust) - ASP.NET MVC**

## Notes

Ensure that the appropriate assemblies are referenced based on the trust mode and platform to avoid runtime errors and ensure seamless integration of DocIO functionalities.

<!-- tags: [syncfusion, winforms, docio, deployment, trust mode, dlls, asp.net, windows forms, wpf, silverlight, medium trust] keywords: [essential docio, assemblies, full trust, partial trust, reference, windows forms, asp.net, wpf, silverlight, mvc] -->
```