<template>
  <span>
    Hello, {{ args.name }}!
    <br/>
    <rv-button
      label="Click me"
      @click="onClicked"
    />
    <br/>
      <div v-for="item in args.dikt" :key="item.label">
        <rv-input  :label="item.label" />
        {{ item.label }}
      </div>
    <div>
      <rv-slider
        :min="min"
        :max="max"
        v-model="numClicks"
        label
        :showMinMax="minmax"
        @change="onSlide"
      />
    </div>
  </span>
</template>

<script>
import { ref } from 'vue'
import { Streamlit } from 'streamlit-component-lib'
import { useStreamlit } from '../composables'

export default {
  name: 'MyComponent',
  // TODO proper typing
  props: ['args'], // Arguments that are passed to the plugin in Python are accessible in prop "args"

  setup() {
    useStreamlit() // lifecycle hooks for automatic Streamlit resize

    const numClicks = ref(0)
    const onClicked = () => {
      numClicks.value++
      Streamlit.setComponentValue(numClicks.value)
    }
    const onSlide = () => {
      Streamlit.setComponentValue(numClicks.value)
    }

    const min = 0
    const max = 10
    const minmax=true
    const sliderVal = ref(2)
    return {
      numClicks,
      onClicked,
      onSlide,
      min,
      max,
      sliderVal,
      minmax,
    }
  },
}
</script>

