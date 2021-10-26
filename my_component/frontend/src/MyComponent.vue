<template>
  <span>
    Hello, {{ args.name }}! &nbsp;
    <button @click="onClicked">Click Me!</button>
  </span>
  <div><Slider :min=min :max=max v-model=sliderVal label :showMinMax=minmax /></div>
  <div><Button label="test"/></div>
</template>

<script>
import { ref } from "vue"
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"
import {
  Input, LayoutButton, Slider, ColorPicker, Button
} from '@robovision/quasar-ui-rvai-base'

export default {
  name: "MyComponent",
  components: {  Button, Slider },
  props: ["args"], // Arguments that are passed to the plugin in Python are accessible in prop "args"
  setup() {
    useStreamlit() // lifecycle hooks for automatic Streamlit resize

    const numClicks = ref(0)
    const onClicked = () => {
      numClicks.value++
      Streamlit.setComponentValue(numClicks.value)
    }

    const min = 1
    const max = 5
    const minmax=true
    const sliderVal = ref(2)
    return {
      numClicks,
      onClicked,
      min,
      max,
      sliderVal,
      minmax,
    }
  },
}
</script>
