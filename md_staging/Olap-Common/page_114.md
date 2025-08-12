```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_114.jpeg
document_name: Olap Common
page_number: 114
page_id: Olap Common#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:38Z
fidelity: lossless
-->

# Essential Olap Common

## Overview
- Demonstrates the process of integrating OlapGrid with a web project.
- Explains adding assemblies as references and configuring a WCF Service.
- Highlights the steps to create and configure a WCF Service named `OlapManager`.

## Content

### OlapGrid in Design
The image titled "Figure 17: OlapGrid in Designer Page" illustrates the Visual Studio designer with the OlapGrid tool being selected in the toolbox. The XAML code and project structure are visible, showing the integration of the OlapGrid component into the project.

#### Steps to Integrate OlapGrid

1. **Add Assemblies as References:**
   - Add the following two assemblies as references to the web project:
     - **Syncfusion.Olap.Base**
     - **Syncfusion.OlapSilverlight.BaseWrapper**

2. **Add WCF Service:**
   - Add a WCF Service to the web project by following these steps:
     - Right-click the **Project**.
     - Select **Add New Item**.
     - Choose **WCF Service**.
   - **Name the service as `OlapManager`**.
     - Delete the `IOLapManager.cs` file as the service has to be inherited with the `IOLapDataProvider`.

### Figure: OlapGrid in Designer Page

![OlapGrid in Designer Page](attachment:Figure_17_OlapGrid_in_Designer_Page.jpg)

### Setting Up the WCF Service

- **Name of the Service:** `OlapManager`
- **File to Delete:** `IOLapManager.cs`
- **Inheritance:** The service must inherit from `IOLapDataProvider`.

## Page-level Navigation/TOC (if applicable)

- **Step 1:** Add required assemblies.
- **Step 2:** Configure WCF Service.

## Cross References

See also:
- Documentation on OlapGrid component.
- WCF Service implementation guide.

## RAG Annotations

<!-- 
tags: [OlapGrid, WCF Service, OlapManager, Syncfusion Winforms, version 11.4.0.26]
keywords: [OlapGrid, Designer, Visual Studio, WCF, Service, Syncfusion, Integration, Reference, Assemblies, OlapManager, IOLapDataProvider]
-->
```