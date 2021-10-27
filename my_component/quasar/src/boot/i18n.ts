import { boot } from 'quasar/wrappers'
import { createI18n } from 'vue-i18n'

const SUPPORTED_LOCALES = ['en'] as const
const DEFAULT_LOCALE = SUPPORTED_LOCALES[0]

const i18nInstance = createI18n({
  locale: DEFAULT_LOCALE,
  messages: {},
  legacy: false
})

// export const i18n = i18nInstance.global

export default boot(({ app }) => {
  // Set i18n instance on app
  app.use(i18nInstance)
})
