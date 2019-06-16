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

Will generate an image named `flowchart.jpg` in current dir that looks like ![this](https://github.com/KrishKasula/txtoflow/tree/master/examples/flowchart.jpg?raw=true "Simple FlowChart")

All the conditions and states can be arbitary strings too

```python3
from txtoflow import txtoflow

txtoflow.generate(
    '''
    First Node;
    if (A != 10) {
        B;
    } else if (Just a String) {
        Another String;
    } else {
        Else Body;
        More Statements;
        while (While also works) {
            While Body;
        }
        Link back;
    }
    Final Node;
    '''
)
```

Will still generate image like ![this](https://github.com/KrishKasula/txtoflow/tree/master/examples/strings.jpg?raw=true "Strings FlowChart")

## Examples

More examples can be found [here](https://github.com/KrishKasula/txtoflow/tree/master/examples)
