import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'
import { Quasar } from 'quasar'
import App from './App.vue'
import quasarUserOptions from './quasar-user-options'

const i18n = createI18n({
  locale: 'en',
  messages: {},
  legacy: false
})

const app = createApp(App)
app.use(Quasar, quasarUserOptions)
app.use(i18n)
app.mount('#app')
