![Python package](https://github.com/jefpadfi/PandasDataframeGUIKivy/workflows/Python%20package/badge.svg?branch=master)

# DataframeGUIKivy

Port of Dataframe GUI module to a Kivy widget. Original module can be found at this repository: https://github.com/bluenote10/PandasDataFrameGUI

# Updates
This fork has been updated to use the current version of all required libraries.

* matplotlib _png is no longer needed to be imported and was removed
*  pandas.DataFrame.from_items was [deprecated since version 0.23.0](https://github.com/pandas-dev/pandas/blob/v0.23.4/pandas/core/frame.py#L1422-L1507) 
and has been replaced with pandas.DataFrame.from_dict
* kivy.garden.matplotlib was giving me trouble so I just included the source in garden.matplotlib
* added in requirements.txt so all requirements can be installed through pip.

## Demo Run Instructions

```sh
$ python demo.py
```

## Demo Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/MichaelStott/DataframeGUIKivy/master/docs/sc1.png">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/MichaelStott/DataframeGUIKivy/master/docs/sc2.png">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/MichaelStott/DataframeGUIKivy/master/docs/sc3.png">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/MichaelStott/DataframeGUIKivy/master/docs/sc4.png">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/MichaelStott/DataframeGUIKivy/master/docs/sc5.png">
</p>

