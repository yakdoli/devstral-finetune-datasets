```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_097.jpeg
document_name: common
page_number: 097
page_id: common#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:04:14Z
fidelity: lossless
-->

# Essential Common

1. Open the command prompt in administrator mode and navigate to the following location:  
   {Installed Drive}\{ProgramFiles Folder}\Syncfusion\Essential Studio\{version}\Utilities\Project Migration\  
   Eg: C:\Program Files (x86)\Syncfusion\Essential Studio\11.3.0.30\Utilities\Project Migration\  

2. Run the `ProjectMigrationConsole.exe` with the following arguments:  
   `/source:"sourcepath" /studio:"Essential Studio version" /framework:"[v3.5] / [v2.0] / [v4.0] / [v4.5]" /backup:"Backupfolderpath" /hintpath:"[False] / [True]"`  
   Eg: `/source:"C:\Users\Vadivel\Documents\Visual Studio 2012\Projects\WindowsFormsApplication3" /studio:"11.2.0.25" /framework:"v4.0" /backup:"E:\ProjectMigrationBackup\WindowsFormsApplication3" /hintpath:"False"`

The following screen shot illustrates this.  

[Image description: The image is cropped or is empty. Please refer to the original document.]

## 1.13.8 Project Templates

Syncfusion provides Project Templates for the ASP.NET MVC platform to automatically refer the necessary reference and resource files in an application. However, this is not applicable to other platforms. In the other platforms (such as Windows Forms, WPF, Silverlight, and ASP.NET), the Syncfusion controls will be automatically configured in the Microsoft Visual Studio Toolbox after the setup has been installed, and the controls can be used in the application by simply dragging them from the toolbox.

<!-- tags: [Syncfusion Winforms, Project Migration, Project Templates] keywords: [Syncfusion, Essential Studio, Windows Forms, WPF, Silverlight, ASP.NET MVC, Toolbox, Project Templates, Project Migration] -->
```