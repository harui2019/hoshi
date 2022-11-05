from typing import Optional, Hashable, NamedTuple

"""

- Before:
        
>>> print(" ### Qiskit version outdated warning")
>>> print("Please keep mind on your qiskit version, an very outdated version may cause some problems.")
>>> print(" - Local Qiskit version ".ljust(40, '-')+f" {__qiskit_version__['qiskit']}")
>>> print(" - Latest Qiskit version ".ljust(40, '-')+f" {latest_version}")
```     
### Qiskit version outdated warning
Please keep mind on your qiskit version, an very outdated version may cause some problems.
- Local Qiskit version ---------------- 0.39.0
- Latest Qiskit version --------------- 0.39.0
```
        
- After:
        
>>> check_msg = Hoshi([
        ('divider', 60),
        ('h3', 'Qiskit version outdated warning'),
        ('txt', "Please keep mind on your qiskit version, an very outdated version may cause some problems."),
        ('itemize', 'Local Qiskit version', __qiskit_version__['qiskit']),
        {
            'type': 'itemize',
            'description': 'Latest Qiskit version',
            'value': latest_version,
        }
        ],
        ljust_describe_len=40,
    )
>>> print(check_msg)

```
        
------------------------------------------------------------
 ### Qiskit version outdated warning
 Please keep mind on your qiskit version, an very outdated version may cause some problems.
 - Local Qiskit version ------------------- 0.39.0
 - Latest Qiskit version ------------------ 0.39.0
```

Hoshi - A process content printer ?

## Why this name?
    I made it when I was listening the songs made by Hoshimachi Suisei, a VTuber in Hololive. I was inspired by her songs, and I made this tool. I named it Hoshi, which means star in Japanese. I hope this tool can help you to make your code more beautiful.

    (Hint: The last sentence is auto-complete by Github Copilot from 'Hoshimachi' to the end. That's meaning that Github Copilot knows VTuber, Hololive, even Suisei, who trains it with such content and how. "Does Skynet subscribe to Virtual Youtuber?")
"""


def hnprint(title, heading=3):
    """Print a title.

    Args:
        title (str): tilte of the section.
        heading (int, optional): Heading level. Defaults to 3.

    Returns:
        _type_: _description_
    """
    content = " "+"#"*heading+" {}".format(title)

    return content


def divider(length: int = 60):
    """Print a divider.

    Args:
        length (int, optional): Length of the divider. Defaults to 60.
    """
    content = "-"*length

    return content


def _ljustFilling(
    previous: str,
    length: Optional[int] = None,
    filler: str = '-'
) -> tuple[str, int]:

    previous = str(previous)
    if length is None or length == 0:
        length = len(previous)
        length = 5*(int(length/5)+2)

    return (previous+' ').ljust(length, filler)+' ', length


def itemize(
    description: str,
    value: Optional[any] = None,
    hint: Optional[str] = None,
    listing_level: int = 1,

    listing_itemize: str = '-',
    ljust_description_len: int = 0,
    ljust_description_filler: str = '-',
    ljust_value_len: int = 0,
    ljust_value_filler: str = '.',
    ljust_value_max_len: int = 40,
    hint_itemize: str = '#',

    export_len: bool = False,
):
    """_summary_

    Args:
        subscribe (str): _description_
        value (any): _description_
        hint (str, optional): _description_. Defaults to ''.
    """
    description = str(description)

    content = ''
    if not value is None:
        value = str(value)
        subscribe_str, ljust_description_len = _ljustFilling(
            previous=description,
            length=ljust_description_len,
            filler=ljust_description_filler
        )
        content += (" "*(2*listing_level-1) +
                    "{} {}".format(listing_itemize, subscribe_str))
    else:
        content += (" "*(2*listing_level-1) +
                    "{} {}".format(listing_itemize, description))

    if (not hint is None) and (hint != ''):
        hint = str(hint)
        if not value is None:
            value_str, ljust_value_len = _ljustFilling(
                previous=value,
                length=ljust_value_len,
                filler=ljust_value_filler
            )
        else:
            value_str, ljust_value_len = _ljustFilling(
                previous='',
                length=ljust_value_len,
                filler=ljust_value_filler
            )
        if ljust_value_len > ljust_value_max_len:
            ljust_value_len = 0
            content += ' '+str(value)
            content += '\n'+(" "*(2*listing_level))+hint
        else:
            content += value_str+' '+hint_itemize+' '+hint
    else:
        if not value is None:
            content += ' '+str(value)

    if export_len:
        return content, ljust_description_len, ljust_value_len
    else:
        return content


