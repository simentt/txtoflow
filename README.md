# txtoflow (Translate To Flowchart)

The Python library can be used to generate flowcharts from pseudocode.

## Installation

  `pip install txtoflow`

## Usage

```python3
from txtoflow import txtoflow

txtoflow.generate(
    '''
    if (A) {
        B;
    } else {
        C;
        D;
        while (E) {
            F;
        }
        G;
    }
    H;
    '''
)
```

Will generate an image named `flowchart.jpg` in current dir that looks like
![this](https://github.com/KrishKasula/txtoflow/tree/master/examples/flowchart.jpg)

## Examples

More examples can be found [here](https://github.com/KrishKasula/txtoflow/tree/master/examples)
