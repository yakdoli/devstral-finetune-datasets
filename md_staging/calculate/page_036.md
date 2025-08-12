```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: calculate
page_number: 036
page_id: calculate#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:00:18Z
fidelity: lossless
-->

## Overview

- Easily set up forms that have calculation dependencies among various controls.
- With Essential Calculate, you can set properties that will indicate that you want formula dependencies to be tracked so that the values are automatically updated when a dependent value changes. Or you can turn off the overhead of tracking dependencies and have formulas calculated from scratch when you need a particular formula value.
- Essential Calculate can be used in manual mode or automatic mode.
- The manual mode works when you explicitly request for a value. At that point, the calculation is done from scratch to obtain the computed value.
- In automatic mode, Essential Calculate maintains a dependency list. Hence, when a value is changed, any formula that depends on it is recalculated at that particular point.

## Content

### 3.5 Quick Start

This section will show you how easy it is to get started using Essential Calculate. It will give you a basic introduction to the concepts you need to know before getting started with the product and some tips and ideas on how to use Essential Calculate in your projects.

#### Console Application Using CalcQuickBase

In this section, you will learn how to use the `CalcQuickBase` object to perform arbitrary calculations from a Console Application. This will show you the minimal steps that are required to use Essential Calculate to add calculation support to an application. This quick application lets you type algebraic expressions using a `Console.ReadLine` and display the calculated results using a `Console.WriteLine`.

#### Windows Application Using CalcQuickBase

In this section, you will create a Windows Application that uses a `CalcQuickBase` object that handles arbitrary variables in its calculations.

#### Adding Calculation Support to an Arbitrary Array with an ICalcData Interface

This section will demonstrate how to add calculation support to an arbitrary array of doubles by adding an additional row and column to hold summary information.
```