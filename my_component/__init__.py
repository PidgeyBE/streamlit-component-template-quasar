import streamlit as st
import streamlit.components.v1 as components
import json
import os
import time

_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        "my_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "my_component", path=build_dir)

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
if 'init' not in st.session_state:
    st.session_state.init = True
    st.session_state.parameters = {'epochs': {
        "id": "epochs",
        "label": "epochs",
        "infoText": "Just some epochs",
        "type": "integer",
        "value": 11,
        "error": False,
        "errorMessage": "",
    },
    'batch_size': {
        "id": "batch_size",
        "label": "batch size",
        "infoText": "Just some batch size",
        "type": "integer",
        "value": 4,
        "error": False,
        "errorMessage": "",
    }
    }
    st.session_state.last_ui_update = time.time()
    st.session_state.debounce = time.time()

print("RELOAD")
def my_component(name="test", key=None):
    component_value = _component_func(name=name, text="hellookes",
     parameters=st.session_state.parameters, debounce=st.session_state.debounce, key=name, default=None
    )
    if component_value is not None:
        update = json.loads(component_value)
        timestamp = float(update["timestamp"])
        updated_parameters = update["parameters"]
        if timestamp != st.session_state.last_ui_update:
            st.session_state.last_ui_update = timestamp
            st.session_state.parameters.update(updated_parameters)
            return True
        return False

st.subheader("Component with constant args")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
change = my_component("World")
print(change)

# PERFORM DATA CHECKS
if st.session_state.init and change:
    # CHECK EPOCHS
    if int(st.session_state.parameters["epochs"]["value"]) > 100:
        msg = "Epoch should be smaller than 100!"
        error = True
    else:
        msg = ""
        error = False

    st.info(msg)
    st.session_state.parameters["epochs"]["error"] = error
    st.session_state.parameters["epochs"]["errorMessage"] = msg

    # CHECK BATCH SIZE
    if int(st.session_state.parameters["batch_size"]["value"]) not in [1,2,4,8,16,32,64,128]:
        msg = "Batch size should be a power of 2!"
        error = True
    else:
        msg = ""
        error = False

    st.info(msg)
    st.session_state.parameters["batch_size"]["error"] = error
    st.session_state.parameters["batch_size"]["errorMessage"] = msg

    st.markdown(st.session_state.parameters)

    # if experimental_rerun is done, Vue-side is updated,
    # but this in turn can trigger a change in values   # SHOULD NOT CAUSE CHANGE IN VALUES?
    # so we debounce this case
    st.session_state.debounce = time.time()
    st.experimental_rerun()

st.markdown(st.session_state.parameters)
st.markdown("---")
