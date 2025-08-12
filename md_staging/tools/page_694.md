```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_694.jpeg
document_name: tools
page_number: 694
page_id: tools#page_694
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the FolderBrowser control in Windows Forms.
- Explains key features and functionalities of FolderBrowser.
- Provides insights into location, style, and text settings.

## Content

### FolderBrowser Control

#### Overview

- **Figure 432:** FolderBrowser Control

##### See Also
- Additional features and documentation for the FolderBrowser control are referenced.

#### Features

- **FolderBrowser implements a convenient and easy to use wrapper for the Win32 Shell Folder Browser API and contains the following features:**

##### Location Settings

- **The location where the FolderBrowser Dialog points to, can be set to any desired location by the user.**
- **The StartLocation property provides various options to specify the location of the root folder from which browsing is to be started.**

##### Style Settings

- **The FolderBrowser Dialog can be displayed in various styles using the Style property of the FolderBrowser.**
- **The FolderBrowser provides options to display Templates and create folders using the "Make New Folder" button.**

##### Text Settings

- **[unclear] settings for customizing the text displayed in the FolderBrowser.**

## API Reference

- Namespace: [unclear]
- Class: FolderBrowserControl
- Properties:
  - StartLocation: Specifies the root folder for browsing.
  - Style: Determines the display style of the FolderBrowser.
- Methods: [unclear]
- Events: [unclear]

## Code Examples

### Example: Using FolderBrowser in a Form

```csharp
using Syncfusion.Windows.Forms.Tools;
using System;
using System.Windows.Forms;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();

        // Initialize FolderBrowser control
        FolderBrowser folderBrowser = new FolderBrowser();

        // Set start location
        folderBrowser.StartLocation = Environment.SpecialFolder.MyComputer;

        // Set style
        folderBrowser.Style = Syncfusion.Windows.Forms.Tools.BrowserStyle.Metro;

        // Add FolderBrowser to the form
        Controls.Add(folderBrowser);
    }
}
```

#### See also:
- [3.5.7.1.1 Features](#)
- [FolderBrowser Documentation](#)

<!-- tags: Windows Forms, FolderBrowser, Syncfusion Winforms, API Reference, Code Examples keywords: FolderBrowser Control, StartLocation, Style, Text Settings, Win32 Shell Folder Browser API, Features -->
```