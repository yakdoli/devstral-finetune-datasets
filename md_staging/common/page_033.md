```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_033.jpeg
document_name: common
page_number: 033
page_id: common#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:00:40Z
fidelity: lossless
-->

## Overview

- This page discusses the availability of both **online** and **local documentation** for Syncfusion products.
- It explains how to access the **offline user guide** through the **Utilities > Documentation** menu.
- Guidance is provided for users on how to install or download local documentation if it is not already installed.

## Content

### Online Documentation

We have provided comprehensive documentation online to help you better understand our products.

- **User Guide**: Provides a step-by-step introduction and instructions for using the product.
- **Class Reference**: Detailed reference of all classes, methods, and properties used in the product.

### Local Documentation

Documentation pertaining to our products can be installed with your copy of Syncfusion's local resources. Explore the three categories of documentation to have a better idea of our products.

- **VS2005/VS2008 Class Reference and User Guide**
- **VS2010 Class Reference**
- **VS2010 User Guide**

#### Offline User Guide

**Figure 26: Offline User Guide**

![](https://example.com/image_url) <!-- Placeholder for the image shown in the document -->

**Note**: If you not installed local documentation, then prompt will open to download the setup.

### Online Documentation

**Syncfusion provides comprehensive documentation online to help you understand Essential Studio product better. This can be accessed from the Utilities > Documentation > Online Documentation.**

## API Reference

### Getting Started with Offline Documentation
- **Installation**: Ensure local documentation is installed with your Syncfusion product copy.
- **Access**: Navigate through the utilities menu to access the user guide and class reference for different Visual Studio versions.

### Local Documentation Setup
- **VS2005 and VS2008**: Contains documentation references for these specific versions.
- **VS2010**: Includes both class reference and user guide tailored for VS2010.

## Code Examples

### Retrieving Documentation Context
```csharp
// Example: Accessing Documentation
public void AccessDocumentation()
{
    // Navigate to local documentation via Syncfusion Utility Menu
    var documentationPath = "Utilities\\Documentation\\Local Documentation";
    // Open the required documentation file
    Process.Start(documentationPath);
}
```

## Page-level Navigation/TOC

- **Online Documentation**
  - User Guide
  - Class Reference
- **Local Documentation**
  - Installation and Setup
  - Accessing User Guide
  - Class Reference

## Cross References

See also:
- **Syncfusion Product Documentation**: For a complete overview of available resources.
- **Syncfusion Website**: For support and updates.

<!-- tags: [syncfusion, winforms, essential studio, documentation, version 11.4.0.26] keywords: [online documentation, local documentation, user guide, class reference, winforms, syncfusion, essential studio] -->
```