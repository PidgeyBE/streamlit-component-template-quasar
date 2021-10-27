<template>
  <span>
    Hello, {{ args.name }}!
    <br/>
    <rv-button
      label="Click me"
      @click="onClicked"
    />
    <br/>
      <div v-for="item in parameters" :key="item.id">
        <table><tr>
        <td>
        <rv-input :class="item.class" :label="item.label" :infoText="item.infoText" :modelValue="item.value" @update:modelValue="onUpdate(item.id, $event)"/>
        </td><td><a v-if="item.error" style="color:red">ERROR: {{ item.errorMessage }}</a></td></tr>
        </table>
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
import { ref, onMounted, onUpdated } from 'vue'
import { Streamlit } from 'streamlit-component-lib'
import { useStreamlit } from '../composables'



export default {
  name: 'MyComponent',
  // TODO proper typing
  props: ['args'], // Arguments that are passed to the plugin in Python are accessible in prop "args"

  setup(props) {
    useStreamlit() // lifecycle hooks for automatic Streamlit resize

    const numClicks = ref(0)
    const parameters = ref({})
    const debounce = ref(0)

    onMounted(() => {
      /* eslint-disable */
      console.log("mounted!")
      parameters.value = props.args.parameters 
    })

    onUpdated(() => {
      /* eslint-disable */
      // Check if update is from python, with updated timestamp
      // If so, update state
      if (props.args.debounce > debounce.value) {
        parameters.value = props.args.parameters
        debounce.value = props.args.debounce
        console.log("updated!")
        console.log(props.args.parameters.epochs)
      }
    })

    const onClicked = () => {
      numClicks.value++
      // Streamlit.setComponentValue(numClicks.value)
    }
    const onSlide = () => {
      console.log('slide')
    }
    function onUpdate (id, value) {
      console.log(value)
      console.log(id)
      console.log(parameters.value.epochs)
      for (const [key, item] of Object.entries(parameters.value)) {
        if (key == id) item.value = value 
      }
      console.log(parameters.value.epochs)
      Streamlit.setComponentValue(JSON.stringify(parameters.value))
    }
    const min = 0
    const max = 10
    const minmax=true
    const sliderVal = ref(2)
    return {
      numClicks,
      onClicked,
      onSlide,
      onUpdate,
      parameters,
      min,
      max,
      sliderVal,
      minmax,
    }
  },
}
</script>

