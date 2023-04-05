import os
import streamlit.components.v1 as components

from typing import Tuple

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "build")
_component_func = components.declare_component("new_component_name", path=build_dir)

"""
_component_func = components.declare_component(
    "st_labs",
    url="http://localhost:3001",
)"""


# pass json to the component
def st_labs(json:str ,label: str, min_value: int, max_value: int, value: int = 0, key=None) -> int:
    component_value = _component_func(json=json,label=label, minValue=min_value, maxValue=max_value, initialValue=[value], key=key, default=[value])
    return component_value

