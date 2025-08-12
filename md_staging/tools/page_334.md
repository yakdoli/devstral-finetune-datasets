```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_334.jpeg
document_name: tools
page_number: 334
page_id: tools#page_334
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:32Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Discusses the persistence of user entries in comboboxes for FTP server addresses in Windows Forms applications.
- Introduces the `AutoAppend` class for auto-persisting previously entered items in comboboxes without additional code.
- Explains how `AutoAppend` populates combo box controls with persisted items.

### Content

#### FTP Server Address Persistence in Comboboxes
For instance, in an FTP client application, if the user is allowed to enter the FTP address of the servers in a combobox, it is not possible to provide a complete list of all possible FTP servers. When the user enters an FTP server into a combobox, the value is lost unless the developer writes additional code to persist the user entries in the registry or in a file. Also, at initialization, the combobox should be reinitialized with the saved items from the registry or file into which the values were saved.

#### The `AutoAppend` Class
The `AutoAppend` class provides auto-persisting of previously entered items in a Windows Forms combobox based on a category keyword and also populates the combobox control's items collection with the persisted list.

The `AutoAppend` class provides this service for any combobox control without the developer having to write any code for the persisting and reading of the values.

#### Example of AutoAppend Usage
The following screenshot illustrates the usage of the `AutoAppend` class to persist items previously entered in a combobox and add them to the items collection of the combobox.

![AutoAppend functionality at RunTime](https://example.com/autocombo.png)
*Figure 148: AutoAppend functionality at RunTime*

#### Features

- **New entries can be added to control's AutoAppend list programmatically**.
- **It can be used with AutoComplete control**.

#### Associating AutoAppend with a control

### Summary of Features

The `AutoAppend` class provides an auto-persisting of previously entered items in a Windows Forms combobox based on a category keyword and also populates the combobox control's items collection with the persisted list. It has the following features:

- New entries can be added to the control's AutoAppend list programmatically.
- It can be used with `AutoComplete` control.

### Cross References
- For more information on `AutoComplete` control, refer to the relevant section in the documentation.

## Tags and Keywords
<!-- tags: [Syncfusion, AutoAppend, Windows Forms, combobox, FTP servers, persisting, registry, AutoComplete, AutoAppend class, Windows Forms control] keywords: [AutoAppend, combobox, persistence, Windows Forms, development, FTP servers, registry, settings] -->
```