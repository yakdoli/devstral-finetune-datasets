```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_252.jpeg
document_name: XlsIO
page_number: 252
page_id: XlsIO#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:23Z
fidelity: lossless
-->

# Page Setup and Header/Footer Configuration

## Overview
- This section explains how to configure page headers and footers using the Page Setup dialog box in XlsIO.
- Details the options available for customizing and aligning headers and footers.

## Content

### Page Setup Dialog Box

The Page Setup dialog box allows you to insert headers and footers. Here are the key elements:

#### Figure 86: Page Setup Dialog Box to insert Headers and Footers

- **Header:**  
  The Header field allows you to input text for the page header. Example:  
  `Syncfusion Confidential, 5/28/2013, Page 1`
  
- **Footer:**  
  The Footer field allows you to input text for the page footer. Currently set to `(none)`.

- **Additional Options:**
  - **Different odd and even pages:** Check this option to have different headers and footers for odd and even pages.
  - **Different first page:** Check this option to have a different header and footer for the first page.
  - **Scale with document:** Ensures the header and footer scale with the document.
  - **Align with page margins:** Aligns the header and footer with the page margins.

- **Buttons:**  
  - **Custom Header...:** Opens a dialog for customizing the header text.
  - **Custom Footer...:** Opens a dialog for customizing the footer text.
  - **Options...:** Provides additional formatting options.

#### Figure 87: Header Dialog Box

The Header dialog box offers options for formatting text and inserting elements into the header:

- **Text Formatting:**  
  Select text and choose the font button to format the text.

- **Insert Page Elements:**  
  Position the insertion point in the edit box and choose the appropriate button for inserting:
  - Page number
  - Date
  - Time
  - File path
  - Filename
  - Tab name

- **Insert Picture:**  
  Press the Insert Picture button to add an image to the header. Use the Format Picture button to adjust the picture.

- **Sections:**  
  The header can be divided into three sections:  
  - **Left section:**  
  - **Center section:**  
  - **Right section:**

  Each section can be customized independently.

### Summary

This section provides a comprehensive guide for setting up headers and footers in Excel documents using the Page Setup dialog box. It offers customization options to align with specific formatting requirements and ensures consistency across pages.

## Cross References
- For more details on Customizing Headers and Footers, refer to the associated documentation sections.

## Notes
- The screenshots provided are illustrative and show example configurations.

<!-- tags: [Syncfusion, Winforms, XlsIO, Header, Footer, Page Setup, Customization] keywords: [Syncfusion Confidential, page number, date, time, file path, filename, tab name, text formatting, picture insertion, left section, center section, right section, different odd and even pages, different first page, scale with document, align with page margins] -->
```