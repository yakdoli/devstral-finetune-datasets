```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_031.jpeg
document_name: DocIo
page_number: 031
page_id: DocIo#page_031
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:00Z
fidelity: lossless
-->

# Essential DocIO

- Deploying Essential DocIO in a Windows Application
- Creating a Word Document

## Deploying Essential DocIO in a Windows Application

In order to deploy an application that uses the Syncfusion assemblies, the referenced Syncfusion assemblies should reside in the application folder where the exe file exists, in the target machine.

In order to do that, go to the Solution Explorer; Under References, select all the Syncfusion assemblies and then change the Copy Local property of the Syncfusion assemblies to true and compile the project.

Now, the Syncfusion assemblies referenced in the project will be copied to the output directory along with the application executable (bin/debug/).

Deploy the exe file along with the Syncfusion assemblies found, to the target machine. Be sure that these Syncfusion assemblies reside in the same location as the application exe file, in the target machine.

![Properties and Solution Explorer](https://example.com/properties-and-solution-explorer.png)

## Code Examples (Deployment)

### Setting Copy Local to True for Syncfusion Assemblies

To ensure that the required Syncfusion assemblies are included with your application, follow these steps:

1. Open your project in Visual Studio.
2. Navigate to the **Solution Explorer**.
3. Expand the **References** node in your project.
4. Locate and select all the Syncfusion assemblies.
5. Right-click on the selected assemblies and choose **Properties**.
6. In the Properties window, set the **Copy Local** property to **True**.
7. Save the changes and recompile your project.

This ensures that all the necessary libraries are included in the output directory when deploying your application.

## Cross References

See also:
- [Syncfusion Documentation on Deploying Applications](https://www.syncfusion.com/documentation)
- [Essential DocIO Documentation](https://www.syncfusion.com/products/docio)

<!-- tags: [syncfusion, essential-docio, windows-applications, deployment, copy-local, assemblies, target-machine] keywords: [syncfusion, docio, essential-docio, windows, application, deploy, copy-local, assemblies, deployment, target-machine, solution-explorer, references] -->
```
