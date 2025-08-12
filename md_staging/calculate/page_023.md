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