class Hoshi:

    _availablePrint = ['h1', 'h2', 'h3', 'h4',
                       'h5', 'h6', 'txt', 'itemize', 'divider']
    __name__ = 'Hoshi'

    class _config_container(NamedTuple):
        listing_level: int = 1
        listing_itemize: str = '-'
        ljust_description_len: Optional[int] = None
        ljust_description_filler: str = '-'
        ljust_value_len: Optional[int] = None
        ljust_value_filler: str = '.'
        ljust_value_max_len: int = 40
        hint_itemize: str = '#'
        divider_length: int = 60

    def __init__(
        self,
        raw: list[tuple[str]],
        name: str = 'Hoshi',

        listing_level: int = 1,
        listing_itemize: str = '-',
        ljust_description_len: int = 0,
        ljust_description_filler: str = '-',
        ljust_value_len: int = 0,
        ljust_value_filler: str = '.',
        ljust_value_max_len: int = 40,
        hint_itemize: str = '#',
        divider_length: int = 60,
        **kwargs
    ):
        """

        - Before:

        >>> print(" ### Qiskit version outdated warning")
        >>> print("Please keep mind on your qiskit version, an very outdated version may cause some problems.")
        >>> print(" - Local Qiskit version ".ljust(40, '-')+f" {__qiskit_version__['qiskit']}")
        >>> print(" - Latest Qiskit version ".ljust(40, '-')+f" {latest_version}")
        ```     
        ### Qiskit version outdated warning
        Please keep mind on your qiskit version, an very outdated version may cause some problems.
        - Local Qiskit version ---------------- 0.39.0
        - Latest Qiskit version --------------- 0.39.0
        ```

        - After:

        >>> check_msg = Hoshi([
                ('divider', 60),
                ('h3', 'Qiskit version outdated warning'),
                ('txt', "Please keep mind on your qiskit version, an very outdated version may cause some problems."),
                ('itemize', 'Local Qiskit version', __qiskit_version__['qiskit']),
                {
                    'type': 'itemize',
                    'description': 'Latest Qiskit version',
                    'value': latest_version,
                }
                ],
                ljust_describe_len=40,
            )
        >>> print(check_msg)

        ```

        ------------------------------------------------------------
         ### Qiskit version outdated warning
         Please keep mind on your qiskit version, an very outdated version may cause some problems.
         - Local Qiskit version ------------------- 0.39.0
         - Latest Qiskit version ------------------ 0.39.0
        ```
        Hoshi - A process content printer ?

        ## Why this name?
            I made it when I was listening the songs made by Hoshimachi Suisei, a VTuber in Hololive. I was inspired by her songs, and I made this tool. I named it Hoshi, which means star in Japanese. I hope this tool can help you to make your code more beautiful.

            (Hint: The last sentence is auto-complete by Github Copilot from 'Hoshimachi' to the end. That's meaning that Github Copilot knows VTuber, Hololive, even Suisei, who trains it with such content and how. "Does Skynet subscribe to Virtual Youtuber?")
        """

        self.__name__ = 'Hoshi'
        self._raw = []
        for item in raw:
            if isinstance(item, (tuple, list)):
                if item[0] in self._availablePrint:
                    if len(item) > 1:
                        self._raw.append(item)
                else:
                    self._raw.append(('txt', item))
            elif isinstance(item, dict):
                if 'type' in item:
                    if item['type'] in self._availablePrint:
                        self._raw.append(item)
            else:
                self._raw.append(('txt', item))

        self._config = self._config_container(**{
            'listing_level': listing_level,
            'listing_itemize': listing_itemize,
            'ljust_description_len': ljust_description_len,
            'ljust_description_filler': ljust_description_filler,
            'ljust_value_len': ljust_value_len,
            'ljust_value_filler': ljust_value_filler,
            'ljust_value_max_len': ljust_value_max_len,
            'hint_itemize': hint_itemize,
            'divider_length': divider_length,
        })
        self._update()

    def _update(self):
        self._print_list = []
        _formated = []
        
        for item_raw in self._raw:
            item = {}
            if isinstance(item_raw, dict):
                item = item_raw
            elif isinstance(item_raw, (tuple, list)):
                item['type'] = item_raw[0]
                if item['type'] == 'itemize':
                    item['description'] = str(item_raw[1])
                    item['value'] = item_raw[2] if len(
                        item_raw) > 2 else None
                    item['hint'] = item_raw[3] if len(
                        item_raw) > 3 else None
                    item['listing_level'] = item_raw[4] if len(
                        item_raw) > 4 else self._config.listing_level
                elif item['type'] == 'txt':
                    item['text'] = item_raw[1]
                    item['listing_level'] = item_raw[2] if len(
                        item_raw) > 2 else self._config.listing_level
                elif item['type'] == 'divider':
                    item['length'] = item_raw[1] if len(
                        item_raw) > 1 else self._config.divider_length
                elif item['type'] == 'h1':
                    item['title'] = item_raw[1]
                    item['heading'] = 1
                elif item['type'] == 'h2':
                    item['title'] = item_raw[1]
                    item['heading'] = 2
                elif item['type'] == 'h3':
                    item['title'] = item_raw[1]
                    item['heading'] = 3
                elif item['type'] == 'h4':
                    item['title'] = item_raw[1]
                    item['heading'] = 4
                elif item['type'] == 'h5':
                    item['title'] = item_raw[1]
                    item['heading'] = 5
                elif item['type'] == 'h6':
                    item['title'] = item_raw[1]
                    item['heading'] = 6
                else:
                    raise ValueError(f"Unknown print type, '{item['type']}'.")
            else:
                raise TypeError(
                    f"Unknown item type. '{item}', '{type(item)}'.")

            content = ''
            item_input = {k: v for k, v in item.items() if k != 'type'}
            # config
            if item['type'] == 'itemize':
                item_input['listing_itemize'] = self._config.listing_itemize if 'listing_itemize' not in item_input else item_input['listing_itemize']
                item_input['ljust_description_len'] = 0 if 'ljust_description_len' not in item_input else item_input['ljust_description_len']
                item_input['ljust_description_filler'] = self._config.ljust_description_filler if 'ljust_description_filler' not in item_input else item_input['ljust_description_filler']
                item_input['ljust_value_len'] = 0 if 'ljust_value_len' not in item_input else item_input['ljust_value_len']
                item_input['ljust_value_filler'] = self._config.ljust_value_filler if 'ljust_value_filler' not in item_input else item_input['ljust_value_filler']
                item_input['ljust_value_max_len'] = self._config.ljust_value_max_len if 'ljust_value_max_len' not in item_input else item_input['ljust_value_max_len']
                item_input['hint_itemize'] = self._config.hint_itemize if 'hint_itemize' not in item_input else item_input['hint_itemize']
                content, ljust_description_len, ljust_value_len = itemize(
                    **item_input,
                    export_len=True
                )
                if ljust_description_len > self._config.ljust_description_len:
                    self._config = self._config._replace(
                        ljust_description_len=ljust_description_len)
                if ljust_value_len > self._config.ljust_value_len:
                    self._config = self._config._replace(
                        ljust_value_len=ljust_value_len)
            
            _formated.append(item)

        for item in _formated:
            item_input = {k: v for k, v in item.items() if k != 'type'}
            
            # string add
            if item['type'] in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                self._print_list.append(hnprint(**item_input))
            elif item['type'] == 'txt':
                self._print_list.append(self.txt(**item_input))
            elif item['type'] == 'divider':
                self._print_list.append(divider(**item_input))
            elif item['type'] == 'itemize':
                item_input['ljust_description_len'] = self._config.ljust_description_len
                item_input['ljust_value_len'] = self._config.ljust_value_len
                content = itemize(**item_input)
                self._print_list.append(content)
            else:
                raise ValueError("Unknown print type.")

    def __str__(self):
        content = ''
        for item in self._print_list:
            content += item
            content += '\n'
        return content

    def __repr__(self):

        content = self.__str__()
        content += f'by <{self.__name__}>'
        return content

    def print(self):
        for item in self._print_list:
            print(item)
    
    def newline(self, item):
        self._raw.append(item)
        self._update()

    def h1(self, text: str):
        return hnprint(text, heading=1)

    def h2(self, text: str):
        return hnprint(text, heading=2)

    def h3(self, text: str):
        return hnprint(text, heading=3)

    def h4(self, text: str):
        return hnprint(text, heading=4)

    def h5(self, text: str):
        return hnprint(text, heading=5)

    def h6(self, text: str):
        return hnprint(text, heading=6)

    def txt(self, text: str, listing_level: int = 1):
        return (" "*(2*listing_level-1))+str(text)

    def divider(self, length: int = 60):
        return divider(length)

    def itemize(
        self,
        desc: str,
        value: Optional[any] = None,
        hint: str = '',
    ):
        return itemize(
            description=desc,
            value=value,
            hint=hint,
            **self._config._asdict(),
        )
