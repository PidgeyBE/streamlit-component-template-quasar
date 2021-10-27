<template>
  <span>
    Hello, {{ args.name }}!
    <br/>
    <Button
      label="Click me"
      @click="onClicked"
    />
    <br/>
      <div v-for="item in args.dikt" :key="item.label">
        <Input :label="item.label" :infoText="item.infoText" />
        {{ item.label }}
      </div>
    <div>
      <Slider
        :min="min"
        :max="numClicks"
        v-model="sliderVal"
        label
        :showMinMax="minmax"
      />
    </div>
    <div>
      <Input label="foo" />
    </div>
  </span>
</template>

<script>
import { ref } from 'vue'
import { Streamlit } from 'streamlit-component-lib'
import { useStreamlit } from "./streamlit"
import { Button, Input, Slider, Tooltip } from '@robovision/quasar-ui-rvai-base'

export default {
  name: 'MyComponent',

  components: {
    Button,
    Input,
    Slider
  },

  
  // TODO proper typing
  props: ['args'], // Arguments that are passed to the plugin in Python are accessible in prop "args"

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

