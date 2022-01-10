
## INSTALLATION

Don't have the module building yet, so to install you can run:
> pip install .

in the checked out directory.

To uninstall, run:
> pip uninstall keydecomposer

## Purpose
This script provides a way to idenfify the smallest unique column set in a pandas dataframe of any size.

## Dependencies
> pip install pandas

## Usage
```
import keydecomposer as kd

frame = pd.DataFrame() # generate this however you want

unique_set = kd.decompose_frame(frame)
```

## Warnings
The unique column set is only for the exact dimensions and values of the dataframe passed in.
Passing in a partial set of a larger frame will provide a unique column set for the partial frame only.

## Future Changes
Implement a unique column shortcut - instead of parsing the frame, identify a unique column from the start and shortcut the process.
Add a flag to return all valid unique column sets instead of the smallest one.
Check and see if the pd.Concat call can be optimized.
