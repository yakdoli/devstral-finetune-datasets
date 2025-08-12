```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_140.jpeg
document_name: common
page_number: 140
page_id: common#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:19Z
fidelity: lossless
-->

## Essential Common

### Overview
- Add Resources for different cultures.
- Add supported cultures.
- Assign a Current UI Culture to the application.

### Content

#### Add Resources
To localize Syncfusion Silverlight controls, you need to create resource files for each culture.

The following steps illustrate this:
1. Add Resource (.resx) files in the Resources folder for different cultures. (Here, .resx files in a different culture or invariant culture should be placed in the **Resources** folder of your project.)
2. Resource files should be named as `AssemblyName.CultureName.resx` and `AssemblyName.resx` for the invariant culture.

**Where**
- **AssemblyName**: Syncfusion Silverlight Control Assembly Name.
- **CultureName**: Culture Code of the resource that you want to show in the UI.

If your conversion is only for the invariant culture, the .resx file does not need to contain a culture suffix.

**Example:**
- `Syncfusion.Ribbon.Silverlight.fr-FR.resx` – French resource for `Syncfusion.Ribbon.Silverlight` assembly.
- `Syncfusion.Ribbon.Silverlight.resx` – Invariant Culture resource for `Syncfusion.Ribbon.Silverlight` assembly.

#### Add Supported Cultures
It is very important to add supported cultures in the sample application project before you run the application.

Follow the steps below to localize strings for your culture:
1. In the **Solution Explorer**, right-click your sample application project and choose **Unload Project**. The project will be unavailable.
2. Right-click the project again, and select the **Edit SampleProjectName.csproj** option.
3. In the `.csproj` file, find the `<SupportedCultures></SupportedCultures>` tags. By default, the tags will be empty. So, add the cultures that you want to be supported, separating each with a semicolon.

**Example:** `<SupportedCultures>fr-FR</SupportedCultures>`

4. Save the project and reload it by right-clicking the **SampleProjectName.csproj** and choosing **Reload SampleProjectName.csproj**.

#### Assign Current UI Culture to the Application
By default, the Current Culture will be `en-US`. You can change the CurrentUICulture. Here, CurrentUICulture should be set before the **InitializeComponent** in your **Startup** page (here, **MainPage.xaml.cs**) or you can do it in **App.xaml.cs** in the **Application_Startup** event.
```