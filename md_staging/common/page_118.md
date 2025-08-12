```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: common
page_number: 118
page_id: common#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:58Z
fidelity: lossless
-->

## Overview

- The document outlines the process of completing the installation of Syncfusion Metro Studio 2.
- Describes the functionality provided by Metro Studio Dashboard after the installation of the Metro Studio Source Code Add-on.
- Highlights the creation of icons using Metro Studio Dashboard.

## Content

### Installation Completion

#### Figure 111: Installation Completed

![Installation Completed](#)

The Setup has finished installing Syncfusion Metro Studio on your computer. Click Finish to exit Setup. The option to run Metro Studio is pre-selected.

#### Using Metro Studio Dashboard

Once the Metro Studio Source Code Add-on is installed, Metro Studio Dashboard provides the option to create icons.

#### Metro Studio Dashboard Interface

![Metro Studio Dashboard](#)

- **Icon Category**: Medical
- **Available Icons**:
  - Ambulance
  - Appointment
  - Band Aid
  - Blood
  - Dental
  - Doctor
  - Dropper
  - Eyehospital
  - First Aid
  - Heart
  - Heart ECG
  - Hospital

#### Creating a Project

The dashboard includes a button to "Drop to create a project."

---

### Page-Level Navigation

This section describes the installation and use of Syncfusion Metro Studio 2, focusing on the features available after adding the Metro Studio Source Code Add-on.

---

## API Reference

- **Namespace**: Syncfusion.Windows
- **Class**: MetroStudioDashboard
- **Methods**:
  - `OpenIconEditor()`
  - `RunMetroStudio()`
- **Properties**:
  - `IsAddOnInstalled`
  - `CurrentIconCategory`

---

## Code Examples

```csharp
using Syncfusion.Windows;

// Check if the add-on is installed
if (MetroStudioDashboard.IsAddOnInstalled)
{
    // Open the icon editor
    MetroStudioDashboard.OpenIconEditor();
}
```

---

## Cross References

- Refer to the "Installing Syncfusion Metro Studio" section in the main guide for detailed installation instructions.
- See the "Customizing Icons" section for more information on creating and editing icons using Metro Studio Dashboard.

---

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Metro Studio, Installation, Icon Creation, Dashboard] keywords: [Syncfusion Metro Studio 2, Add-on, Installation Completion, Icon Editor, Metro Studio Dashboard] -->
```