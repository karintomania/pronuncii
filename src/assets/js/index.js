import Alpine from 'alpinejs'
window.Alpine = Alpine

import assessmentInit from './main/assessment'
window.assessmentInit = assessmentInit
import testInit from './main/test'
window.testInit = testInit

Alpine.start()
