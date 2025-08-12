```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: ProjIO
page_number: 009
page_id: ProjIO#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:56:27Z
fidelity: lossless
-->

# Essential ProjIO

## Overview

- A demonstration of using Syncfusion's Essential ProjIO library to read and write Microsoft Project xml files.
- Focuses on navigating through the ProjIO samples within the Essential Studio Reporting Windows Forms Dashboard.
- Steps to access and explore features in ProjIO using the Windows Forms interface.

## Content

### Essential Studio Reporting Windows Forms Dashboard

#### Figure 2: Essential Studio Reporting Windows Forms Dashboard

- The dashboard provides an overview of the functionalities available in the Essential Studio for Windows Forms, including support for generating reports and interacting with various document formats.
- The sidebar on the left lists categories like DocIO, Mail Merge, and Import & Export, indicating the variety of tasks that can be performed.
- A central panel displays the features of the selected category, with sample images and links to further details.

#### Exploring ProjIO

1. **Accessing ProjIO Samples**
   
   - **Step 1:** Open the Windows Forms Dashboard.
   - **Step 2:** Click on **ProjIO** from the bottom-left pane to access the ProjIO samples. This action will display the various ProjIO functionalities.

#### Figure 3: Essential Studio Reporting ProjIO Samples

- This figure highlights the ProjIO samples available in the dashboard.
- The sidebar shows options like **Getting Started**, **Resources**, and **Tasks**, which suggest different aspects of ProjIO that users can explore.
- The main section provides a brief introduction to Essential ProjIO, emphasizing its capabilities to read and write Microsoft Project xml files without relying on COM interop.

#### Browsing ProjIO Features

1. **Step 3:** Select any of the samples from the displayed options to navigate through their specific features.

### Key Features of Essential ProjIO

- **Read and Write XML Files:** Essential ProjIO is designed to manipulate Microsoft Project xml files directly, offering full control over project management tasks.
- **Non-Dependency on COM Interop:** It does not require COM interop, providing flexibility to use ProjIO on systems without Microsoft Project installed.
- **Self-Contained Library:** Built entirely in C#, it ensures compatibility and portability across .NET environments.

## API Reference

### Namespaces and Classes

- **Syncfusion.ProjIO**
  - **Syncfusion.ProjIO.ProjectManager**: Handles operations related to managing and manipulating Microsoft Project xml files.
  - **Syncfusion.ProjIO.ResourceManager**: Functions related to managing resources within a project.

### Methods and Properties

- **ProjectManager**
  - **Load(string filePath)**: Loads a Microsoft Project file from the specified path.
  - **Save(string filePath)**: Saves the current state of the project to the specified path.
  - **Resources**: A collection of all resources in the project.

- **ResourceManager**
  - **AddResource(string name, DateTime start, DateTime finish)**: Adds a new resource to the project with specified name and time duration.
  - **RemoveResource(string resourceId)**: Removes a resource from the project based on its unique identifier.

## Code Examples

### Example 1: Basic Project Management

```csharp
using Syncfusion.ProjIO;

// Load a project file
ProjectManager projectManager = new ProjectManager();
projectManager.Load("path_to_project.mpp");

// Access resources
foreach (var resource in projectManager.Resources)
{
    Console.WriteLine($"Resource Name: {resource.Name}");
}

// Save the project
projectManager.Save("updated_project.mpp");
```

### Example 2: Adding a New Resource

```csharp
using Syncfusion.ProjIO;

ProjectManager projectManager = new ProjectManager();
projectManager.Load("path_to_project.mpp");

// Create a new resource manager
ResourceManager resourceManager = projectManager.ResourceManager;

// Add a resource
resourceManager.AddResource("New Resource", new DateTime(2023, 1, 1), new DateTime(2023, 12, 31));

// Save the project
projectManager.Save("updated_project.mpp");
```

## Page-level Navigation/TOC

- **Windows Forms Dashboard Overview**
- **Accessing ProjIO Samples**
- **Navigating ProjIO Features**
- **API and Code Examples**

## Cross References

- See also: [Essential DocIO](#essential-docio), [Essential Mail Merge](#essential-mail-merge), [Essential Import & Export](#essential-import-export)

<!-- tags: [syncfusion, projio, windowsforms, msproject, xml, net-framework] keywords: [ProjIO, Essential Studio, Windows Forms, Microsoft Project, XML, COM Interop, DocIO, Mail Merge] -->
```