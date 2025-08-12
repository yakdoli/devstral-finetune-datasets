```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_009.jpeg
document_name: DICOM
page_number: 009
page_id: DICOM#page_009
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:28:02Z
fidelity: lossless
-->

# Essential DICOM

## Overview
- Demonstrates the process of creating a new WPF application using Visual Studio.
- Guides through integrating Syncfusion.Core and Syncfusion.DICOM.Base libraries into the project.
- Focuses on setting up a WPF application for DICOM-related functionalities.

## Content

### Creating a New WPF Application

The following steps detail the process of creating a new WPF application and integrating the necessary Syncfusion libraries.

1. **Create a New WPF Application**
   - Open Visual Studio and navigate to the "New Project" dialog box.
   - Select "WPF Application" from the list of templates under "Visual C#."
   - Configure the project settings such as the project name, location, and solution name.
   - Ensure the project targets the appropriate .NET Framework version (e.g., 3.5 as shown in the figure).

   **Figure 3: New Project dialog box-WPF Application**
   ![New Project dialog box: WPF Application](New Project dialog box image)

   Upon completion, a new WPF application will be created.

2. **Open the Main Form in the Designer**
   - After creating the WPF application, open the main form of the application in the designer.
   - This will allow you to start designing the user interface for your application.

3. **Add Syncfusion References**
   - Add the required Syncfusion libraries to the project:
     - **Syncfusion.Core**
     - **Syncfusion.DICOM.Base**
   - These references will enable access to Syncfusion's DICOM functionalities within your WPF application.

## API Reference

### Namespaces and Classes
- **Syncfusion.Core**: Provides core functionality for Syncfusion controls and utilities.
- **Syncfusion.DICOM.Base**: Contains base classes and utilities for handling DICOM data.

## Code Examples

### Sample Code for Integrating Syncfusion Libraries

```csharp
// Adding Syncfusion References
using Syncfusion.Core;
using Syncfusion.DICOM.Base;

// Example Usage in Code
public class DICOMApplication
{
    public void InitializeDICOM()
    {
        // Initialize DICOM functionality
        DICOMBase.Initialize();
    }
}
```

## Page-level Navigation/TOC

- Creating a New WPF Application
  - New Project Dialog Box
  - WPF Application Setup
  - Integrating Syncfusion Libraries

## Cross References

- See also: [Syncfusion Core Documentation](https://www.syncfusion.com/documentation/common/uwp/getting-started)
- See also: [Syncfusion DICOM Documentation](https://www.syncfusion.com/documentation/dicom)

<!-- tags: Essential DICOM, WPF, Syncfusion.Core, Syncfusion.DICOM.Base, setup, library integration -->
```