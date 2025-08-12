```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_043.jpeg
document_name: HTMLUI
page_number: 043
page_id: HTMLUI#page_043
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:54Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Describes how to embed and retrieve HTML files as resources in a Windows Forms project.
- Guides through configuring the Solution Explorer and setting BuildAction properties for the HTML file.
- Explains the use of C# code to load embedded resources at runtime.

## Content

### Solution Explorer Configuration

#### Step 1: Viewing the Solution Explorer
- The HTML file will be shown in the Solution Explorer, as depicted in the following figure:

![Tree view of the Solution Explorer](https://example.com/figure20)

#### Figure 20: Tree view of the Solution Explorer

#### Step 2: Configuring BuildAction for the Resource HTML File
- In the properties grid of the resource HTML file, specify its **BuildAction** as **Embedded Resource**.

![Properties Window of the Resource HTML File](https://example.com/figure21)

#### Figure 21: Properties Window of the Resource HTML File

### Code Implementation for Retrieving Embedded Resources

#### C# Code to Load the Embedded Resource
The file can be retrieved from the resource by using the following C# code:

```csharp
// Load the specified HTML file which is marked as the project's embedded resource.
htmlStream = (Stream)Assembly.GetExecutingAssembly().GetManifestResourceStream
```

### Summary
- Demonstrates the process of embedding an HTML file as a resource in a Windows Forms application.
- Provides guidance on configuring the BuildAction property and retrieving the resource using C# code.
- Ensures the resource is accessible during runtime for use in HTML user interfaces.

## API Reference

### Methods Used
- **Assembly.GetExecutingAssembly()**: Retrieves the assembly that contains the currently executing code.
- **GetManifestResourceStream**: Loads the specified resource as a stream from the executing assembly.

## Code Examples

#### Example: Retrieving an Embedded HTML File
```csharp
// C#
// Load the specified HTML file which is marked as the project's embedded resource.
htmlStream = (Stream)Assembly.GetExecutingAssembly().GetManifestResourceStream
```

## Page-level Navigation/TOC (if applicable)
- **Step 1: Viewing the Solution Explorer**
- **Step 2: Configuring BuildAction for the Resource HTML File**
- **C# Code to Load the Embedded Resource**

## Cross References
- See also: Resource Management in Windows Forms.
- See also: Using Embedded Resources in Complex UI Applications.

<!-- tags: [WinForms, HTMLUI, embedded resources, assembly, version: 11.4.0.26] keywords: [Solution Explorer, BuildAction, resource management, assembly manifest, C# code, HTML files] -->
```