<!-- 
  We bootstrap our Component to Streamlit with our scoped slot in the top-level App.
  This is where scoped slot passes Streamlit `args` data from itself to children MyComponent.
  You should not have to edit this, but are free to do so :)
-->
<template>
  <div id="app">
    <WithStreamlitConnection v-slot="{ args }">
      <MyComponent :args="args" />
    </WithStreamlitConnection>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import MyComponent from "./MyComponent.vue"

// "withStreamlitConnection" is a scoped slot. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue"

import '@robovision/quasar-ui-rvai-base/dist/index.min.css'

export default defineComponent({
  name: "App",
  components: {
    MyComponent,
    WithStreamlitConnection,
  },
})
</script>

<style>
body {
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
