```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_699.jpeg
document_name: tools
page_number: 699
page_id: tools#page_699
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:04Z
fidelity: lossless
-->

### FolderBrowser Properties

| FolderBrowser Properties | Description |
|--------------------------|-------------|
| StartLocation | Specifies the location of the root folder from which to start browsing. It is the functional equivalent of setting the PIDL value. |
|  | - Desktop, <br> - Internet, <br> - Programs, <br> - Controls, <br> - Printers, <br> - Personal, <br> - Favorites, <br> - Startup, <br> - Recent, <br> - SendTo, <br> - BitBucket, <br> - StartMenu, <br> - MyDocuments, <br> - MyMusic, <br> - MyVideo, <br> - DesktopDirectory, <br> - MyComputer, <br> - NetworkNeighborhood, <br> - NetHood, <br> - Fonts, <br> - Templates, <br> - MyPictures, <br> - CommonDocuments, <br> - CommonAdminTools, <br> - AdminTools, <br> - NetAndDialUpConnections, |

## Overview
- Describes the `StartLocation` property of the FolderBrowser control.
- Explains how to specify the root folder location for browsing.
- Lists the various predefined locations available for the `StartLocation` property.

## Content
### FolderBrowser Properties

#### StartLocation
The `StartLocation` property specifies the location of the root folder from which browsing begins. It is equivalent to setting the PIDL (Pointer ID List) value in native shell dialogs. This property determines the starting point in the file system or special folders, allowing users to navigate from a predefined location.

The possible values for `StartLocation` include a variety of well-known locations:

- **Desktop**: The user's desktop folder.
- **Internet**: The Internet Explorer folder.
- **Programs**: The Programs folder.
- **Controls**: The Controls folder.
- **Printers**: The Printers folder.
- **Personal**: The Personal folder.
- **Favorites**: The Favorites folder.
- **Startup**: The Startup folder.
- **Recent**: The Recent Items folder.
- **SendTo**: The SendTo folder.
- **BitBucket**: The Recycle Bin folder.
- **StartMenu**: The Start Menu folder.
- **MyDocuments**: The My Documents folder.
- **MyMusic**: The My Music folder.
- **MyVideo**: The My Video folder.
- **DesktopDirectory**: The Desktop folder.
- **MyComputer**: The My Computer root folder.
- **NetworkNeighborhood**: The Network Neighborhood folder.
- **NetHood**: The Network Neighborhood folder (another alias).
- **Fonts**: The Fonts folder.
- **Templates**: The Templates folder.
- **MyPictures**: The My Pictures folder.
- **CommonDocuments**: The Common Documents folder.
- **CommonAdminTools**: The Common Admin Tools folder.
- **AdminTools**: The Admin Tools folder.
- **NetAndDialUpConnections**: The Network Connections folder.

This property is particularly useful when you want to restrict or guide the user to specific areas of the file system or special folders, ensuring a consistent starting point for their browsing experience.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, FolderBrowser, StartLocation, Root Folder] keywords: [StartLocation, PIDL, Root Folder, Browsing, Special Folders, Desktop, Internet, MyDocuments] -->
```